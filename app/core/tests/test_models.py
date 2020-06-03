from django.test import TestCase
from django.contrib.auth import get_user_model as User


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "kwalanick@gmail.com"
        password = 'Testpass123'

        user = User().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_nomalized(self):
        """New user email is normalized"""
        email = 'test@KWALANICK.COM'
        user = User().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """New User Email Validation Test"""
        with self.assertRaises(ValueError):
            User().objects.create_user(None, 'test@123')

    def test_create_new_super_user(self):
        """Test create  new super user"""
        user = User().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
