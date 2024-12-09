from django.core.management.base import BaseCommand
from multitask.models import User, Products, Order
import random
from threading import Thread

class Command(BaseCommand):
    help = 'Simulate simultaneous insertions into Users, Orders, and Products'

    def insert_users(self):
        users_data = [
            (1, "Alice", "alice@example.com"),
            (2, "Bob", "bob@example.com"),
            (3, "Charlie", "charlie@example.com"),
            (4, "David", "david@example.com"),
            (5, "Eve", "eve@example.com"),
            (6, "Frank", "frank@example.com"),
            (7, "Grace", "grace@example.com"),
            (8, "Alicey", "alicey@example.com"),
            (9, "Henry", "henry@example.com"),
            (10, "Jane", "jane@example.com")
        ]
        for user_data in users_data:
            User.objects.using('users_db').create(id=user_data[0], name=user_data[1], email=user_data[2])

    def insert_products(self):
        products_data = [
            (1, "Laptop", 1000.00),
            (2, "Smartphone", 700.00),
            (3, "Headphones", 150.00),
            (4, "Monitor", 300.00),
            (5, "Keyboard", 50.00),
            (6, "Mouse", 30.00),
            (7, "Laptop", 1000.00),
            (8, "Smartwatch", 250.00),
            (9, "Gaming Chair", 500.00),
            (10, "Earbuds", -50.00)
        ]
        for product_data in products_data:
            Products.objects.using('products_db').create(id=product_data[0], name=product_data[1], price=product_data[2])

    def insert_orders(self):
        orders_data = [
            (1, 1, 1, 2),
            (2, 2, 2, 2),
            (3, 3, 3, 5),
            (4, 4, 4, 1),
            (5, 5, 5, 3),
            (6, 6, 6, 4),
            (7, 7, 7, 2),
            (8, 8, 8, 0),
            (9, 9, 9, 1),
            (10, 10, 10, 2)
        ]
        for order_data in orders_data:
            Order.objects.using('orders_db').create(id=order_data[0], user=order_data[1], product=order_data[2], quantity=order_data[3])

    def run_insertions(self):
        # Using threads to simulate simultaneous insertions
        threads = []
        for func in [self.insert_users, self.insert_products, self.insert_orders]:
            thread = Thread(target=func)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.stdout.write(self.style.SUCCESS('Simulated insertions completed'))

    def handle(self, *args, **kwargs):
        self.run_insertions()
