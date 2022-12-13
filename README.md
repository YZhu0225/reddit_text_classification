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

In this project, we created a text classifier Hugging Face Spaces app and Gradio interface that classifies not safe for work (NSFW) content, specifically text that is considered inappropriate and unprofessional. We used a pre-trained DistilBERT transformer model for the sentiment analysis. The model was fine-tuned on Reddit posts and predicts 2 classes - which are NSFW and safe for work (SFW).

### Get Reddit data
* Data pulled in notebook `reddit_data/reddit_new.ipynb`
### Verify GPU works
* Run pytorch training test: `python utils/quickstart_pytorch.py`
* Run pytorch CUDA test: `python utils/verify_cuda_pytorch.py`
* Run tensorflow training test: `python utils/quickstart_tf2.py`
* Run nvidia monitoring test: `nvidia-smi -l 1`

### Finetune text classifier model and upload to Hugging Face 
* In terminal, run `huggingface-cli login`
* Run `python fine_tune_berft.py` to finetune the model on Reddit data 
* Run `rename_labels.py` to change the output labels of the classifier
* Check out the fine-tuned model [here](https://huggingface.co/michellejieli/inappropriate_text_classifier) 
* Check out the spaces app [Spaces APP](https://huggingface.co/spaces/yjzhu0225/reddit_text_classification_app)

