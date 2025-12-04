import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.sharing import split_secret, combine_shares

class ModernSecretSharingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secret Sharing System")
        self.geometry("800x700")

        # --- Configure root window resizing ---
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # --- Main Frames ---
        self.split_frame = self._create_section("Split Secret", 0)
        self.combine_frame = self._create_section("Combine Shares", 1)

        # --- Populate Sections ---
        self._create_split_widgets()
        self._create_combine_widgets()

    def _create_section(self, title, row):
        frame = ttk.LabelFrame(self, text=title, padding=(15, 10))
        frame.grid(row=row, column=0, padx=15, pady=10, sticky="nsew")
        frame.columnconfigure(1, weight=1)
        return frame

    def _create_split_widgets(self):
        # --- Input Fields ---
        ttk.Label(self.split_frame, text="Secret:").grid(row=0, column=0, sticky="w", pady=5)
        self.secret_entry = ttk.Entry(self.split_frame)
        self.secret_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)

        ttk.Label(self.split_frame, text="Number of Shares (n):").grid(row=1, column=0, sticky="w", pady=5)
        self.num_shares_entry = ttk.Entry(self.split_frame, width=15)
        self.num_shares_entry.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        ttk.Label(self.split_frame, text="Threshold (k):").grid(row=2, column=0, sticky="w", pady=5)
        self.threshold_entry = ttk.Entry(self.split_frame, width=15)
        self.threshold_entry.grid(row=2, column=1, sticky="w", pady=5, padx=5)

        # --- Action Button ---
        button_frame = ttk.Frame(self.split_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        split_button = ttk.Button(button_frame, text="Split Secret", command=self.split_secret_gui, width=20)
        split_button.pack()

        # --- Output Area ---
        ttk.Label(self.split_frame, text="Generated Shares:").grid(row=4, column=0, sticky="w", pady=5)
        self.shares_text = scrolledtext.ScrolledText(self.split_frame, height=5, wrap=tk.WORD)
        self.shares_text.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5)
        self.split_frame.rowconfigure(5, weight=1)

        # --- Message Area ---
        self.split_message_label = ttk.Label(self.split_frame, text="", wraplength=550)
        self.split_message_label.grid(row=6, column=0, columnspan=2, sticky="w", pady=5)

    def _create_combine_widgets(self):
        # --- Input Area ---
        ttk.Label(self.combine_frame, text="Enter Shares (one per line):").grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        self.combine_text = scrolledtext.ScrolledText(self.combine_frame, height=5, wrap=tk.WORD)
        self.combine_text.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=5)
        self.combine_frame.rowconfigure(1, weight=1)

        # --- Action Button ---
        button_frame = ttk.Frame(self.combine_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        combine_button = ttk.Button(button_frame, text="Combine Shares", command=self.combine_shares_gui, width=20)
        combine_button.pack()
        
        # --- Message Area ---
        self.combine_message_label = ttk.Label(self.combine_frame, text="", wraplength=550)
        self.combine_message_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)

    def _set_message(self, label, text, is_error=False):
        label.config(text=text, foreground="red" if is_error else "green")

    def split_secret_gui(self):
        secret = self.secret_entry.get()
        if not secret:
            self._set_message(self.split_message_label, "Secret cannot be empty.", is_error=True)
            return

        try:
            num_shares = int(self.num_shares_entry.get())
            threshold = int(self.threshold_entry.get())
        except ValueError:
            self._set_message(self.split_message_label, "Number of shares and threshold must be integers.", is_error=True)
            return

        try:
            shares = split_secret(secret, num_shares, threshold)
            self.shares_text.delete('1.0', tk.END)
            self.shares_text.insert(tk.END, "\n".join(shares))
            self._set_message(self.split_message_label, "Shares generated successfully.")
        except ValueError as e:
            self._set_message(self.split_message_label, f"Error: {e}", is_error=True)

    def combine_shares_gui(self):
        shares_str = self.combine_text.get('1.0', tk.END).strip()
        if not shares_str:
            self._set_message(self.combine_message_label, "Please enter shares to combine.", is_error=True)
            return
        
        shares = shares_str.splitlines()
        
        try:
            secret = combine_shares(shares)
            self._set_message(self.combine_message_label, f"Secret recovered successfully: {secret}")
        except Exception as e:
            self._set_message(self.combine_message_label, f"Error: Could not recover secret. Details: {e}", is_error=True)

def main():
    app = ModernSecretSharingApp()
    app.mainloop()

if __name__ == "__main__":
    main()
