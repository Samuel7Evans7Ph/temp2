import sqlite3

def add_file_path(file_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('ML_Database1.db')
    cursor = conn.cursor()

    query_stmt = f"INSERT INTO files (file_name, process_status) VALUES ( '{file_name}', 'In Progress');"
    cursor.execute(query_stmt)

    conn.commit()

    cursor.close()
    conn.close()
    return




