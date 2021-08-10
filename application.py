from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
@application.route('/<message>')
def hello_world(message='Hello World'):
    return render_template('index.html', message=message)


if __name__ == "__main__":
    application.debug = True
    application.run()
