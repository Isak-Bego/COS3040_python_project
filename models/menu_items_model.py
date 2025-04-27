import csv
import os
from models.base_model import BaseModel

MENU_ITEMS_FILE_PATH = "data/menu_items.csv"

class MenuItemModel(BaseModel):

    def create(self, name, category, price):
        item_id = 1  # Default starting ID
        # Check if the menu item already exists by name
        if os.path.exists(MENU_ITEMS_FILE_PATH):
            with open(MENU_ITEMS_FILE_PATH, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    item_id = max(item_id, int(row[0]))
                    if row and row[1] == name:
                        print(f"Error: Menu item {name} already exists. Cannot create item.")
                        return

        # Now create the menu item
        with open(MENU_ITEMS_FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)

            # If the file is new or empty, write the header first
            if os.stat(MENU_ITEMS_FILE_PATH).st_size == 0:
                writer.writerow(["id", "name", "category", "price"])

            writer.writerow([item_id+1, name, category, price]) # increase the max id with one to ensure uniqueness

        print(f"Menu item {name} with category {category} and price {price} created.")

    def read(self, item_id):
        # Read menu item's details from the CSV file by ID.
        with open(MENU_ITEMS_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if int(row[0]) == item_id:
                    print(f"Menu item found: {row}")
                    return {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
        print(f"Menu item with ID {item_id} not found.")
        return None

    def read_all(self):
        # Read and return all menu items, skipping the header.
        with open(MENU_ITEMS_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            items = list(reader)

        if not items:
            print("No menu items found.")
            return []

        return items

    def update(self, item_id, new_name=None, new_category=None, new_price=None):
        # Update menu item's details in the CSV file.
        updated = False
        with open(MENU_ITEMS_FILE_PATH, mode='r') as file:
            rows = list(csv.reader(file))

        with open(MENU_ITEMS_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == item_id:
                    if new_name:
                        row[1] = new_name
                    if new_category:
                        row[2] = new_category
                    if new_price:
                        row[3] = new_price
                    updated = True
                writer.writerow(row)

        if updated:
            print(f"Menu item with ID {item_id} updated.")
        else:
            print(f"Menu item with ID {item_id} not found.")

    def delete(self, item_id):
        # Delete menu item's record from the CSV file.
        deleted = False
        with open(MENU_ITEMS_FILE_PATH, mode='r') as file:
            rows = list(csv.reader(file))

        with open(MENU_ITEMS_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] != item_id:
                    writer.writerow(row)
                else:
                    deleted = True

        if deleted:
            print(f"Menu item with ID {item_id} deleted.")
        else:
            print(f"Menu item with ID {item_id} not found.")
