python
import streamlit as st
from fastapi import FastAPI

# Define your application using FastAPI
app = FastAPI()

# Define your Streamlit app
def run_app():
    st.set_page_config(page_title="Real-Time Social Media Monitoring", page_icon=":bar_chart:", layout="wide")
    st.title("Real-Time Social Media Monitoring")
    # Add your Streamlit components here

# Define your endpoints using FastAPI
@app.get("/")
def get_home():
    return {"message": "Welcome to the Real-Time Social Media Monitoring"}

if __name__ == "__main__":
    run_app()
