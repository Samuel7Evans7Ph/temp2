import sqlite3

def create_tables():
    sql_stmts= [' create table if not exists files(file_id integer primary key,file_name text NOT NULL,process_status varchar(255));','insert into ']
    # print("hai")

    try:
        with sqlite3.connect('ML_Database1.db') as conn:
            cursor=conn.cursor()
            print("workig?")
            for stmt in sql_stmts:
                cursor.execute(stmt)
                # cursor.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


if __name__=="__main__":
    create_tables()
