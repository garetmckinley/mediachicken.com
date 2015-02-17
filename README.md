# mediachicken
flask application for mediachicken.com. It is a custom written blogging engine built for heroku (but deployable on any server) and flask. It runs off a few various technologies including markdown for posts. It also runs without a database, it's post indexes are created on run and stored in yaml files. Eventually this will likely be switched to Redis or similar to eliminate the need for constant file IO.

# what's inside
- Python 3.4 + flask - core engine
- jade - templating language
- SCSS - template styling
- Coffeescript - custom template scripts
- Markdown - posts are written in markdown
- YAML - post meta data is stored in YAML headers, also for indexes.
- Grunt - for automagical compilation and compression of themes.


# credits
## developers
- @mediachicken Garet McKinley - creator

## assets

- skrollr - https://github.com/Prinzhorn/skrollr
- bootstrap - http://getbootstrap.com
- jQuery - http://jquery.com
