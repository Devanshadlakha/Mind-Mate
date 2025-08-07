# utils/db.py

from pymongo import MongoClient
import streamlit as st

# Use Streamlit's secrets system
@st.cache_resource
def init_connection():
    return MongoClient(st.secrets["MONGO_URI"])

client = init_connection()
db = client["emotion_app"]
