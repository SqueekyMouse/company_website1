import streamlit as st
import pandas
##commit: Initial commit: built home page and data file parsing Sec22
st.set_page_config(layout='wide')
# st.title('The Best Company')
st.header('The Best Company')
st.write("""
        The multinational security corporation The Best Company was reported \
        to have obtained over thirty dummy corporations to secure million dollar \
        contracts from various governments. After the backlash from \
        The Best Company's "reckless misconduct" in Dodo, the security corporation \
        successfully obtained lucrative contracts under several subsidiaries.
        """)

st.subheader('Our Team')

col1,dummy_col1,col2,dummy_col2,col3=st.columns([1.5,.5,1.5,.5,1.5])

df=pandas.read_csv('data.csv') ## default sep is , !!!
tidx=int(len(df.index)/3)

with col1:
    for index,row in df[:tidx].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index,row in df[tidx:tidx*2].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index,row in df[tidx*2:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")
