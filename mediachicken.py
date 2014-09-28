from flask import (Flask, request, session, g,
                   redirect, url_for, abort, render_template, flash)
import os


SETTINGS = os.path.join(os.path.dirname(__file__), "conf.py")

app = Flask(__name__)
app.config.from_envvar('SETTINGS', silent=True)


if __name__ == '__main__':
    app.run()
