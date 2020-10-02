import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import tensorflow as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt
import random
import json

with op("Chatbot.json") as file:
    data = json.load(file)

print(data["Chatbot"])