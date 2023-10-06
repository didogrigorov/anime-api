from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
import pytest

class FooTest2(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="didogrigorov", is_superuser=True)
        self.user.save()

    def test_my_user(self):
        me = User.objects.get(username="didogrigorov")
        assert me.is_superuser


class FooTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def this_wont_run(self):
        print('Fail')

    def test_this_will(self):
        print('Win')
