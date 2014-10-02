from slugify import slugify
import os
import mediachicken
import unittest
import tempfile
import time
import yaml
import shutil


class MediaChickenTestCase(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.join(os.path.dirname(__file__),
                                     'mediachicken/posts')
        self.categories = (
            # First let's try a long category with a simple uppercase name
            "My Awesome Testing Category",
            # Now let's try a long category with a more complex name
            "lowercase category!",
        )

        self.posts = {
            slugify(self.categories[0]): (
                {
                    'title': "My First Blog Post",
                    'date': "1/25/2013 12:00",
                    'status': "Published",
                    'author': "John Doe",
                },
                {
                    'title': "My second blog post, EVER!",
                    'date': "3/10/2013 4:20",
                    'status': "Published",
                    'author': "John Doe",
                },
                {
                    'title': "This one is just a draft",
                    'date': "3/13/2014 3:21",
                    'status': "Draft",
                    'author': "John Doe",
                },
                {
                    'title': "This one is just a draft",
                    'date': "6/29/2014 3:21",
                    'status': "Draft",
                    'author': "John Doe",
                },
            ),
            slugify(self.categories[1]): (
                {
                    # if a date is not given, it should set the day to now
                    'title': "My latest post, in a different category!",
                    'status': "Published",
                    'author': "Jane Doe",
                },
            )
        }

        for category in self.categories:
            os.makedirs(os.path.join(self.base_dir, category))

    def tearDown(self):
        for category in self.categories:
            shutil.rmtree(os.path.join(self.base_dir, category))

    def create_test_posts(self):
        for category in self.categories:
            posts = self.posts[slugify(category)]
            for post in posts:
                slug = slugify(post['title'])
                header = mediachicken.functions.create_post_header(**post)
                body = " ".join(["%s by %s... " % (post['title'],
                    post['author']) for x in range(1,100)])
                try:
                    post_file = open(os.path.join(self.base_dir, category, slug+'.md'), 'w+')
                    post_file.write(body)
                    post_file.close()
                except:
                    return False
        return True


    def test_posts(self):

        assert self.create_test_posts() is True

def test():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
