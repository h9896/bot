from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import cropy

bot = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('0tYqNww5XfdxS4da6XOVJb1aGgi69ECvrpzmC8uaSi0Dx7NJZn1QuC0ZeWbueHyVyZvzpinse65AoEqNCNYQJDsN32AyUPbvnGy4kPzJhRZWZgiJxy1CBcSw+49f+YaXbDZJ66VUJap5Yd7Pt/FlcwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2178286775facf5086cae13a98e6ef32')

# 監聽所有來自 /callback 的 Post Request
@bot.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    bot.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    lis = ["BTC", "ETH", "ZEC", "XRP"]
    msg = msg.upper()
    if msg not in lis:
        print("Sorry this crypto currency is not in service!")
        print("Please type again!")
        content = "Sorry this crypto currency is not in service!"
    else:
        p = cropy.price(msg).last_price()
        print("{0}/USD: {1}".format(msg, p))
        content = "{0}/USD: {1}".format(msg, p)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = content))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    bot.run(host='0.0.0.0', port=port)