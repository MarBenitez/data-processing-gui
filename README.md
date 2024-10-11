# Data Processing GUI for Sensor Data Analysis

Welcome to the **Data Processing GUI for Sensor Data Analysis** repository! This project demonstrates the application of an MVP (Model-View-Presenter) architecture to build a data processing GUI for analyzing sensor data. It uses Python's Tkinter library for the GUI, and pandas for data manipulation and transformation.&#x20;

### Key Features

- **Data Loading**: Load CSV files containing sensor data.
- **Data Visualization**: View raw sensor data directly in the GUI.
- **Data Processing**: Apply specific transformations to sensor readings, including temperature conversion, humidity scaling, and CO2 compensation.
- **Export Processed Data**: Save processed data back to CSV format.
- **Modular Design**: Clear separation between the data (Model), GUI (View), and business logic (Presenter), making it easy to extend or modify.

### Technology Stack

- **Python 3.10+**
- **Tkinter** for GUI
- **pandas** for data processing

### Modular & Extensible

The repository is designed to be a **template for any type of data processing**. With a well-structured and modularized codebase, **small modifications** in the processing logic can repurpose this tool for different types of data and transformations. This flexibility allows users to adapt the application for various use cases with minimal effort.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/marbenitez/data-processing-gui.git
   ```

2. **Install dependencies**:
   Ensure you have Python 3.10+ installed, then run:

   ```sh
   pip install -r requirements.txt
   ```

## How to Run

- Run the main script to start the application:
  ```sh
  python main.py
  ```

## Directory Structure

- **main.py**: Entry point to run the GUI application.
- **model.py**: Contains the `Model` class for managing data.
- **view\.py**: Implements the `View` class for creating the GUI components.
- **presenter.py**: Contains the `Presenter` class that connects the Model and View, handling user interactions and business logic.
- **app.py**: Holds utility functions for data processing and transformation.

## Example Use Case

The application is capable of processing sensor data including **Temperature, Humidity, and CO2** levels. Data can be loaded from a CSV file, processed with the appropriate transformations (e.g., converting temperature from Celsius to Kelvin), and exported back to a CSV file. The modular design also allows for adding new data types or processing functions with minimal changes to the codebase.

### Potential Extensions

- Adapt the data processing logic to analyze **financial data**, **sales data**, or **health statistics** by modifying the functions in `app.py`.
- Change the **View** to accommodate different input types or visualizations, like plotting charts using matplotlib.

### Screenshots

![load](https://github.com/MarBenitez/data-processing-gui/blob/main/images/load-csv.png)

![input](https://github.com/MarBenitez/data-processing-gui/blob/main/images/show-input.png)

![analyzed](https://github.com/MarBenitez/data-processing-gui/blob/main/images/analyze-data.png)
