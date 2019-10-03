import unittest
from app.models import User,Pitch,Comment
from app import db

def setUp(self):
    '''
    Sets up the tests to be tested 
    '''
    self.user_Krasivaya = User(username = 'Krasivaya',password = 'passtest', email = 'test@test.com')
    self.pitch_one = Pitch(pitch = 'blabla',category = 'Product',user = self.user_Krasivaya)
    self.new_comment = Comment(comment = 'nice bla',pitch = self.pitch_one,user = user_Krasivaya)


def tearDown(self):
    '''
    Tears down the values after every test
    '''
    Pitch.query.delete()
    User.query.delete()
    Comment.query.delete()

def test_check_instance_variables(self):
    '''
    Tests the instances of comment
    '''
    self.assertEquals(self.pitch_one.pitch,'blabla')
    self.assertEquals(self.pitch_one.category,'Product')
    self.assertEquals(self.pitch_one.user,self.user_Krasivaya)

def test_instance_of_comment(self):
    '''
    test comment of instances
    '''
    self.assertEquals(self.new_comment.comment,'nice bla')
    self.assertEquals(self.new_comment.pitch,self.pitch_one)
    self.assertEquals(self.new_comment.user,self.user_Krasivaya)

def test_save_picth(self):
    self.pitch_one.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)