import tkinter as tk
from tkinter import messagebox, scrolledtext
import sys
import os

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.sharing import split_secret, combine_shares

class SecretSharingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secret Sharing System")
        self.geometry("600x650")
        self.resizable(False, False) # Added to fix scrolling issue

        # --- Main Frames ---
        split_frame = tk.LabelFrame(self, text="Split Secret", padx=10, pady=10)
        split_frame.pack(padx=10, pady=10, fill="x") # expand=True removed for scrolling fix

        combine_frame = tk.LabelFrame(self, text="Combine Shares", padx=10, pady=10)
        combine_frame.pack(padx=10, pady=10, fill="x") # expand=True removed for scrolling fix

        # --- Split Section Widgets ---
        tk.Label(split_frame, text="Secret:").grid(row=0, column=0, sticky="w", pady=2)
        self.secret_entry = tk.Entry(split_frame, width=50)
        self.secret_entry.grid(row=0, column=1, pady=2, sticky="ew") # Added sticky="ew" for horizontal expansion

        tk.Label(split_frame, text="Number of Shares (n):").grid(row=1, column=0, sticky="w", pady=2)
        self.num_shares_entry = tk.Entry(split_frame, width=10)
        self.num_shares_entry.grid(row=1, column=1, sticky="w", pady=2)

        tk.Label(split_frame, text="Threshold (k):").grid(row=2, column=0, sticky="w", pady=2)
        self.threshold_entry = tk.Entry(split_frame, width=10)
        self.threshold_entry.grid(row=2, column=1, sticky="w", pady=2)

        split_button = tk.Button(split_frame, text="Split Secret", command=self.split_secret_gui)
        split_button.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(split_frame, text="Generated Shares:").grid(row=4, column=0, sticky="w", pady=2)
        self.shares_text = scrolledtext.ScrolledText(split_frame, width=70, height=10, wrap=tk.WORD)
        self.shares_text.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew") # Added sticky="ew" for horizontal expansion

        # --- Combine Section Widgets ---
        tk.Label(combine_frame, text="Enter shares (one per line):").grid(row=0, column=0, sticky="w", pady=2)
        self.combine_text = scrolledtext.ScrolledText(combine_frame, width=70, height=10, wrap=tk.WORD)
        self.combine_text.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew") # Added sticky="ew" for horizontal expansion

        combine_button = tk.Button(combine_frame, text="Combine Shares", command=self.combine_shares_gui)
        combine_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.recovered_secret_label = tk.Label(combine_frame, text="Recovered Secret: ", font=("Arial", 10, "bold"))
        self.recovered_secret_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)

        # Configure columns to expand
        split_frame.grid_columnconfigure(1, weight=1)
        combine_frame.grid_columnconfigure(0, weight=1) # The scrolled text area is in column 0, spanning 2 columns
        combine_frame.grid_columnconfigure(1, weight=1) # The scrolled text area is in column 0, spanning 2 columns


    def split_secret_gui(self):
        secret = self.secret_entry.get()
        try:
            num_shares = int(self.num_shares_entry.get())
            threshold = int(self.threshold_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Number of shares and threshold must be integers.")
            return

        try:
            shares = split_secret(secret, num_shares, threshold)
            self.shares_text.delete('1.0', tk.END)
            for share in shares:
                self.shares_text.insert(tk.END, share + "\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def combine_shares_gui(self):
        shares_str = self.combine_text.get('1.0', tk.END).strip()
        if not shares_str:
            messagebox.showerror("Invalid Input", "Please enter shares to combine.")
            return
        
        shares = shares_str.splitlines()
        
        try:
            secret = combine_shares(shares)
            self.recovered_secret_label.config(text=f"Recovered Secret: {secret}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not recover secret. Ensure you have provided enough valid shares. Details: {e}")
            self.recovered_secret_label.config(text="Recovered Secret: ")

def main():
    app = SecretSharingApp()
    app.mainloop()

if __name__ == "__main__":
    main()