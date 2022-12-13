---
title: reddit_text_classification_app 
emoji: 🐠
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 3.13.0
app_file: app.py
pinned: false
---


# reddit_text_classification

Ideas - text classification 

API that does a microservice

Use swagger documentation

Filter words 
Query on it
Text classification - sentiment analysis

Filter, spam, sensitive content, cuss words

https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/

Look for explicit things, further research on which subreddit to use 

Find data contains labels with data that is similar to how people type on reddit

Figure out which model 

If it does 

Next steps:
EOD Wednesday 

Meet next Monday 12:30 PM

https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/



Trying to break the project into as small as pieces as possible, where we are able to get in static copy of some known matches and some where they dont match, some examples of posts that are good and some examples of posts are bad, get everything locally first, and then once we get that working, then will try to hook it up to API, get reddit api (if we can get it), real time stuff - cherry on sundae (nice to have) but without the system working, better to not do it at all, download posts first, take half an hour to see if API gave me ability to grab a post, use API to grab a few posts, put in some fake bad words, inject some bad words into it inject into original post, get everything working, hugging face model to detect toxic content (that itself is good enough), have some data, get spaces app, command line tool app, 99% on that, real time is only if we have time 

Things to do: 
- (Yuanjing and Xiaoquan) Find examples of reddit posts for both classes we are trying to classify, Convert to CSV (2 columns - text, class), 2 classes, Thursday December 8, 2022
- (Michelle) Find Hugging Face model to use to classify posts
- (Michelle) Finetune model on reddit posts and upload to Hugging Face (create API)
- (Susanna) Create CLI or spaces app on Hugging Face
- Connect to real time (optional) 
- (Xiaoquan and Yuanjing) Make demo video 


Due date: December 16, 2022 

Demo - split up the workload so that it uses everybody’s best talents, not everyone has to present, break problem up so that final outcome is the best, one person really good at editing, can be editor, if one person is good at voiceocer then do the voiceover, if one person is good at documentation, then one person does documentation, if one person is doing coding, then one person is doing coding, 
