# readMe

Python Framework 중에 Flask를 이용하여 Client단과 연동을 해보자.

Client - Server - DB

- Client: 기본적인 HTML, CSS, JavaScript
- Server: Flask Framework
- DB: PostgreSQL



## install

```bash
$ pip install flask # Flask Framework
$ pip install psycopg2 # PostgreSQL 연결 라이브러리
```

> `psycopg2-binary`를 설치하여 진행하기도 합니다.
>
> psycopg2-binary의 경우에는 개발 및 테스트를 위한 실용적인 선택입니다.
>
> 배포용으로 생각한다면 빌드된 패키지인 psycopg2를 권장드립니다.


## 수업중 시간상 못다룬 내용

1. Material UI ICON

```html
<!-- CDN 추가 -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
    rel="stylesheet">

<!-- Favorite Icon -->
<!-- 선만 있는 하트 -->
<span class="material-icons">
    favorite_border
</span>

<!-- 채워진 하트 -->
<span class="material-icons">
    favorite
</span>
```

공식적으로 들어갔던 Material 사이트에서 나온 방식과는 다르게 해당 방안을 진행해야 되었습니다.

해당 부분에 대해서는 추후 더 살펴보고 파악되면 추가하여 올리도록 하겠습니다.

2. Likes INSERT & DELETE

`database.py`에서 close 함수 부분에 `conn.commit()`함수가 추가되었습니다.

```python
def close():
    conn.commit()
    cursor.close()
    conn.close()
```



### 참고내용

- psycopg2 psycopg2-binary

https://stackoverflow.com/questions/70330567/what-is-the-different-about-psycopg2-and-psycopg2-binary-python-package