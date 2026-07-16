"""Themed vocabulary. Each entry: hi (Devanagari), translit, en (English), gender (m/f/None)."""

def w(hi, translit, en, gender=None):
    return {"hi": hi, "translit": translit, "en": en, "gender": gender}

VOCAB = {
    "Numbers 1-20": [
        w("एक", "ek", "one"), w("दो", "do", "two"), w("तीन", "teen", "three"), w("चार", "chaar", "four"),
        w("पांच", "paanch", "five"), w("छह", "chhah", "six"), w("सात", "saat", "seven"), w("आठ", "aaTh", "eight"),
        w("नौ", "nau", "nine"), w("दस", "das", "ten"), w("ग्यारह", "gyaarah", "eleven"), w("बारह", "baarah", "twelve"),
        w("तेरह", "terah", "thirteen"), w("चौदह", "chaudah", "fourteen"), w("पंद्रह", "pandrah", "fifteen"),
        w("सोलह", "solah", "sixteen"), w("सत्रह", "satrah", "seventeen"), w("अठारह", "aThaarah", "eighteen"),
        w("उन्नीस", "unnees", "nineteen"), w("बीस", "bees", "twenty"),
    ],
    "Numbers - tens": [
        w("तीस", "tees", "thirty"), w("चालीस", "chaalees", "forty"), w("पचास", "pachaas", "fifty"),
        w("साठ", "saaTh", "sixty"), w("सत्तर", "sattar", "seventy"), w("अस्सी", "assee", "eighty"),
        w("नब्बे", "nabbe", "ninety"), w("सौ", "sau", "hundred"), w("हज़ार", "hazaar", "thousand"),
    ],
    "Family": [
        w("परिवार", "parivaar", "family", "m"), w("माता / माँ", "maataa / maan", "mother", "f"),
        w("पिता / पापा", "pitaa / paapaa", "father", "m"), w("भाई", "bhaai", "brother", "m"),
        w("बहन", "bahan", "sister", "f"), w("बेटा", "beTaa", "son", "m"), w("बेटी", "beTee", "daughter", "f"),
        w("पति", "pati", "husband", "m"), w("पत्नी", "patnee", "wife", "f"),
        w("दादा", "daadaa", "paternal grandfather", "m"), w("दादी", "daadee", "paternal grandmother", "f"),
        w("नाना", "naanaa", "maternal grandfather", "m"), w("नानी", "naanee", "maternal grandmother", "f"),
        w("चाचा", "chaachaa", "uncle (father's younger brother)", "m"), w("मामा", "maamaa", "uncle (mother's brother)", "m"),
        w("दोस्त", "dost", "friend", None), w("बच्चा", "bachchaa", "child", "m"),
    ],
    "Food & Dining": [
        w("खाना", "khaanaa", "food", "m"), w("पानी", "paanee", "water", "m"), w("चावल", "chaaval", "rice", "m"),
        w("रोटी", "roTee", "flatbread", "f"), w("दाल", "daal", "lentils", "f"), w("सब्ज़ी", "sabzee", "vegetables", "f"),
        w("दूध", "doodh", "milk", "m"), w("चीनी", "cheenee", "sugar", "f"), w("नमक", "namak", "salt", "m"),
        w("मसाला", "masaalaa", "spice", "m"), w("चम्मच", "chammach", "spoon", "m"), w("बिल", "bil", "bill/check", "m"),
        w("फल", "phal", "fruit", "m"), w("सेब", "seb", "apple", "m"), w("केला", "kelaa", "banana", "m"),
        w("चाय", "chaay", "tea", "f"), w("कॉफ़ी", "kofee", "coffee", "f"), w("मीठा", "meeThaa", "sweet/dessert", "m"),
        w("अंडा", "andaa", "egg", "m"), w("मांस", "maans", "meat", "m"),
    ],
    "Time & Days": [
        w("समय", "samay", "time", "m"), w("घंटा", "ghanTaa", "hour", "m"), w("मिनट", "minat", "minute", "m"),
        w("आज", "aaj", "today", None), w("कल", "kal", "yesterday/tomorrow", None), w("परसों", "parson", "day before/after", None),
        w("सुबह", "subah", "morning", "f"), w("दोपहर", "dopahar", "afternoon", "f"), w("शाम", "shaam", "evening", "f"),
        w("रात", "raat", "night", "f"), w("सोमवार", "somvaar", "Monday", "m"), w("मंगलवार", "mangalvaar", "Tuesday", "m"),
        w("बुधवार", "budhvaar", "Wednesday", "m"), w("गुरुवार", "guruvaar", "Thursday", "m"),
        w("शुक्रवार", "shukravaar", "Friday", "m"), w("शनिवार", "shanivaar", "Saturday", "m"), w("रविवार", "ravivaar", "Sunday", "m"),
        w("हफ्ता", "haftaa", "week", "m"), w("महीना", "maheenaa", "month", "m"), w("साल", "saal", "year", "m"),
    ],
    "Colors": [
        w("लाल", "laal", "red"), w("नीला", "neelaa", "blue"), w("हरा", "haraa", "green"), w("पीला", "peelaa", "yellow"),
        w("काला", "kaalaa", "black"), w("सफ़ेद", "safed", "white"), w("गुलाबी", "gulaabee", "pink"), w("नारंगी", "naarangee", "orange"),
        w("बैंगनी", "baingnee", "purple"), w("भूरा", "bhooraa", "brown"),
    ],
    "Shopping & Money": [
        w("दुकान", "dukaan", "shop", "f"), w("बाज़ार", "baazaar", "market", "m"), w("कीमत", "qeemat", "price", "f"),
        w("सस्ता", "sastaa", "cheap", "m"), w("महंगा", "mahangaa", "expensive", "m"), w("पैसा", "paisaa", "money", "m"),
        w("रुपया", "rupayaa", "rupee", "m"), w("छूट", "chhooT", "discount", "f"), w("साइज़", "saaiz", "size", "m"),
        w("बड़ा", "baDaa", "big", "m"), w("छोटा", "choTaa", "small", "m"),
    ],
    "Directions & Transport": [
        w("रास्ता", "raastaa", "way/path", "m"), w("दायें", "daayen", "right", None), w("बायें", "baayen", "left", None),
        w("सीधे", "seedhe", "straight", None), w("पास", "paas", "near", None), w("दूर", "door", "far", None),
        w("स्टेशन", "sTeshan", "station", "m"), w("हवाई अड्डा", "havaai aDDaa", "airport", "m"), w("टैक्सी", "taiksee", "taxi", "f"),
        w("बस", "bas", "bus", "f"), w("ट्रेन", "Tren", "train", "f"), w("गाड़ी", "gaaDee", "car/vehicle", "f"),
    ],
    "Body Parts": [
        w("सिर", "sir", "head", "m"), w("आँख", "aankh", "eye", "f"), w("नाक", "naak", "nose", "f"),
        w("कान", "kaan", "ear", "m"), w("मुँह", "munh", "mouth", "m"), w("हाथ", "haath", "hand", "m"),
        w("पैर", "pair", "foot/leg", "m"), w("पेट", "peT", "stomach", "m"), w("दिल", "dil", "heart", "m"),
        w("बाल", "baal", "hair", "m"),
    ],
    "Animals": [
        w("कुत्ता", "kuttaa", "dog", "m"), w("बिल्ली", "billee", "cat", "f"), w("गाय", "gaay", "cow", "f"),
        w("घोड़ा", "ghoDaa", "horse", "m"), w("हाथी", "haathee", "elephant", "m"), w("शेर", "sher", "lion", "m"),
        w("बंदर", "bandar", "monkey", "m"), w("पक्षी / चिड़िया", "pakshee / chiDiyaa", "bird", "f"),
        w("मछली", "machhlee", "fish", "f"), w("साँप", "saanp", "snake", "m"),
    ],
    "Weather & Nature": [
        w("मौसम", "mausam", "weather", "m"), w("बारिश", "baarish", "rain", "f"), w("धूप", "dhoop", "sunshine", "f"),
        w("हवा", "havaa", "wind/air", "f"), w("बादल", "baadal", "cloud", "m"), w("गर्मी", "garmee", "heat/summer", "f"),
        w("सर्दी", "sardee", "cold/winter", "f"), w("पेड़", "peD", "tree", "m"), w("फूल", "phool", "flower", "m"),
        w("आसमान", "aasmaan", "sky", "m"),
    ],
    "Professions": [
        w("डॉक्टर", "doktar", "doctor", None), w("शिक्षक / अध्यापक", "shikshak / adhyaapak", "teacher", "m"),
        w("इंजीनियर", "injiniyar", "engineer", None), w("वकील", "vakeel", "lawyer", None), w("किसान", "kisaan", "farmer", "m"),
        w("व्यापारी", "vyaapaaree", "businessperson", None), w("छात्र", "chhaatra", "student", "m"), w("नर्स", "nars", "nurse", "f"),
    ],
    "Common Adjectives": [
        w("अच्छा", "achchhaa", "good"), w("बुरा", "buraa", "bad"), w("सुंदर", "sundar", "beautiful"),
        w("नया", "nayaa", "new"), w("पुराना", "puraanaa", "old (things)"), w("गर्म", "garm", "hot"),
        w("ठंडा", "ThanDaa", "cold"), w("आसान", "aasaan", "easy"), w("मुश्किल", "mushkil", "difficult"),
        w("खुश", "khush", "happy"), w("उदास", "udaas", "sad"), w("थका", "thakaa", "tired"),
    ],
    "Question Words": [
        w("क्या", "kyaa", "what"), w("कौन", "kaun", "who"), w("कहाँ", "kahaan", "where"), w("कब", "kab", "when"),
        w("क्यों", "kyon", "why"), w("कैसे", "kaise", "how"), w("कितना", "kitnaa", "how much/many"),
    ],
    "Pronouns": [
        w("मैं", "main", "I"), w("तू", "too", "you (intimate)"), w("तुम", "tum", "you (informal)"),
        w("आप", "aap", "you (formal)"), w("यह", "yah", "he/she/it (this)"), w("वह", "vah", "he/she/it (that)"),
        w("हम", "ham", "we"), w("ये", "ye", "they (these)"), w("वे", "ve", "they (those)"),
    ],
}

def all_vocab_flat():
    flat = []
    for theme, words in VOCAB.items():
        for item in words:
            e = dict(item)
            e["theme"] = theme
            flat.append(e)
    return flat
