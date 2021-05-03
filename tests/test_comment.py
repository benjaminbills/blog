import unittest
from app.models import Blog,User,Comment
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
            self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
            self.new_blog = Blog(
              id = 12,
              title='Why am I here',
              urlToImage="https://image.tmdb.org/t/p/w500/jdjdjdjn",
              description='This movie is the best thing since sliced bread',
              blog_content = 'we are here to make plans on how to prevent ww6',
              user = self.user_James
            )
            self.new_comment = Comment(
              blog_id= self.new_blog.id,
              description='This movie is the best thing since sliced bread',
              user = self.user_James 
              )

    def tearDown(self):
            Comment.query.delete()
            User.query.delete()
            Blog.query.delete()

    def test_check_instance_variables(self):
            self.assertEquals(self.new_comment.blog_id,12)
            self.assertEquals(self.new_comment.description,'This movie is the best thing since sliced bread')
            self.assertEquals(self.new_comment.user,self.user_James)

    

