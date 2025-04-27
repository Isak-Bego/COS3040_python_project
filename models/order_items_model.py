import csv
import os
import uuid
from time import sleep

from models.base_model import BaseModel

ORDER_ITEMS_FILE_PATH = "data/order_items.csv"

"""
This module contains all the CRUD business logic for the Order Items table.
"""

class OrderItemModel(BaseModel):

    def create(self, item_id, quantity, order_id=None, preparation_status=False):
        """Adds an item to an order."""
        if(order_id is None):
            order_id = str(uuid.uuid4())

        # Check if the item already exists in the order
        if os.path.exists(ORDER_ITEMS_FILE_PATH):
            with open(ORDER_ITEMS_FILE_PATH, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    if row and row[0] == order_id and row[1] == item_id:
                        print(f"Error: Item with ID {item_id} already exists in order {order_id}.")
                        return

        # Now add the new item to the order
        with open(ORDER_ITEMS_FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            # If the file is new or empty, write the header first
            if os.stat(ORDER_ITEMS_FILE_PATH).st_size == 0:
                writer.writerow(["order_id", "item_id", "quantity", "preparation_status"])

            writer.writerow([order_id, item_id, quantity, preparation_status])

        print(f"Item {item_id} with quantity {quantity} added to order {order_id}.")

    def delete(self, order_id, item_id):
        """Removes an item from an order."""
        removed = False
        print(order_id, item_id)
        sleep(7)
        with open(ORDER_ITEMS_FILE_PATH, mode='r') as file:
            rows = list(csv.reader(file))

        with open(ORDER_ITEMS_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] != order_id or row[1] != item_id:
                    writer.writerow(row)
                else:
                    removed = True

        if removed:
            print(f"Item {item_id} removed from order {order_id}.")
        else:
            print(f"Item {item_id} not found in order {order_id}.")

    def read(self, order_id):
        """Retrieves all items in a given order."""
        items_in_order = []
        with open(ORDER_ITEMS_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if row[0] == order_id:
                    items_in_order.append({
                        "order_id": row[0],
                        "item_id": row[1],
                        "quantity": row[2],
                        "preparation_status": row[3]
                    })

        if items_in_order:
            return items_in_order
        else:
            print(f"No items found for order {order_id}.")
            return []


    def read_all(self):
        # Read and return all menu items, skipping the header.
        with open(ORDER_ITEMS_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            items = list(reader)

        if not items:
            print("No menu items found.")
            return []

        return items

    def update(self, order_id, item_id, new_quantity=None, new_preparation_status=None):
        """Updates an item in the order."""
        # Not implemented yet
        raise NotImplementedError("Update method is not implemented.")
