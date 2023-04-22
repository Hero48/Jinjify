from bs4 import BeautifulSoup
import streamlit as st
from streamlit_ace import st_ace
import random
import streamlit.components.v1 as components


st.title('Jinjify')



def html_to_flaskform(html_input):
    soup = BeautifulSoup(html_input, 'html.parser')

    # Modify the form tag to include the "method" attribute
    form_tag = soup.find('form')
    if form_tag is not None:
        form_tag['method'] = 'POST'
        form_tag.append('{{ form.csrf_token }}')  # Add the hidden_tag() after modifying the form tag

    # Modify each input tag to use FlaskForm syntax
    for input_tag in soup.find_all('input'):
        if 'name' in input_tag.attrs and input_tag['name'] != '':
            input_tag['required'] = True
            input_tag['id'] = input_tag['name']
            input_tag.replace_with('{{ form.' + input_tag['name'] + '(required=True, id="' + input_tag['name'] + '") }}')

    for textarea_tag in soup.find_all('textarea'):
        if 'name' in textarea_tag.attrs and textarea_tag['name'] != '':
            textarea_tag['required'] = True
            textarea_tag['id'] = textarea_tag['name']
            textarea_tag.replace_with('{{ form.' + textarea_tag['name'] + '(required=True, id="' + textarea_tag['name'] + '") }}')

    # Output the modified HTML as a Jinja template
    return soup.prettify()



slogans = [    "Transform your HTML to FlaskForm Jinja templates in minutes with Jinjify!",    "Say goodbye to tedious HTML-to-Jinja conversions with Jinjify.",    "Effortlessly create FlaskForm Jinja templates from your HTML code with Jinjify.",    "Jinjify: the ultimate tool for converting HTML to FlaskForm Jinja templates.",    "Streamline your FlaskForm development process with Jinjify.",    "Jinjify: HTML-to-Jinja conversions made easy.",    "FlaskForm Jinja templates made simple with Jinjify.",    "Jinjify: the hassle-free way to convert HTML to FlaskForm Jinja templates.",    "Revolutionize your FlaskForm workflow with Jinjify.",    "Jinjify: the fastest and easiest way to generate FlaskForm Jinja templates.",    "Transform your HTML to FlaskForm Jinja templates with Jinjify's easy-to-use interface.",    "Generate FlaskForm Jinja templates from your HTML code effortlessly with Jinjify.",    "Jinjify: the time-saving solution for HTML-to-Jinja conversions.",    "FlaskForm Jinja templates made easy: discover Jinjify.",    "Say goodbye to complex FlaskForm Jinja templates with Jinjify's streamlined conversion process.",    "Jinjify: the tool that simplifies FlaskForm Jinja template creation.",    "Simplify your FlaskForm development process with Jinjify's HTML-to-Jinja conversion capabilities.",    "Transform your HTML code into elegant FlaskForm Jinja templates with Jinjify's intuitive platform.",    "Jinjify: the tool that takes the headache out of FlaskForm Jinja template creation.",    "Efficiently create FlaskForm Jinja templates from your HTML code with Jinjify's powerful features."]



st.header("Welcome to JINJIFY")
st.write(f"{random.choice(slogans)}")

# html_input = st.text_area("Enter Your HTML `code` here", height=200)
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
    st.subheader('HTML to JINJA `code`')
    st.write(f"""```{html_to_flaskform(code)}```""")
    st.subheader('Preview')
    components.html(code, width=800, height=600)
