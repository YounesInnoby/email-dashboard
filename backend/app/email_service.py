import imaplib
import email
from email.header import decode_header
import base64
import fitz
import io
from openai import OpenAI
from io import BytesIO
from schemas import schema
import json



IMAP_SERVER = "mx.freenet.de"
EMAIL_ACCOUNT = "rostfrei_demo@freenet.de"
EMAIL_PASSWORD = "RostfreiStahl1!"
llm = "gpt-4o"
client = OpenAI(api_key='SK_REDACTED')
#openai_api_key = "SK_REDACTED"



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

def get_emails():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        mail.select("inbox")

        _, messages = mail.search(None, "ALL")
        message_ids = messages[0].split()
        email_list = []

        for msg_id in message_ids[-10:]:
            _, msg_data = mail.fetch(msg_id, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

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

                            completion = client.chat.completions.create(
                                model=llm,
                                messages=[
                                    {"role": "system", "content": """Für den folgenden Text müssen alle aufgeführten Positionen einzeln extrahiert werden mit den zugehörig definierten Attributen im angelieferten JSON Format. 
                                    Orientiere dich bei der Antwort hauptsächlich am vorgegebenen Text und extrahiere Informationen nur, wenn du dir auch wirklich sicher bist."""
                                    },
                                    {
                                       "role": "user",
                                        "content": pdf_text
                                    }
                                ],
                                response_format=schema,
                            )
                            response = completion.choices[0].message.content

            response = json.loads(response)
            search_terms = [str(v).strip().lower() for v in extract_non_empty_values(response)]
            all_words = extract_text_with_positions(pdf_attachment)
            highlight_fields = filter_words_if_in_target_texts(all_words, search_terms)
            highlight_pdf = highlight_and_return_base64(pdf_attachment, highlight_fields)

            email_list.append({
                "id": msg_id.decode(),
                "subject": subject,
                "sender": sender,
                "body": email_body,
                "pdf_attachment": highlight_pdf,
                "pdf_text": pdf_text,  # 🆕 PDF-Text wird hier gespeichert
                "response" : response,
                "status": "unbearbeitet"
            })

        mail.logout()
        return email_list

    except Exception as e:
        return {"error": str(e)}



