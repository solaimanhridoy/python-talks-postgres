import psycopg2 as pg

# Connect the database
con = pg.connect(
    host = "127.0.0.1",
    database = "postgres",
    user = "postgres",
    password = "fuckpass",
)

# Cursor
cursor = con.cursor()

# query execution
cursor.execute("SELECT id, first_name, last_name FROM person;")

rows = cursor.fetchall()

for r in rows:
    print (f"{r[0]} {r[1]} {r[2]}")

# Commit the changes
con.commit()

# Cursor closing
cursor.close()

# Close the connection
con.close()