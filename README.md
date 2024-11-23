# Real-Time Data Optimization with Genetic Algorithms

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.3-green)](https://flask.palletsprojects.com/)
[![Flask-SocketIO](https://img.shields.io/badge/Flask--SocketIO-5.1.0-yellow)](https://flask-socketio.readthedocs.io/)
[![WebSockets](https://img.shields.io/badge/WebSockets-gevent-blue)](https://gevent.org/)
[![DEAP](https://img.shields.io/badge/DEAP-1.3.1-orange)](https://deap.readthedocs.io/)

This project demonstrates the application of genetic algorithms for real-time data optimization, integrated with a Flask API and a dynamic frontend using **HTML**, **CSS**, and **JavaScript**. The backend utilizes **WebSockets** for live data processing and communication, while the frontend provides real-time visualization and interaction with the data.

## Features

- **Flask API** to handle requests and manage real-time data processing.
- **WebSockets** for continuous and efficient real-time communication.
- **Genetic Algorithm (GA)** for real-time decision-making and optimization.
- Dynamic **HTML**, **CSS**, and **JavaScript** frontend to visualize performance metrics and results.
- **Cloud-based processing** for scalable real-time data handling.

## Technologies

- **Python** (Flask)
- **Flask-SocketIO**
- **WebSockets** (using gevent for asynchronous handling)
- **HTML**, **CSS**, and **JavaScript**
- **Genetic Algorithms** (DEAP library)
- **Flask-Cors** for cross-origin resource sharing (CORS)

## Installation

### Prerequisites

Make sure you have the following installed:

- **Python** (>= 3.6)
- **pip** (Python package installer)

### Install Dependencies

Clone this repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

requirements.txt:
shell
Copy code
Flask==2.0.3
Flask-Cors==3.0.10
Flask-SocketIO==5.1.0
Werkzeug>=2.0,<3.0
deap>=1.3.1  
gevent

## Running the Application
Start the Flask server by running the following command:

```bash
python app.py
```

Open your browser. The application should automatically launch and be accessible at:
http://127.0.0.1:5000

## API Endpoints
/ (GET): Serves the main web page (index.html).
/start (POST): Starts the real-time data processing using the genetic algorithm.
/stop (POST): Stops the data processing.
/metrics (GET): Retrieves the latest metrics.

## Frontend
The frontend is built using HTML, CSS, and JavaScript to visualize the real-time data and metrics processed by the Flask API. 
It connects to the server using WebSockets to receive live updates on performance metrics and optimization results.

## Example of Socket Communication
The backend emits the following metrics to the frontend:

```json
{
  "response_time": "time_taken_for_run",
  "performance_metrics": {
    "fitness_value": "current_fitness_value",
    "generations": "number_of_generations"
  },
  "improvement_rate": "percentage_change_in_fitness",
  "avg_time_per_generation": "average_time_per_generation"
}
```

## Contributing
Feel free to fork this repository, open issues, and submit pull requests if you would like to contribute improvements or fix bugs.

## License
This project is licensed under the MIT License.
