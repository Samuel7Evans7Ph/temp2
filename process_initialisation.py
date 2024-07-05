import sqlite3
from meta_integrate import *
import cv2

def initialise(image_file_name):

    query1=f"UPDATE files SET process_status='running' where file_name='{image_file_name}';"

    conn=sqlite3.connect('ML_Database1.db')
    cursor=conn.cursor()
    cursor.execute(query1)

    conn.commit()
    img=cv2.imread(os.path.join("Uploaded_Images",image_file_name))
    print(img)
    meta_integrate(img)


    query2 =f"UPDATE files SET process_status='done' where file_name='{image_file_name}';"

    cursor.execute(query2)
    conn.commit()
    cursor.close()
    conn.close()


    print("hai")



    
    return



