import streamlit as st
import pandas as pd


st.set_page_config(layout="wide", page_title="Server Configuration", page_icon=":satellite:")

st.sidebar.title("About")
st.sidebar.info(
    """
    GitHub repository: <https://github.com/AntoineMellerio/natixis_challenge>
    """
)

st.title('Server Configuration')

upload = st.file_uploader("Upload your Web App file here:")

if upload is not None:
    df = pd.read_csv(upload)

    server = st.selectbox('Choose a specific server to analyze:', df.name_server.unique())
    df_server = df[df['name_server'] == server]

    if df_server.is_periodic.unique()[0] == True:
        st.markdown()
    
    else:
        st.text(server, ' has not a periodic behaviour.')
