import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import VITCalculator
from src.predictor import VITPredictor

class TestVITCalculator(unittest.TestCase):

    def test_calculate_attendance_score(self):
        self.assertEqual(VITCalculator.calculate_attendance_score(75.0), 5)
        self.assertEqual(VITCalculator.calculate_attendance_score(85.0), 5)
        self.assertEqual(VITCalculator.calculate_attendance_score(74.9), 0)
        self.assertEqual(VITCalculator.calculate_attendance_score(60.0), 0)

    def test_calculate_course_total(self):
        total = VITCalculator.calculate_course_total(50, 50, 100, 25, 80.0)
        self.assertEqual(total, 100.0)

        total = VITCalculator.calculate_course_total(25, 25, 50, 20, 70.0)
        self.assertEqual(total, 55.0)

    def test_check_attendance_eligibility(self):
        res = VITCalculator.check_attendance_eligibility(16, 20, 10)
        self.assertTrue(res["eligible"])
        self.assertNotIn("can_recover", res)

        res = VITCalculator.check_attendance_eligibility(10, 20, 20)
        self.assertFalse(res["eligible"])
        self.assertTrue(res.get("can_recover", False))

        res = VITCalculator.check_attendance_eligibility(5, 20, 2)
        self.assertFalse(res["eligible"])
        self.assertFalse(res.get("can_recover", False))

class TestVITPredictor(unittest.TestCase):

    def test_predict_required_tee_marks(self):
        res = VITPredictor.predict_required_tee_marks(45.0, 75.0)
        self.assertTrue(res["achievable"])
        self.assertEqual(res["required_tee"], 75.0)

        res = VITPredictor.predict_required_tee_marks(10.0, 90.0)
        self.assertFalse(res["achievable"])

if __name__ == "__main__":
    unittest.main()