'''app.py: A quick flask app to demonstrate the basics of Flask

Flask requires knowledge of HTML and Jinja2 templating. The website created also uses Bootstrap,
but that's just to make the front end pretty. If only for REST APIs, then this is not too important. 
'''

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/process', methods=['POST'])
def process():
    out = dict(request.form)
    '''out: a dictionary holding keys as the NAME attribute of each input/ select tag enclosed in
the form. Values: the form entry. Take the form input and process it in the function,
MUST RETURN with a return render_template or a string: HTML, or not'''
    return render_template('result.html', data=out)
    '''render_template can take any number of extra arguments, which can be used
in the HTML using Jinja2 templating engine which comes with Flask.'''


@app.route('/get_greet', methods=['GET'])
def greet():
    d = {}
    for thing in request.args:
        d[thing] = request.args[thing]
    # Do processing and function calls here finally return jsonify({ ... })

    return jsonify({'msg': 'Hi! You passed in args' if d else 'Hi!', 'args': d})


if __name__ == '__main__':
    app.run()
