import streamlit as st
import pickle
import numpy as np
st.header('Search Engine')
book_names = pickle.load(open('book_names.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
final_rating = pickle.load(open('final_rating.pkl','rb'))
book_names=book_names.insert(0,'')

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=1 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url 


selected_books = st.selectbox(
    "Search for your Book",
    book_names 
)
if st.button('Search'):
    if selected_books in book_names:
        recommended_books,poster_url=recommend_book(selected_books)
        st.image(poster_url[0])
        st.text(recommended_books[0])