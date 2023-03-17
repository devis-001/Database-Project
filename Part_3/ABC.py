import sqlite3
import sys

sys.builtin_module_names

def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"ABC.sqlite")

def main():