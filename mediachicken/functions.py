from mediachicken import app
from slugify import slugify
from dateutil.parser import parse
import os
import re
import sys
import yaml


def simple_deslugify(slug):
    return re.sub(r'-', ' ', slug).title()


def md_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0] + suffix


def post_exists(category, slug):
    filename = os.path.join(
        app.config["BASE_DIR"], "posts", category, slug + ".md")
    if os.path.isfile(filename):
        return True
    return False


def get_post(category, slug):

    def handle_post_exists(filename):
        file = open(filename, 'r')
        contents = file.read()
        header = re.search(
            "```([\\s\\S]*?)```", contents, re.I | re.S).group(1)
        body = re.sub("```([\\s\\S]*?)```", "", contents)

        params = yaml.load(header)

        params['DATE'] = parse(params['DATE'])

        return [header, body, params]

    if post_exists(category, slug):
        filename = os.path.join(
            app.config["BASE_DIR"], "posts", category, slug + ".md")
        return handle_post_exists(filename)
    elif post_exists(simple_deslugify(category), slug):
        filename = os.path.join(
            app.config["BASE_DIR"], "posts", simple_deslugify(category), slug + ".md")
        return handle_post_exists(filename)


def sort_posts(posts, order='DESC'):
    reverse = True if order == 'DESC' else False
    return sorted(posts, key=lambda item: item['date'], reverse=reverse)


def get_posts_from_index():
    posts_index = os.path.join(app.config["BASE_DIR"], "posts", "index.yml")
    yml = yaml.load(open(posts_index, 'r').read())
    return sort_posts(yml)


def build_post_index():
    posts_dir = os.path.join(app.config["BASE_DIR"], "posts")
    posts_index = os.path.join(app.config["BASE_DIR"], "posts", "index.yml")
    posts = []
    for root, folders, files in os.walk(posts_dir):
        for category in folders:
            category_dir = os.path.join(root, category)
            category_slug = slugify(category)
            for slugroot, folders, files in os.walk(category_dir):
                for slug in files:
                    slug = slug.split('.')[0]
                    header, body, params = get_post(category, slug)
                    summary = md_truncate(body, 500)
                    post = {
                        'title': params['TITLE'],
                        'slug': slug,
                        'date': params['DATE'],
                        'status': params['STATUS'],
                        'summary': summary,
                        'permalink': '/%s/%s/' % (category_slug, slug),
                        'category': {
                            'title': category,
                            'slug': category_slug
                        }
                    }
                    posts.append(post)
    index = open(posts_index, 'w+')
    index.write(yaml.dump(posts))


build_post_index()
