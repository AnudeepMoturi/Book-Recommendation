import streamlit as st
import pandas as pd
import pickle

st.set_page_config(layout="wide")
popular_df = pickle.load(open('popular.pkl','rb'))
st.header("BOOK STORE")
book_name = list(popular_df['Book-Title'].values)
image=list(popular_df['Image-URL-M'].values)
rating=list(popular_df['avg_rating'].values)
author=list(popular_df['Book-Author'].values)

for x in range(0,10):
        col1=st.columns(5)
        a=x*5
        j=0
        for i in range(a,a+5):
                with col1[j]:
                        st.image(image[i],width=130)
                        st.text(book_name[i])
                        st.text(f'Author- {author[i]}')
                        st.text(f'Rating - {rating[i]:.2f}')
                        j=j+1

# col2=st.columns(5)
# for i in range(5,10):
#        with col2[i]:
#               st.image(image[i],width=130)
#               st.text(book_name[i])
