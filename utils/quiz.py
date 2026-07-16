"""Quiz generation helpers."""
import random


def mcq_from_vocab(pool, item, direction="hi_to_en", n_options=4):
    """Build a multiple-choice question. direction: 'hi_to_en' or 'en_to_hi'."""
    if direction == "hi_to_en":
        question = item["hi"]
        correct = item["en"]
        distractors_field = "en"
    else:
        question = item["en"]
        correct = item["hi"]
        distractors_field = "hi"

    others = [x[distractors_field] for x in pool if x is not item and x[distractors_field] != correct]
    random.shuffle(others)
    distractors = others[: n_options - 1]
    options = distractors + [correct]
    random.shuffle(options)
    return {"question": question, "correct": correct, "options": options, "item": item}


def mcq_from_letters(pool, item, n_options=4):
    """Devanagari letter -> transliteration sound quiz."""
    question = item["hi"]
    correct = item["translit"]
    others = [x["translit"] for x in pool if x is not item and x["translit"] != correct]
    random.shuffle(others)
    options = others[: n_options - 1] + [correct]
    random.shuffle(options)
    return {"question": question, "correct": correct, "options": options, "item": item}


def mcq_from_verb_form(verbs_dict, key, tense, pronoun, gender_idx, n_options=4):
    """Build a fill-in verb-conjugation MCQ. gender_idx: 0=masc, 1=fem."""
    verb = verbs_dict[key]
    correct = verb[tense][pronoun][gender_idx]
    # gather distractors from other forms of same verb + other verbs same tense/pronoun
    pool = []
    for k, v in verbs_dict.items():
        for p in v[tense]:
            for g in (0, 1):
                form = v[tense][p][g]
                if form != correct:
                    pool.append(form)
    random.shuffle(pool)
    options = list(dict.fromkeys(pool))[: n_options - 1] + [correct]
    options = list(dict.fromkeys(options))
    while len(options) < n_options and len(options) < len(pool):
        options.append(pool.pop())
    random.shuffle(options)
    return {"correct": correct, "options": options, "verb": verb, "pronoun": pronoun, "tense": tense, "gender_idx": gender_idx}
