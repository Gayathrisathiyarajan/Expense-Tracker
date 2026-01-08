# Expense Tracker

## 📌 Project Overview
A simple Expense Tracker web application built using Python, Django. It allows users to manage their daily expenses with full CRUD functionality, generate category-wise summary reports, and download expense data in Excel format.

---

## 🚀 Features
- Add, view, update, and delete expenses (CRUD)
- Category-wise expense summary report
- Download full expense report in Excel format
- Clean and user-friendly UI

---

## 🛠️ Tech Stack
- **Programming Language:** Python 3  
- **Framework:** Django  
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, JavaScript, jQuery
- **Report:** Excel (openpyxl)

---

## 📊 Expense Fields
- Date
- Category
- Amount
- Payment Mode
- Merchant Name
- Location
- Description
- Notes
- Created By

---

## 🗄️ Database
- Uses SQLite (Django default database)
- Database is created fresh using migrations
- Data can be added via the UI after setup

---

## 📈 Reports
- Category-wise summary report displayed in the UI
- Complete expense data downloadable as an Excel file

---

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Gayathrisathiyarajan/Expense-Tracker.git
cd Expense-Tracker
```

2. Create virtual environment & activate:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the Project:

```bash
python manage.py runserver
```

6. Access the app at:

```bash
http://127.0.0.1:8000/
```

---

## 👩‍💻 Author  

**Gayathri S**  
- 📧 Email: gayathrisathiyarajan@gmail.com
- 🌐 GitHub: [Gayathrisathiyarajan](https://github.com/Gayathrisathiyarajan)

