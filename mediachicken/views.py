from flask import (Flask, request, session, g,
                   redirect, url_for, abort,
                   render_template, flash, Response, json, send_file)

from mediachicken import app, cache, functions
import os.path
from markdown import markdown
import re
import yaml


@app.route('/')
@cache.cached(timeout=5)
def index():
    return render_template('index.jade',
                           posts=functions.get_posts_from_index()[:5])


@app.route('/<category>/<slug>/')
def singlepost(category, slug):
    header, body, params = functions.get_post(category, slug)
    if params['STATUS'].lower() == "published":
        html = markdown(body)
        return render_template('singlepost.jade', body=html, params=params)
    else:
        abort(404)  # 404


@app.route('/<category>/<slug>/img/<image>')
def singlepost_img(category, slug, image):
    filename = "posts/%s/%s/%s" % (category, functions.simple_deslugify(slug), image)
    return send_file(filename, mimetype='image/png')
