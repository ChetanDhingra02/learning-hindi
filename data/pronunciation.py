"""Pronunciation-focused lesson content (sound system deep dive)."""

PRONUNCIATION_INTRO = """
Hindi is almost perfectly phonetic — once you master the sound system below, you can
pronounce virtually any word correctly on sight. English/French speakers usually need
focused practice on two contrasts that don't exist in their native languages: **aspiration**
and **retroflex consonants**. Use the audio buttons throughout this app to hear native
pronunciation (requires an internet connection the first time each word is played; audio is
cached locally afterward).
"""

VOWEL_LENGTH_NOTE = """
### Vowel length matters — it changes meaning
Hindi vowels come in short/long pairs: **इ/ई** (i/ii), **उ/ऊ** (u/uu). These aren't just
stylistic — mixing them up can change the word entirely:

- सिल (sil, "grinding stone") vs. सील (siil, "seal/stamp")
- पुल (pul, "bridge") vs. फूल (phuul, "flower")

Practice holding the long vowels roughly twice as long as the short ones.
"""

ASPIRATION_NOTE = """
### Aspiration: क vs ख, प vs फ, त vs थ...
Hold a strip of paper or a lit match in front of your mouth.

- **Unaspirated** (क, प, त, ट, च): the paper should barely move — no puff of air.
- **Aspirated** (ख, फ, थ, ठ, छ): the paper should flap sharply — a real puff of breath.

English speakers naturally aspirate "p, t, k" at the start of words (say "pin" and you'll
feel it) — so your natural English "p" sound is actually closer to Hindi's **फ**, not **प**.
This is the #1 giveaway of a foreign accent — practice consciously suppressing aspiration on
unaspirated letters.
"""

RETROFLEX_NOTE = """
### Retroflex vs Dental: ट vs त, ड vs द, ण vs न
- **Dental**: touch your tongue tip to the back of your top front teeth. Softer than English t/d.
- **Retroflex**: curl your tongue tip up and back toward the roof of your mouth, then release.

This distinction doesn't exist in English or French — it takes deliberate ear training.

| Dental (soft) | Retroflex (curled back) |
|---|---|
| ताला (taalaa) — lock | टाला (Taalaa) — avoided |
| दाल (daal) — lentils | डाल (Daal) — branch |
| नाली (naalii) — drain | (rare initial retroflex ण) |
"""

NASAL_NOTE = """
### Nasal vowels (leverage your French!)
Hindi nasalizes vowels using **ं** (anusvara) or **ँ** (chandrabindu) — a vowel pronounced
partly through the nose. If you speak French, you already produce this sound in words like
*bon* or *un*. Compare:

- है (hai, "is") vs. हैं (hain, "are" — plural/formal)
- हा (haa, exclamation) vs. हाँ (haan, "yes")
"""

STRESS_NOTE = """
### Word stress
Hindi stress is lighter and more even across syllables than English — avoid the strong
English habit of heavily stressing one syllable and reducing the others to a schwa. Aim
for a more even rhythm, closer to French.
"""

SYLLABLE_TIPS = """
### Reading any new word: a 3-step method
1. **Break it into aksharas** (consonant+vowel units) — Devanagari is built this way, so
   read letter-cluster by letter-cluster, not sound by sound.
2. **Watch for conjuncts** (two consonants glued together with no vowel between — a halant
   join) — these represent a consonant cluster pronounced together, like the "sk" in "skool".
3. **Check word-final consonants** — a bare consonant at the very end of a word usually drops
   its inherent "a" sound in speech (this app's transliteration already reflects that): किताब
   is "kitaab", not "kitaaba".
"""
