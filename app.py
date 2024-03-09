from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY_CHALLENGE_WEBSOCKET'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')  # indicate what template will be called


@socketio.on('message') # creating an event
def handle_message(msg):
    print(f"mensagem recebida: {msg}")
    # The method emit serves to create an event to send to client side.
    # The parameter broadcast when is enabled, transmit the messages to all users logged.
    emit('message', msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
