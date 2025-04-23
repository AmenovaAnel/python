import psycopg2

def delete_data(count):
    # Подключаемся к базе данных один раз
    try:
        with psycopg2.connect(host="localhost", database="userbot", user="postgres", password="051221") as conn:
            with conn.cursor() as cur:
                for _ in range(count):
                    # Запрашиваем имя и номер в одном блоке
                    name = input("Enter name: ")
                    number = input("Enter phone number: ")
                    
                    # Выполняем удаление
                    command = "CALL dlt(%s, %s);"
                    cur.execute(command, (name, number))
                
                # Фиксируем изменения
                conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error occurred: {error}")

