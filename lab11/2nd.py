import psycopg2

def delete_data(name=None, number=None):
    # Если параметры не переданы, запрашиваем их у пользователя
    if not name or not number:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
    
    command = "CALL dlt(%s, %s);"
    
    try:
        # Открываем соединение с базой данных
        with psycopg2.connect(host="localhost", database="userbot", user="postgres", password="051221") as conn:
            with conn.cursor() as cur:
                # Выполняем команду удаления
                cur.execute(command, (name, number))
                # Фиксируем изменения
                conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error occurred: {error}")

