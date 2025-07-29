schema = {
    "type": "json_schema",
    "json_schema":
    {
        "name": "order_schema",
        "schema": {
            "type": "object",
            "properties": {
                "Kunde": {
                    "type": "string",
                    "description": "The name of the customer."
                },
                "Datum": {
                    "type": "string",
                    "description": "The date of the order."
                },
                "Positionen": {
                    "type": "array",
                    "description": "List of items in the order.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Positionstyp": {
                                "type": "string",
                                "description": "Differentiation if the listed position is a product, packaging, a requested certificate or Transport/Freight for the product.",
                                "enum": ['Product', 'Certificate', 'Quality Test']
                            },
                            "Position": {
                                "type": "number",
                                "description": "The position number of the item."
                            },
                            "Quality Test": {
                                "type": "string",
                                "description": "This Item is only required if the Positionstyp is 'Quality Test' and indicates which type of test is required.",
                                "enum": ['Kaltzugversuch', 'Warmzugversuch', 'Permeabilitätsprüfung', 'US Flächenprüfung',
                                         'US Randzonenprüfung', 'Zugversuch', 'Ultraschallprüfung',
                                         'Kerbschlagbiegeversuch', 'IK-Test', 'US Prüfung', ""]
                            },
                            "Form": {
                                "type": "string",
                                "description": "The form of the item.",
                                "enum": [
                                    'Knieblech',
                                    'Brücke',
                                    'Langloch',
                                    'Platte',
                                    'Trapez',
                                    'Rechteck mit Ausschnitt',
                                    'Dreieck',
                                    'Flansch',
                                    'Knotenblech',
                                    'Kreissegment',
                                    'Ellipse',
                                    'Geteilte Ronde',
                                    'Rohrstütze',
                                    'Ronde',
                                    'Rechteck',
                                    'Hebeauge',
                                    'Halb Ronde',
                                    'Rechteck mit Lochgitter',
                                    'Freiform',
                                    'Kreuzstück',
                                    'Kreis in Kreis',
                                    'Stütze',
                                    'Streifen',
                                    'Ring mit Fortsatz',
                                    'Abstützung',
                                    'Hantel mit Kreis',
                                    'Rechteck mit Radien',
                                    'Fuss',
                                    'Ringsegment',
                                    'Ganztafel',
                                    'Steckscheibe',
                                    'Achteck mit Langloch',
                                    'Ring',
                                    'Konus',
                                    'halber Kreisring',
                                    'L-Stück',
                                    'Stütze mit Schlitz',
                                    ''
                                ]
                            },
                            "Menge": {
                                "type": "number",
                                "description": "The quantity of the item."
                            },
                            "Laenge": {
                                "type": "number",
                                "description": "The length of the item , which is described in the size description."
                            },
                            "Breite": {
                                "type": "number",
                                "description": "The width of the item , which is described in the size description."
                            },
                            "Dicke": {
                                "type": "number",
                                "description": "The thickness of the item."
                            },
                            "Werkstoff": {
                                "type": "string",
                                "description": "The material of the item, which is described as a specific material code."
                            },
                            "Oberflächengüte": {
                                "type": "string",
                                "description": "The surface quality of the item describes by a specific code.",
                                "enum": ['1D', '2E', '2B', '1C', '']

                            },
                            "Norm": {
                                "type": "string",
                                "description": "The normed standard demanded for the product. These could be international, european or german standards, which usually are indicated by DIN, EN or ASME at the beginning."
                            },
                            "Zeugnis": {
                                "type": "string",
                                "description": "The certificate related to the item.",
                                'enum': [
                                    '3rd party inspection by ABS',
                                    '3rd party inspection by Lloyds Register, Industry',
                                    '3.2 TÜV (für EN-Werkstoff, nicht für ASME)',
                                    '3rd party inspection 3.2 by TÜV', '3.1',
                                    '3rd party inspection by DNV-GL',
                                    '3rd party inspection by Bureau Veritas',
                                    '3rd party inspection by Lloyds Register, Marine',
                                    'nur 3.2 Werkszeugnis (Teile ohne TÜV-Umstempelung)',
                                    ''
                                ]
                            },
                            "Schneiden": {
                                "type": "string",
                                "description": "The cutting method used.",
                                "enum": [
                                    'Wasserstrahl 1 Kopf',
                                    'Plasma Qualitätsschnitt aussen / Trennschnitt innen',
                                    'Sägen 2 Kopf Trennschnitt',
                                    'Wasserstrahl 2 Kopf Qualitätsschnitt',
                                    'Laser 1 Kopf Qualitätsschnitt',
                                    'Wasserstrahl 2 Kopf Trennschnitt',
                                    'Laser 2 Kopf Trennschnitt',
                                    'Sägen 1 Kopf Trennschnitt',
                                    'Plasma 1 Kopf Trennschnitt',
                                    'Wasserstrahl 1 Kopf Trennschnitt',
                                    'Plasma 2 Kopf',
                                    'Wasserstrahl 1 Kopf Trennschnitt aussen / Qualitätsschnitt innen',
                                    'Sägen', 'Laser 2 Kopf Qualitätsschnitt',
                                    'Sägen Trennschnitt',
                                    'Sägen 1 Kopf Qualitätsschnitt',
                                    'Wasserstrahl',
                                    'Plasma 1 Kopf Qualitätsschnitt',
                                    'Wasserstrahl 2 Kopf Trennschnitt aussen / Qualitätsschnitt innen',
                                    'Laser 1 Kopf',
                                    'Plasma',
                                    'Plasma 1 Kopf Trennschnitt aussen / Qualitätsschnitt innen',
                                    'Laser', 'Laser 2 Kopf Trennschnitt aussen / Qualitätsschnitt innen',
                                    'Wasserstrahl 1 Kopf Qualitätsschnitt',
                                    'Laser 1 Kopf Trennschnitt',
                                    'Plasma 2 Kopf Trennschnitt',
                                    'Laser Trennschnitt',
                                    'Plasma Qualitätsschnitt',
                                    'Wasserstrahl 1 Kopf Qualitätsschnitt aussen / Trennschnitt innen',
                                    'Plasma 2 Kopf Qualitätsschnitt',
                                    'Wasserstrahl Trennschnitt',
                                    'Laser 1 Kopf Trennschnitt aussen / Qualitätsschnitt innen',
                                    'Wasserstrahl 2 Kopf',
                                    'Plasma Trennschnitt',
                                    'Wasserstrahl Trennschnitt aussen / Qualitätsschnitt innen',
                                    'Wasserstrahl 2 Kopf Qualitätsschnitt aussen / Trennschnitt innen',
                                    '',
                                ]
                            },
                            "SchleifenUnten": {
                                "type": "string",
                                "description": "Describes the grinding method on the lower side, if this is desired by the client.",
                                "enum": ['Bandschleifen', 'Präz.-Schleifen', ""]
                            },
                            "SchleifenOben": {
                                "type": "string",
                                "description": "Describes the grinding method on the upper side, if this is desired by the client.",
                                "enum": ['Bandschleifen', 'Präz.-Schleifen', ""]
                            }
                        },
                        "required": [
                            "Positionstyp",
                            "Position",
                            "Form",
                            "Menge",
                            "Laenge",
                            "Breite",
                            "Dicke",
                            "Werkstoff",
                            "Oberflächengüte",
                            "Norm",
                            "Zeugnis",
                            "Schneiden",
                            "SchleifenUnten",
                            "SchleifenOben",
                            "Quality Test"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            "required": [
                "Kunde",
                "Datum",
                "Positionen"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}


schema_PT = {
    "type": "json_schema",
    "json_schema":
    {
        "name": "order_schema",
        "schema": {
            "type": "object",
            "properties": {
                "Bestellung-Nr": {
                    "type": "string",
                    "description": "The number/ID of the order."
                },
                "Datum": {
                    "type": "string",
                    "description": "The date of the order."
                },
                "Projekt/Kommissions-Nr": {
                    "type": "string",
                    "description": "The project or commission number of the order."
                },
                "Positionen": {
                    "type": "array",
                    "description": "List of items in the order.",
                    "items": {
                        "type": "object",
                        "properties": {

                            "Position": {
                                "type": "number",
                                "description": "The position number of the item."
                            },
                            "Menge": {
                                "type": "number",
                                "description": "The quantity of the item."
                            },
                            "Artikel": {
                                "type": "string",
                                "description": "The name of the item.",
                            },
                            "Laenge": {
                                "type": "number",
                                "description": "The length of the item , which is described in the size description."
                            },
                            "Breite": {
                                "type": "number",
                                "description": "The width of the item , which is described in the size description."
                            },
                            "Höhe": {
                                "type": "number",
                                "description": "The height of the item."
                            },
                            "Material": {
                                "type": "string",
                                "description": "The material of the item, which is described. This could be described like 'Vierkant-Stahl' or something similar or described as a material Code."
                            },
                            "Norm": {
                                "type": "string",
                                "description": "The normed standard demanded for the product. These could be international, european or german standards, which usually are indicated by DIN, EN or ASME at the beginning."
                            },
                            "Zeugnis": {
                                "type": "string",
                                "description": "The certificate required to the item. This could be for example WZ 3.1 or similar.",

                            },
                            "Oberfläche": {
                                "type": "string",
                                "description": "This describes the surface quality of the item.",

                            }
                        },
                        "required": [

                            "Position",
                            "Menge",
                            "Artikel",
                            "Laenge",
                            "Breite",
                            "Höhe",
                            "Material",
                            "Norm",
                            "Zeugnis",
                            "Oberfläche"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            "required": [
                "Bestellung-Nr",
                "Datum",
                "Projekt/Kommissions-Nr",
                "Positionen"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}
