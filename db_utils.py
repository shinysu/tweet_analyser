"""
functions for interaction with the database.
"""
from db_secrets import DB_NAME, USER_NAME, PASSWORD, HOST
import pymysql


def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or Noneinsert_into_user_input
    """
    try:
        conn = pymysql.connect(host=HOST,
                               user=USER_NAME,
                               password=PASSWORD,
                               db=DB_NAME,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        return conn
    except:
        return None


def run_query(query, args=[], conn=None):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param query: a SQL query
    :return:
    """
    if not conn:
        conn = create_connection()

    with conn.cursor() as cursor:
        if query.lower().startswith("select"):
            cursor.execute(query=query, args=args) if args else cursor.execute(query=query)
            return cursor.fetchall()
        else:
            cursor.execute(query=query, args=args)
    try:
        conn.commit()
    except Exception as e:
        print("ERROR OCCURED WHILE DB COMMIT --- DB_UTILS: 43", e)