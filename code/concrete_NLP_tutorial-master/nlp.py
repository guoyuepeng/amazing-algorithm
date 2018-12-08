#! /usr/bin/python3
# coding=utf-8

import keras
import nltk
import pandas as pd
import numpy as np
import re
import codecs
from nltk.tokenize import RegexpTokenizer

### 将notebook转换成python代码 ###


def sanitize_characters(raw, clean):
    for line in input_file:
        out = line
        output_file.write(line)

# 清洗数据
def standardize_text(df, text_field):
    df[text_field] = df[text_field].str.replace(r"http\S+", "")
    df[text_field] = df[text_field].str.replace(r"http", "")
    df[text_field] = df[text_field].str.replace(r"@\S+", "")
    df[text_field] = df[text_field].str.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
    df[text_field] = df[text_field].str.replace(r"@", "at")
    df[text_field] = df[text_field].str.lower()
    return df

if __name__ == '__main__':
    # codecs.open一般不会出现编码问题，优于open
    input_file = codecs.open("socialmedia_relevant_cols.csv", "r",encoding='utf-8', errors='replace')
    output_file = open("socialmedia_relevant_cols_clean.csv", "w")
    sanitize_characters(input_file, output_file)

    questions = pd.read_csv("socialmedia_relevant_cols_clean.csv")
    questions = standardize_text(questions, "text")
    questions.to_csv("clean_data.csv")

    clean_questions = pd.read_csv("clean_data.csv")

    # 分词
    tokenizer = RegexpTokenizer(r'\w+')

    clean_questions["tokens"] = clean_questions["text"].apply(tokenizer.tokenize)