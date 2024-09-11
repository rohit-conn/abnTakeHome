import time
import random
import os
from flask import Flask

app = Flask(__name__)

host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.getenv('FLASK_RUN_PORT', 5000))
debug = os.getenv('FLASK_DEBUG', 'False')

def generate_log():
    logs = [
        "Success",
        "Created",
        "Failed",
    ]
    return random.choice(logs)

@app.route('/api_1')
def api_call():
    log_message = generate_log()
    print(f"Operation log: {log_message}")
    time.sleep(0.5)  # Wait for half a second
    return f"completed: {log_message}"

@app.route('/health_check')
def health_check():
    return f"healthy"

if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
