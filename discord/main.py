
import discord
import datetime
import requests
from bs4 import BeautifulSoup as bs
import re

DISCORD_BOT_TOKEN = ''
URL = '' # 학교 URL

ANIMAL_URL = {
	'고양이': 'https://api.thecatapi.com/v1/images/search',
	'강아지': 'https://api.thedogapi.com/v1/images/search',
}

MEALS = {'조식': 0, '중식': 1, '석식': 2}

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# 정규 표현식
def rep(content):
    rep_content = re.sub(r'[^가-힣]', '', content)
    return rep_content

# The Cat/Dog API
def get_animal_data(url):
	response = requests.get(url)
	img_url = 'https://blog.kakaocdn.net/dn/cihkwk/btrXVhcYJdR/de6bdvpkPI5iJv7w1iVzm0/img.png'
	if response.status_code == 200:
		data = response.json()
		img_url = data[0].get('url')
	return img_url

# 식단 가져오기: 학교마다 수정 필요
def get_meal_data(idx):
    now = datetime.datetime.now().strftime('%Y%m%d')
    response = requests.get(URL, params={'ymd': now})
    if response.status_code == 200:
        html = response.text
        soup = bs(html, 'html.parser')

        result = f'{now} 데이터가 없습니다.'
        data_list = soup.select('#usm-content-body-id > ul.tch-lnc-list > li.tch-lnc-wrap')
        if data_list and len(data_list) > idx:
            split_data_list = data_list[idx].text.strip().split('\n')
            result_data_list = []
            for data in split_data_list:
                if data:
                    result_data_list.append(rep(data))
            
            select_meal = result_data_list[0]
            result = f'[{select_meal}:{now}]'
            for data in result_data_list[1:]:
                result += '\n-' + data

        return result

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!'):
        if message.content[1:3] in MEALS:
            meal_data = get_meal_data(MEALS[message.content[1:3]])
            await message.channel.send(meal_data)
        elif message.content[1:4] in ANIMAL_URL:
            target = message.content[1:4]
            img_url = get_animal_data(ANIMAL_URL[target])
            embed = discord.Embed(title=target, color=discord.Color.random())
            embed.set_image(url=img_url)
            await message.channel.send(embed=embed)

client.run(DISCORD_BOT_TOKEN)