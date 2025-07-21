from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model
model = joblib.load('spam_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        output = model.predict([message])
        result = "This Message is a SPAM Message." if output == [1] else "This Message is Not a SPAM Message."
        return render_template('index.html', result=result, message=message)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
