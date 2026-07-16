"""Conversational phrases by category."""

def ph(hi, translit, en):
    return {"hi": hi, "translit": translit, "en": en}

PHRASES = {
    "Greetings": [
        ph("नमस्ते", "namaste", "hello / goodbye"),
        ph("आप कैसे हैं?", "aap kaise hain?", "How are you? (formal)"),
        ph("मैं ठीक हूँ", "main Theek hoon", "I am fine"),
        ph("आपका नाम क्या है?", "aapkaa naam kyaa hai?", "What is your name? (formal)"),
        ph("मेरा नाम ___ है", "meraa naam ___ hai", "My name is ___"),
        ph("आप कहाँ से हैं?", "aap kahaan se hain?", "Where are you from?"),
        ph("मैं ___ से हूँ", "main ___ se hoon", "I am from ___"),
        ph("आपसे मिलकर खुशी हुई", "aapse milkar khushee huee", "Nice to meet you"),
        ph("फिर मिलेंगे", "phir milenge", "see you again"),
        ph("शुभ रात्रि", "shubh raatri", "good night"),
    ],
    "Politeness": [
        ph("धन्यवाद / शुक्रिया", "dhanyavaad / shukriyaa", "thank you"),
        ph("कृपया", "kripayaa", "please"),
        ph("माफ़ कीजिए", "maaf keejiye", "excuse me / sorry"),
        ph("कोई बात नहीं", "koee baat naheen", "no problem / you're welcome"),
        ph("हाँ", "haan", "yes"),
        ph("नहीं", "naheen", "no"),
        ph("कृपया धीरे बोलिए", "kripayaa dheere boliye", "Please speak slowly"),
        ph("मुझे हिंदी नहीं आती", "mujhe hindee naheen aatee", "I don't know Hindi"),
        ph("क्या आप अंग्रेज़ी बोलते हैं?", "kyaa aap angrezee bolte hain?", "Do you speak English?"),
    ],
    "Dining": [
        ph("मेनू दिखाइए", "menu dikhaaiye", "Show me the menu"),
        ph("एक पानी की बोतल दीजिए", "ek paanee kee botal deejiye", "Give me a bottle of water"),
        ph("यह बहुत स्वादिष्ट है", "yah bahut svaadishT hai", "This is very delicious"),
        ph("बिल दीजिए", "bil deejiye", "Bring the bill"),
        ph("मुझे भूख लगी है", "mujhe bhookh lagee hai", "I am hungry"),
        ph("मुझे प्यास लगी है", "mujhe pyaas lagee hai", "I am thirsty"),
    ],
    "Shopping": [
        ph("इसकी कीमत क्या है?", "iskee qeemat kyaa hai?", "What is the price of this?"),
        ph("क्या छूट मिलेगी?", "kyaa chhooT milegee?", "Will I get a discount?"),
        ph("यह बहुत महंगा है", "yah bahut mahangaa hai", "This is very expensive"),
        ph("मैं यह लूँगा / लूँगी", "main yah loongaa / loongee", "I will take this (m/f)"),
    ],
    "Directions": [
        ph("स्टेशन कहाँ है?", "sTeshan kahaan hai?", "Where is the station?"),
        ph("सीधे जाइए", "seedhe jaaiye", "Go straight"),
        ph("दायें मुड़िए", "daayen muDiye", "Turn right"),
        ph("बायें मुड़िए", "baayen muDiye", "Turn left"),
        ph("कितनी दूर है?", "kitnee door hai?", "How far is it?"),
    ],
    "Emergencies": [
        ph("मदद कीजिए!", "madad keejiye!", "Help!"),
        ph("मुझे डॉक्टर चाहिए", "mujhe doktar chaahiye", "I need a doctor"),
        ph("पुलिस को बुलाइए", "pulis ko bulaaiye", "Call the police"),
        ph("मैं खो गया / गई हूँ", "main kho gayaa / gaee hoon", "I am lost (m/f)"),
    ],
    "Small Talk": [
        ph("आज मौसम कैसा है?", "aaj mausam kaisaa hai?", "How's the weather today?"),
        ph("आपका काम क्या है?", "aapkaa kaam kyaa hai?", "What do you do (for work)?"),
        ph("मुझे यह पसंद है", "mujhe yah pasand hai", "I like this"),
        ph("मुझे समझ नहीं आया", "mujhe samajh naheen aayaa", "I didn't understand"),
        ph("कृपया दोहराइए", "kripayaa doharaaiye", "Please repeat"),
    ],
}

def all_phrases_flat():
    flat = []
    for cat, items in PHRASES.items():
        for item in items:
            e = dict(item)
            e["category"] = cat
            flat.append(e)
    return flat
