from app.models import User,Comments
import unittest
from app import db
class CommentTest(unittest.TestCase):


    def setUp(self):
        self.user_Collo=User(username="collo",password="tomjerry",email="colo@gmail.com")
        self.new_comment=Comments(pitch_id=10,pitch_title="Drone",comments="Nice app")
    def tearDown(self):
        Comments.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,10)
        self.assertEquals(self.new_comment.pitch_title,"Drone")
        self.assertEquals(self.new_comment.comments,"Nice app")

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments=Comments.get_comments(10)
        self.assertTrue(len(got_comments)==1)
