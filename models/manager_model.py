import csv

from models.base_model import BaseModel


class ManagerModel(BaseModel):

    def create(self, username, password):
        # Create a new manager entry in the CSV file.
        with open('managers.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print(f"Manager {username} created with password: {password}")

    def read(self, username):
        # Read manager's credentials from the CSV file.
        with open('managers.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    print(f"Manager found: {row}")
                    return {"username": row[0], "password": row[1]}
        print("Manager not found.")
        return None

    def update(self, username, new_username=None, new_password=None):
        # Update manager's credentials in the CSV file.
        updated = False
        with open('managers.csv', mode='r') as file:
            rows = list(csv.reader(file))

        with open('managers.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == username:
                    if new_username:
                        row[0] = new_username
                    if new_password:
                        row[1] = new_password
                    updated = True
                writer.writerow(row)

        if updated:
            print(f"Manager {username} updated.")
        else:
            print("Manager not found.")

    def delete(self, username):
        # Delete manager's credentials from the CSV file.
        deleted = False
        with open('managers.csv', mode='r') as file:
            rows = list(csv.reader(file))

        with open('managers.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] != username:
                    writer.writerow(row)
                else:
                    deleted = True

        if deleted:
            print(f"Manager {username} deleted.")
        else:
            print("Manager not found.")


