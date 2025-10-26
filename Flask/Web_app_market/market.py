from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to your Flask App!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)