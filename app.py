from flask import Flask
from datetime import datetime

app = Flask(__name__)
call_count = 0

@app.route('/')
def home():
    global call_count
    call_count += 1
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Local time: {local_time}<br>Total calls: {call_count}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)