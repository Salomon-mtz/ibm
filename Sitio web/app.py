from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")

@app.route('/sign_in')
def sign_in():
    return render_template("sign_up.html")

@app.route('/about/proposal')
def proposal():
    return render_template("sign_up.html")

@app.route('/about/members')
def members():
    return render_template("sign_up.html")


if __name__ == '__main__':
    app.run(debug = True)
