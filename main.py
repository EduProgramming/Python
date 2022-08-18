from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    form_data = request.form
    user_id = form_data.get('user-id')
    user_pwd = form_data.get('user-pwd')
    print('ID:', user_id)
    print('Password:', user_pwd)
    return 'Success'


if __name__ == '__main__':
    app.run(host='localhost', debug=True)