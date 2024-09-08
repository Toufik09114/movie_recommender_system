import sqlite3

def view_table(table_name):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM {table_name};")
        rows = c.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

table_data = view_table('users')
print(f"history table")
for row in table_data:
    print(row)