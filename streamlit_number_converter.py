import streamlit as st
import base_conversion as bc

try: 

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
    
    def show_results(result, to_decimal, base, value):
        if to_decimal == True:
            st.html(f"<div style='display: flex'><h1>{value}</h1><h2>{base}</h2><h1>=</h1><h1>{result}</h1><h2>10</h2></div>")
        else:
            st.html(f"<div style='display: flex'><h1>{value}</h1><h2>10</h2><h1>=</h1><h1>{result}</h1><h2>{base}</h2></div>")



    st.set_page_config(page_title="Number Converter", page_icon=None, layout='wide', initial_sidebar_state="auto", menu_items=None)
    st.sidebar.header("Number Converter")
    form = st.sidebar.form("convert_form")
    # with st.sidebar.form("convert_form"):
    convert_to_decimal = form.radio(
        "From base to decimal?",
        options= ["Yes", "No"],
         captions=["base -> 10", "10 -> base"],
        horizontal=True,
    )

    to_decimal = True if convert_to_decimal == "Yes" else False
    print('convert_to_decimal', convert_to_decimal, "to_decimal", to_decimal)

    value = form.text_input("Enter value")
    base = form.selectbox("Select Base", (2, 8, 16)) 

    print("value", value, "base", base)
    submitted = form.form_submit_button("Convert")
    if submitted:
        result = ""
        if to_decimal == True:
            result = bc.to_decimal(base, value) 
        else:
            result = bc.to_base(base, value)
        show_results(result, to_decimal, base, value)

except Exception as e:
        st.toast(f"The error occur: {e}")