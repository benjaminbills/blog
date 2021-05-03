import unittest
from app.models import Blog,User
from app import db

class BlogModelTest(unittest.TestCase):
      def setUp(self):
              self.user_Ben = User(username = 'ben',password = 'ben', email = 'ben@test.com')
              self.new_blog = Blog(
                title='Why am I here',
                urlToImage="https://image.tmdb.org/t/p/w500/jdjdjdjn",
                description='This movie is the best thing since sliced bread',
                blog_content = 'we are here to make plans on how to prevent ww6',
                user = self.user_Ben
                )
      def tearDown(self):
              Blog.query.delete()
              User.query.delete()

      def test_check_instance_variables(self):
              self.assertEquals(self.new_blog.title,'Why am I here')
              self.assertEquals(self.new_blog.urlToImage,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
              self.assertEquals(self.new_blog.description,'This movie is the best thing since sliced bread')
              self.assertEquals(self.new_blog.blog_content,'we are here to make plans on how to prevent ww6')
              self.assertEquals(self.new_blog.user,self.user_Ben)

      def test_save_blog(self):
              self.new_blog.save_blog()
              self.assertTrue(len(Blog.query.all())>0)
