from flask import Flask, render_template, request

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
        print('ID:', user_id)
        print('Password:', user_pwd)
        return 'Success'
    return render_template('login.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        form_data = request.form
        return 'Success'
    return render_template('join.html')


if __name__ == '__main__':
    app.run(host='localhost', debug=True)