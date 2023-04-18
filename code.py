import streamlit as st
from streamlit_lottie import st_lottie

import requests
import re

def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def validate(email, password):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.write("Invalid email")
    elif not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
        st.write("Invalid password")
    else:
        st.write("Valid email and password")

st_lottie(load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_4wgfqgfc.json"), speed=1, width=500, height=500, key="panda")

st.markdown(
    """
    <style>
        .panda {
            width: 100px;
            height: 100px;
            background-image: url(https://i.imgur.com/4LsZQzJ.png);
            position: relative;
            animation: blink 5s infinite;
        }

        @keyframes blink {
            0% {background-position: 0 0;}
            98% {background-position: 0 0;}
            99% {background-position: -100px 0;}
            100% {background-position: -100px 0;}
        }
    </style>
    <div class="panda"></div>
    """,
    unsafe_allow_html=True
)

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    validate(email, password)









