import streamlit as st
st.title("This is by python")
st.header("My name is gautam maurya")
st.header("Fill the form")
name=st.text_input("Enter your name")
fname=st.text_input("Enter your Father name")
address=st.text_area("Enter your Address")
classdata=st.selectbox("Enter your class",(1,2,3,4,5,6,7,8,9,10,11,12))

button=st.button("Done")
if button:
    st.markdown(f""""
                Name:{name}
                Father Name:{fname}
                Address:{address}
                ClassData:{classdata}    
                """)