import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Login")
        
        self.attempts = 0  # Track login attempts
        self.max_attempts = 3  # Maximum allowed attempts
        
        self.label = tk.Label(master, text="Enter your PIN:")
        self.label.pack()

        self.pin_entry = tk.Entry(master, show="*")
        self.pin_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.check_pin)
        self.login_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def check_pin(self):
        # Assume the correct PIN is "1234"
        correct_pin = "1234"
        entered_pin = self.pin_entry.get()

        if entered_pin == correct_pin:
            messagebox.showinfo("Success", "Login successful!")
            self.attempts = 0  # Reset attempts on success
            self.pin_entry.delete(0, tk.END)  # Clear entry
        else:
            self.attempts += 1
            messagebox.showerror("Error", "Incorrect PIN.")

            if self.attempts >= self.max_attempts:
                self.login_button.config(state=tk.DISABLED)  # Disable login button
                messagebox.showwarning("Warning", "Three unsuccessful attempts. The police will be called.")
                self.master.quit()  # Optional: close the application

            self.pin_entry.delete(0, tk.END)  # Clear entry after each attempt

if __name__ == "__main__":
    root = tk.Tk()
    atm_app = ATM(root)
    root.mainloop()
