import factory
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from faker import Faker
from nose.tools import eq_, ok_
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import User
from .factories import UserFactory

fake = Faker()


class TestUserListTestCase(APITestCase):
    """ Tests / list operations. """

    def setUp(self):
        self.url = reverse("core")

    def test_get_request_succeeds(self):
        raise "Not implemented yet"
