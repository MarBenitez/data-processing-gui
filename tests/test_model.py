import unittest
import pandas as pd
from src.model import Model

class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        self.model = Model()
        self.test_data = pd.DataFrame({"Sensor": ["Temperature", "Humidity", "CO2"], "Value": [25.5, 45.0, 400]})
        self.processed_data = pd.DataFrame({"Sensor": ["Temperature", "Humidity"], "Value": [298.65, 0.45]})

    def test_set_data(self) -> None:
        self.model.data = self.test_data
        pd.testing.assert_frame_equal(self.model.data, self.test_data)

    def test_set_processed_data(self) -> None:
        self.model.processed_data = self.processed_data
        pd.testing.assert_frame_equal(self.model.processed_data, self.processed_data)

    def test_initial_data_empty(self) -> None:
        self.assertTrue(self.model.data.empty, "Initial data should be an empty DataFrame.")
        self.assertTrue(self.model.processed_data.empty, "Initial processed data should be an empty DataFrame.")

if __name__ == "__main__":
    unittest.main()