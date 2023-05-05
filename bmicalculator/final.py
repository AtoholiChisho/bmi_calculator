import streamlit as st

# Title of the web page
st.title('BMI Calculator')

# Input fields for collecting user information
name = st.text_input('Enter your name')
gender = st.radio('Select your gender', ['Male', 'Female'])
age = st.number_input('Enter your age', min_value=1, max_value=100)
address = st.text_area('Enter your address')
hobbies = st.multiselect('Select your hobbies', ['Reading', 'Travelling', 'Music', 'Sports'])
weight = st.number_input('Enter your weight in kg', min_value=1, max_value=500)
height = st.number_input('Enter your height in cms', min_value=1, max_value=300)

# Calculation of BMI
if height > 0:
    bmi = round(weight / ((height/100) ** 2), 2)
else:
    bmi = 0

# Displaying the BMI result
if st.button('Calculate BMI'):
    if bmi == 0:
        st.write("Please enter a valid height value")
    else:
        st.write(f'Hello {name}, your BMI is {bmi}.')
