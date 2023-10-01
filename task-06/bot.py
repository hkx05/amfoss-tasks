import discord
import csv
from scraper import get_cricket_score

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.content.startswith('/livescore'):
        t1, t1_score, t2, t2_score, status = get_cricket_score()  # Call your web scraping function

        # Send the message
        await message.channel.send(f'{t1} : {t1_score}\n{t2} : {t2_score}\nstatus : {status}')

        # Append data to CSV
        with open('history.csv', mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            data = [t1, t1_score, t2, t2_score, status]
            csv_writer.writerow(data)

        if message.content.startswith('/generate'):
            with open('history.csv', 'rb') as file:
                await message.channel.send(file=discord.File(file, 'history.csv'))
        
        if message.content.startswith('/help'):
            await message.channel.send('Commands :\n/livescore - get the livescore.\n/generate - get the csv of the previous livescores')
  
client.run('MTE1NDc5ODUzMDE4NDA5NzgyMw.Grj0ip.DzM0aFdCkiImCH_zskh8zUAkwVNMxL-bP5IK0c')