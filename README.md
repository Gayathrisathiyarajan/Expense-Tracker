# Expense Tracker

## 📌 Project Overview
This is a simple and user-friendly Expense Tracker web application built using Python and Django. It helps users easily record, view, update, and manage their daily expenses. The application also provides category-wise expense summaries and allows users to download expense reports in Excel format.

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

##  ScreenShots
<img width="1918" height="1079" alt="Expense tracker form" src="https://github.com/user-attachments/assets/788439db-b3b8-4035-bc54-3b6dec18a007" />
<img width="1892" height="1079" alt="expense tracker insert" src="https://github.com/user-attachments/assets/fc54e97f-c975-40e1-9af9-314dbc45fa40" />
<img width="1919" height="1079" alt="expense tracker listing" src="https://github.com/user-attachments/assets/20d08dc3-bf43-44c9-ad3c-146b82230cd1" />
<img width="1919" height="1079" alt="expense tacker update" src="https://github.com/user-attachments/assets/658db667-7770-4947-83d0-a1f929f2cb46" />
<img width="1919" height="1078" alt="expense tacker report" src="https://github.com/user-attachments/assets/65ed4979-6a45-445c-8772-12a7d5742642" />
<img width="1918" height="1078" alt="expense tacker excel" src="https://github.com/user-attachments/assets/97f2c22f-383c-47a8-ab5c-23920670e8df" />
board.png)
