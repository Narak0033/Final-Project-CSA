import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import datetime

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect("bookstore.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        telegram_number TEXT NOT NULL
    );
    """)

    cursor.execute("DROP TABLE IF EXISTS book_purchases;")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS book_purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        description TEXT,
        quantity INTEGER NOT NULL,  -- Added quantity column
        purchase_date TEXT,
        delivery_date TEXT,
        FOREIGN KEY(email) REFERENCES users(email)
    );
    """)

    conn.commit()
    conn.close()



root = tk.Tk()
root.title("Welcome to Bookstore")
root.geometry("800x800")
root.configure(bg="light blue")
root.resizable(False, False)

frame = tk.Frame(root, bg="light blue")
frame.pack(expand=True)

try:
    original_image = Image.open("/Users/hornnarak/Downloads/BOOKS.jpg")
    resized_image = original_image.resize((300, 200))
    photo = ImageTk.PhotoImage(resized_image)
except Exception as e:
    print(f'Error loading image: {e}')
    photo = None

def switch_to_homepage():
    for widget in frame.winfo_children():
        widget.destroy()

    image_label = tk.Label(frame, image=photo, bg="light blue")
    image_label.pack(pady=20)

    title_label = tk.Label(frame, text="SUN BORE", font=("Times New Roman", 40, "bold", "italic"), bg="light blue", fg='dark blue')
    title_label.pack(pady=20)

    welcome_label = tk.Label(frame, text="Welcome to the Book Online Store!", font=("Times New Roman", 28, "bold"),
                             bg="light blue", fg="dark blue")
    welcome_label.pack(pady=5)

    about_us_label = tk.Label(
        frame,
        text="About Us:\n"
             "We are passionate about bringing the joy of books to everyone, everywhere especially to book lover! \n"
             "This application will help you to explore, pre-order, and purchase a book that you want in an acceptable price with every existence books.\n\n"
             "Join us and embark on a literary journey like no other!\n\n"
             "Stop waiting anymore, comes and registers with us",
        font=("Times New Roman", 16),
        bg="light blue",
        fg="black",
        justify="center",
        wraplength=600
    )
    about_us_label.pack(pady=20)

    login_button = tk.Button(frame, text="Login", font=("Times New Roman", 16), bg="white", fg="black",
                             command=switch_to_login_screen)
    login_button.pack(pady=10)

    register_button = tk.Button(frame, text="Register", font=("Times New Roman", 16), bg="white", fg="black",
                                 command=switch_to_register_screen)
    register_button.pack(pady=10)


def switch_to_register_screen():
    for widget in frame.winfo_children():
        widget.destroy()

    image_label = tk.Label(frame, image=photo, bg="light blue")
    image_label.pack(pady=10)

    title_label = tk.Label(frame, text="Register", font=("Times New Roman", 36, "bold", "italic"), bg="light blue", fg="dark blue")
    title_label.pack(pady=10)

    label_username = tk.Label(frame, text="Username:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_username.pack(pady=5)
    global entry_username
    entry_username = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_username.pack(pady=5)

    label_email = tk.Label(frame, text="Email:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_email.pack(pady=5)
    global entry_email
    entry_email = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_email.pack(pady=5)

    label_password = tk.Label(frame, text="Password:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_password.pack(pady=5)
    global entry_password
    entry_password = tk.Entry(frame, font=("Times New Roman", 16), width=30, show="*")
    entry_password.pack(pady=5)

    label_confirm_password = tk.Label(frame, text="Confirm Password:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_confirm_password.pack(pady=5)
    global entry_confirm_password
    entry_confirm_password = tk.Entry(frame, font=("Times New Roman", 16), width=30, show="*")
    entry_confirm_password.pack(pady=5)


    label_telegram = tk.Label(frame, text="Telegram Number:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_telegram.pack(pady=5)
    global entry_telegram
    entry_telegram = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_telegram.pack(pady=5)

    register_button = tk.Button(frame, text="Register", font=("Times New Roman", 16), bg="white", fg="black", command=register_user)
    register_button.pack(pady=20)

    back_button = tk.Button(frame, text="Back to Homepage", font=("Times New Roman", 16), bg="white", fg="black", command=switch_to_homepage)
    back_button.pack(pady=10)

def register_user():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    telegram_number = entry_telegram.get()

    if username and email and password and telegram_number:
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, email, password, telegram_number)
                VALUES (?, ?, ?, ?)
            """, (username, email, password, telegram_number))
            conn.commit()
            conn.close()

            messagebox.showinfo("Registration Successful", f"Welcome, {username}! Your account has been registered.")
            entry_username.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            entry_confirm_password.delete(0, tk.END)
            entry_telegram.delete(0, tk.END)

            switch_to_purchase_screen(email)

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "User with this email already exists!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "All fields are required!")

def switch_to_login_screen():
    for widget in frame.winfo_children():
        widget.destroy()

    image_label = tk.Label(frame, image=photo, bg="light blue")
    image_label.pack(pady=10)

    title_label = tk.Label(frame, text="Login", font=("Times New Roman", 36, "bold", "italic"), bg="light blue", fg="dark blue")
    title_label.pack(pady=10)

    label_username = tk.Label(frame, text="Username:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_username.pack(pady=5)
    entry_username = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_username.pack(pady=5)

    label_email = tk.Label(frame, text="Email:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_email.pack(pady=5)
    entry_email = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_email.pack(pady=5)

    label_password = tk.Label(frame, text="Password:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_password.pack(pady=5)
    entry_password = tk.Entry(frame, font=("Times New Roman", 16), width=30, show="*")
    entry_password.pack(pady=5)

    login_button = tk.Button(frame, text="Login", font=("Times New Roman", 16), bg="white", fg="black", command=lambda: login_user(entry_username.get(), entry_email.get(), entry_password.get()))
    login_button.pack(pady=20)

    back_button = tk.Button(frame, text="Back to Homepage", font=("Times New Roman", 16), bg="white", fg="black", command=switch_to_homepage)
    back_button.pack(pady=10)

def login_user(username, email, password):
    if username and email and password:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM users WHERE username = ? AND email = ? AND password = ?
        """, (username, email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
            switch_to_purchase_screen(user[2])  # Pass the email to purchase screen
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
    else:
        messagebox.showerror("Error", "Please fill in both fields.")


def switch_to_purchase_screen(user_email):
    global entry_title, entry_author, entry_description, entry_quantity

    for widget in frame.winfo_children():
        widget.destroy()

    image_label = tk.Label(frame, image=photo, bg="light blue")
    image_label.pack(pady=10)

    title_label = tk.Label(frame, text="Pre-Order Books", font=("Times New Roman", 36, "bold", "italic"), bg="light blue", fg="dark blue")
    title_label.pack(pady=10)

    label_email = tk.Label(frame, text="Email or Password:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_email.pack(pady=5)
    email_entry = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    email_entry.insert(0, user_email)
    email_entry.config(state="readonly")
    email_entry.pack(pady=5)

    label_title = tk.Label(frame, text="Book's Title:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_title.pack(pady=5)
    entry_title = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_title.pack(pady=5)

    label_author = tk.Label(frame, text="Author's Name:", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_author.pack(pady=5)
    entry_author = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_author.pack(pady=5)

    label_description = tk.Label(frame, text="Description (Location):", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_description.pack(pady=5)
    entry_description = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_description.pack(pady=5)

    label_quantity = tk.Label(frame, text="Quantity (7$/unit):", font=("Times New Roman", 16), bg="light blue", fg="black")
    label_quantity.pack(pady=5)
    entry_quantity = tk.Entry(frame, font=("Times New Roman", 16), width=30)
    entry_quantity.pack(pady=5)

    purchase_button = tk.Button(frame, text="Pre-order", font=("Times New Roman", 16), bg="white", fg="black",
                                 command=lambda: purchase_book(user_email, entry_title.get(), entry_author.get(),
                                                               entry_description.get(), entry_quantity.get()))
    purchase_button.pack(pady=20)
    back_button = tk.Button(frame, text="Go to Profile Page", font=("Times New Roman", 16), bg="white", fg="black",
                            command=lambda: switch_to_user_profile(user_email))
    back_button.pack(pady=10)

def purchase_book(email, title, author, description, quantity):
    if email and title and author and quantity:
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")

            purchase_date = datetime.date.today()
            delivery_date = purchase_date + datetime.timedelta(days=7)

            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO book_purchases (email, title, author, description, quantity, purchase_date, delivery_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (email, title, author, description, quantity, purchase_date.isoformat(), delivery_date.isoformat()))
            conn.commit()
            conn.close()

            messagebox.showinfo("Purchase Successful", f"Thank you for pre-ordering {title} by {author}!")

            entry_title.delete(0, tk.END)
            entry_author.delete(0, tk.END)
            entry_description.delete(0, tk.END)
            entry_quantity.delete(0, tk.END)

            switch_to_user_profile(email)

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "All fields are required!")

def switch_to_user_profile(user_email):
    for widget in frame.winfo_children():
        widget.destroy()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users WHERE email = ?", (user_email,))
    user = cursor.fetchone()
    if user:
        username = user[0]
    else:
        username = "User"

    cursor.execute("""
        SELECT title, author, quantity, purchase_date, delivery_date FROM book_purchases WHERE email = ?
    """, (user_email,))
    purchases = cursor.fetchall()
    conn.close()

    image_label = tk.Label(frame, image=photo, bg="light blue")
    image_label.pack(pady=10)

    title_label = tk.Label(frame, text=f"Profile Page: {username}", font=("Times New Roman", 36, "bold", "italic"), bg="light blue", fg="dark blue")
    title_label.pack(pady=10)

    history_label = tk.Label(frame, text="Purchase History:", font=("Times New Roman", 18, "bold"), bg="light blue", fg="black")
    history_label.pack(pady=10)

    total_cost = 0
    for purchase in purchases:
        title, author, quantity, purchase_date, delivery_date = purchase
        total_cost += quantity * 7 + 3  # Base cost $7 per book + $3 delivery fee


        try:
            delivery_datetime = datetime.datetime.strptime(delivery_date, "%Y-%m-%d")
            current_datetime = datetime.datetime.now()
            time_remaining = delivery_datetime - current_datetime

            if time_remaining.total_seconds() > 0:
                hours_remaining = time_remaining.total_seconds() // 3600
                time_status = f"({int(hours_remaining)} hours until delivery)"
            else:
                time_status = "(Delivered)"
        except Exception as e:
            time_status = "(Invalid delivery date)"

        purchase_label = tk.Label(
            frame,
            text=f"{title} by {author} (Quantity: {quantity}) "
                 f"(Ordered: {purchase_date}, Delivery: {delivery_date}) {time_status}",
            font=("Times New Roman", 16),
            bg="light blue",
            fg="black"
        )
        purchase_label.pack(pady=5)

    total_label = tk.Label(frame, text=f"Total Cost: ${total_cost}", font=("Times New Roman", 18, "bold"), bg="light blue", fg="black")
    total_label.pack(pady=10)

    back_button = tk.Button(frame, text="Back to Pre-order", font=("Times New Roman", 16), bg="white", fg="black",
                             command=lambda: switch_to_purchase_screen(user_email))
    back_button.pack(pady=20)


create_tables()
switch_to_homepage()
root.mainloop()
