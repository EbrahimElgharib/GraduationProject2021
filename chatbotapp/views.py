from django.shortcuts import render
from rest_framework.response import Response
from django.conf import settings
# from rest_framework import status, viewsets
# from rest_framework.decorators import action, api_view
import spacy
nlp = spacy.load("en_core_web_sm")
import tensorflow as tf
import tflearn
import numpy
import random
import json
import pickle
from time import sleep
with open("spacial files/data.json") as dataFile:
    dataSet=json.load(dataFile)
try:
    with open("dataSet.pickle", "rb") as file:
        tok_patterns, tags, input, output=pickle.load(file)
except:

    # list for store patterns
    patterns=[]
    # list for store tokenized patterns
    tok_patterns=[]
    # list to store tags
    tags=[]
    # list to store indexes for tags and patterns
    indexes=[]
    for intent in dataSet["intents"]:
        for pattern in intent["patterns"]:
            # making tokenization for pattern(returning alist of tokens)
            word=nlp(pattern)
            # storing patterns
            patterns.append(word)
            # storing tokenized patterns
            tok_patterns.extend(word)
            # appending tag for this pattern in tags list
            # storing the tag for this pattern
            indexes.append(intent["tag"])
        if(intent["tag"] not in tags):
            tags.append(intent["tag"])
    # making lemmatization for tokenized patterns
    tok_patterns=[w.lemma_ for w in tok_patterns if not (w.pos_=='PUNCT' or w.pos_=='AUX' or w.pos_=='ADV' or w.pos_=='ADP' or w.pos_=='DET' or w.pos_=='PRON'or w.pos_=='SCONJ' or w.pos_=='SYM' or w.pos_=='SPACE')]
    # removing repetition in tok_patterns and sorted the list
    tok_patterns=list(set(tok_patterns))
    # sorting tags list
    tags=sorted(tags)
    # shaping data
    # create input 2 lists for input and output
    input=[]
    output=[]
    empty_list=list(0 for _ in range(len(tags)))
    for i, patt in enumerate(patterns):
        patt_tokens=[]
        wrds=[w.lemma_ for w in patt if not (w.pos_=='PUNCT' or w.pos_=='AUX' or w.pos_=='ADV' or w.pos_=='ADP' or w.pos_=='DET' or w.pos_=='PRON' or w.pos_=='SCONJ' or w.pos_=='SYM' or w.pos_=='SPACE')]
        for wd in tok_patterns:
            if wd in wrds:
                patt_tokens.append(1)
            else:
                patt_tokens.append(0)
        input.append(patt_tokens)
        zero_list=empty_list[:]
        zero_list[tags.index(indexes[i])]=1
        output.append(zero_list)
    input=numpy.array(input)
    output=numpy.array(output)
    with open ("dataSet.pickle", "wb") as file:
        pickle.dump((tok_patterns, tags, input, output ), file)

# cleaning cashe
# tf.compat.v1.reset_default_graph()
# create neural network
net= tflearn.input_data(shape=[None, len(input[0])])
net=tflearn.fully_connected(net,16)
net=tflearn.fully_connected(net,16)
net=tflearn.fully_connected(net,16)
net=tflearn.fully_connected(net, len(output[0]), activation="softmax")
net=tflearn.regression(net)
model=tflearn.DNN(net)
try:
    model.load("model.tflearn")
except:
    model.fit(input,output, n_epoch=1000, batch_size=4, show_metric=True)
    model.save("model.tflearn")



# compare user message with tok_patterns
def user_message(input_msg, tok_wrds):
    zeros_patt=[0 for _ in range(len(tok_wrds))]
    tok_msg=nlp(input_msg)
    tok_msg=[word.lemma_ for word in tok_msg if not (word.pos_=='PUNCT' or word.pos_=='AUX' or word.pos_=='ADV' or word.pos_=='ADP' or word.pos_=='DET' or word.pos_=='PRON' or word.pos_=='SCONJ' or word.pos_=='SYM' or word.pos_=='SPACE')]
    print("###################")
    print(tok_msg)
    for s in tok_msg:
        for i,w in enumerate(tok_wrds):
            if(w==s):
                zeros_patt[i]=1
    return numpy.array(zeros_patt)

def chatBot(message):
    res=model.predict([user_message(message, tok_patterns)])[0]
    res_index=numpy.argmax(res)
    print(res_index)
    print(tags[res_index])
    res_tag=tags[res_index]
    if(res[res_index]>0.8):
        for intent in dataSet["intents"]:
            if intent["tag"]==res_tag:
                Responses=intent["responses"]
        sleep(2)
        bot=random.choice(Responses)
        return(bot)
    else:
        return("Sorry, I can not understand your question!")
    

# @api_view(['GET'])
def chatbot(request):
    res=str(chatBot(request.data["msg"]))
    return Response(res)