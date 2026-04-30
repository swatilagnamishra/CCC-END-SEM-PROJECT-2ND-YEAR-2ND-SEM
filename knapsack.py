import tkinter as tk
from tkinter import messagebox

class KnapsackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("0/1 Knapsack - DP")
        self.root.geometry("550x550")

        self.items = []

        # Title
        tk.Label(root, text="0/1 Knapsack (Dynamic Programming)", font=("Arial", 16)).pack(pady=10)

        # Input Frame
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Weight:").grid(row=0, column=0)
        self.weight_entry = tk.Entry(frame)
        self.weight_entry.grid(row=0, column=1)

        tk.Label(frame, text="Value:").grid(row=1, column=0)
        self.value_entry = tk.Entry(frame)
        self.value_entry.grid(row=1, column=1)

        tk.Label(frame, text="Capacity:").grid(row=2, column=0)
        self.capacity_entry = tk.Entry(frame)
        self.capacity_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Item", command=self.add_item).pack(pady=5)
        tk.Button(root, text="Solve Knapsack", command=self.solve_knapsack).pack(pady=5)
        tk.Button(root, text="Clear", command=self.clear_all).pack(pady=5)

        # Listbox
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", fg="green")
        self.result_label.pack(pady=10)

    def add_item(self):
        try:
            weight = int(self.weight_entry.get())
            value = int(self.value_entry.get())

            if weight <= 0 or value <= 0:
                messagebox.showerror("Error", "Values must be positive")
                return

            self.items.append((weight, value))
            self.listbox.insert(tk.END, f"Weight: {weight}, Value: {value}")

            self.weight_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")

    def solve_knapsack(self):
        try:
            capacity = int(self.capacity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid capacity")
            return

        n = len(self.items)

        if n == 0:
            messagebox.showwarning("Warning", "No items added")
            return

        # DP Table
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Fill table
        for i in range(1, n + 1):
            weight, value = self.items[i - 1]
            for w in range(capacity + 1):
                if weight <= w:
                    dp[i][w] = max(value + dp[i - 1][w - weight], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        result = dp[n][capacity]

        # Backtracking to find selected items
        w = capacity
        selected_items = []

        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_items.append(self.items[i - 1])
                w -= self.items[i - 1][0]

        # Display result
        result_text = f"Maximum Value: {result}\nSelected Items:\n"
        for item in selected_items:
            result_text += f"Weight: {item[0]}, Value: {item[1]}\n"

        self.result_label.config(text=result_text)

    def clear_all(self):
        self.items.clear()
        self.listbox.delete(0, tk.END)
        self.result_label.config("")
        self.capacity_entry.delete(0, tk.END)

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackApp(root)
    root.mainloop()
