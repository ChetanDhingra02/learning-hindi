"""Builds a unified searchable index across vocab, phrases, verbs, and alphabet."""
from data.vocab import all_vocab_flat
from data.phrases import all_phrases_flat
from data.verbs import VERBS
from data.alphabet import ALL_LETTERS


def build_index():
    entries = []

    for v in all_vocab_flat():
        entries.append({
            "hi": v["hi"], "translit": v["translit"], "en": v["en"],
            "type": "Vocabulary", "category": v["theme"], "extra": v.get("gender") or "",
        })

    for p in all_phrases_flat():
        entries.append({
            "hi": p["hi"], "translit": p["translit"], "en": p["en"],
            "type": "Phrase", "category": p["category"], "extra": "",
        })

    for key, v in VERBS.items():
        entries.append({
            "hi": v["hi"], "translit": v["translit"], "en": v["meaning"],
            "type": "Verb", "category": "Verbs", "extra": v.get("note", ""),
        })

    for l in ALL_LETTERS:
        entries.append({
            "hi": l["hi"], "translit": l["translit"], "en": f"({l['type']})",
            "type": "Letter", "category": "Devanagari Script", "extra": "",
        })

    return entries


def search(entries, query):
    if not query or not query.strip():
        return []
    q = query.strip().lower()
    results = []
    for e in entries:
        haystack = f"{e['hi']} {e['translit']} {e['en']} {e['category']}".lower()
        if q in haystack:
            results.append(e)
    return results
