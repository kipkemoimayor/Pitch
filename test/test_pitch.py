import unittest
from app.models import Pitches
from app import db

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch=Pitches(pitch="android app",author="colo",title="galaxy",id=12)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitches))
    def test_init(self):
        self.assertEqual(self.new_pitch.pitch,"android app")
        self.assertEqual(self.new_pitch.author,"colo")
        self.assertEqual(self.new_pitch.title,"galaxy")
        self.assertEqual(self.new_pitch.id,12)
