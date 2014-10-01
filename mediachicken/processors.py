import yaml
import os.path
from mediachicken import app


@app.context_processor
def utility_processor():

    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)

    def import_yml(name):
        filename = '%s/%s.yml' % (app.config["BASE_DIR"], name)

        if os.path.isfile(filename):
            data = yaml.load(open(filename, 'r'))
            return data
        return dict(err="Failed to load %s" % filename)

    return dict(format_price=format_price,
                import_yml=import_yml)
