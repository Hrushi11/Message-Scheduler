import streamlit as st
from run import send_mssg_personal, squeeze


st.title("Scheduled Messenger")

ph_num = ("+91" + str(st.number_input("Input your phone number", format="%i", min_value=0, max_value=9999999999))).split(".")[0]
mssg = st.text_area("Type your message here")
hr = st.number_input("Enter hour in 24hrs format", format="%i", min_value=0)
min_ = st.number_input("Enter minutes", format="%i", min_value=0)
if st.button("Send", help="Click this to send your message"):
    st.info("Your request is being processed...")
    send_mssg_personal(ph_num, squeeze(mssg), hr, min_)
    st.success("Your Message has been sent")
    st.balloons()