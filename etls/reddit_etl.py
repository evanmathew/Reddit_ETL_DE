import sys
import praw
from praw import Reddit # praw is a python wrapper for the reddit API
import pandas as pd # for transforming data
import numpy as np # for transforming data
from utils.constants import POST_FIELDS #POSTFIELDS are declared in ./utils/constants.py



def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    """
    Connects to Reddit using the provided client information and returns a Reddit instance.

    Parameters:
    - client_id: str, the client ID for authentication
    - client_secret: str, the client secret for authentication
    - user_agent: str, the user agent for authentication

    Returns:
    - Reddit: a Reddit instance connected using the provided credentials

    Raises:
    - SystemExit: if there is an error connecting to Reddit
    """
    
    # Connect to Reddit using the provided client information
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        
        # Print a message indicating successful connection
        print('connected to reddit')
        
        # Return the Reddit instance
        return reddit
    
    # If there is an error, print the error message and exit the program
    except Exception as e:
        print(e)
        sys.exit(1)
        
        
       
       
       
     
def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    """
    Extracts posts from a subreddit based on the provided filters.

    Parameters:
    - reddit_instance: Reddit instance used for authentication
    - subreddit: str, the name of the subreddit to extract posts from
    - time_filter: str, the time filter to apply to the extraction
    - limit: int, the maximum number of posts to extract (default: None)

    Returns:
    - List[Dict[str, Any]], a list of dictionaries representing the extracted posts.
      Each dictionary contains information about a single post, with keys matching the
      fields in the POST_FIELDS constant.
    """

    # Get the subreddit object from the Reddit instance
    subreddit = reddit_instance.subreddit(subreddit)

    # Get the top posts from the subreddit based on the provided filters
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    # Initialize an empty list to store the extracted posts
    post_lists = []

    # Iterate over each post and extract the relevant information
    for post in posts:
        # Convert the post object to a dictionary
        post_dict = vars(post)
        
        # Extract the relevant fields from the post dictionary
        post = {key: post_dict[key] for key in POST_FIELDS}
        
        # Add the extracted post to the list
        post_lists.append(post)

    # Return the list of extracted posts
    return post_lists





def transform_data(post_df: pd.DataFrame):
    """
    Transform the post DataFrame by converting data types and handling missing values.

    Parameters:
    - post_df: pd.DataFrame, the DataFrame containing post data

    Returns:
    - pd.DataFrame, the transformed post DataFrame
    """
    # Convert epoch time to datetime
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')

    # Convert boolean column to True/False
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)

    # Convert author column to string type
    post_df['author'] = post_df['author'].astype(str)

    # Handle missing values in the 'edited' column
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)

    # Convert num_comments and score columns to integer
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)

    # Convert title column to string type
    post_df['title'] = post_df['title'].astype(str)

    return post_df





def load_data_to_csv(data: pd.DataFrame, path: str):
    """
    Load a DataFrame to a CSV file.

    Parameters:
    - data: pd.DataFrame, the DataFrame to be loaded
    - path: str, the path to the CSV file

    This function loads a DataFrame to a CSV file. It takes in a DataFrame and a path
    to a CSV file, and saves the DataFrame to the specified file.

    """
    # Load the DataFrame to a CSV file
    # The index=False argument ensures that the index is not included in the CSV file
    data.to_csv(path, index=False)
