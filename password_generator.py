import tkinter as tk
from tkinter import messagebox, StringVar, Frame, Label, Entry, Radiobutton, Button
import random


def update_messages():
    """Clear error messages."""
    length_error_label.config(text="")
    complexity_error_label.config(text="")


def generate_weak_password(length):
    """Generate a weak password with uppercase and lowercase letters."""
    return "".join(
        chr(random.choice([random.randint(65, 90), random.randint(97, 122)]))
        for _ in range(length)
    )


def generate_moderate_password(length):
    """Generate a moderate password with letters and digits."""
    return "".join(
        chr(random.choice([random.randint(65, 90), random.randint(97, 122), random.randint(48, 57)]))
        for _ in range(length)
    )


def generate_strong_password(length):
    """Generate a strong password with letters, digits, and special characters."""
    return "".join(chr(random.randint(33, 126)) for _ in range(length))


def generate_password():
    """Main function to generate and display the password."""
    if not password_length.get():
        length_error_label.config(text="Error: Length field is empty.")
        r.after(2000, update_messages)
        return

    if not password_length.get().isdigit():
        length_error_label.config(text="Error: Length must be a number.")
        r.after(2000, update_messages)
        return

    length = int(password_length.get())
    if length < 5 or length > 50:
        length_error_label.config(text="Error: Length must be between 5 and 50.")
        r.after(2000, update_messages)
        return

    if not password_complexity.get():
        complexity_error_label.config(text="Error: Select password complexity.")
        r.after(2000, update_messages)
        return

    # Generate password based on selected complexity
    if password_complexity.get() == "weak":
        password = generate_weak_password(length)
    elif password_complexity.get() == "moderate":
        password = generate_moderate_password(length)
    else:
        password = generate_strong_password(length)

    # Display the password in a new window
    result_window = tk.Toplevel(r)
    result_window.title("Generated Password")
    result_window.geometry("500x100")
    result_window.config(bg="#1E1E1E")
    Label(
        result_window,
        text=password,
        bg="#1E1E1E",
        fg="#FF8C00",
        font=("Consolas", 16, "bold"),
        wraplength=480,
    ).pack(pady=20)


# Main Application
r = tk.Tk()
r.title("Password Generator")
r.geometry("500x300")
r.config(bg="#FFFAF0")

# Heading
Label(
    r,
    text="Password Generator",
    bg="#1E1E1E",
    fg="#FF8C00",
    font=("Helvetica", 18, "bold"),
).pack(pady=10, fill=tk.X)

# Password Length Input
frame_length = Frame(r, bg="#FFFAF0")
frame_length.pack(pady=20)

Label(frame_length, text="Password Length:", bg="#FFFAF0", font=("Arial", 12)).grid(row=0, column=0, padx=5)
password_length = StringVar()
Entry(
    frame_length,
    textvariable=password_length,
    font=("Arial", 12),
    width=10,
    justify="center",
).grid(row=0, column=1, padx=5)
length_error_label = Label(frame_length, text="", bg="#FFFAF0", fg="red", font=("Arial", 10))
length_error_label.grid(row=1, column=1, pady=5)

# Password Complexity Selection
frame_complexity = Frame(r, bg="#FFFAF0")
frame_complexity.pack()

password_complexity = StringVar()
Radiobutton(
    frame_complexity,
    text="Weak",
    variable=password_complexity,
    value="weak",
    bg="#FFFAF0",
    font=("Arial", 12),
).grid(row=0, column=0, padx=5)
Radiobutton(
    frame_complexity,
    text="Moderate",
    variable=password_complexity,
    value="moderate",
    bg="#FFFAF0",
    font=("Arial", 12),
).grid(row=0, column=1, padx=5)
Radiobutton(
    frame_complexity,
    text="Strong",
    variable=password_complexity,
    value="strong",
    bg="#FFFAF0",
    font=("Arial", 12),
).grid(row=0, column=2, padx=5)
complexity_error_label = Label(r, text="", bg="#FFFAF0", fg="red", font=("Arial", 10))
complexity_error_label.pack(pady=5)

# Action Buttons
frame_buttons = Frame(r, bg="#FFFAF0")
frame_buttons.pack(pady=10)

Button(
    frame_buttons,
    text="Generate Password",
    bg="#1E1E1E",
    fg="#FF8C00",
    font=("Arial", 12),
    command=generate_password,
).grid(row=0, column=0, padx=10)
Button(
    frame_buttons,
    text="Quit",
    bg="#1E1E1E",
    fg="#FF8C00",
    font=("Arial", 12),
    command=r.quit,
).grid(row=0, column=1, padx=10)

r.mainloop()
