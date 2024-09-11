import time
import random
import os
from flask import Flask

app = Flask(__name__)

EXTERNAL_INTGERATION_KEY = os.getenv('EXTERNAL_INTGERATION_KEY','')
debug = os.getenv('FLASK_DEBUG', 'False')
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

## Adding a simple return for testing the existnce of environment can be expanded to accomadate return call od download API
@app.route('/download_external_logs')
def download_external_logs():
    if EXTERNAL_INTGERATION_KEY == "":
        return f"Missing API token", 403
    else:
        return f"Do API call", 200


if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
