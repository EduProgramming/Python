from flask import Flask, render_template, request
import database as db # database.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user_id = form_data.get('user-id')
        user_pwd = form_data.get('user-pwd')
        data = db.is_login(user_id, user_pwd)
        if data:
            return "Success"
        return "Fail"
    return render_template('login.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        form_data = request.form
        return 'Success'
    return render_template('join.html')

@app.route("/likes", methods=["GET","POST"])
def likes():
    if request.method == "POST":
        likes = db.likes(1)
        return str(likes)
    likes = db.counting_likes()
    if likes:
        likes = likes[0]
    # TODO: Session을 통해서 유저의 데이터를 받으면 해당 유저가 Like를 눌렀는지 안눌렀는지 파악 필요
    #     -> DB에서 SELECT한 후에 결과에 따라 처리되게 해야함
    # Flask의 Jinja2 문법 사용을 위해 -> likes를 페이지 렌더링을하면서 보냄
    return render_template("likes.html", likes = likes)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)