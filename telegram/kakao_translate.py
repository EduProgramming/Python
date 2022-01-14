from decouple import config
import requests

API_URL = 'https://dapi.kakao.com'
method = '/v2/translation/translate'

APP_KEY = config('KAKAO_API_TOKEN')

headers = {
    'Authorization': f'KakaoAK {APP_KEY}',
    'Content-type': 'application/x-www-form-urlencoded'
}

data = {
    'query': '안녕하세요. 문장이 번역되는지 확인합니다.\n 누가누가누가',
    'src_lang': 'kr',
    'target_lang': 'en'
}

response = requests.post(API_URL+method, headers=headers, data=data)

if response.status_code == 200:
    result = response.json()
    sentence = ''
    translated_text = result.get('translated_text')
    for text in translated_text:
        sentence += text[0] + ' '

    print(sentence)