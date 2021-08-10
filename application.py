from flask import Flask, render_template


# print a nice greeting.
def say_hello(username="World"):
    return f'<p>Hello {username}!</p>\n'


# some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>TASK Hello world</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>:Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)


# add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

@application.route('/<message>')
def hello_world(message='Hello World'):
    return render_template('index.html', message=message)


# add a rule when the page is accessed with a name appended to the site
# URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#                                                   header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
