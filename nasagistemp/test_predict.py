import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import sys

class TestPredictionScript(unittest.TestCase):
    @patch('joblib.load')
    @patch('sys.argv', ['predict.py', '2030'])
    def test_prediction_output(self, mock_load):
        mock_model = MagicMock()
        mock_model.predict.return_value = np.array([1.23])
        mock_load.return_value = mock_model

        with patch('builtins.print') as mocked_print:
            import predict  # Re-import inside the test to trigger script run

            mocked_print.assert_any_call("starting prediction...")
            mocked_print.assert_any_call("prediction for year 2030")
            mocked_print.assert_any_call(1.23)

if __name__ == '__main__':
    unittest.main()
