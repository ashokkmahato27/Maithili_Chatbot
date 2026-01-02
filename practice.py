import streamlit as st
import datetime 

st.title("SUN GE PAGLI")

if st.button("केना छि"):
    st.success("भगले कि नै अइय स")

today = datetime.date.today()
selected_date = st.date_input("Select a date", today)

dob = st.date_input("जन्म तिथि चुनू:")

if dob:
    today = datetime.date.today()   # ✅ FIX HERE
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Your age is: {age} वर्ष")

#_____ Sidebar

home= st.sidebar.button("Home")
about= st.sidebar.button("About")
if home:
    st.write("एहि ठाम अहाँकेँ स्वागत अछि!")
if about:
    st.write("ई एक साधारण Streamlit एप्लिकेशन अछि जे मैथिली भाषा मे इंटरैक्ट करैत अछि।")

col1, col2 = st.columns(2)
with col1:
    st.header("बायाँ कॉलम")
    st.write("ई बायाँ कॉलम अछि।")
with col2:
    st.header("दायाँ कॉलम")
    st.write("ई दायाँ कॉलम अछि।")

with st.expander("steps to use"):
    st.write("""
    1. एप्लिकेशन खोलू।
    2. अपन जन्म तिथि चुनू।
    3. अहाँक आयु देखू।
    4. साइडबार मे होम आ अबाउट बटन के उपयोग करू।
    """)

#-----markdown 
st.markdown('## मैथिली मे Streamlit एप्लिकेशन')
st.markdown('>ई एप्लिकेशन अहाँकेँ मैथिली भाषा मे इंटरैक्ट करबाक सुविधा दैत अछि।')