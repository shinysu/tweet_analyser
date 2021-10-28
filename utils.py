from db_utils import run_query, create_connection


def insert_into_raw_tweets(tweet):
    sql_query = """insert into raw_tweets (tweet_id,tweet,tweet_date) VALUES (%s,%s,%s)"""
    run_query(sql_query, [tweet[0], tweet[1], tweet[2]])


def write_to_db(tweets):
    print(tweets)
    for tweet in tweets:
        insert_into_raw_tweets(tweet)


if __name__ == '__main__':
    insert_into_raw_tweets([123, 'text1', '10-12-2010'])
