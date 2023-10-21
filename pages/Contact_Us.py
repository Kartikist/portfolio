import streamlit as st
from contact_email import send_email 

st.header("Contact Me")

with st.form(key='email_forms'):
    user_email = st.text_input("Your e-mail",placeholder="Enter you email")
    option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)
    message = st.text_area("Your Message",placeholder="Write us your message")
    button = st.form_submit_button("Submit")
    if button:
        message = "Subject: Protfolio App" + '\n'+ message + '\n' + user_email
        send_email(message)
        st.info("Your email was sent succesfully.")
        