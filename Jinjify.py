import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Jinjify Landing Page", page_icon=":memo:")

# Add a header
st.title("Welcome to Jinjify")

# Add a brief description of the program
st.write("Jinjify is a software for Python Flask and Django developers. It converts your HTML code to Jinja templates, making it easier for you to work with these frameworks. With Jinjify, you can convert normal HTML forms to FlaskForm Jinja templates, generate form classes for HTML forms, and edit your HTML file to be a Jinja template.")

# Add a section for features
st.header("Features")

# Add a bullet point list of features
st.write("""
- Convert normal HTML forms to FlaskForm Jinja templates
- Generate form classes for HTML forms
- Edit your HTML file to be a Jinja template
""")

# Add a call-to-action button
st.button("Get Started")

# Add a footer with your contact information
st.write("---")
st.markdown("Contact us on [Telegram](https://t.me/spykvng) for support and inquiries.")
