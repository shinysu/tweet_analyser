import streamlit as st
from tweepy_utils import get_tweets
from pandas import DataFrame
from utils import write_to_db


def get_user_name():
    username = st.text_input('Enter the user name')
    if '@' in username:
        username = username.split('@')[1]
    print(username)
    return username


username = get_user_name()
#data_load_state = st.text('Loading data...')
tweets = get_tweets(username)
write_to_db(tweets)
df = DataFrame(tweets, columns=["id", "tweets", "created_at"])
if username:
    print(username)
    st.title('Dashboard of ' + username)
    st.table(df['tweets'])
