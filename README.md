# Final-Project-CSA (Online Bookstore Application)
Project title: SUN BORE

# Project Problem 
The application aims to solve the issue of the lack of an online platform for purchasing books in Cambodia. The inspiration stems from the growing number of readers and bookstore owners in the region. The system provides a convenient way for book lovers to pre-order books online. It currently focuses on readers and futurely will develop on the functionality for bookstore owners to add inventory.

# Project Overview
This project is a Tkinter-based GUI application that enables users to pre-order books online. The application provides a simple interface for user registration, login, book ordering, and viewing order history.

## Project Features
- **User Registration**: Secure registration with email, password, and Telegram number.
- **Login System**: Authenticate users and redirect them to the main interface.
- **Book Pre-Order**: Simplified process for ordering books with quantity and delivery tracking.
- **Order History**: Users can view their past purchases and track delivery status.

## Code Function
- connect_db()	Establishes a connection to the SQLite database.
- create_tables()	Initializes the database schema for users and book purchases.
- register_user()	Handles user registration and input validation.
- login_user()	Authenticates users and redirects to the purchase screen on success.
- purchase_book()	Records book pre-orders and calculates delivery dates.
- switch_to_homepage()	Displays the application's homepage.
- switch_to_register_screen()	Displays the registration form for new users.
- switch_to_login_screen()	Displays the login form for existing users.
- switch_to_purchase_screen()	Shows the book pre-order form and handles purchases.
- switch_to_user_profile()	Displays the user's profile with order history and total cost calculation.

## Requirements Before Run the Code
1. **Dependencies**:
   - Python 3.x
   - `Pillow` library (`pip install Pillow`)
2. **Image Setup**:
   - Replace the image path in the code with the path to your desired image.

## Database
The application uses an SQLite database (`bookstore.db`) with the following tables:
- **Users**: Stores user information (username, email, password, Telegram number).
- **Book Purchases**: Tracks book orders, including titles, quantities, and delivery dates.
- **Users' Data**: The users' data will be storing in the table plus.

## Running the Application
1. Clone the repository.
2. Install dependencies using:
   ```bash
   pip install Pillow

