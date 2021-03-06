import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_system_time():
    return str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)