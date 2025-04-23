import psycopg2

def update(nickname, score):
    """Обновляет счет пользователя."""
    command = """
        UPDATE scores
        SET score = %s
        WHERE user_name = %s;
    """
    try:
        with psycopg2.connect(host="localhost", database="userbot", user="postgres", password="051221") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (score, nickname))
                conn.commit()  # 🔥 без этого изменения не сохранятся
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при обновлении очков:", error)
