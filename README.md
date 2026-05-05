# Number converter

## Final Project for CSC.221.40C Introduction to Problem Solving and Programming course.

This application allows to convert numbers from decimal number system (base 10) to binary (base2), octal (base 8), and hexadecimal (base 16) numbers, and vice versa. 

The functions to convert to decimal and to bases 2, 8, and 16 are in base_conversion.py file.

The goal was to implement this conversion using custom function with additional error handling.


__Project structure__

- base_conversion.py holds functions to convert data
- graphic.py contain code for tkinter graphic user interface. 
- streamlit_number_converter.py contain code for streamlit.
- _Streamlit app deployed here:_ https://annapestova-number-converter.streamlit.app

To run locally:
- clone repository

For graphic.py file: 
- requires Python and Tkinter to be installed on your system.
- run graphic.py file

For streamlit_number_converter.py file: 
- requires Python and Streamlit to be installed on your system.
- command to run streamlit application locally: `streamlit run streamlit_number_converter.py`

**Tkinter GUI screenshots:**

_- main page_
![default view Tkinter GUI](image.png)
_- conversion result_
![conversion result Tkinter GUI](image-1.png)
_- error message_
![error Tkinter GUI](image-2.png)

**Streamlit screenshots:**

_- main page_
![default view Streamlit](image-3.png)
_- conversion result_
![conversion Streamlit](image-4.png)
_- error message_
![error Streamlit](image-5.png)


