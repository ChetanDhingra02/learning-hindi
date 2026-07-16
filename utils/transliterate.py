"""
A rule-based Devanagari -> readable Roman transliterator.
Not a full linguistic model, but handles: matras, halant/conjuncts, nukta letters,
anusvara/chandrabindu/visarga, and word-final schwa (inherent 'a') deletion,
which is what makes output actually readable/speakable (e.g. "kitaab" not "kitaaba").
"""

VOWEL_INDEP = {
    "अ": "a", "आ": "aa", "इ": "i", "ई": "ii", "उ": "u", "ऊ": "uu",
    "ऋ": "ri", "ॠ": "rii", "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au",
    "ऍ": "ae", "ऑ": "aw", "अं": "an", "अः": "ah",
}
MATRA = {
    "ा": "aa", "ि": "i", "ी": "ii", "ु": "u", "ू": "uu",
    "ृ": "ri", "ॄ": "rii", "े": "e", "ै": "ai", "ो": "o", "ौ": "au",
    "ॅ": "ae", "ॉ": "aw",
}
CONSONANTS = {
    "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ng",
    "च": "ch", "छ": "chh", "ज": "j", "झ": "jh", "ञ": "ny",
    "ट": "T", "ठ": "Th", "ड": "D", "ढ": "Dh", "ण": "N",
    "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
    "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
    "य": "y", "र": "r", "ल": "l", "व": "v",
    "श": "sh", "ष": "Sh", "स": "s", "ह": "h",
}
NUKTA_MAP = {  # consonant + nukta -> borrowed sound
    "क": "q", "ख": "kh", "ग": "g", "ज": "z", "ड": "r", "ढ": "rh", "फ": "f", "य": "y",
}
SPECIAL_CLUSTERS = {  # literal 3-codepoint sequences (consonant + halant + consonant)
    "क्ष": "ksh", "ज्ञ": "gy", "त्र": "tr", "श्र": "shr", "द्य": "dy",
}
HALANT = "\u094d"
NUKTA = "\u093c"
ANUSVARA = "\u0902"
CHANDRABINDU = "\u0901"
VISARGA = "\u0903"


def _translit_word(word):
    out = []
    i, n = 0, len(word)
    while i < n:
        # try 3-codepoint special clusters first
        triplet = word[i:i + 3]
        if triplet in SPECIAL_CLUSTERS:
            base_sound = SPECIAL_CLUSTERS[triplet]
            i += 3
            out.append(_finish_consonant(base_sound, word, i, n))
            # _finish_consonant tells us how many extra chars it consumed via return + we re-derive i
            i = _advance_after_consonant(word, i, n)
            continue

        ch = word[i]

        if ch in VOWEL_INDEP:
            out.append(VOWEL_INDEP[ch])
            i += 1
            continue

        if ch in CONSONANTS:
            base_sound = CONSONANTS[ch]
            j = i + 1
            if j < n and word[j] == NUKTA:
                base_sound = NUKTA_MAP.get(ch, base_sound)
                j += 1
            # what follows the consonant?
            if j < n and word[j] == HALANT:
                out.append(base_sound)  # no vowel, conjunct continues
                i = j + 1
                continue
            elif j < n and word[j] in MATRA:
                out.append(base_sound + MATRA[word[j]])
                i = j + 1
                continue
            elif j < n and word[j] == ANUSVARA:
                out.append(base_sound + "an")
                i = j + 1
                continue
            elif j < n and word[j] == CHANDRABINDU:
                out.append(base_sound + "an")
                i = j + 1
                continue
            elif j < n and word[j] == VISARGA:
                out.append(base_sound + "ah")
                i = j + 1
                continue
            else:
                # bare consonant, inherent 'a' -- drop it if this is the last letter of the word
                if j == n:
                    out.append(base_sound)
                else:
                    out.append(base_sound + "a")
                i = j
                continue

        if ch == ANUSVARA:
            out.append("n")
            i += 1
            continue
        if ch == CHANDRABINDU:
            out.append("n")
            i += 1
            continue
        if ch == VISARGA:
            out.append("h")
            i += 1
            continue
        if ch == "।":
            out.append(".")
            i += 1
            continue
        if ch in (HALANT, NUKTA):
            i += 1
            continue
        # punctuation / spaces / digits / anything else: pass through
        out.append(ch)
        i += 1
    return "".join(out)


def _finish_consonant(base_sound, word, i, n):
    """Handle what follows a multi-codepoint special cluster (same logic as single consonant)."""
    if i < n and word[i] == HALANT:
        return base_sound
    elif i < n and word[i] in MATRA:
        return base_sound + MATRA[word[i]]
    elif i < n and word[i] == ANUSVARA:
        return base_sound + "an"
    elif i < n and word[i] == VISARGA:
        return base_sound + "ah"
    else:
        if i == n:
            return base_sound
        return base_sound + "a"


def _advance_after_consonant(word, i, n):
    if i < n and word[i] == HALANT:
        return i + 1
    elif i < n and word[i] in MATRA:
        return i + 1
    elif i < n and word[i] in (ANUSVARA, VISARGA, CHANDRABINDU):
        return i + 1
    return i


def transliterate(text):
    """Public entry point. Handles multi-word phrases (splits on spaces, keeps punctuation)."""
    if not text:
        return ""
    parts = text.split(" ")
    return " ".join(_translit_word(p) for p in parts)


if __name__ == "__main__":
    tests = ["पानी", "धन्यवाद", "नमस्ते", "किताब", "स्कूल", "ज्ञान", "अच्छा",
             "राजा", "लड़का", "ठंडा", "मैं", "हूँ", "कैसे", "अनार", "ऋषि", "औरत",
             "पता", "स्थान", "इंटरनेट", "पासवर्ड", "मेरा नाम राज है।"]
    for t in tests:
        print(t, "->", transliterate(t))
