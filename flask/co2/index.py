from flask import Flask
from flask import request, jsonify
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=['POST'])
def index():
    dict_data = {}
    data = request.get_data()
    print(data)
    if data:
        data_str = data.decode('utf-8')
        data_str = data_str.replace('?', '')
        params = data_str.split('&')

        for param in params:
            param_data = param.split('=')
            param_key = param_data[0]
            param_value = param_data[1] or '0'
            dict_data[param_key] = param_value
        socketio.emit('update', dict_data)
    return jsonify(dict_data)
    
@app.route("/page", methods=['GET'])
def page():
    return render_template('index.html')

app.run(host='0.0.0.0', port=12345)