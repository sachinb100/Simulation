# Simulation
Distributed System Simulation.
This project simulates a distributed system where different types of data (e.g., Users, Orders,Products) are stored in separate SQLite databases. Multiple threads will perform simultaneous insert operations into these databases.

Run the Project:
1.Clone the repo
git clone https://github.com/sachinb100/simulation.git
cd simulation

2. Create a Virtual Environment
python3 -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


3. Install Required Dependencies
pip install -r requirements.txt


4.Apply Migrations
python manage.py makemigrations
python manage.py migrate --database=users_db
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db

5. Simulate the insertions using the custom management command
python manage.py multitask_insertions

6. Check the Data
 By accessing the respective SQLite databases:

    a)users.db for user data.
    b)products.db for product data.
    c)orders.db for order data.

