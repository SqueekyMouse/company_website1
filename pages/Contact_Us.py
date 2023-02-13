import streamlit as st
from send_email import send_email
import pandas
##commit: contact us page and email module Sec23

df=pandas.read_csv('topics.csv')
st.header('Contact Us')

with st.form(key='email_form'):
    user_email=st.text_input('Your email address')
    # query_type=st.selectbox('What topic do you want to discuss?',
    #                     ('Job Inquiries','Project Proposals','Other'))
    query_type=st.selectbox('What topic do you want to discuss?',df['topic'])
    raw_message=st.text_area('Text')
    message=f"""\
Subject: New Inquiry

Type: {query_type}
Email: {user_email}
{raw_message}"""

    submit=st.form_submit_button('Submit')
    if submit:
        # print(message)
        send_email(message)
        st.info('Mail sent!')
    
