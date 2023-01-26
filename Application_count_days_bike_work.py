import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.dates import DAYS_PER_MONTH
from matplotlib.figure import Figure
import json

# directory for JSON file
bycicle_dir = "/Users/victorciugurean/Desktop/OTARIE/python_scripts/widget_bike/"
cost_gain = 0

class BicycleTrackerApp(tk.Tk):
    def __init__(self):
            super().__init__()
            self.title("Bicycle Tracker App")
            try:
                with open(bycicle_dir + "bicycle_data.json", "r") as f:
                    self.data = json.load(f)
            except:
                self.data = {}
            self.create_widgets()

    def create_widgets(self):
        self.date_label = tk.Label(self, text="Date (YYYY-MM-DD):")
        self.date_label.pack()

        self.date_entry = tk.Entry(self)
        self.date_entry.pack()

        self.distance_label = tk.Label(self, text="Distance (km):")
        self.distance_label.pack()

        self.distance_entry = tk.Entry(self)
        self.distance_entry.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register_data)
        self.register_button.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.pack()

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.update_graph()
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def register_data(self):
        date = self.date_entry.get()
        distance = float(self.distance_entry.get())
        self.data[date] = distance
        self.update_graph()

    def update_graph(self):
        self.ax.clear()
        self.ax.bar(list(self.data.keys()), list(self.data.values()))
        self.ax.set_xlabel("Date")
        self.ax.set_ylabel("Total distance")
        self.ax.set_title(f'Total days the bycicle was used: {len(self.data)}' + '\nTotal gain is: ' + str(len(self.data)*3) + '€')
        self.canvas.draw()

    def save_data(self):
        with open(bycicle_dir + "bicycle_data.json", "w") as f:
            json.dump(self.data, f)

app = BicycleTrackerApp()
app.mainloop()