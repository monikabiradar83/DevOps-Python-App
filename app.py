from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps! Welcome to My First Flask Application."

@app.route('/about')
def about():
    return "This application is deployed using Docker and Jenkins."

if __name__ == "__main__":
    app.run(debug=True)