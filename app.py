from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for SocketIO

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('control')
def handle_control(data):
    direction = data['direction']
    print(f"Received command: {direction}")
    socketio.emit('command_received', {'status': 'Command processed'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
