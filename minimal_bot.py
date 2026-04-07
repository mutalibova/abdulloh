import urllib.request
import urllib.parse
import json
import time

BOT_TOKEN = "8451604369:AAFs_4ENgiyKwnlCpUaqBEX6T4xocTVDd_w"
CHAT_ID = "7411186644"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

# Inline tugmalar va javoblar
buttons = {
    "🛠 Texnik": "hozirda sizda tehnik muommo bo`lsa siz workmate ilovasidan chiqing va telefonni o`chirib yoqib yuboring va texnik muammo hal✔✔✔. murojat qilganinggiz uchun rahmat ❤❤❤💚     ",
    "👤 Profil": "agar sizda profile bilan bogliq muommo bo`lsa biz uni hal qilamiz nazarimda sizda shu muommolar bor masalan 1️⃣ birinchisi profile kodini unitish 2️⃣ profilega post qo`ya olmaslik  3️⃣ yana bitta muommo sizni profilizi hech kim koo`rmasligi biz buni tushundik tez orada moommoni bartaraf qilamiz❤❤❤💖",
    "🧱 ish o`rganish": "agar siz ish organish qismiga qanday kirishni bilmasangi men sizga buni o`rgataman birinchi workmate ilovasiga kiring pastdagi ishlar tugmasini bosing va oynadan hohlagan ishingizni tanlash qarabsizki siz ish o`rganishga tayyorsiz🎉🎉🎉🎉",
    "📄 til o`rganish": "siz til o`rganishni hohlasangiz workmate ilovasiga kirib tillar bo`limaga o`ting va hohlagan tilni tanlab organing va davlatlarga ish yuzasidan sayohat qiling✈✈🛬 ",
    "❓ Boshqa": "Boshqa muammolarni ham admin ko‘rib chiqadi."
}

def send_message(text, chat_id=CHAT_ID, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = BASE_URL + f"sendMessage?chat_id={chat_id}&text={text}"
    if reply_markup:
        reply_markup_json = urllib.parse.quote_plus(json.dumps(reply_markup))
        url += f"&reply_markup={reply_markup_json}"
    try:
        urllib.request.urlopen(url, timeout=5)
    except Exception as e:
        print("Xato yuborishda:", e)

def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    if offset:
        url += f"?offset={offset}"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read())
            return data
    except Exception as e:
        print("Xato olishda:", e)
        return {"result": []}

def main():
    last_update_id = None
    print("Bot ishga tushdi. /start yozing.")
    while True:
        updates = get_updates(offset=last_update_id)
        for update in updates.get("result", []):
            last_update_id = update["update_id"] + 1

            if "message" in update:
                message = update["message"]
                user_id = message["from"]["id"]
                text = message.get("text", "")

                # /start bosilganda inline tugmalar bilan muammo ko‘rsatish
                if text == "/start":
                    keyboard = {"inline_keyboard": [[{"text": k, "callback_data": k}] for k in buttons.keys()]}
                    send_message("Salom! Muammoingizni tanlang:", reply_markup=keyboard)
                    continue

            # Agar tugma bosilgan bo‘lsa, callback_query keladi
            if "callback_query" in update:
                callback = update["callback_query"]
                data = callback["data"]  # Tugma nomi
                chat_id = callback["message"]["chat"]["id"]
                # Tugma bo‘yicha javob
                response = buttons.get(data, "Admin tez orada javob beradi.")
                send_message(response, chat_id=chat_id)

        time.sleep(1)

if __name__ == "__main__":
    main()
