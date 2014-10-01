import yaml
import os.path
from mediachicken import app


@app.context_processor
def utility_processor():

    def import_yml(name):
        filename = '%s/%s.yml' % (app.config["BASE_DIR"], name)

        if os.path.isfile(filename):
            data = yaml.load(open(filename, 'r'))
            return data
        return dict(err="Failed to load %s" % filename)

    return dict(import_yml=import_yml)
