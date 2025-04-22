import psycopg2
import csv

# Подключение к БД
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="botusers",  
    user="postgres",       
    password="051221"
)

cur = conn.cursor()

# Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()

# Ввод из консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

# Загрузка из CSV
def insert_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()

# Обновление
def update_entry():
    name = input("Enter name to update: ")
    phone = input("Enter new phone: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
    conn.commit()

# Удаление
def delete_entry():
    value = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()

# Запрос с фильтрами
def query_data():
    filter_value = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s OR phone = %s", (filter_value, filter_value))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Меню
def main():
    create_table()
    while True:
        print("\n1. Insert from console\n2. Insert from CSV\n3. Update\n4. Delete\n5. Query\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv("input.csv")
        elif choice == '3':
            update_entry()
        elif choice == '4':
            delete_entry()
        elif choice == '5':
            query_data()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
