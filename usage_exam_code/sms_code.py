"""
알리고 API 시스템을 통한 문자 보내기
1건당 금액 발생
"""

import requests
import csv

url = "https://apis.aligo.in/send/"


f = open(csv_file_name, 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    # Element: name = line[0]


    data = {
        'key': key_value,
        'user_id': user_id,
        'sender': sender_tel,
        'receiver': receiver_tel,
        'msg': f'message',
        'msg_type': 'LMS', #SMS:단문/LMS:장문/MMS:사진
    }

    res = requests.post(url, data)
    print(res.json())
f.close()