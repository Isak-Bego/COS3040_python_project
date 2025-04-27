import csv
from models.base_model import BaseModel

class EmployeeModel(BaseModel):

    def create(self, name, surname, role, unique_passkey):
        # Create a new employee entry in the CSV file.
        with open('employees.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, surname, role, unique_passkey])
        print(f"Employee {name} {surname} with role {role} and passkey {unique_passkey} created.")

    def read(self, name, surname):
        # Read employee's details from the CSV file.
        with open('employees.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name and row[1] == surname:
                    print(f"Employee found: {row}")
                    return {"name": row[0], "surname": row[1], "role": row[2], "unique_passkey": row[3]}
        print(f"Employee {name} {surname} not found.")
        return None

    def update(self, name, surname, new_name=None, new_surname=None, new_role=None, new_passkey=None):
        # Update employee's details in the CSV file.
        updated = False
        with open('employees.csv', mode='r') as file:
            rows = list(csv.reader(file))

        with open('employees.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == name and row[1] == surname:
                    if new_name:
                        row[0] = new_name
                    if new_surname:
                        row[1] = new_surname
                    if new_role:
                        row[2] = new_role
                    if new_passkey:
                        row[3] = new_passkey
                    updated = True
                writer.writerow(row)

        if updated:
            print(f"Employee {name} {surname} updated.")
        else:
            print(f"Employee {name} {surname} not found.")

    def delete(self, name, surname):
        # Delete employee's record from the CSV file.
        deleted = False
        with open('employees.csv', mode='r') as file:
            rows = list(csv.reader(file))

        with open('employees.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] != name or row[1] != surname:
                    writer.writerow(row)
                else:
                    deleted = True

        if deleted:
            print(f"Employee {name} {surname} deleted.")
        else:
            print(f"Employee {name} {surname} not found.")

