from django.test import TestCase, Client
from django.contrib.auth import get_user_model as User
from django.urls import reverse


class AdminSiteTests(TestCase):

    # function run before every test is run
    def setUp(self):
        self.client = Client()
        self.admin_user = User().objects.create_superuser(
            email='kwalanick@gmail.com',
            password='Test@123'
        )

        self.client.force_login(self.admin_user)
        self.user = User().objects.create_user(
            email='test@nai.com',
            password='test',
            name='Test 010010 2020'
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the user create page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
