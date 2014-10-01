from flask import (Flask, request, session, g,
                   redirect, url_for, abort,
                   render_template, flash, Response, json)

from mediachicken import app, cache, functions
import os.path
from markdown import markdown
import re
import yaml


@app.route("/redis.json")
def clouds():
    data = app.redis.getset("this", "shit")
    return str(data)


@app.route('/')
@cache.cached(timeout=5)
def index():
    app.redis.rpush("members", "Adam")
    return render_template('index.jade',
                           posts=functions.get_posts_from_index()[:5])


@app.route('/<category>/<slug>/')
def singlepost(category, slug):
    header, body, params = functions.get_post(category, slug)
    if params['STATUS'] == "Published":
        html = markdown(body)
        return render_template('singlepost.jade', body=html, params=params)
    else:
        pass  # 404
