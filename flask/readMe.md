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
<link
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
  rel="stylesheet"
/>

<!-- Favorite Icon -->
<!-- 선만 있는 하트 -->
<span class="material-icons"> favorite_border </span>

<!-- 채워진 하트 -->
<span class="material-icons"> favorite </span>
```

[https://developers.google.com/fonts/docs/material_icons#icon_font_for_the_web](https://developers.google.com/fonts/docs/material_icons#icon_font_for_the_web)

공식 홈페이지에 나와 있는 방법과 document에 나와 있는 사용 방식이 다르게 되어 있습니다.

페이지 상에서는

```html
<span class="material-icons-outlined">
  favorite_border
</span>
```

이러한 방식을 설명하고 있는 반면에,

```html
<span class="material-icons">
  favorite_border
</span>
```

문서 내에서는 위와 같이 설명하고 있습니다.

사용이 되는 방식은 문서에 기재되어 있는 방식을 사용해야 합니다.

class명이 `material-icons`를 사용하고 내부적은 text값이 해당 아이콘의 모양을 나타내는 방식을 취하고 있습니다.



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
