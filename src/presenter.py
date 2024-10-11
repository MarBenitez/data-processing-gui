from typing import Protocol
from model import Model
from app import transform_data, process_data
import pandas as pd

class View(Protocol):
    def set_data(self, data: pd.DataFrame) -> None:
        ...
    def run(self) -> None:
        ...
    def on_load_csv_button_click(self) -> None:
        ...
    def on_show_input_data_button_click(self) -> None:
        ...
    def on_analyze_button_click(self) -> None:
        ...
    def on_export_button_click(self) -> None:
        ...

class Presenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.view.presenter = self

    def load_data(self, file_path: str) -> None:
        self.model.data = pd.read_csv(file_path)

    def show_input_data(self) -> None:
        self.view.set_data(self.model.data)

    def analyze_data(self, selected_option: str) -> None:
        processed_data = process_data(self.model.data, selected_option)
        self.model.processed_data = transform_data(processed_data)
        self.view.set_data(self.model.processed_data)

    def export_data(self, file_path: str) -> None:
        self.model.processed_data.to_csv(file_path)

    def run(self) -> None:
        self.view.run()