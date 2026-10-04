# Real-World CLI Budget Tracker

A production-grade, terminal-based personal finance utility built in **Python**. This project showcases high-integrity file handling, defensive parsing loops, real-time input validations, and categorical data analysis metrics.

## 🚀 Key Engineering Features
* **Bulletproof Error Handling:** Implements persistent `while True` validation blocks to gracefully capture and isolate input errors without application termination.
* **Chronological Data Validation:** Integrates Python's native `datetime` module to strictly enforce realistic calendar parsing constraints (e.g., rejecting non-existent calendar dates like February 30th).
* **Data Continuity Protections:** Built using robust Context Managers (`with open`) ensuring that runtime interruptions or crashes safely flush pending tracking streams to disk without corrupting historical indices.
* **Implicit Data Analytics:** Automatically runs categorical matrix summaries to evaluate global asset distributions, showing exact spending percentage weights per category tag.

## 🛠️ Built With
* **Python 3.x**
* Native Libraries: `sqlite3`, `datetime`, `os`

## 📦 How to Install and Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd cli-budget-tracker
   ```

2. **Execute the Application:**
   ```bash
   python budget_tracker.py
   ```

## 📊 Sample Output Demo
```text
================ RELATIONAL SQL STATEMENT (budget_vault.db) ================
Date         | Category           | Amount    
--------------------------------------------------
2026-10-01   | Rent               | \$1200.00   
2026-10-02   | Groceries          | \$150.50    
2026-10-04   | Utilities          | \$85.00     
--------------------------------------------------
NET SQL TOTAL METRIC:             | \$1435.50

--- SPENDING METRICS BY SQL CATEGORY GROUP ---
 * Rent           : \$1200.00   (83.6%)
 * Groceries      : \$150.50    (10.5%)
 * Utilities      : \$85.00     (5.9%)
```

## 🧠 C Foundation Context
This project was conceptualized to translate bare-metal, low-level structural formatting workflows (like manual tracking file pointers and matrix data printing learned in **C**) over to modern, high-level defensive development structures utilizing **Python** paradigms.