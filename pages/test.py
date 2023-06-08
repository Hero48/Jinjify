import streamlit as st
from tinydb import TinyDB, Query

# Initialize database
db = TinyDB('db.json')

# Define database query
template_query = Query()

# Define input fields
header_input = st.text_area("Header")
footer_input = st.text_area("Footer")
text_input = st.text_area("Text")

# Store header and footer in database
if st.button("Save Template"):
    db.insert({"header": header_input, "footer": footer_input})

# Display saved templates
templates = db.all()
if templates:
    selected_template = st.selectbox("Select a template", [str(template.doc_id) for template in templates])
    header_input = templates[int(selected_template)-1]["header"]
    footer_input = templates[int(selected_template)-1]["footer"]

# Display result
if st.button("Generate"):
    st.write(header_input)
    st.write(text_input)
    st.write(footer_input)
