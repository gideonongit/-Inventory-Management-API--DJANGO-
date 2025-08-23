📦 Inventory Management System (Python Django + DRF)


🚀 Project Overview

The Inventory Management System is a web-based application built using Python Django and Django REST Framework (DRF).
It focuses on managing stocks, sales, and purchases while providing administrators with full control over the system.

Key features include:

📊 Graphical representation of data for better insights

🏷️ Manage products, categories, suppliers, and stock movements

🔒 Secure role-based authentication (Admin & Staff)

📝 Reports generation for inventory and sales tracking

This project is ideal for small to medium-sized businesses seeking an efficient way to handle stock operations.

✨ Features

✅ User Authentication (Admin & Staff roles)
✅ Add/Edit/Delete Products
✅ Track stock quantity with low-stock alerts
✅ Record inward and outward product movements
✅ Categorize products
✅ Supplier management
✅ Generate inventory and transaction reports
✅ RESTful APIs for frontend/mobile integration

🛠️ Tech Stack

Backend: Python, Django, Django REST Framework

Database: SQLite (default) / PostgreSQL (recommended)

Authentication: Token-based (via rest_framework.authtoken)

Frontend: Django Admin Panel (default), APIs available for integration

📂 Models Overview
🔐 User

username, email, password

role (admin, staff), date_joined

📦 Product

name, description, SKU, quantity, price, category, date_added

🗂 Category

name, description

🧾 Supplier

name, contact_info

🧮 Order

product, quantity, type (in/out), date, supplier, staff_user

📄 StockLog

product, change_type (added/removed), quantity, timestamp
