#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from miller import helpers
from miller.models import Story, Author


dir_path = os.path.dirname(os.path.realpath(__file__))

# python manage.py test miller.test.test_models_story.StoryTest
class StoryTest(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(
        username='test-user-profile', 
        email='jacob@jacob', 
        password='top_secret')

    # document creation
    author = self.user.authorship.first()
    author.fullname=u'Jacob Jakobson'
    author.affiliation=u'University of kolingemstuff'
    author.save()

    coauthor = Author(
      fullname=u'Jenna Rapunzel',
      affiliation=u'Open University of Maliningrad'
    )
    coauthor.save()
    
    self.story = Story(
        title=u'The happy story of the Promo', 
        abstract=u'Considering the changes in the new brand buzz, the happy story has an happy ending',
        contents=u'## Basic \n\nWith a nice paragraph[^1] and some footnotes.\n\n### this is a third level\n\nsome text...\n\n[^1]: footnote content',
        owner=self.user
    )
    self.story.save()
    self.story.authors.add(coauthor)
    print [a.fullname for a in self.story.authors.all()]
    self.assertTrue(os.path.exists(self.story.get_path()))



  def _test_download_docx(self):
    path = self.story.download(outputFormat='docx')
    self.assertTrue(os.path.exists(path))


  def _test_download_pdf(self):
    path = self.story.download(outputFormat='pdf')
    self.assertTrue(os.path.exists(path))

  def _test_delete(self):
    path = self.story.get_path()
    self.story.delete()
    self.assertFalse(os.path.exists(path))

    
  def _test_delete_user(self):
    path = self.user.profile.get_path()
    self.user.delete()
    self.assertFalse(os.path.exists(path))
   
    
  def test_suite(self):
    self._test_download_pdf()
    self._test_delete()
    self._test_delete_user()