from mediachicken import app


@app.template_filter('datetime')
def format_datetime(value, format='short'):
    if format == 'short':
        format = "%m/%d/%y"
    elif format == 'long':
        format = "%m/%d/%y"
    elif format == 'timeago':
        format = "%m/%d/%y"
    return value.strftime(format)
