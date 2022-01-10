from decouple import config
import requests

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
APP_KEY = config('KAKAO_API_TOKEN')

# Telegram -> Image 넘어오는 데이터 형식 파악 필요

# 1. 로컬 파일에서 진행
# 2. 웹 URL 주소를 통한 진행
# 3. Telegram Image를 통해 넘어오는 데이터 확인

headers = {
    'Authorization': f'KakaoAK {APP_KEY}'
}

try:
    files = {'image': open('./assets/test.jpg', 'rb')}
    response = requests.post(API_URL, headers=headers, files=files)
    if response.status_code == 200:
        result = response.json()
        facial_attributes = result['result']['faces'][0]['facial_attributes']
        gender = facial_attributes.get('gender')
        if gender['male'] > gender['female']:
            print('남자', end=' ')
        else:
            print('여자', end=' ')
        age = facial_attributes.get('age')
        print(f'{int(age)} 살 추정')
except FileNotFoundError as e:
    print(e)