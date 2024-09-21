from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_socketio import SocketIO  # Import SocketIO
import threading
import time

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)  # Initialize SocketIO

# Array and loop management
array = [1, 2, 3]
global is_running, loop_thread
lock = threading.Lock()

def start_loop():
    """Continuously rearranges the array every second while is_running is True."""
    global array, is_running
    while is_running:
        with lock:
            array.append(array.pop(0))  # Rotate array
            print(f"Array rearranged: {array}")
            socketio.emit('update_data', {'data': array})  # Emit updated array to clients
        time.sleep(1)

@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    """Start the looping process to rearrange the array."""
    if is_running:
        # If already running, stop it before starting a new one
        stop()  # Call the stop function
    is_running = True
    loop_thread = threading.Thread(target=start_loop)
    loop_thread.start()
    return jsonify({"message": "Loop started."}), 200

@app.route('/stop', methods=['POST'])
def stop():
    """Stop the looping process."""
    global is_running  # Declare as global first
    if is_running:
        is_running = False
        return jsonify({"message": "Loop stopped."}), 200
    return jsonify({"message": "Loop is not running."}), 400

@app.route('/metrics', methods=['GET'])
def metrics():
    """Return the current state of the array."""
    with lock:
        current_array = array.copy()
    return jsonify({"current_array": current_array}), 200

if __name__ == '__main__':
    is_running = False  # Ensure starting state is known
    loop_thread = None
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

