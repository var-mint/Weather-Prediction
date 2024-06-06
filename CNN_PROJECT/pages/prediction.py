import keras
import streamlit as st
from skimage.io import imread
from skimage.transform import resize
import google.generativeai as genai



def main():
    st.set_page_config(
        page_title="Predict Weather",
        page_icon=":smiley:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.image("https://cdn.dribbble.com/users/2277649/screenshots/8498294/weather_dribbble_size.gif.gif", use_column_width=True)
    st.markdown("""
        <style>
            body {
                background-image: url("https://cdn.dribbble.com/users/2277649/screenshots/8498294/weather_dribbble_size.gif.gif");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
        </style>
    """, unsafe_allow_html=True)




    categ=['Rain','Rainbow','Lightning','Sandstorm']
    up_img=st.file_uploader("Upload an image",type=['jpg','jpeg','png'])
    if up_img:
        st.image(up_img,channels="BGR",width=400)

        st.title(":blue[PREDICT WEATHER]")
        model=keras.models.load_model("pages/cnn_project.h5")
        print("image loaded")

        st.markdown("""
                <style>
                    .stButton>button {
                        background-color: #000000;
                        color: green;
                        border-radius: 5px;
                    }
                </style>
            """, unsafe_allow_html=True)

        pred=st.button('IDENTIFY WEATHER')

        genai.configure(api_key='AIzaSyBcwxS9JsZRLVA4EnXsvLP4jmqAcq6FqnA')
        bot = genai.GenerativeModel('gemini-pro')

        if pred:
            def pred(x):
                pic = imread(x)
                print("Image loaded")
                img= resize(pic,(100, 100, 3))
                img=img.reshape(1,100,100,3)
                y_new = model.predict(img)
                ind = y_new.argmax()
                ans = categ[ind]
                return ans

            prediction=pred(up_img)
            st.write("The weather is,")
            st.title(prediction)
            if prediction=='Lightning':
                response = bot.generate_content("give me 5 safety tips to save myself from Lightning")
                st.write("Here are some safety tips to save yourself from :red[Lightning],")
                st.write(response.text)

            elif prediction=='Sandstorm':
                response = bot.generate_content("give me 5 safety tips to save myself from Sandstorm")
                st.write("Here are some safety tips to save yourself from :red[Sandstorm],")
                st.write(response.text)

            else:
                pass
main()









