#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
#from sentence_transformers import SentenceTransformer
import sentence_transformers

def regex(text):
    regex = "[a-zA-Z]+at"
    match = re.match(regex, text)
    
    if match:
        return True
    else:
        return False

def sentence():
    real = "all-MiniLM-L6-v2"
    model = sentence_transformers.SentenceTransformer(real)

    return 0
