import openai
import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('token'))
openai.api_key = os.getenv('openai')

@bot.message_handler(func=lambda _: True)
def handle_message(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.7,
    max_tokens=1024,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  bot.send_message(chat_id=message.from_user.id, text=response['choices'] [0] ['text'])


bot.polling()