"""Generates randomized, self-checkable homework worksheets from the app's data pools."""
import random
import re

from data.vocab import all_vocab_flat, VOCAB
from data.phrases import all_phrases_flat
from data.verbs import VERBS, PRONOUNS, PRONOUN_LABELS
from utils.transliterate import transliterate


def normalize(s):
    """Loose normalization for comparing user-typed transliteration answers."""
    s = s.lower().strip()
    s = re.sub(r"[^a-z]", "", s)
    s = re.sub(r"(.)\1+", r"\1", s)  # collapse doubled letters (aa->a, kk->k etc.)
    return s


def build_worksheet(topic, n=10):
    """topic: 'Script Basics' | 'Vocabulary' | 'Verbs' | 'Phrases' | 'Mixed Review'"""
    exercises = []

    def vocab_translate_q(item):
        return {
            "type": "type_answer",
            "prompt": f"How do you say **\"{item['en']}\"** in Hindi? (type the transliteration)",
            "accept": [item["translit"]],
            "reveal": f"{item['hi']} ({item['translit']})",
        }

    def vocab_recognize_q(item, pool):
        others = [x["en"] for x in pool if x["en"] != item["en"]]
        random.shuffle(others)
        options = others[:3] + [item["en"]]
        random.shuffle(options)
        return {"type": "mcq", "prompt": f"What does **{item['hi']}** ({item['translit']}) mean?",
                "options": options, "answer": item["en"]}

    def phrase_translate_q(item):
        return {
            "type": "type_answer",
            "prompt": f"How do you say **\"{item['en']}\"** in Hindi? (type the transliteration)",
            "accept": [item["translit"]],
            "reveal": f"{item['hi']} ({item['translit']})",
        }

    def verb_conjugate_q():
        vkey = random.choice(list(VERBS.keys()))
        verb = VERBS[vkey]
        tense = random.choice(["present", "future"])
        pronoun = random.choice(PRONOUNS)
        gender_idx = random.choice([0, 1])
        gender_word = "masculine" if gender_idx == 0 else "feminine"
        correct = verb[tense][pronoun][gender_idx]
        correct_translit = transliterate(correct)
        subj = PRONOUN_LABELS[pronoun]
        return {
            "type": "type_answer",
            "prompt": f"Conjugate **{verb['hi']}** ({verb['meaning']}) for {subj}, {gender_word} subject, {tense} tense. (type the transliteration)",
            "accept": [correct_translit],
            "reveal": f"{correct} ({correct_translit})",
        }

    vocab_pool = all_vocab_flat()
    phrase_pool = all_phrases_flat()

    if topic == "Vocabulary":
        items = random.sample(vocab_pool, min(n, len(vocab_pool)))
        for i, item in enumerate(items):
            if i % 2 == 0:
                exercises.append(vocab_translate_q(item))
            else:
                exercises.append(vocab_recognize_q(item, vocab_pool))

    elif topic == "Phrases":
        items = random.sample(phrase_pool, min(n, len(phrase_pool)))
        for item in items:
            exercises.append(phrase_translate_q(item))

    elif topic == "Verbs":
        for _ in range(n):
            exercises.append(verb_conjugate_q())

    elif topic == "Mixed Review":
        pool_funcs = []
        vitems = random.sample(vocab_pool, min(n, len(vocab_pool)))
        pitems = random.sample(phrase_pool, min(max(1, n // 3), len(phrase_pool)))
        for item in vitems[: n // 2]:
            exercises.append(vocab_translate_q(item) if random.random() > 0.5 else vocab_recognize_q(item, vocab_pool))
        for item in pitems:
            exercises.append(phrase_translate_q(item))
        while len(exercises) < n:
            exercises.append(verb_conjugate_q())
        exercises = exercises[:n]
        random.shuffle(exercises)

    return exercises



