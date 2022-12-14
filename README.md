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

## Introduction

In this project, we created a text classifier Hugging Face Spaces app and Gradio interface that classifies not safe for work (NSFW) content, specifically text that is considered inappropriate and unprofessional. We used a pre-trained DistilBERT transformer model for the sentiment analysis. The model was fine-tuned on Reddit posts and predicts 2 classes - which are NSFW and safe for work (SFW).

## Workflow

### Get Reddit data
* Data pulled in notebook `reddit_data/reddit_new.ipynb`

### Verify GPU works
* Run pytorch training test: `python utils/quickstart_pytorch.py`
* Run pytorch CUDA test: `python utils/verify_cuda_pytorch.py`
* Run tensorflow training test: `python utils/quickstart_tf2.py`
* Run nvidia monitoring test: `nvidia-smi -l 1`

### DistilBERT transformer model

### Finetune text classifier model and upload to Hugging Face 
* In terminal, run `huggingface-cli login`
* Run `python fine_tune_berft.py` to finetune the model on Reddit data 
* Run `rename_labels.py` to change the output labels of the classifier
* Check out the fine-tuned model [here](https://huggingface.co/michellejieli/inappropriate_text_classifier) 
* Check out the spaces app [Spaces APP](https://huggingface.co/spaces/yjzhu0225/reddit_text_classification_app)

### Gradio interface
* In terminal, run `python3 app.py`
* Put reddit URL in *input_url* and get output
![WechatIMG3674](https://user-images.githubusercontent.com/112578003/207481683-9a38c9e9-fd8f-48d9-be59-27f1583f96b6.jpeg)
