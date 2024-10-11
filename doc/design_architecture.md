# Data Processing GUI - Design Architecture

## Overview

The "Data Processing GUI" project is an interactive data processing application built with the **Model-View-Presenter (MVP)** architecture. This document explains the architecture design, the relationships between modules, and why this approach was chosen. The design aims to achieve modularity, separation of concerns, and extensibility, ensuring that the project can easily be reused or extended for other data processing needs.

## MVP Design Pattern

The MVP pattern separates the application logic into three distinct layers:

1. **Model**: Represents the data and the logic to manage it. In this project, the `model.py` file handles all data operations, including setting, getting, and processing data from the CSV files.

2. **View**: Handles the graphical user interface (GUI) and user interactions. The `view.py` file is responsible for all UI components and ensuring that users can interact with the application effectively. The view does not contain any logic about how data is processed or handled.

3. **Presenter**: Acts as the "middleman" between the Model and the View. It retrieves the data from the model, formats or processes it as needed, and updates the view. In this project, `presenter.py` includes the logic for loading, processing, and exporting data, linking the model and the view seamlessly.

This structure helps ensure that each layer has a single responsibility:

- The **Model** handles all data-related operations.
- The **View** is focused solely on displaying information and capturing user actions.
- The **Presenter** contains the core logic, updating the view based on model changes.

This separation facilitates easy testing, as each component can be tested independently. Additionally, it allows modifications to be made in one layer (e.g., changing how data is stored in the model) without affecting the other components.

## Modules Breakdown

- **`model.py`**: This module contains the `Model` class, which stores the data and its processed version. The model keeps the state of the dataset and exposes methods for the Presenter to manipulate the data.

- **`view.py`**: This module contains the `View` class, which uses **Tkinter** to display buttons, menus, and a text widget. The view triggers specific methods in the Presenter based on user actions, such as clicking buttons to load or export data.

- **`presenter.py`**: The `Presenter` connects the model to the view. It listens to commands from the view, processes data via `app.py`, and updates the view. For example, when a user selects "Analyze Data," the Presenter processes the data and asks the view to display the result.

- **`app.py`**: This module contains the data processing logic, including filtering the data based on the selected sensor type and transforming it (e.g., converting temperature to Kelvin). This modularity ensures that the processing logic is isolated and can be updated independently of the UI.

- **`main.py`**: Acts as the entry point to the application. It initializes the model, view, and presenter, and starts the application.

## Why MVP?

The MVP architecture is ideal for this type of data processing GUI application because:

- **Separation of Concerns**: The GUI components, data handling, and logic are strictly separated. This makes the code more maintainable and reduces complexity.
- **Testability**: The Model and Presenter are easy to unit test, as they do not depend on the UI framework.
- **Reusability and Extensibility**: The View is decoupled from the logic, allowing different UIs to be built on top of the same logic, or easily replace the data processing logic without altering the UI.

## Extending and Reusing the Template

The modular design also allows this project to serve as a **template for different types of data processing tasks**. The data processing logic in `app.py` can be easily modified to process different data types or use other transformations. The Presenter and View can also be adapted to accommodate new features, such as different data visualizations or inputs.

This extensibility, combined with the MVP pattern, makes the project highly adaptable for different domains and purposes while retaining a clean and organized structure.

