import streamlit as st

st.title("Hello CampusX")
st.header("Learning Streamlit")
st.subheader("Title hai bhai ")


st.write("Hello here ")

# for simple markdown 

st.markdown("""
So the thing is you don't need anything to make it **beautiful**  

- It is already  
- Don't need HTML tags  
- Works *perfectly* fine
""")

# for code 

st.code("""

def add(a,b):
        return a+b

        """)


# For latex 
st.latex("""
x^2 + y^2 +2 = 0
         """)


# for dataframe

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aryan","Hero","Alom"],
    'marks':[23,56,89]

})

st.dataframe(df)


# Metrices

st.metric("Test","Money","4%")
st.metric("Test","Loss","- 4%")


# jason 
st.json({
    "Name": ["Aryan","Hero","Alom"],
    'marks':[23,56,89]

})



# lts create button 

email = st.text_input("ENter email")
password = st.text_input("Password bhai")

btn = st.button("Bottn hai ")

if btn:
    if( email == "gay@gmail.com") and password == "1234":
        st.balloons()
    else:
        st.error("Error hai bhai")

# sidebar 
st.sidebar.markdown("### Side bar hai")

# dropdown 

gender = st.selectbox("Gender",["Male","Female","Joy"]
             )
gender


# Upload file 

st.file_uploader("Upload file ")





