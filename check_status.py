import os
import sqlite3




def present_status(image_file_path):
    query=f"select process_status from files where file_name='{image_file_path}';"
    
    conn=sqlite3.connect('ML_Database1.db')
    cursor=conn.cursor()
    cursor.execute(query)
    status=cursor.fetchone()
    print(status)

    conn.commit()

    return status 

