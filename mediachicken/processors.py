import yaml
import os.path
from mediachicken import app


@app.context_processor
def utility_processor():

    def css(url):
        return '<link href="%s" rel="stylesheet">\n' % url

    def js(url):
        return '<script type="text/javascript" src="%s"></script>\n' % url

    def meta(params):
        tag = '<meta'
        try:
            tag += ' name="%s"' % params['name']
        except:
            pass
        try:
            tag += ' content="%s"' % params['content']
        except:
            pass
        try:
            tag += ' charset="%s"' % params['charset']
        except:
            pass
        tag += '>\n'
        print(tag)
        return tag

    def favicon(url):
        return '<link href="%s" rel="shortcut icon">\n' % url

    def import_yml(name, dir=None):
        if dir:
            filename = '%s/%s/%s.yml' % (app.config["BASE_DIR"], dir, name)
        else:
            filename = '%s/%s.yml' % (app.config["BASE_DIR"], name)

        if os.path.isfile(filename):
            data = yaml.load(open(filename, 'r'))
            return data
        return dict(err="Failed to load %s" % filename)

    def template_header():
        src =import_yml('header', 'templates')
        header = ''


        def script(content):
            return '<script type="text/javascript">%s</script>\n' % content


        tags = {
            "css": css,
            "js": js,
            "meta": meta,
            "script": script,
            "favicon": favicon,
        }


        for tag in src.items():
            tag, params = tag
            if type(params) == type(list()):
                for i in range(0, len(params)):
                    try:
                        header += tags[tag](params[i])
                    except:
                        print("No parser to process tag of", tag, "type.")
            else:
                print(tag, "isn't a list")

        print(header)
        return header

    def template_footer():
        src =import_yml('footer', 'templates')
        footer = ''


        def script(content):
            return '<script type="text/javascript">%s</script>\n' % content


        tags = {
            "css": css,
            "js": js,
            "meta": meta,
            "script": script,
        }


        for tag in src.items():
            tag, params = tag
            if type(params) == type(list()):
                for i in range(0, len(params)):
                    try:
                        footer += tags[tag](params[i])
                    except:
                        print("No parser to process tag of", tag, "type.")
            else:
                print(tag, "isn't a list")

        print(footer)
        return footer


    return dict(import_yml=import_yml, template_header=template_header, template_footer=template_footer)

