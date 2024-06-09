import cx_Oracle
import traceback

conn = None
try:
    conn=cx_Oracle.connect("system/123@127.0.0.1/xe")
    print("Connect successfully to db")
    print("db Version:", conn.version)
    print("username:", conn.username)
except cx_Oracle.DatabaseError:
    print("sorry connection failed")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("disconnected with the database")