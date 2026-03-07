from django.test import TestCase

class MyAppTests(TestCase):
    def test_hello_world(self):
        self.assertEqual(1 + 1, 2)