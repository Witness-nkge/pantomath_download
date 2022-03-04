import streamlit as st
from PIL import Image

st.image(Image.open('icon.png'))

st.title('Pantomath')

st.write('''Pantomath is an android application developed by software mavens
 which can be used by students to get help in aswering comprehesion
 questions etc
 
 The app uses cognitive function that can answer questions for you based
 on the context you provided. The context can be from a book, comprehension or anything''')

st.header("Usage")
st.write('''CONTEXT

It can be uploaded as an image document , e.g a picture containing a context from
the comprehesion you want to ask questions based on.

Or you can type it manually on the  'input context'  field

After you can type in a question then hit answer button to get answers''')

st.header('App snippet')
st.image(Image.open('image.png'))
st.info('''to learn more about Pantomath visit our facebook page @WMaven

click the below button to download pantomath''')
st.download_button( 

    label="Download Pantomath",

    data= 'app-release.apk',

    file_name='Pantomath.apk',

    mime='application/vnd.android.package-archive',

)
