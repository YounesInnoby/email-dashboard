import imaplib
import email
from email.header import decode_header
from pydantic import BaseModel
import base64
import fitz
import io
from openai import OpenAI
from io import BytesIO
from schemas import schema, schema_PT, schema_Joke2, schema_Fischer
import json
from pdf2image import convert_from_bytes
import tempfile
import base64
import os
import pickle
import openpyxl
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import time
from structured_logprobs.main import add_logprobs, add_logprobs_inline
import math
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import ast


IMAP_SERVER = "mx.freenet.de"
EMAIL_ACCOUNT = "rostfrei_demo@freenet.de"
EMAIL_PASSWORD = "RostfreiStahl1!"
llm = "gpt-4o"
client = OpenAI(api_key='SK_REDACTED')
#openai_api_key = "SK_REDACTED"

#Kunden = pd.read_pickle("./samples/Kunden WHG.pkl")
#Kunden["embedding"] = Kunden["embedding"].apply(ast.literal_eval)
presentation_mode = True

email_list = []
email_ids = []

def get_embedding(text, model="text-embedding-3-small"):
    response = client.embeddings.create(
        input=[text],  # Liste von Strings
        model=model
    )
    return response.data[0].embedding

def extract_text_from_pdf(pdf_base64: str) -> str:
    """Extrahiert Text aus einer Base64-kodierten PDF mit PyMuPDF."""
    try:
        pdf_bytes = base64.b64decode(pdf_base64)
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "\n".join([page.get_text("text") for page in pdf_document])
        return text or "Kein Text in der PDF gefunden."

    except Exception as e:
        return f"Fehler beim PDF-Parsing: {str(e)}"

def load_pdf_from_base64(base64_data: str):
    pdf_bytes = base64.b64decode(base64_data)
    return fitz.open("pdf", pdf_bytes)

def extract_text_with_positions(pdf_base64: str):
    base64_pdf = pdf_base64
    doc = load_pdf_from_base64(base64_pdf)
    all_words = []
    for page_number in range(len(doc)):
        page = doc[page_number]
        words = page.get_text("words")  # returns list of (x0, y0, x1, y1, "word", block_no, line_no, word_no)
        for w in words:
            all_words.append({
                "page": page_number + 1,
                "bbox": w[:4],
                "text": w[4]
            })
    return all_words

def filter_words_if_in_target_texts(all_words, target_texts):
    filtered = [
        word for word in all_words
        if any(word["text"].lower() in t.lower() for t in target_texts)
    ]
    return filtered


def split_values_confidences(data):
    """
    Trennt rekursiv ein Dict (ggf. mit Listen) mit {"value", "confidence"}-Struktur
    in zwei parallele Dicts: nur Werte und nur Confidence Scores.
    """
    if isinstance(data, dict):
        # Spezialfall: {"value": ..., "confidence": ...}
        if set(data.keys()) == {"value", "confidence"}:
            return data["value"], data["confidence"]
        # Allgemein: dict mit beliebigen keys
        values_dict = {}
        confs_dict = {}
        for k, v in data.items():
            val, conf = split_values_confidences(v)
            values_dict[k] = val
            confs_dict[k] = conf
        return values_dict, confs_dict
    elif isinstance(data, list):
        vals, confs = zip(*(split_values_confidences(item) for item in data))
        return list(vals), list(confs)
    else:
        # Primitive Werte (sollte eigentlich nie vorkommen)
        return data, None


def highlight_and_return_base64(base64_pdf: str, highlight_fields: list) -> str:
    doc = load_pdf_from_base64(base64_pdf)

    for f in highlight_fields:
        page = doc[f["page"] - 1]
        rect = fitz.Rect(*f["bbox"])

        shape = page.new_shape()
        shape.draw_rect(rect)
        shape.finish(
            color=(1, 0, 0),        # Randfarbe (rot)
            fill=(1, 0, 0),         # Füllfarbe (rot)
            fill_opacity=0.3        # Transparenz
        )
        shape.commit()

    output_buffer = BytesIO()
    doc.save(output_buffer)
    doc.close()
    return base64.b64encode(output_buffer.getvalue()).decode("utf-8")


def extract_non_empty_values(data):
    values = []

    def recurse(obj):
        if isinstance(obj, dict):
            for value in obj.values():
                recurse(value)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)
        else:
            # Prüfe auf nicht-leeren Wert (ignoriert "", None, leere Strings)
            if obj not in ("", None):
                values.append(obj)

    recurse(data)
    return values


import json
import re


def parse_gpt_json(content: str, max_positionen: int = None) -> dict | None:
    """
    Versucht eine GPT-JSON-Antwort robust zu parsen und optional zu reparieren.

    :param content: Die GPT-Antwort als String.
    :param max_positionen: (Optional) Maximale Anzahl Positionen, die in der Liste erhalten bleiben sollen.
    :return: Das geparste JSON als Dictionary oder None bei Fehler.
    """
    try:
        # Entferne Markdown-Hülle (z. B. ```json … ```)
        content = content.strip()
        content = re.sub(r"^```(json)?\n?", "", content)
        content = re.sub(r"\n?```$", "", content)

        # Optional: Truncate Positionen-Liste, wenn zu lang
        if max_positionen is not None:
            # Positionen-Liste isolieren und kürzen
            pattern = r'"Positionen"\s*:\s*\[(.*?)\](,?)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                positions_raw = match.group(1)
                split_items = re.split(r"\},\s*\{", positions_raw)
                truncated = "},{".join(split_items[:max_positionen])
                if len(split_items) > 1:
                    truncated = "{" + truncated + "}"
                content = re.sub(pattern,
                                 f'"Positionen": [{truncated}]',
                                 content, flags=re.DOTALL)

        # Klammern fixen: Falls z. B. am Ende abgeschnitten
        last_brace = content.rfind("}")
        if last_brace != -1:
            content = content[:last_brace + 1]

        # Letzter Versuch zu parsen
        return json.loads(content)

    except json.JSONDecodeError as e:
        print("⚠️ Fehler beim Parsen der GPT-Antwort:")
        print(e)
        print("→ Inhalt (gekürzt):", content[:500])
        return None


def get_emails():
    #time.sleep(17)
    client_name = 'MEFA'
    with open(f"./samples/{client_name}.pkl", "rb") as f:
        loaded_dict = pickle.load(f)
        mapping = dict(zip([dict['subject'] for dict in loaded_dict], loaded_dict))

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        mail.select("inbox")

        _, messages = mail.search(None, "ALL")
        message_ids = messages[0].split()

        for msg_id in message_ids:
            try:
                msg_id_str = msg_id.decode()
                print(msg_id_str)
                if msg_id_str not in email_ids:
                    email_ids.append(msg_id_str)
                    _, msg_data = mail.fetch(msg_id, "(RFC822)")
                    raw_email = msg_data[0][1]
                    msg = email.message_from_bytes(raw_email)

                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")


                    pfad = f"./samples/{subject}.pdf"


                    if presentation_mode:
                        print(pfad)
                        if os.path.exists(pfad):
                            print("PDF gefunden")
                            with open(pfad, "rb") as f:
                                pdf_attachment = base64.b64encode(f.read()).decode("utf-8")

                            email_tmp = mapping[subject]
                            email_tmp["pdf_attachment"] = pdf_attachment

                            #if ('Lieferadresse' in email_tmp['response'].keys()) and (client_name == 'Osmo Holz'):
                                # Eingabetext zum Vergleichen
                             #   query = email_tmp['response']['Lieferadresse']
                              #  query_embedding = get_embedding(query)

                                # Kosinusähnlichkeit berechnen (alle Zeilen gegen den Suchstring)
                              #  Kunden['similarity'] = Kunden['embedding'].apply(
                              #      lambda x: cosine_similarity([x], [query_embedding])[0][0]
#                                )

 #                               # Ergebnisse sortieren (höchste Ähnlichkeit zuerst)
  #                              Kunden_sorted = Kunden.sort_values(by='similarity', ascending=False)
#
 #                               email_tmp['response']['Kundennummer Mapping WHG'] = list(Kunden_sorted['KUNDEN-NUMMER '])[0]

                            email_list.append(email_tmp)

                    else:

                        if client_name in subject:

                            sender = msg.get("From")
                            email_body = None
                            pdf_attachment = None
                            pdf_text = None  # 🆕 Hier speichern wir den extrahierten PDF-Text
                            response = None
                            if msg.is_multipart():
                                for part in msg.walk():
                                    content_type = part.get_content_type()
                                    content_disposition = str(part.get("Content-Disposition"))

                                    if content_type == "text/plain" and "attachment" not in content_disposition:
                                        email_body = part.get_payload(decode=True).decode("utf-8", errors="ignore")

                                    elif "application/pdf" in content_type:
                                        filename = part.get_filename()
                                        if filename:
                                            pdf_attachment = base64.b64encode(part.get_payload(decode=True)).decode("utf-8")
                                            pdf_text = extract_text_from_pdf(pdf_attachment)  # 🆕 PDF-Text extrahieren
                                            #pdf_text = "\n\n".join(extract_text_blocks_from_pdf(pdf_attachment))

                                            # Konvertiere PDF in PNG (erste Seite)
                                            pdf_bytes = base64.b64decode(pdf_attachment)
                                            images = convert_from_bytes(pdf_bytes, dpi=150)

                                            #with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
                                            #    images[0].save(tmp_img.name, format='PNG')
                                            #    tmp_img_path = tmp_img.name

                                            # PNG in base64 kodieren
                                            #with open(tmp_img_path, "rb") as image_file:
                                            #    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

                                            # Baue Messages mit mehreren image_url-Einträgen
                                            image_messages = []
                                            for img in images:
                                                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
                                                    img.save(tmp_img.name, format='PNG')
                                                    with open(tmp_img.name, "rb") as f:
                                                        encoded_image = base64.b64encode(f.read()).decode("utf-8")
                                                        image_messages.append({
                                                            "type": "image_url",
                                                            "image_url": {
                                                                "url": f"data:image/png;base64,{encoded_image}",
                                                                "detail": "high"
                                                            }
                                                        })


                                            # GPT-4o Vision-Anfrage
                                            print('create API call')
                                            vision_completion = client.chat.completions.create(
                                                model="gpt-5",
                                                messages=[
                                                    {
                                                        "role": "system",
                                                        "content": "Du bist ein KI-Assistent für die Extraktion von Informationen aus kaufmännischen Dokumenten. Achte darauf, alle Attribute gemäß dem JSON-Schema korrekt zurückzugeben. Felder, die nicht im Dokument enthalten sind, dürfen weggelassen werden. Wenn eine Tabelle von Teilen im Dokument enthalten ist und eine der Positionen in der Bestellung auf den Namen der Tabelle referenziert, dann muss jede Position aus der Tabelle hierfür eingesetzt werden mit dem in der Position definierten Lieferdatum"
                                                    },
                                                    {
                                                        "role": "user",
                                                        "content": image_messages + [
                                                            {
                                                                "type": "text",
                                                                "text": "Ermittle mir aus dem angehangenen kaufmännischen Dokument alle benötigten Attribute und ignoriere die Felder, die nicht im Dokument enthalten sind."
                                                            }
                                                        ]
                                                    }
                                                ],
                                                response_format=schema_Fischer
                                            )

                                            response = json.loads(vision_completion.choices[0].message.content)

                                            values, confidences = split_values_confidences(response)
                                            print(values)
                                            print(confidences)


                            #response = json.loads(response)
                            search_terms = [str(v).strip().lower() for v in extract_non_empty_values(response)]
                            all_words = extract_text_with_positions(pdf_attachment)
                            highlight_fields = filter_words_if_in_target_texts(all_words, search_terms)
                            highlight_pdf = highlight_and_return_base64(pdf_attachment, highlight_fields)


                            email_list.append({
                                "id": msg_id.decode(),
                                "Kategorie" : values['Dokumententyp'],
                                "subject": subject,
                                "sender": sender,
                                "body": email_body,
                                "pdf_attachment": highlight_pdf,
                               "pdf_text": pdf_text,  # 🆕 PDF-Text wird hier gespeichert
                                "response" : values,
                                 "confidence": confidences,
                                "status": "unbearbeitet"
                            })


            except Exception as e:
                print(e)

        mail.logout()
        return email_list

    except Exception as e:
        print(f"Fehler beim Abrufen der E-Mails: {str(e)}")
        return {"error": str(e)}






def transform_excel(file):
    # Excel öffnen
    wb = openpyxl.load_workbook("datei.xlsx")
    ws = wb.active

    # Daten aus Excel einlesen
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(list(row))

    # PDF erstellen
    pdf = SimpleDocTemplate("output.pdf", pagesize=landscape(A4))
    table = Table(data)

    # Tabellenstil
    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black)
    ])
    table.setStyle(style)

    pdf.build([table])


