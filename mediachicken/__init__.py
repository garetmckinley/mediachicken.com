from flask import Flask
from flask.ext.cache import Cache
from werkzeug.routing import BaseConverter
import os


class RegexConverter(BaseConverter):

    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.url_map.converters['regex'] = RegexConverter
app.config.from_object('mediachicken.conf')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


from mediachicken import functions, processors, filters, views
