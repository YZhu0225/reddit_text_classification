'''
Run 'python3 app.py' in terminal
Follow local URL
'''

import praw
import pandas as pd
from praw.models import MoreComments
from transformers import pipeline
#from transformers import DistilBertTokenizerFast
import gradio as gr
import numpy as np
import praw
import pandas as pd
from Keys import reddit_keys

reddit= praw.Reddit(client_id=reddit_keys['client_id'],		 # your client id
					client_secret=reddit_keys['client_secret'],	 # your client secret
                    usernme = reddit_keys['usernme'], #profile username
                    password = reddit_keys['password'], #profile password
					user_agent=reddit_keys['user_agent'])	 # your user agent


classifier = pipeline("sentiment-analysis", model="michellejieli/NSFW_text_classifier")

#input_url = "https://www.reddit.com/r/europe/comments/r0hthg/sweden_is_taking_the_lead_to_persuade_the_rest_of/"

def extract_comments(input_url):
    submission = reddit.submission(url=input_url)
    #posts_dict = {"Post text":[],}
    posts_dict = {"Post text":[], "class": []}
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        
        posts_dict["Post text"].append(top_level_comment.body)
        posts_dict["class"].append(classifier(top_level_comment.body)[0]['label'])
    df = pd.DataFrame(posts_dict)
    percent_exp = np.count_nonzero(np.array(df["class"]) == 'NSFW') / df.shape[0]
    output_msg = "Reddit page is contains no explicit content. Page is safe for users under 18."
    if percent_exp > 0:
        output_msg = f"Reddit page contains some explicit content. Users under the age of 18 should proceed with caution. \n{percent_exp * 100:.0f}% explicit."
    if percent_exp > 0.5:
        output_msg = f"Reddit page contains major explicit content. Users be wary. \n{percent_exp * 100:.0f}% explicit."
    return output_msg

# use gradio to create a web interface take a wikipedia page and summarize it
iface = gr.Interface(
    fn=extract_comments,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Enter Reddit page link",
    ),
    outputs="text",
)


if __name__ == "__main__":
    iface.launch()
