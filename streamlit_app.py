
import streamlit as st

# Title of the app
st.title('Hello Streamlit!')

# Some text for the user
st.write("Welcome to your first Streamlit app!")

if st.button('Click me'):
    st.write("You clicked the button!")


import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit with Charts!")

# Generate random data
data = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])

# Display chart
st.line_chart(data)


import streamlit as st

st.title("Hello Streamlit with Input!")

# Get user input
name = st.text_input("What's your name?")

# Display a greeting
if name:
    st.write(f"Hello, {name}!")