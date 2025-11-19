import streamlit as st
import pickle as pkl
import pandas as pd

#load the model
with open(r"hearing_test_model.pkl", "rb") as file:
    model = pkl.load(file)
#set the title
#st.title("Hearing Test Classification")

#set the header
st.header("Hearing Test Data Classification using Machine Learning")

#set the subheader
#st.subheader("Predict if a patient will suffer with hearing disability by using age and a physical score")
st.text("Predict if a patient will suffer with hearing disability by using age and a physical score")

#get the input data from the user
age = st.text_input("Age of the Patient")
physical_score = st.text_input(("Physical Score of the Patient"))

#add a button to predict the output 
button =st.button("Predict ")

#check if the button is pressed
if button:
    print(f"Age:{age}, type={type(age)}")
    print(f"Physical Score:{physical_score}, type={type(physical_score)}")  
    
    #predict the result using model
    result = model.predict([[int(age),float(physical_score)]])
    #print(result)
    #print(f"Result: {result}, type={type(result)}")
    
    #print success or error
    if result[0] == 1:
        st.success("The result is positive ")
    elif result[0] == 0:
        st.error("The result is negative ")
    