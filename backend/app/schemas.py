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
                            "Masse": {
                                "type": "number",
                                "description": "The mass of the item, described in kg. If not provided, keep this blank or 0.0."
                            },
                            "Stück": {
                                "type": "number",
                                "description": "The quantity of the item. If not provided, keep this blank or 0.0. If its only written in text as 'eine', 'zwei' and so on, please set the quantity accordingly."
                            },
                            "Artikel": {
                                "type": "string",
                                "description": "The name of the item.",
                            },
                            "Laenge": {
                                "type": "number",
                                "description": "The length of the item , which is described in the size description. If 3 sizes are available it has to be interpreted like 'length x width x height'."
                            },
                            "Breite": {
                                "type": "number",
                                "description": "The width of the item , which is described in the size description. If 3 sizes are available, width is always the medium one. 'VK' stands for 'Vierkant' and means, that the provided size after is the width and height at the same time. 'FL' stands for 'Flach' and means, that the provided sizes after describe the width and height of the item.If 3 sizes are available it has to be interpreted like 'length x width x height'."
                            },
                            "Höhe": {
                                "type": "number",
                                "description": "The height of the item, which is described in the size description. If 3 sizes are available, height is always the smallest one. 'VK' stands for 'Vierkant' and means, that the provided size after is the width and height at the same time. 'FL' stands for 'Flach' and means, that the provided sizes after describe the width and height of the item.If 3 sizes are available it has to be interpreted like 'length x width x height'."
                            },
                            "Material": {
                                "type": "string",
                                "description": "The material of the item, which is described. This has to be described in a EN normed format. The following dictionary describes all possible options. If only the Code in the keys is provided, this has to be mapped to the correct value. Otherwise, if one of the values is provided, this will be the correct material. "
                            },
                            "Norm": {
                                "type": "string",
                                "description": "The normed standard demanded for the product. These could be international, european or german standards, which usually are indicated by DIN, EN or ASME at the beginning followed by a numeric Code like 'DIN/EN 12345'."
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
                            "Masse",
                            "Stück",
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



schema_Joke = {
    "type": "json_schema",
    "json_schema":
    {
        "name": "order_schema",
        "schema": {
            "type": "object",
            "properties": {
                "Dokumententyp": {
                    "type": "string",
                    "enum" : ["Rechnung", "Bestellung", "Bestellbestätigung", ""],
                    "description": "The type of the provided document."
                },
                "Rechnungsnummer": {
                    "type": "string",
                    "description": "Invoice number, if the document type is an invoice or if the document provides an invoice number."
                },
                "Bestellnummer": {
                    "type": "string",
                    "description": "Order number, if the document type is a order or if the document provides an order number."
                },
                "Auftragsnummer": {
                    "type": "string",
                    "description": "Job number, if the document type is an order or order confirmation or if the document provides a job number."
                },
                "Datum": {
                    "type": "string",
                    "description": "The document date."
                },
                "Kundennummer": {
                    "type": "string",
                    "description": "the client number or client ID."
                },
                "Ansprechpartner": {
                    "type": "string",
                    "description": "The contact person provided in the document."
                },
                "Lieferant": {
                    "type": "string",
                    "description": "The name of the delivering company."
                },
                "Lieferantennummer": {
                    "type": "string",
                    "description": "The number/ID of the delivering company."
                },
                "Lieferadresse" : {
                    "type": "string",
                    "description": "The delivery address of the client."
                },
                "Versandadresse" : {
                    "type": "string",
                    "description": "The shipping address of the client."
                },
                "Positionen": {
                    "type": "array",
                    "description": "List of items in the order.",
                    "items": {
                        "type": "object",
                        "properties": {

                            "Position": {
                                "type": "string",
                                "description": "The position number of the item."
                            },
                            "Artikelnummer": {
                                "type": "string",
                                "description": "The article number of the item."
                            },
                            "Artikelbezeichnung": {
                                "type": "string",
                                "description": "The name of the item and the underlying description."
                            },
                            "Referenznummer": {
                                "type": "string",
                                "description": "The reference number of the item."
                            },
                            "Kundenartikelnummer": {
                                "type": "string",
                                "description": "The customer article number of the item."
                            },
                            "Verpackungseinheit Stück": {
                                "type": "number",
                                "description": "the number of items per packaging unit."
                            },
                            "Stück": {
                                "type": "number",
                                "description": "The quanitity of items or packaging units."
                            },
                            "Lieferdatum": {
                                "type": "string",
                                "description": "The delivery date of the item.",
                            },
                            "Einzelpreis": {
                                "type": "number",
                                "description": "The single price per item."
                            },
                            "Positionspreis": {
                                "type": "number",
                                "description": "The aggregated price per position for all items."
                            },
                            "Artikeldurchmesser": {
                                "type": "number",
                                "description": "The diameter of the item , which is described in the size description."
                            },
                            "Artikelbreite": {
                                "type": "number",
                                "description": "The width of the item , which is described in the size description."
                            },
                            "Artikellänge": {
                                "type": "number",
                                "description": "The length of the item , which is described in the size description."
                            },
                            "Artikelhöhe": {
                                "type": "number",
                                "description": "The height of the item, which is described in the size description."
                            }
                        },
                        "required": [

                            "Position",
                            "Artikelnummer",
                            "Artikelbezeichnung",
                            "Stück",
                            "Einzelpreis",
                            "Positionspreis"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            "required": [
                "Dokumententyp",
                "Datum",
                "Positionen"
            ],
            "additionalProperties": False
        },
        "strict": False
    }
}

schema_Joke2 = {
    "type": "json_schema",
    "json_schema": {
        "name": "order_schema",
        "schema": {
            "type": "object",
            "properties": {
                "Dokumententyp": {
                    "type": "object",
                    "description": "The type of the provided document.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "enum": ["Rechnung", "Bestellung", "Bestellbestätigung", ""],
                            "description": "The type of the provided document."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score between 0 (uncertain) and 1 (very certain) for this attribute."
                        }
                    },
                    "required": ["value", "confidence"]
                },
                "Rechnungsnummer": {
                    "type": "object",
                    "description": "Invoice number, if the document type is an invoice or if the document provides an invoice number.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "Invoice number, if the document type is an invoice or if the document provides an invoice number."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Rechnungsnummer."
                        }
                    }
                },
                "Bestellnummer": {
                    "type": "object",
                    "description": "Order number, if the document type is a order or if the document provides an order number.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "Order number, if the document type is a order or if the document provides an order number."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Bestellnummer."
                        }
                    }
                },
                "Auftragsnummer": {
                    "type": "object",
                    "description": "Job number, if the document type is an order or order confirmation or if the document provides a job number.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "Job number, if the document type is an order or order confirmation or if the document provides a job number."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Auftragsnummer."
                        }
                    }
                },
                "Datum": {
                    "type": "object",
                    "description": "The document date.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The document date."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Datum."
                        }
                    }
                },
                "Kundennummer": {
                    "type": "object",
                    "description": "the client number or client ID.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "the client number or client ID."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Kundennummer."
                        }
                    }
                },
                "Ansprechpartner": {
                    "type": "object",
                    "description": "The contact person provided in the document.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The contact person provided in the document."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Ansprechpartner."
                        }
                    }
                },
                "Lieferant": {
                    "type": "object",
                    "description": "The name of the delivering company.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The name of the delivering company."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Lieferant."
                        }
                    }
                },
                "Lieferantennummer": {
                    "type": "object",
                    "description": "The number/ID of the delivering company.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The number/ID of the delivering company."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Lieferantennummer."
                        }
                    }
                },
                "Lieferadresse": {
                    "type": "object",
                    "description": "The delivery address of the client.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The delivery address of the client."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Lieferadresse."
                        }
                    }
                },
                "Versandadresse": {
                    "type": "object",
                    "description": "The shipping address of the client.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The shipping address of the client."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Versandadresse."
                        }
                    }
                },
                "Positionen": {
                    "type": "array",
                    "description": "List of items in the order.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Position": {
                                "type": "object",
                                "description": "The position number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The position number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Position."
                                    }
                                }
                            },
                            "Artikelnummer": {
                                "type": "object",
                                "description": "The article number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The article number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelnummer."
                                    }
                                }
                            },
                            "Artikelbezeichnung": {
                                "type": "object",
                                "description": "The name of the item and the underlying description.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The name of the item and the underlying description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelbezeichnung."
                                    }
                                }
                            },
                            "Referenznummer": {
                                "type": "object",
                                "description": "The reference number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The reference number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Referenznummer."
                                    }
                                }
                            },
                            "Kundenartikelnummer": {
                                "type": "object",
                                "description": "The customer article number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The customer article number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Kundenartikelnummer."
                                    }
                                }
                            },
                            "Verpackungseinheit Stück": {
                                "type": "object",
                                "description": "the number of items per packaging unit.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "the number of items per packaging unit."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Verpackungseinheit Stück."
                                    }
                                }
                            },
                            "Stück": {
                                "type": "object",
                                "description": "The quanitity of items or packaging units.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The quanitity of items or packaging units."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Stück."
                                    }
                                }
                            },
                            "Lieferdatum": {
                                "type": "object",
                                "description": "The delivery date of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The delivery date of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Lieferdatum."
                                    }
                                }
                            },
                            "Einzelpreis": {
                                "type": "object",
                                "description": "The single price per item.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The single price per item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Einzelpreis."
                                    }
                                }
                            },
                            "Positionspreis": {
                                "type": "object",
                                "description": "The aggregated price per position for all items.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The aggregated price per position for all items."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Positionspreis."
                                    }
                                }
                            },
                            "Artikeldurchmesser": {
                                "type": "object",
                                "description": "The diameter of the item , which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The diameter of the item , which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikeldurchmesser."
                                    }
                                }
                            },
                            "Artikelbreite": {
                                "type": "object",
                                "description": "The width of the item , which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The width of the item , which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelbreite."
                                    }
                                }
                            },
                            "Artikellänge": {
                                "type": "object",
                                "description": "The length of the item , which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The length of the item , which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikellänge."
                                    }
                                }
                            },
                            "Artikelhöhe": {
                                "type": "object",
                                "description": "The height of the item, which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The height of the item, which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelhöhe."
                                    }
                                }
                            }
                        },
                        "required": [
                            "Position",
                            "Artikelnummer",
                            "Artikelbezeichnung",
                            "Stück",
                            "Einzelpreis",
                            "Positionspreis"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            "required": [
                "Dokumententyp",
                "Datum",
                "Positionen"
            ],
            "additionalProperties": False
        },
        "strict": False
    }
}


schema_Fischer = {
    "type": "json_schema",
    "json_schema": {
        "name": "order_schema",
        "schema": {
            "type": "object",
            "properties": {
                "Dokumententyp": {
                    "type": "object",
                    "description": "The type of the provided document.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "enum": ["Rechnung", "Bestellung", "Bestellbestätigung", "Kundenanfrage", ""],
                            "description": "The type of the provided document."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score between 0 (uncertain) and 1 (very certain) for this attribute."
                        }
                    },
                    "required": ["value", "confidence"]
                },
                "Kundename" : {
                    "type": "object",
                    "description": "name of the client who the document was created from.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "name of the client who the document was created from.",
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Kundenname."
                        }
                    }
                },
                "Anfragenummer" : {
                    "type": "object",
                    "description": "document number, if the document is of type 'Anfrager'.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "document number, if the document is of type 'Anfrager'.",
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Anfragenummer."
                        }
                    }
                },
                "Rechnungsnummer": {
                    "type": "object",
                    "description": "Invoice number, if the document type is an invoice or if the document provides an invoice number.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "Invoice number, if the document type is an invoice or if the document provides an invoice number."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Rechnungsnummer."
                        }
                    }
                },
                "Bestellnummer": {
                    "type": "object",
                    "description": "Order number, if the document type is a order or if the document provides an order number.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "Order number, if the document type is a order or if the document provides an order number."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Bestellnummer."
                        }
                    }
                },
                "Auftragsnummer": {
                    "type": "object",
                    "description": "Job number, if the document type is an order or order confirmation or if the document provides a job number.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "Job number, if the document type is an order or order confirmation or if the document provides a job number."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Auftragsnummer."
                        }
                    }
                },
                "Datum": {
                    "type": "object",
                    "description": "The document date.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The document date."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Datum."
                        }
                    }
                },
                "Kundennummer": {
                    "type": "object",
                    "description": "the client number or client ID.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "the client number or client ID."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Kundennummer."
                        }
                    }
                },
                "Ansprechpartner": {
                    "type": "object",
                    "description": "The contact person provided in the document.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The contact person provided in the document."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Ansprechpartner."
                        }
                    }
                },
                "Lieferant": {
                    "type": "object",
                    "description": "The name of the delivering company.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The name of the delivering company."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Lieferant."
                        }
                    }
                },
                "Lieferantennummer": {
                    "type": "object",
                    "description": "The number/ID of the delivering company.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The number/ID of the delivering company."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Lieferantennummer."
                        }
                    }
                },
                "Lieferadresse": {
                    "type": "object",
                    "description": "The delivery address of the client.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The delivery address of the client."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Lieferadresse."
                        }
                    }
                },
                "Versandadresse": {
                    "type": "object",
                    "description": "The shipping address of the client.",
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "The shipping address of the client."
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score for Versandadresse."
                        }
                    }
                },
                "Positionen": {
                    "type": "array",
                    "description": "List of items in the order.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Position": {
                                "type": "object",
                                "description": "The position number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The position number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Position."
                                    }
                                }
                            },
                            "Artikelnummer": {
                                "type": "object",
                                "description": "The article number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The article number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelnummer."
                                    }
                                }
                            },
                            "Artikelbezeichnung": {
                                "type": "object",
                                "description": "The name of the item and the underlying description.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The name of the item and the underlying description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelbezeichnung."
                                    }
                                }
                            },
                            "Referenznummer": {
                                "type": "object",
                                "description": "The reference number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The reference number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Referenznummer."
                                    }
                                }
                            },
                            "Kundenartikelnummer": {
                                "type": "object",
                                "description": "The customer article number of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The customer article number of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Kundenartikelnummer."
                                    }
                                }
                            },
                            "Verpackungseinheit Stück": {
                                "type": "object",
                                "description": "the number of items per packaging unit.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "the number of items per packaging unit."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Verpackungseinheit Stück."
                                    }
                                }
                            },
                            "Stück": {
                                "type": "object",
                                "description": "The quanitity of items or packaging units.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The quanitity of items or packaging units."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Stück."
                                    }
                                }
                            },
                            "Lieferdatum": {
                                "type": "object",
                                "description": "The delivery date of the item.",
                                "properties": {
                                    "value": {
                                        "type": "string",
                                        "description": "The delivery date of the item."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Lieferdatum."
                                    }
                                }
                            },
                            "Einzelpreis pro Einheit": {
                                "type": "object",
                                "description": "The single price per unit.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The single price per unit."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Einzelpreis pro Einheit."
                                    }
                                }
                            },
                            "Menge pro Einheit": {
                                "type": "object",
                                "description": "quantity of items per unit, which 'Einzelpreis pro Einheit' is calculated on.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "quantity of items per unit, which 'Einzelpreis pro Einheit' is calculated on."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Menge pro Einheit."
                                    }
                                }
                            },
                            "Positionspreis": {
                                "type": "object",
                                "description": "The aggregated price per position for all items.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The aggregated price per position for all items."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Positionspreis."
                                    }
                                }
                            },
                            "Artikeldurchmesser": {
                                "type": "object",
                                "description": "The diameter of the item , which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The diameter of the item , which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikeldurchmesser."
                                    }
                                }
                            },
                            "Artikelbreite": {
                                "type": "object",
                                "description": "The width of the item , which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The width of the item , which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelbreite."
                                    }
                                }
                            },
                            "Artikellänge": {
                                "type": "object",
                                "description": "The length of the item , which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The length of the item , which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikellänge."
                                    }
                                }
                            },
                            "Artikelhöhe": {
                                "type": "object",
                                "description": "The height of the item, which is described in the size description.",
                                "properties": {
                                    "value": {
                                        "type": "number",
                                        "description": "The height of the item, which is described in the size description."
                                    },
                                    "confidence": {
                                        "type": "number",
                                        "description": "Confidence score for Artikelhöhe."
                                    }
                                }
                            }
                        },
                        "required": [
                            "Position",
                            "Artikelnummer",
                            "Artikelbezeichnung",
                            "Stück",
                            "Einzelpreis",
                            "Positionspreis"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            "required": [
                "Dokumententyp",
                "Datum",
                "Positionen"
            ],
            "additionalProperties": False
        },
        "strict": False
    }
}
