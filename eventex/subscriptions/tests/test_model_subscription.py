from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Gabriel Cardoso de Faria',
            cpf='42045392899',
            email='gacarfaria@gmail.com',
            phone='12-98129-4975'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)