import streamlit as st
marks = st.number_input("Enter Your Marks:",  min_value=1)
total = st.number_input("Enter Your Total Marks", min_value=1)
percentage = marks / total *100
st.subheader(f':blue[Your Percentage:, :blue[{percentage}]')

if percentage >=60 and percentage < 80:
    st.success('Excellent')
elif percentage >=60 and percentage <60:
    st.info("Good")
elif percentage >=40 and percentage <60:
    st.warning("fail")

st.button("1")
