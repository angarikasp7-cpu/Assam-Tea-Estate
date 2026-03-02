import tkinter as tk
from tkinter import messagebox

class TeaEstateGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tea Estate Game")
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to the Tea Estate Game", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Estate Management", command=self.estate_management).pack(pady=10)
        tk.Button(self.root, text="Worker Management", command=self.worker_management).pack(pady=10)
        tk.Button(self.root, text="Production", command=self.production).pack(pady=10)
        tk.Button(self.root, text="Market", command=self.market).pack(pady=10)
        tk.Button(self.root, text="Financial Report", command=self.financial_report).pack(pady=10)
        tk.Button(self.root, text="Exit", command=root.quit).pack(pady=10)

    def estate_management(self):
        self.clear_window()
        tk.Label(self.root, text="Estate Management Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def worker_management(self):
        self.clear_window()
        tk.Label(self.root, text="Worker Management Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def production(self):
        self.clear_window()
        tk.Label(self.root, text="Production Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def market(self):
        self.clear_window()
        tk.Label(self.root, text="Market Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def financial_report(self):
        self.clear_window()
        tk.Label(self.root, text="Financial Report Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TeaEstateGame(root)
    root.mainloop()