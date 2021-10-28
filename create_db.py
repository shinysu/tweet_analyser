from db_secrets import DB_NAME, USER_NAME, PASSWORD, HOST
import pymysql


def create_connection(DB_NAME):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = pymysql.connect(host=HOST,
                               user=USER_NAME,
                               password=PASSWORD,
                               db=DB_NAME,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        return conn
    except Exception as e:
        print("Connection to the database could not be created: ", e)
        return None


def create_tables(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Exception as e:
        print("Tables could not be created:", e)


def create_db():
    """
    A function used to create a database file to store all the data
    """
    connection = create_connection(DB_NAME)
    sql_create_raw_tweets_table = """CREATE TABLE IF NOT EXISTS raw_tweets (
                                  tweet_id INTEGER,
                                  tweet text,
                                  tweet_date timestamp); """

    sql_create_tweets_table = """CREATE TABLE IF NOT EXISTS tweets (
                                      tweet_id INTEGER PRIMARY KEY,
                                      tweet text
                                    ); """

    sql_create_hashes_table = """CREATE TABLE IF NOT EXISTS hash_tags (
                                          id INTEGER PRIMARY KEY AUTO_INCREMENT,
                                          tweet_id INTEGER NOT NULL,
                                          hash_tags text
                                        ); """

    sql_create_mentions_table = """CREATE TABLE IF NOT EXISTS mentions (
                                          id INTEGER PRIMARY KEY AUTO_INCREMENT,
                                          tweet_id INTEGER NOT NULL,
                                          mentions text
                                        ); """

    create_tables(conn=connection, create_table_sql=sql_create_raw_tweets_table)
    create_tables(conn=connection, create_table_sql=sql_create_tweets_table)
    create_tables(conn=connection, create_table_sql=sql_create_hashes_table)
    create_tables(conn=connection, create_table_sql=sql_create_mentions_table)


if __name__ == '__main__':
    create_connection(DB_NAME)
    create_db()
