

import itertools
import string
import csv
from concurrent.futures import ProcessPoolExecutor, as_completed

def read_passwords_from_csv(file_path):
    passwords = set()
    try:
        with open(file_path, 'passwordcollections.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                passwords.update(row)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return passwords

def try_password(attempt_password, target_password):
    return attempt_password if attempt_password == target_password else None

def generate_passwords(characters, length):
    return (''.join(attempt) for attempt in itertools.product(characters, repeat=length))

def password_cracker(target_password, max_length, csv_file):


    if target_password in passwords_from_csv:
        print(f"Password found in CSV: {target_password}")
        return target_password

    print("Password not found in CSV file. Trying all combinations now...")


    with ProcessPoolExecutor() as executor:
        for length in range(1, max_length + 1):
            futures = []
            for attempt in generate_passwords(characters, length):


                if len(futures) >= 1000:
                    for future in as_completed(futures):
                        result = future.result()
                        if result:
                            print(f"Password found: {result}")
                            return result
                    futures = []

            for future in as_completed(futures):
                result = future.result()
                if result:
                    print(f"Password found: {result}")
                    return result

    print("Password not found.")
    return None

target_password = 'a1B'
max_length = 3
csv_file = 'passwords.csv'


