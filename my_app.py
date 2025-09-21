import streamlit as st
import pandas as pd
import os
import base64 
import numpy as np
import altair as alt

st.write("Hi my cute and kind pookie🥹")
st.image(os.path.join(os.getcwd(),"stickers", "pig.webp"),width=200)
st.divider()
st.write('here are 2 buttons that do not work🥳')
pressed_yes=st.button('Yes')
print(pressed_yes)
pressed_no=st.button('No')
print(pressed_no)
