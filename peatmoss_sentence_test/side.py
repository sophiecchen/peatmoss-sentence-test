#!/usr/bin/python
# -*- coding: utf-8 -*-

import sentence_transformers

def pure_import():
    real = "all-MiniLM-L6-v2"
    model = sentence_transformers.SentenceTransformer(real)

    return 0
