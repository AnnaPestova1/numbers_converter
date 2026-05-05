'''
This code uses Streamlit library and allows to interact with user. Information about deployment is in the Readme.md
'''

import streamlit as st
import base_conversion as bc

try: 
# style for headers
    st.markdown(
        """
    <style>
        h1{
            font-size: 4em;
            padding-left: 0.1em;
            padding-right: 0.1em;
        }
        h2{
            font-size: 2em;
            padding-left: 0.1em;
            padding-right: 0.1em;
            align-content: end;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    
    # display result depends on the type of conversion - allow to display input and output numbers and bases.
    def show_results(result, to_decimal, base, value):
        if to_decimal == True:
            st.html(f"<div style='display: flex'><h1>{value}</h1><h2>{base}</h2><h1>=</h1><h1>{result}</h1><h2>10</h2></div>")
        else:
            st.html(f"<div style='display: flex'><h1>{value}</h1><h2>10</h2><h1>=</h1><h1>{result}</h1><h2>{base}</h2></div>")

    st.set_page_config(page_title="Number Converter", page_icon=None, layout='wide', initial_sidebar_state="auto", menu_items=None)

    # Sidebar menu
    st.sidebar.header("Number Converter")
    form = st.sidebar.form("convert_form")
    convert_to_decimal = form.radio(
        "From base to decimal?",
        options= ["Yes", "No"],
         captions=["base -> 10", "10 -> base"],
        horizontal=True,
    )

    # to_decimal is a boolean based on the user response
    to_decimal = True if convert_to_decimal == "Yes" else False

    # user choose number and base
    value = form.text_input("Enter value")
    base = form.selectbox("Select Base", (2, 8, 16)) 

    # variable hold state about form submission
    submitted = form.form_submit_button("Convert")

    # show hint if form not submitted
    hint = "Pick conversion on the left" if not submitted else ""
    st.text(hint)

    result = ""

    # when form submitted methods to_decimal or to_base call depends on the to_decimal boolean
    if submitted:
        if to_decimal == True:
            result = bc.to_decimal(base, value) 
        else:
            result = bc.to_base(base, value)

        # after calculations result is shown on the main part
        show_results(result, to_decimal, base, value)
    
    # allow reset side form
    def reset_form():
        global submitted
        submitted = False
         
    # show reset button if form submitted  
    if submitted:
        st.button('Clear result', on_click=reset_form)


except Exception as e:
    st.toast(f"The error occur: {e}", duration=10)
