import sqlite3
from datetime import datetime
import os

# Define our database file connection target
DB_FILE = "budget_vault.db"

def init_database():
    """Initializes the SQLite database engine and creates structural schema."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Create relational column definitions with explicit type invariants
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL
                )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"❌ Database Engine Initialization Failure: {e}")

def get_validated_date():
    """Forces the user to provide a valid, real-world chronological date constraint."""
    while True:
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_str:
            return datetime.today().strftime('%Y-%m-%d')
        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date.strftime('%Y-%m-%d')
        except ValueError:
            print("❌ Invalid calendar entry. Format must be exact YYYY-MM-DD. Try again.")

def get_validated_amount():
    """Strictly enforces clean, positive non-zero financial entry values."""
    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount <= 0:
                print("❌ Out of bounds. Expenses must be a positive number greater than 0.")
                continue
            return amount
        except ValueError:
            print("❌ Input parsing error. Please enter a valid decimal number.")

def add_expense():
    """Inserts clean, typed datasets directly into SQL tables securely."""
    print("\n--- SECURE TRANSACTION RECORDING (SQL) ---")
    date = get_validated_date()
    category = input("Enter category (e.g., Food, Rent): ").strip().title()
    if not category:
        category = "Uncategorized"
    amount = get_validated_amount()

    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Use parameterized execution (?) to completely block SQL Injection attacks
            cursor.execute(
                "INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)",
                (date, category, amount)
            )
            conn.commit()
        print(f"✅ Success! Transaction committed securely to SQL database.")
    except sqlite3.Error as e:
        print(f"❌ Database Write Transaction Interrupted: {e}")

def view_expenses():
    """Queries SQL ledger records to run performant global calculations."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            
            # Query 1: Fetch all chronological transactions
            cursor.execute("SELECT date, category, amount FROM expenses ORDER BY date DESC")
            rows = cursor.fetchall()
            
            if not rows:
                print("\n Empty SQL ledger instance found. No transactions recorded yet.")
                return

            print(f"\n================ RELATIONAL SQL STATEMENT ({DB_FILE}) ================")
            print(f"{'Date':<12} | {'Category':<18} | {'Amount':<10}")
            print("-" * 50)
            
            for date, category, amount in rows:
                print(f"{date:<12} | {category:<18} | ${amount:<10.2f}")

            # Query 2: Let the database engine calculate aggregates directly
            cursor.execute("SELECT SUM(amount) FROM expenses")
            total_spent = cursor.fetchone()[0] or 0.0
            
            print("-" * 50)
            print(f"{'NET SQL TOTAL METRIC:':<33} | ${total_spent:.2f}")

            # Query 3: Group and aggregate categories efficiently using pure SQL syntax
            print("\n--- SPENDING METRICS BY SQL CATEGORY GROUP ---")
            cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC")
            category_metrics = cursor.fetchall()

            for cat, subtotal in category_metrics:
                percentage = (subtotal / total_spent) * 100 if total_spent > 0 else 0
                print(f" * {cat:<15}: ${subtotal:<9.2f} ({percentage:.1f}%)")
                
    except sqlite3.Error as e:
        print(f"❌ Relational Engine Read Query Exception: {e}")

def main():
    init_database()
    
    while True:
        print("\n======================= SQL METRIC MENU =======================")
        print("1. Log an Expense (Write to SQL Table)")
        print("2. View Statement & Category Statistics (SQL Queries)")
        print("3. Safely Terminate Application")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("\nShutting down engine safely. SQLite database closed.")
            break
        else:
            print("❌ Invalid menu matrix option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()