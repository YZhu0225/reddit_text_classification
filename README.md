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

# Reddit Explicit Text Classifier

![maven](http://img.shields.io/badge/Python-3.10.4-green)
![maven](http://img.shields.io/badge/gradio-3.13.0-orange)
![maven](http://img.shields.io/badge/praw-7.6.1-blue)
![maven](http://img.shields.io/badge/huggingface-0.11.1-yellowgreen)
![maven](http://img.shields.io/badge/torch-1.13.0-yellow)
![maven](http://img.shields.io/badge/transformers-4.25.1-lightgrey)

[![Python application test with Github Actions](https://github.com/YZhu0225/reddit_text_classification/actions/workflows/main.yml/badge.svg)](https://github.com/YZhu0225/reddit_text_classification/actions/workflows/main.yml) 
[![Sync to Hugging Face hub](https://github.com/YZhu0225/reddit_text_classification/actions/workflows/sync_to_hugging_face_hub.yml/badge.svg)](https://github.com/YZhu0225/reddit_text_classification/actions/workflows/sync_to_hugging_face_hub.yml)

## Demo
[<img width="700" src="https://user-images.githubusercontent.com/112578003/207716480-a5ac9596-8095-46d5-9df9-d6973af38e3e.png">](https://youtu.be/0OY0CCK3lI4 "Reddit")

## Introduction

Reddit is a place where people come together to have a variety of conversations on the internet. However, the negative impacts of abusive language on users in online communities are severe. As students passionate about data science, we are interested in detecting inappropriate and unprofessional Reddit posts and warning users based on the url of the posts. 

In this project, we created a text classifier Hugging Face Spaces app and Gradio interface that classifies not safe for work (NSFW) content, specifically text that is considered inappropriate and unprofessional. We used a pre-trained DistilBERT transformer model for the sentiment analysis. The model was fine-tuned on Reddit posts and predicts 2 classes - which are NSFW and safe for work (SFW).

## Workflow
<p align="center">
  <img width="750" height="450" src="https://user-images.githubusercontent.com/112578003/207698683-233c228e-c2d0-441f-bbba-139dd24a98d3.png" />
</p>

### Get Reddit data

* Data pulled in notebook `reddit_data/reddit_new.ipynb`

### Verify GPU works in this [repo](https://github.com/nogibjj/Reddit_Classifier_Final_Project)
* Run pytorch training test: `python utils/quickstart_pytorch.py`
* Run pytorch CUDA test: `python utils/verify_cuda_pytorch.py`
* Run tensorflow training test: `python utils/quickstart_tf2.py`
* Run nvidia monitoring test: `nvidia-smi -l 1`

### DistilBERT transformer model

<p align="center">
  <img width="700" height="350" src="https://user-images.githubusercontent.com/112578003/207486477-a40d62be-8d06-4a35-ae4c-7077569bef44.png" />
</p>

### Finetune text classifier model and upload to Hugging Face 
* In terminal, run `huggingface-cli login`
* Run `python fine_tune_berft.py` to finetune the model on Reddit data 
* Run `rename_labels.py` to change the output labels of the classifier
* Check out the fine-tuned model [here](https://huggingface.co/michellejieli/inappropriate_text_classifier) 
* Check out the spaces app [Spaces APP](https://huggingface.co/spaces/yjzhu0225/reddit_text_classification_app)

### Gradio interface
* In terminal, run `python3 app.py`
* Open the browser
* Put reddit URL in *input_url* and get output

**WARNING Reddit URL**
<p align="center">
  <img width="700" height="250" src="https://user-images.githubusercontent.com/112578003/207698979-f3751140-fc91-4613-9892-c22f2e5b7dfa.png">
</p>

**SAFE Reddit URL**
<p align="center">
  <img width="700" height="250" src="https://user-images.githubusercontent.com/112578003/207699308-8847e2f3-be76-47e4-8a0b-ba4406f5a693.png">
</p>

### Reference
[1] “CADD_dataset,” GitHub, Sep. 26, 2022. https://github.com/nlpcl-lab/cadd_dataset

[2] H. Song, S. H. Ryu, H. Lee, and J. Park, “A Large-scale Comprehensive Abusiveness Detection Dataset with Multifaceted Labels from Reddit,” ACLWeb, Nov. 01, 2021. https://aclanthology.org/2021.conll-1.43/
‌
‌
