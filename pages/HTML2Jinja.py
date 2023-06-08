from bs4 import BeautifulSoup
import streamlit as st 
from streamlit_ace import st_ace



def convert_html_to_template(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')

    for tag in soup.find_all('img'):
        if 'src' in tag.attrs:
            tag.attrs['src'] = "{{ url_for('static', filename='" + tag.attrs['src'] + "') }}"

    for tag in soup.find_all('link'):
        if 'href' in tag.attrs and tag.attrs['href'].endswith('.css'):
            href = tag.attrs['href']
            # if not urllib.parse.urlparse(href).netloc:
            tag.attrs['href'] = "{{ url_for('static', filename='" + href + "') }}"

    for tag in soup.find_all('script'):
        if 'src' in tag.attrs:
            tag.attrs['src'] = "{{ url_for('static', filename='" + tag.attrs['src'] + "') }}"

    return str(soup)


st.header('`HTML` to `Jinja` Template')
st.subheader('HTML CODE')
code = st_ace(
    placeholder="Enter code here...",
    language="html",
    theme="dawn",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=False,
    show_print_margin=True,
    wrap=True,
    auto_update=True,
    readonly=False,
)

if code:
    st.write('___')
    st.subheader('Jinja CODE')
    st.write(f"""
            ``` {convert_html_to_template(code)} ```

        """)