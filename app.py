import streamlit as st
from PIL import Image

image = Image.open('C:\\Users\\witness nkge\\Pictures\\icon.png')
st.image(image)

st.title('Download Pantomath')

st.header('Introduction')
st.write('''Pantomath is an android application developed by software mavens at Maven.\n\nThe fouder of the app witness nkge
, cant really ellaborate on the idea behind the app or what the app is all about but what he can conclude is that Pantomath
does things for English studends.\nPantomath contain cognitive functions that can absolutely write essays
, answer comprehension questions, summarize text for you and also it provides english lanuage tolbox for learning.''')

st.header('App snippets')
image1 = Image.open(image_main)
image2 = Image.open(Image_answer)
image3 = Image.open(summary)
image4 = Image.open(language)

st.image(image1)
st.image(image2)
st.image(image3)
st.image(image4)

st.info('to learn more on how you can use pantomath for your English studies visit our facebook page @WMaven')


st.download_button( 

    label="Download Pantomath",

    data='app-release.apk',

    file_name='Pantomath.apk',

    mime='application/vnd.android.package-archive',

)
