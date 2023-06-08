import streamlit as st
from streamlit_ace import st_ace
from tinydb import TinyDB, Query
from bs4 import BeautifulSoup


db = TinyDB('db.json')
table = db.table('templates')


st.title('Jinjify')
st.subheader("Convert Your HTML `CODE` to JINJA")


st.write("Enter Your header HTML `code` here")  
header_input = st_ace(
    placeholder="Header code here...",
    language="html",
    theme="monokai",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=False,
    show_print_margin=True,
    wrap=True,
    key="header",
    auto_update=True,
    readonly=False,
)


st.write("Enter Your footer HTML `code` here")
footer_input = st_ace(
    placeholder="Footer code here...",
    language="html",
    theme="monokai",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=False,
    show_print_margin=True,
    wrap=True,
    key="footer",
    auto_update=True,
    readonly=False,)

col1, col2 = st.columns(2)

with col1:

    # Store header and footer in database
    if st.button("Save Template"):
        db.insert({"header": header_input, "footer": footer_input})
        bt.success('Template saved')
with col2:
    if st.button('Clear Data'):
        db.truncate()
        st.success('Data cleared')

st.write('___')

# Display saved templates
templates = db.all()
if templates:
    selected_template = st.selectbox("Select a template", [str(template.doc_id) for template in templates])
    header_input = templates[int(selected_template)-1]["header"]
    footer_input = templates[int(selected_template)-1]["footer"]




text_input = st_ace(
        placeholder="Enter code here...",
        language="html",
        theme="monokai",
        keybinding="vscode",
        font_size=14,
        tab_size=4,
        show_gutter=False,
        show_print_margin=True,
        wrap=True,
        key="input",
        auto_update=True,
        readonly=False)


# Display result
if st.button("Generate"):
    st.write(f""" ```
                    {header_input}
                    {text_input}
                    {footer_input}

                        ```

            """)

  