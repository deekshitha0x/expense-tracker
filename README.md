# Expense Tracker 💸

A simple web-based expense tracker built with Flask. Add expenses with categories, view total spending, and delete entries — all through a clean web interface.

## Features
- Add expenses with title, amount, and category
- View all expenses in a table
- See total spending calculated automatically
- Delete individual expenses
- Input validation (no negative or zero amounts)

## Tech Stack
- Python
- Flask
- HTML
- Jinja2 (templating)
  

## How to Run
1. Clone the repository
   git clone https://github.com/deekshitha0x/expense-tracker.git
   cd expense-tracker

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   python app.py

4. Open your browser and go to
   http://127.0.0.1:5000


## Project Structure
expense-tracker/
├── app.py
├── requirements.txt
└── templates/
└── index.html


## Future Improvements
- Add data persistence (currently resets when server restarts)
- Add expense editing
- Add date tracking for expenses
- Add charts for category-wise spending

## Author
Deekshitha — [GitHub](https://github.com/deekshitha0x)
