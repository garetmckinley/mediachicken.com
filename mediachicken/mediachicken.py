from flask import (Flask, request, session, g,
                   redirect, url_for, abort, render_template, flash)
import os


SETTINGS = os.path.join(os.path.dirname(__file__), "conf.py")

app = Flask(__name__)
app.config.from_envvar('SETTINGS', silent=True)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route('/')
def index():
    return render_template('index.jade')


if __name__ == '__main__':
    app.run()
