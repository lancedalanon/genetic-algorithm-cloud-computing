from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import threading
import time
import process  # Ensure this module is correctly implemented
import webbrowser
from engineio.async_drivers import gevent

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='gevent')  # Use gevent for asynchronous socket handling

# Global variable to control the data processing thread
processing_thread = None
is_processing = False
previous_fitness = 0  # Initialize previous fitness for improvement calculation

def process_data():
    """Function to simulate data processing and emit metrics."""
    global is_processing, previous_fitness

    while is_processing:
        start_time = time.time()
        performance_metrics = process.run_genetic_algorithm()  # Call your GA processing function
        elapsed_time = time.time() - start_time  # Calculate time taken for this run

        # Calculate improvement rate and average time per generation
        if previous_fitness == 0:
            improvement_rate = 0  # Avoid division by zero on the first run
        else:
            improvement_rate = (performance_metrics["fitness_value"] - previous_fitness) / previous_fitness * 100
        
        avg_time_per_gen = elapsed_time / performance_metrics["generations"]

        # Update previous fitness for the next iteration
        previous_fitness = performance_metrics["fitness_value"]

        metrics = {
            "response_time": elapsed_time,
            "performance_metrics": performance_metrics,
            "improvement_rate": improvement_rate,
            "avg_time_per_generation": avg_time_per_gen
        }

        # Emit the metrics to the client
        socketio.emit('metrics', metrics)

        # Sleep for a short period to control update frequency (e.g., every 0.2 seconds)
        time.sleep(0.2)

@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    """Start the data processing."""
    global is_processing, processing_thread
    if not is_processing:
        is_processing = True
        processing_thread = threading.Thread(target=process_data)
        processing_thread.start()
        return jsonify({"message": "Processing started."}), 200
    return jsonify({"message": "Processing is already running."}), 400

@app.route('/stop', methods=['POST'])
def stop():
    """Stop the data processing."""
    global is_processing
    if is_processing:
        is_processing = False
        processing_thread.join()  # Wait for the thread to finish
        return jsonify({"message": "Processing stopped."}), 200
    return jsonify({"message": "No processing is currently running."}), 400

@app.route('/metrics', methods=['GET'])
def metrics():
    """Return the latest metrics (could be extended for more details)."""
    return jsonify({"message": "Metrics endpoint."}), 200

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    socketio.run(app, debug=False)
