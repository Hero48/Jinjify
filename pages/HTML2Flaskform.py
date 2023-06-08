import re
import streamlit as st
from streamlit_ace import st_ace

def generate_flaskform_from_html(html_code):
    # Extract form information using regex
    form_regex = r'<form\s+.*?action=[\'"](.*?)[\'"].*?>.*?</form>'
    form_match = re.search(form_regex, html_code, re.DOTALL)
    form_action = form_match.group(1) if form_match else ''
    
    # Extract input field, text area, and select field information using regex
    field_regex = r'<(input|textarea|select)\s+.*?name=[\'"](.*?)[\'"].*?>'
    field_matches = re.findall(field_regex, html_code, re.DOTALL)
    field_data = [(name, tag) for tag, name in field_matches]
    
    # Generate Flask WTF FlaskForm string
    field_strings = [f'    {name} = StringField("{name}")\n\t' if tag == 'input'
                     else f'    {name} = TextAreaField("{name}")\n\t' if tag == 'textarea'
                     else f'    {name} = SelectField("{name}", choices=[("", ""), ("", "")])\n\t' for name, tag in field_data]
    field_string = ''.join(field_strings)
    flaskform_string = f"""
    \tclass MyForm(FlaskForm):
    \t{field_string}    submit = SubmitField('Submit')
    """
    
    return flaskform_string


# html_code = '''
# <!DOCTYPE html> <html> <head> <title>Alternate Form</title> </head> <body> <form method="POST">
# <label>First Name: <input type="text" name="firstName"></label>
# <br>
# <label>Last Name: <input type="text" name="lastName"></label>
# <br>
# <label>Email Address: <input type="email" name="emailAddress"></label>
# <br>
# <label>Age: <input type="number" name="agePreferences"></label>
# <br>
# <label>Comments: <textarea name="commentsSection"></textarea></label>
# <br>
# <label>Gender:
# <select name="genderOptions">

# <option value="male">Male</option> <option value="female">Female</option> <option value="other">Other</option> </select> </label> <br>
# <button type="submit">Submit Form</button>

# </form> </body> </html>
# '''
st.header("Welcome To Form2Flask")

ace_height = 400
ace_width = 600



html_code = st_ace(
    placeholder="Enter code here...",
    language="html",
    theme="atom",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=False,
    show_print_margin=True,
    wrap=True,
    auto_update=True,
    readonly=False,
   
)

flaskform_string = generate_flaskform_from_html(html_code)
# st.subheader('HTML to JINJA `code`')
st.write(f"""```{flaskform_string}```""", width=ace_width, height=900)

