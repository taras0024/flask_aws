from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    hello_world = 'Hello World!!!'
    return render_template('index.html', temp=hello_world)


if __name__ == '__main__':
    app.run()
