import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from langchain import OpenAI
from langchain.prompts import PromptTemplate

openai_api_key='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'

def generate_response(text):
    llm = OpenAI(temperature=0.2, openai_api_key=openai_api_key)
    prompt = PromptTemplate.from_template("你的目标是以佛教的角度为用户的愿望生成祝福，\
用户的愿望：{topic}。\
你需要识别用户的意愿，在众多佛祖或菩萨中找到一位合适的角色，并以他的口吻生成回答，\
你的回答要在0~50字左右，并尽可能引用佛教的经典语录，\
最好在最后备注回答来自于哪某一位佛祖或菩萨。\
比如：求财是来自于财神爷、求子来自于观音等等，需要结合愿望内容。回答：")
    return llm.predict(prompt.format(topic=text))

col1, col2 = st.columns(2)

wishes = [
    "求财",
    "求姻缘", 
    "求顺产",
    "求好运",
    "求升迁",
    "求高中",
    "求买房",
    "求智慧",
    "求平安",
    "求长寿",
    "求顺利",
    "求阖家欢乐",
    "求事业成功",
    "求子女顺遂", 
    "求老有所养",
    "求除灾祛病",
    "求心想事成",
    "求吉星高照",
    "求诸事顺利",
    "求一路顺风"
  ]

with col1:
  image = Image.open('pictures/buddha.jpg')
  st.image(image, caption='bless')

result=[]
with col2:
  with st.form('summarize_form', clear_on_submit=True):
    wish = st.selectbox('我要',wishes)
    submitted = st.form_submit_button('加持')

    if submitted:
        st.spinner('加持中...')
        st.write('为您'+str(wish))
        result=generate_response(wish)
    
    if len(result):
      st.info(result)
