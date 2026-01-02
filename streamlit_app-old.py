import streamlit as st
from auth import is_email_authorized

st.set_page_config(page_title="Login", page_icon="🔐")

# ------------------------------------------------
# Session state init
# ------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None


# ------------------------------------------------
# Redirect if already logged in
# ------------------------------------------------
if st.session_state.logged_in:
    st.switch_page("pages/home.py")


# ------------------------------------------------
# Login UI
# ------------------------------------------------
st.title("🔐 Login")

email = st.text_input("Email address")

if st.button("Login"):
    if not email:
        st.warning("Please enter an email address.")
    elif is_email_authorized(email):
        st.session_state.logged_in = True
        st.session_state.user_email = email.lower()
        st.switch_page("pages/home.py")
    else:
        st.error("Email not authorized.")
