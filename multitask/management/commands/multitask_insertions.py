from django.core.management.base import BaseCommand
from multitask.models import User, Products, Order
from random import randint
# from threading import Thread
from django.db import connections
import threading
from django.db import transaction
class Command(BaseCommand):
        help = 'Simulate multiple insertions into different databases'

        def insert_user(self,index):
            user = User(id=index, name=f'User{index}', email=f'user{index}@example.com')
            user.save(using='users_db')

        def insert_product(self,index):
            

            print(f"Starting insertion for product {index}")
            try:
                product = Products(id=index, name=f'Products{index}', price=100.0 * index)
                product.save(using='products_db')
                print(f"Successfully inserted product {index}")
            except Exception as e:
                print(f"Error inserting product {index}: {e}")

    
        def insert_order(self,index):
            user_id =  index
            product_id = index
            # Fetch the User and Product instances
            user = User.objects.using('users_db').filter(id=user_id).first()
            product = Products.objects.using('products_db').filter(id=product_id).first()

             # Check if both user and product exist in their respective databases
            if User.objects.using('users_db').filter(id=user_id).exists() and Products.objects.using('products_db').filter(id=product_id).exists():
                # Directly use the user_id and product_id (not model instances)
                order = Order(id=index, user=user_id, product=product_id, quantity=randint(1, 5))
                order.save(using='orders_db')
                print(f"Order for User {user_id} and Product {product_id} inserted successfully.")
            else:
                print(f"User or Product with id {user_id} or {product_id} does not exist.")




           



        def run_inserts(self):
            threads = []

            for i in range(1,11):
                t_user = threading.Thread(target=self.insert_user, args=(i,))
                t_product = threading.Thread(target=self.insert_product, args=(i,))
        

                t_user.start()
                t_product.start()

                t_user.join()
                t_product.join()

                t_order = threading.Thread(target=self.insert_order, args=(i,))

                t_order.start()
                threads.append(t_order)

              

                for thread in threads:
                    thread.join()

                self.stdout.write(self.style.SUCCESS('Data inserted successfully into all databases!'))


        def handle(self, *args, **options):
            self.run_inserts()
           
