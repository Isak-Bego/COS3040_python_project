import csv
import os

from models.base_model import BaseModel

"""
This module contains the CRUD business logic for the employees table. 
"""

EMPLOYEES_FILE_PATH = "data/employees.csv"

class EmployeeModel(BaseModel):

    def create(self, name, surname, role, unique_passkey):
        # Check if the passkey already exists
        if os.path.exists(EMPLOYEES_FILE_PATH):
            with open(EMPLOYEES_FILE_PATH, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    if row and row[3] == unique_passkey:
                        print(f"Error: Passkey {unique_passkey} already exists. Cannot create employee.")
                        return

        # Now create employee
        file_exists = os.path.isfile(EMPLOYEES_FILE_PATH)
        with open(EMPLOYEES_FILE_PATH, mode='a') as file:
            writer = csv.writer(file)

            # If the file is new or empty, write the header first
            if os.stat(EMPLOYEES_FILE_PATH).st_size == 0:
                writer.writerow(["name", "surname", "role", "unique_passkey"])

            writer.writerow([name, surname, role, unique_passkey])

        print(f"Employee {name} {surname} with role {role} and passkey {unique_passkey} created.")

    def read(self, passkey):
        # Read employee's details from the CSV file.
        with open(EMPLOYEES_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == passkey:
                    print(f"Employee found: {row}")
                    return {"name": row[0], "surname": row[1], "role": row[2], "unique_passkey": row[3]}
        print(f"Employee not found.")
        return None

    def read_all(self):
        # Read and return all employee records, skipping the header.
        with open(EMPLOYEES_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            employees = list(reader)

        if not employees:
            print("No employees found.")
            return []

        return employees

    def update(self, passkey, new_name=None, new_surname=None, new_role=None, new_passkey=None):
        # Update employee's details in the CSV file.
        updated = False
        with open(EMPLOYEES_FILE_PATH, mode='r') as file:
            rows = list(csv.reader(file))

        with open(EMPLOYEES_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[3] == passkey:
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
            print(f"Employee with passkey {passkey} updated.")
        else:
            print(f"Employee with passkey {passkey} not found.")

    def delete(self, passkey):
        # Delete employee's record from the CSV file.
        deleted = False
        with open(EMPLOYEES_FILE_PATH, mode='r') as file:
            rows = list(csv.reader(file))

        with open(EMPLOYEES_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if not row[3] == passkey:
                    writer.writerow(row)
                else:
                    deleted = True

        if deleted:
            print(f"Employee with passkey {passkey} deleted.")
        else:
            print(f"Employee with passkey {passkey} not found.")

