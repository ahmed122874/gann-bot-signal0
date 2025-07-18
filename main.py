import requests

def send_telegram_message(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, data=data)
    return response.json()

# مثال إرسال إشارة
if __name__ == "__main__":
    token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    message = "🚨 إشارة تداول جديدة: شراء من 123.45 - TP1: 124 - TP2: 125 - TP3: 126 - SL: 122"
    print(send_telegram_message(token, chat_id, message))
