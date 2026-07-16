"""Devanagari script data: vowels, consonants, matras, special marks."""

VOWELS = [
    {"hi": "अ", "translit": "a", "sound": 'like "u" in "but"', "example": "अनार (anaar) — pomegranate"},
    {"hi": "आ", "translit": "aa", "sound": 'like "a" in "father", held longer', "example": "आम (aam) — mango"},
    {"hi": "इ", "translit": "i", "sound": 'like "i" in "sit"', "example": "इमली (imli) — tamarind"},
    {"hi": "ई", "translit": "ii", "sound": 'like "ee" in "see", held longer', "example": "ईख (eekh) — sugarcane"},
    {"hi": "उ", "translit": "u", "sound": 'like "u" in "put"', "example": "उल्लू (ullu) — owl"},
    {"hi": "ऊ", "translit": "uu", "sound": 'like "oo" in "food", held longer', "example": "ऊन (oon) — wool"},
    {"hi": "ऋ", "translit": "ri", "sound": 'a tapped "ri", tongue curls back briefly', "example": "ऋषि (rishi) — sage"},
    {"hi": "ए", "translit": "e", "sound": 'pure "ay" (no glide), like French "été"', "example": "एक (ek) — one"},
    {"hi": "ऐ", "translit": "ai", "sound": 'like "a" in "cat", open and long', "example": "ऐनक (ainak) — glasses"},
    {"hi": "ओ", "translit": "o", "sound": 'pure "o" (no glide), like French "eau"', "example": "ओस (os) — dew"},
    {"hi": "औ", "translit": "au", "sound": 'like "aw" in "law"', "example": "औरत (aurat) — woman"},
]

CONSONANT_GROUPS = [
    {"group": "Velars", "note": "back of tongue against soft palate", "letters": [
        {"hi": "क", "translit": "ka", "sound": "unaspirated k, no puff of air", "example": "कमल (kamal) — lotus"},
        {"hi": "ख", "translit": "kha", "sound": "aspirated k, strong puff of air", "example": "खरगोश (khargosh) — rabbit"},
        {"hi": "ग", "translit": "ga", "sound": 'like "g" in "go"', "example": "गमला (gamla) — flowerpot"},
        {"hi": "घ", "translit": "gha", "sound": "aspirated g", "example": "घर (ghar) — house"},
        {"hi": "ङ", "translit": "nga", "sound": 'nasal "ng" as in "sing" — rare alone', "example": "गंगा (gangaa) — Ganges"},
    ]},
    {"group": "Palatals", "note": "middle of tongue against hard palate", "letters": [
        {"hi": "च", "translit": "cha", "sound": "unaspirated ch, light", "example": "चाय (chaay) — tea"},
        {"hi": "छ", "translit": "chha", "sound": "aspirated ch", "example": "छत (chhat) — roof"},
        {"hi": "ज", "translit": "ja", "sound": 'like "j" in "jam"', "example": "जल (jal) — water"},
        {"hi": "झ", "translit": "jha", "sound": "aspirated j", "example": "झूला (jhoola) — swing"},
        {"hi": "ञ", "translit": "nya", "sound": 'nasal "ny" — rare, mostly in conjuncts', "example": "ज्ञान (gyaan) — knowledge"},
    ]},
    {"group": "Retroflex", "note": "curl tongue tip back — no English/French equivalent", "letters": [
        {"hi": "ट", "translit": "Ta", "sound": 'hard, tongue curled back, like American "tt" in "butter"', "example": "टमाटर (tamaatar) — tomato"},
        {"hi": "ठ", "translit": "Tha", "sound": "aspirated retroflex t", "example": "ठंड (Thand) — cold"},
        {"hi": "ड", "translit": "Da", "sound": "retroflex d", "example": "डमरू (Damroo) — small drum"},
        {"hi": "ढ", "translit": "Dha", "sound": "aspirated retroflex d", "example": "ढोल (Dhol) — drum"},
        {"hi": "ण", "translit": "Na", "sound": "retroflex n", "example": "बाण (baaN) — arrow"},
    ]},
    {"group": "Dentals", "note": "tongue tip on back of front teeth — softer than English t/d", "letters": [
        {"hi": "त", "translit": "ta", "sound": "unaspirated dental t", "example": "तारा (taara) — star"},
        {"hi": "थ", "translit": "tha", "sound": "aspirated dental t", "example": "थाली (thaali) — plate"},
        {"hi": "द", "translit": "da", "sound": "dental d", "example": "दवा (davaa) — medicine"},
        {"hi": "ध", "translit": "dha", "sound": "aspirated dental d", "example": "धनुष (dhanush) — bow"},
        {"hi": "न", "translit": "na", "sound": "dental n", "example": "नमक (namak) — salt"},
    ]},
    {"group": "Labials", "note": "both lips together", "letters": [
        {"hi": "प", "translit": "pa", "sound": "unaspirated p, no puff", "example": "पानी (paani) — water"},
        {"hi": "फ", "translit": "pha", "sound": 'aspirated p — like English "p" in "pin"', "example": "फल (phal) — fruit"},
        {"hi": "ब", "translit": "ba", "sound": 'like "b" in "boy"', "example": "बकरी (bakri) — goat"},
        {"hi": "भ", "translit": "bha", "sound": "aspirated b", "example": "भालू (bhaalu) — bear"},
        {"hi": "म", "translit": "ma", "sound": 'like "m" in "mother"', "example": "मछली (machhli) — fish"},
    ]},
    {"group": "Semivowels", "note": "", "letters": [
        {"hi": "य", "translit": "ya", "sound": 'like "y" in "yes"', "example": "यह (yah) — this"},
        {"hi": "र", "translit": "ra", "sound": "lightly tapped/rolled r", "example": "राजा (raaja) — king"},
        {"hi": "ल", "translit": "la", "sound": 'like "l" in "love"', "example": "लड़का (ladka) — boy"},
        {"hi": "व", "translit": "va", "sound": 'between English "v" and "w"', "example": "वन (van) — forest"},
    ]},
    {"group": "Sibilants & aspirate", "note": "", "letters": [
        {"hi": "श", "translit": "sha", "sound": 'like "sh" in "shine"', "example": "शेर (sher) — lion"},
        {"hi": "ष", "translit": "Sha", "sound": "retroflex sh — rare", "example": "भाषा (bhaasha) — language"},
        {"hi": "स", "translit": "sa", "sound": 'like "s" in "sun"', "example": "सेब (seb) — apple"},
        {"hi": "ह", "translit": "ha", "sound": 'like "h" in "house"', "example": "हाथी (haathi) — elephant"},
    ]},
    {"group": "Compound letters", "note": "treated as extra consonants", "letters": [
        {"hi": "क्ष", "translit": "ksha", "sound": "k + sh blended", "example": "क्षमा (kshama) — forgiveness"},
        {"hi": "त्र", "translit": "tra", "sound": "t + r blended", "example": "त्रिकोण (trikon) — triangle"},
        {"hi": "ज्ञ", "translit": "gya", "sound": 'pronounced "gya"', "example": "ज्ञान (gyaan) — knowledge"},
        {"hi": "श्र", "translit": "shra", "sound": "sh + r blended", "example": "श्री (shri) — Mr./respected"},
    ]},
]

MATRAS = [
    {"mark": "(none — inherent a)", "with_ka": "क", "sound": "ka"},
    {"mark": "ा", "with_ka": "का", "sound": "kaa"},
    {"mark": "ि  (written BEFORE the consonant!)", "with_ka": "कि", "sound": "ki"},
    {"mark": "ी", "with_ka": "की", "sound": "kii"},
    {"mark": "ु", "with_ka": "कु", "sound": "ku"},
    {"mark": "ू", "with_ka": "कू", "sound": "kuu"},
    {"mark": "ृ", "with_ka": "कृ", "sound": "kri"},
    {"mark": "े", "with_ka": "के", "sound": "ke"},
    {"mark": "ै", "with_ka": "कै", "sound": "kai"},
    {"mark": "ो", "with_ka": "को", "sound": "ko"},
    {"mark": "ौ", "with_ka": "कौ", "sound": "kau"},
]

SPECIAL_MARKS = [
    {"mark": "ं", "name": "Anusvara", "function": "Nasalizes the preceding vowel", "example": "हिंदी (hindi) — Hindi"},
    {"mark": "ँ", "name": "Chandrabindu", "function": "Nasalizes an open vowel", "example": "हाँ (haan) — yes"},
    {"mark": "ः", "name": "Visarga", "function": "Light echoing 'h' sound, Sanskrit-derived words", "example": "दुःख (duhkh) — sorrow"},
    {"mark": "़", "name": "Nukta", "function": "Dot under a letter for borrowed sounds (Persian/Arabic/English)", "example": "ज़रा (zara) — a little"},
    {"mark": "्", "name": "Halant / Virama", "function": "Cancels the inherent 'a' — needed for conjuncts", "example": "भगवान् (bhagvaan) — God"},
]

CONJUNCTS = [
    {"conjunct": "स्क", "built_from": "s + k", "example": "स्कूल (skool) — school"},
    {"conjunct": "त्र", "built_from": "t + r", "example": "पत्र (patra) — letter"},
    {"conjunct": "द्व", "built_from": "d + v", "example": "द्वार (dvaar) — door"},
    {"conjunct": "क्त", "built_from": "k + t", "example": "शक्ति (shakti) — power"},
    {"conjunct": "न्द", "built_from": "n + d", "example": "चन्दन (chandan) — sandalwood"},
    {"conjunct": "स्थ", "built_from": "s + th", "example": "स्थान (sthaan) — place"},
]

READING_LADDER = [
    {"level": "1: two letters", "words": [("घर", "ghar", "house"), ("कल", "kal", "yesterday/tomorrow"), ("दिन", "din", "day"), ("नल", "nal", "tap")]},
    {"level": "2: three letters", "words": [("किताब", "kitaab", "book"), ("पानी", "paani", "water"), ("मकान", "makaan", "building"), ("समय", "samay", "time")]},
    {"level": "3: conjuncts", "words": [("स्कूल", "skool", "school"), ("नमस्ते", "namaste", "hello"), ("धन्यवाद", "dhanyavaad", "thank you"), ("दोस्त", "dost", "friend")]},
    {"level": "4: full sentence", "words": [("मेरा नाम राज है।", "meraa naam raaj hai.", "My name is Raj.")]},
]

ALL_LETTERS = [{"hi": v["hi"], "translit": v["translit"], "type": "vowel"} for v in VOWELS] + \
    [{"hi": l["hi"], "translit": l["translit"], "type": "consonant"} for g in CONSONANT_GROUPS for l in g["letters"]]
