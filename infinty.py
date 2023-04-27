import os
import openai
from aiogram import Bot, Dispatcher, executor , types

bot = Bot(token ="6225470956:AAHQCvLFgnBeQNLLWv-ZZzCw5IsHZFIWFIA")
dp = Dispatcher(bot)

openai.api_key ="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"

@dp.message_handler(commands = ['start','help'])
async def welcome(message:types.Message):
    await message.reply("hello i am GPT Infinty chat bot. ask me anything")

@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message.text,
  temperature=0.5,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0
  )
  await message.reply(response.choices[0].text)
  
if __name__ == "__main__":
   executor.start_polling(dp)

