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





### 참고내용

- psycopg2 psycopg2-binary

https://stackoverflow.com/questions/70330567/what-is-the-different-about-psycopg2-and-psycopg2-binary-python-package