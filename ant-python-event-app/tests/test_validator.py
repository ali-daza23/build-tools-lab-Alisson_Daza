import unittest
from src.validator import validate_attendee

class TestValidator(unittest.TestCase):

    def test_valid_attendee(self):
        attendee = {
            "name": "Sara Palacios",
            "email": "sara@example.com",
            "age": 25,
            "ticket_type": "vip",
            "identifier" : "EV-0903"
        }
        self.assertEqual(validate_attendee(attendee), [])

    def test_invalid_email(self):
        attendee = {
            "name": "Juan",
            "email": "juanexample.com",
            "age": 20,
            "ticket_type": "general",
            "identifier" : "EV-1978"
        }
        self.assertIn("Invalid email", validate_attendee(attendee))

    def test_underage_attendee(self):
        attendee = {
            "name": "Ana",
            "email": "ana@example.com",
            "age": 16,
            "ticket_type": "student",
            "identifier" : "EV-1526"
        }
        self.assertIn("Attendee must be 18 or older", validate_attendee(attendee))

    def test_unidentified_attendee(self):
        attendee = {
            "name": "Yoongi",
            "email": "yoongi@example.com",
            "age": 33,
            "ticket_type": "vip",
            "identifier": "EV931326"
        }
        self.assertIn("Invalid registration code", validate_attendee(attendee))

if __name__ == "__main__":
    unittest.main()