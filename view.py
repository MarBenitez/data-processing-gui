import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import pandas as pd
from tkinter import ttk

TITLE = 'Data Processing GUI'

class View:
    def __init__(self) -> None:
        self.presenter: Presenter = None
        self.master = tk.Tk()
        self.master.title(TITLE)
        self.master.geometry('600x400')


        style = ttk.Style()
        style.theme_use('clam') 

        self.init_ui()

    def init_ui(self) -> None:
        self.frame = ttk.Frame(self.master, padding=(10, 10))
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.load_button = ttk.Button(self.frame, text="Load CSV",
                                     command=self.on_load_csv_button_click)
        self.show_input_data_button = ttk.Button(self.frame, text="Show input data",
                                                command=self.on_show_input_data_button_click,
                                                state="disabled")
        self.analyze_button = ttk.Button(self.frame, text="Analyze Data",
                                        command=self.on_analyze_button_click,
                                        state='disabled')
        self.export_button = ttk.Button(self.frame, text="Export Data",
                                       command=self.on_export_button_click,
                                       state='disabled')

        self.selected_option = tk.StringVar(self.master)
        self.options = ["All", "Temperature", "Humidity", "CO2"]
        self.selected_option.set(self.options[0])
        self.option_menu = ttk.OptionMenu(self.frame, self.selected_option, *self.options)

        self.text_widget = tk.Text(self.frame, wrap=tk.WORD)

        self.load_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.show_input_data_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.analyze_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.option_menu.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.export_button.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

        self.text_widget.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def set_data(self, data: pd.DataFrame) -> None:
        self.text_widget.delete("1.0", tk.END)
        if not data.empty:
            self.text_widget.insert(tk.END, str(data))
        else:
            mb.showinfo("Error", "No data to show!")

    def on_load_csv_button_click(self) -> None:
        file_path = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.presenter.load_data(file_path)
            mb.showinfo("Import", "Data successfully loaded!")
            self.show_input_data_button["state"] = "normal"
            self.analyze_button["state"] = "normal"
            self.export_button["state"] = "normal"

    def on_show_input_data_button_click(self) -> None:
        self.presenter.show_input_data()

    def on_analyze_button_click(self) -> None:
        self.presenter.analyze_data(self.selected_option.get())

    def on_export_button_click(self) -> None:
        file_path = fd.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.presenter.export_data(file_path)
            mb.showinfo("Export", "Data successfully exported!")

    def run(self) -> None:
        self.master.mainloop()