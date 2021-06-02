import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime


st.title('My first app')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option


d3 = st.date_input("range, no dates", [])
st.write(d3)
