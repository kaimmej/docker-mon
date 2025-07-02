import os
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

LOG_FILE = os.getenv('LOG_FILE', '.message_log.txt')
if os.path.dirname(LOG_FILE):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            with open(LOG_FILE, 'a') as f:
                f.write(message + '\n')
            flash('Message logged successfully!', 'success')
        else:
            flash('Please enter a message.', 'error')
        return redirect(url_for('index'))

    messages = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            messages = f.readlines()

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5001)), debug=True)