import psycopg2

def part_of_name(pattern=None):
    """Запрос данных по шаблону (часть имени, фамилии или телефона)."""
    
    if not pattern:
        pattern = input("Enter the pattern to search: ")
    
    command = """
        SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s;
        """
    try:
        with psycopg2.connect(host="localhost", database="userbot", user="postgres", password="051221") as conn:
            with conn.cursor() as cur:
                # Используем шаблон поиска для имени и телефона
                cur.execute(command, ('%' + pattern + '%', '%' + pattern + '%'))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No matching records found.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error occurred: {error}")

