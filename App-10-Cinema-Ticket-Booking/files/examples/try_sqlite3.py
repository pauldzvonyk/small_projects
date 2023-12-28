import sqlite3


def create_table():
    conn = sqlite3.connect("../../my_cinema.db")
    conn.execute("""CREATE TABLE "Seat" (
        "seat_id"	TEXT,
        "taken"	INTEGER,
        "price"	REAL)
    """)

    conn.commit()
    conn.close()


def insert_record():
    conn = sqlite3.connect("../../my_cinema.db")
    conn.execute("""
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", "0", "10"), ("A2", "1", "11"), ("A3", "0", "9")
    """)

    conn.commit()
    conn.close()


def select_all():
    conn = sqlite3.connect("../../my_cinema.db")
    cursor = conn.execute("""
    SELECT * FROM "Seat"
    """)
    result = cursor.fetchall()
    conn.close()
    return result


def select_specific_columns():
    conn = sqlite3.connect("../../my_cinema.db")
    cursor = conn.execute("""
    SELECT "seat_id", "price" FROM "Seat"
    """)
    result = cursor.fetchall()
    conn.close()
    return result


def select_with_conditions():
    conn = sqlite3.connect("../../my_cinema.db")
    cursor = conn.execute("""
    SELECT "seat_id", "price" FROM "Seat" WHERE "price" >= 10
    """)
    result = cursor.fetchall()
    conn.close()
    return result


def update_value():
    conn = sqlite3.connect("../../my_cinema.db")
    conn.execute("""
    UPDATE "Seat" SET "taken"=1 WHERE "seat_id"="A2"
    """)
    conn.commit()
    conn.close()


def delete_record():
    conn = sqlite3.connect("../../my_cinema.db")
    conn.execute("""
    DELETE FROM "Seat" WHERE "seat_id" = "A3"
    """)
    conn.commit()
    conn.close()


def update_value_with_queries(occupied, seat_id):
    conn = sqlite3.connect("../../my_cinema.db")
    conn.execute("""
    UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
    """, [occupied, seat_id])
    conn.commit()
    conn.close()


# create_table()
# insert_record()
# print(select_all())
# print(select_specific_columns())
# print(select_with_conditions())
# update_value()
# delete_record()
# update_value_with_queries(occupied=0, seat_id="A2")
