# Python Telegram

https://github.com/python-telegram-bot/python-telegram-bot

Python Telegram Bot 라이브러리를 사용하면 편리하지만, 일반적인 방안을 알아보기 위하여 기초적 방안으로 실행

## Install

Python Version >= 3.6

```bash
$ pip install flask
$ pip install requests
```

#### getUpdates

```json
{'ok': True,
 'result': [{'message': {'chat': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'last_name': 'Joung',
                                  'type': 'private'},
                         'date': 1640071166,
                         'entities': [{'length': 6,
                                       'offset': 0,
                                       'type': 'bot_command'}],
                         'from': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': 'Joung'},
                         'message_id': 1,
                         'text': '/start'},
             'update_id': 32058274},
            {'message': {'chat': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'last_name': 'Joung',
                                  'type': 'private'},
                         'date': 1640071218,
                         'from': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': 'Joung'},
                         'message_id': 2,
                         'sticker': {'emoji': '\ud83d\ude18',
                                     'file_id': 'CAACAgIAAxkBAAMCYcGAMkAsbboociOxxlTaToLyzq8AAgIAA8A2TxMI9W5F-oSnWSME',
                                     'file_size': 15955,
                                     'file_unique_id': 'AgADAgADwDZPEw',
                                     'height': 512,
                                     'is_animated': True,
                                     'set_name': 'HotCherry',
                                     'thumb': {'file_id': 'AAMCAgADGQEAAwJhwYAyQCxtuihyI7HGVNpOgvLOrwACAgADwDZPEwj1bkX6hKdZAQAHbQADIwQ',
                                               'file_size': 4498,
                                               'file_unique_id': 'AQADAgADwDZPE3I',
                                               'height': 128,
                                               'width': 128},
                                     'width': 512}},
             'update_id': 32058275},
            {'message': {'chat': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'last_name': 'Joung',
                                  'type': 'private'},
                         'date': 1640071235,
                         'entities': [{'length': 27,
                                       'offset': 0,
                                       'type': 'url'}],
                         'from': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': 'Joung'},
                         'message_id': 3,
                         'text': 'https://t.me/eduDevJTestBot'},
             'update_id': 32058276},
            {'message': {'chat': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'last_name': 'Joung',
                                  'type': 'private'},
                         'date': 1640133493,
                         'from': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': 'Joung'},
                         'message_id': 6,
                         'text': '확인'},
             'update_id': 32058277},
            {'message': {'chat': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'last_name': 'Joung',
                                  'type': 'private'},
                         'date': 1640133884,
                         'from': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': 'Joung'},
                         'message_id': 7,
                         'text': 'checkTest'},
             'update_id': 32058278},
            {'message': {'chat': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'last_name': 'Joung',
                                  'type': 'private'},
                         'date': 1640134158,
                         'from': {'first_name': 'TaeJune',
                                  'id': 123456789,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': 'Joung'},
                         'message_id': 8,
                         'text': 'update확인'},
             'update_id': 32058279}]}
```



## WebHook

### nGrok

https://ngrok.com/

```bash
ngrok http 5000
```



### Telegram WebHook

https://core.telegram.org/bots/api#setwebhook

**GET방식**

`https://api.telegram.org/bot{TOKEN}/setWebhook`

Webhook이 등록되어 있다면 DELETE역할



**POST방식**

`https://api.telegram.org/bot{TOKEN}/setWebhook?url={SSH_URL}/{TOKEN}`

HTTPS 인증서 있는 URL주소로만 가능



#### webhook Response Data

```json
# 텍스트
{
    "update_id": 32058283,
    "message": {
        "message_id": 12,
        "from": {
            "id": 123456789,
            "is_bot": False,
            "first_name": "TaeJune",
            "last_name": "Joung",
            "language_code": "ko"
        },
        "chat": {
            "id": 123456789,
            "first_name": "TaeJune",
            "last_name": "Joung",
            "type": "private"
        },
        "date": 1640224866,
        "text": "Test01"
        }
    }
}

# 이미지
{
    "update_id": 32058284, 
    "message": {
        "message_id": 13, 
        "from": {
            "id": 123456789, 
            "is_bot": False, 
            "first_name": "TaeJune", 
            "last_name": "Joung", 
            "language_code": "ko"
        }, 
        "chat": {
            "id": 123456789, 
            "first_name": "TaeJune", 
            "last_name": "Joung", 
            "type": "private"
        }, 
        "date": 1640225367, 
        "photo": [
            {
                "file_id": "AgACAgUAAxkBAAMNYcPaV2m3Osjly-j-8jyMw1oEqwYAAtuuMRvE0yBWVrY-vH7cHrYBAAMCAANzAAMjBA", 
                "file_unique_id": "AQAD264xG8TTIFZ4", 
                "file_size": 2033, 
                "width": 90, 
                "height": 68
            }, 
            {
                "file_id": "AgACAgUAAxkBAAMNYcPaV2m3Osjly-j-8jyMw1oEqwYAAtuuMRvE0yBWVrY-vH7cHrYBAAMCAANtAAMjBA", 
                "file_unique_id": "AQAD264xG8TTIFZy", 
                "file_size": 36326, 
                "width": 320, 
                "height": 242
            }, 
            {
                "file_id": "AgACAgUAAxkBAAMNYcPaV2m3Osjly-j-8jyMw1oEqwYAAtuuMRvE0yBWVrY-vH7cHrYBAAMCAAN4AAMjBA", 
                "file_unique_id": "AQAD264xG8TTIFZ9", 
                "file_size": 195102, 
                "width": 800, 
                "height": 606
            }, 
            {
                "file_id": "AgACAgUAAxkBAAMNYcPaV2m3Osjly-j-8jyMw1oEqwYAAtuuMRvE0yBWVrY-vH7cHrYBAAMCAAN5AAMjBA", 
                "file_unique_id": "AQAD264xG8TTIFZ-", 
                "file_size": 294766, 
                "width": 1280, 
                "height": 970
            }
        ]
    }
}

# 위치 정보
{
    "update_id": 32058285,
    "message": {
        "message_id": 14, 
        "from": {
            "id": 123456789, 
            "is_bot": False, 
            "first_name": "TaeJune", 
            "last_name": "Joung", 
            "language_code": "ko"
        }, 
        "chat": {
            "id": 123456789, 
            "first_name": "TaeJune", 
            "last_name": "Joung", 
            "type": "private"
        }, 
        "date": 1640225471, 
        "location": {
            "latitude": 10.12345, 
            "longitude": 123.456789
        }
    }
}
```



```bash
$ ps -fA | grep python
TaeJune+      51       1  0 02:24 pts/1498 00:00:00 grep python

$ kill 1

# 해당 프로세서들을 다 죽임
$ kill -9 $(ps -A | grep python | awk '{print $1}')
```

## KAKAO DEVELOPERS API

```bash
$ pip install python-decouple
```

API TOKEN 숨기기 위해 사용(`.env`파일)