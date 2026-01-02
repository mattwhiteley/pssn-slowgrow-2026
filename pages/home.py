import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

# ------------------------------------------------
# Guard: redirect if not logged in
# ------------------------------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")


# ------------------------------------------------
# Home page UI
# ------------------------------------------------
st.title("🏠 Home")

st.subheader(f"Hello {st.session_state.user_email} 👋")

st.divider()

st.write("You are successfully logged in.")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.switch_page("streamlit_app.py")
