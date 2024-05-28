import streamlit as st
import pickle
from PIL import Image
def main():
    st.title(":green[Placement Prediction]")
    image=Image.open('placemnt.jpg')
    st.image(image,width=1000)

    Age=st.text_input("Enter the age")

    gender = st.radio("Gender", ('Male','Female'))
    if gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    batch = st.selectbox("Select Stream", ('------SELECT--------','Electronics And Communication','Computer Science',
       'Information Technology','Mechanical','Electrical','Civil'))
    if batch == 'Electronics And Communication':
        Stream = 0
    elif batch == 'Computer Science':
        Stream = 1
    elif batch == 'Information Technology':
        Stream = 2
    elif batch == 'Mechanical':
        Stream = 3
    elif batch == 'Electrical':
        Stream = 4
    else:
        Stream = 5

    internship=st.radio("Number of Internships", ('No internships','One','Two','3 & more'))
    if internship == 'No internships':
        Internships = 0
    elif internship =='One':
        Internships = 1
    elif internship =='Two':
        Internships = 2
    else:
        Internships = 3

    CGPA=st.text_input("Enter the CGPA")

    stay = st.radio("Are you stayed at Hostel", ('Yes', 'No'))
    if stay == 'Yes':
        Hostel = 1
    else:
        Hostel = 0

    supply= st.radio("History of Backlogs", ('Yes', 'No'))
    if supply=='Yes':
        HistoryOfBacklogs = 1
    else:
        HistoryOfBacklogs = 0

    features=[Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs]
    model=pickle.load(open('placement.sav','rb'))
    pred=st.button('Predict')
    if pred:
        feature=[int(x) for x in features]
        prediction=model.predict([feature])
        if prediction==1:
            image1 = Image.open('Placed.jpg')
            st.image(image1, width=400)
            st.write("# Placed")
        else:
            image2=Image.open('Not_placed.gif')
            st.image(image2,width=400)
            st.write("# Not placed")
main()

