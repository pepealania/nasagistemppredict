import unittest
import joblib
import numpy as np
import os

class TestModelFile(unittest.TestCase):

    def setUp(self):
        self.model_path = "temperature_model.pkl"

    def test_model_file_exists(self):
        self.assertTrue(os.path.exists(self.model_path), "Model file not found.")

    def test_model_can_be_loaded(self):
        try:
            model = joblib.load(self.model_path)
        except Exception as e:
            self.fail(f"Failed to load model: {e}")

    def test_model_predicts_correctly(self):
        model = joblib.load(self.model_path)
        input_year = np.array([[2030]])  # shape (1, 1)

        try:
            result = model.predict(input_year)
            self.assertTrue(isinstance(result, np.ndarray))
            self.assertEqual(result.shape, (1,))
            self.assertTrue(np.issubdtype(result.dtype, np.number))
        except Exception as e:
            self.fail(f"Model prediction failed: {e}")

if __name__ == '__main__':
    unittest.main()
