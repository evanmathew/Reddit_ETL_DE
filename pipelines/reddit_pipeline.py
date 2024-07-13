# this file is the pipline for reddit and the ETL function are defined in ./etls/reddit_etl.py
import pandas as pd # for transforming data

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    """
    Function to pipeline data from a specified subreddit on Reddit.
    
    Parameters:
    file_name (str): The name of the file to save the extracted data.
    subreddit (str): The subreddit from which to extract the data.
    time_filter (str): The time filter for the extracted posts (default is 'day').
    limit (int): The maximum number of posts to extract (default is None).
    
    Returns:
    str: The file path where the extracted data is saved.
    """
    
    # connect to reddit
    instance = connect_reddit(CLIENT_ID, SECRET, 'Evan')
    
    # extraction post from reddit api
    posts = extract_posts(instance, subreddit, time_filter, limit)
    
    # transformation data
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)
    
    # loading to csv file
    file_path = f'{OUTPUT_PATH}/{file_name}.csv' # OUTPUT_PATH is defined in utils/constants.py (OUTPATH=/opt/airflow/data/output which is mapped to ./data/output)
    load_data_to_csv(post_df, file_path)

    return file_path