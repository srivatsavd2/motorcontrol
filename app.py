from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('control')
def handle_control(data):
    direction = data['direction']
    print(f"Received command: {direction}")
    socketio.emit('command_received', {'status': 'Command processed'})

if __name__ == '__main__':
    print("hi")
    
    socketio.run(app, host='0.0.0.0', port=5000)
