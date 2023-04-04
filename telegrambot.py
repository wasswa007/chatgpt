import telebot
import openai
import os

bot_token = 'put your telegram bot token here'
openai.api_key = "put your open ai key here"

bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def chat_with_openai(message):
    chat_id = message.chat.id
    text = message.text
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Conversation with the bot:\n\nUser: {text}\nBot:",
        temperature=0.5,
        max_tokens=2048,
        n=1,
        stop=None,
        timeout=15,
    )
    
    bot.reply_to(message, response.choices[0].text)

bot.polling()
