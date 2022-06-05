import streamlit as st
from streamlit_lottie import st_lottie

import requests
import json

# functions resposible for the animation
# If we are using it localy
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# if we are using it from url
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="LiDAR", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
#https://docs.streamlit.io/library/api-reference/text
# different forms of text are from that link

add_selectbox = st.sidebar.selectbox(
    "Calculations",
    ("Home", "Laser distance to target", "Time to target", "Frequency", "Wavelength")
)

speed_light = 3*(10**8)

if add_selectbox == "Laser distance to target":
    st.title("Laser distance to target")
    st.subheader(
        "The laser beam travels the distance - D, for the specified time - t. The distance to the target is considered, taking into account the reflection of the beam.")
    st.latex(r'''
         D = tc
         ''')
    travel_time_to_the_target = st.number_input('needed beam travel time to the target (μs)')
    result = (speed_light * travel_time_to_the_target)/1000000
    result_format=int(result)
    if result_format > 0 :
        st.write(f" D = {result_format} m")
elif add_selectbox == "Time to target":
    st.title("Time to target")
    st.subheader(
        "The laser beam travels the distance - D, for the specified time - t. The time to the target is considered, taking into account the reflection of the beam.")
    st.latex(r'''
             t = D/c
             ''')
    distance_to_target = st.number_input('Distance to the target (m)')
    result = (distance_to_target / speed_light) * 1000000
    result_format=int(result)
    if result_format > 0:
        st.write(f" t = {result_format} μs")

elif add_selectbox == "Frequency":
    st.title("Frequency")
    st.subheader(
        "...it is useful to know some simple calculations about frequency.")
    st.latex(r'''
                 f = c/λ
                 ''')
    wavelength = st.number_input('Wavelength - λ (mm)')
    result_format = 0
    try:
        result = ((speed_light / 1000000) /wavelength)
        result_format = int(result)
    except ZeroDivisionError:
        result = 0

    if result_format > 0:
        st.write(f"f = {result_format} GHz")


elif add_selectbox == "Wavelength":
    st.title("Wavelength")
    st.subheader(
        "...it is useful to know some simple calculations about the wavelength.")
    st.latex(r'''
                     λ = c/f
                     ''')
    frequency = st.number_input('Frequency (GHz)')
    result_format = 0
    try:
        result = ((speed_light / 1000000) / frequency)
        result_format = int(result)
    except ZeroDivisionError:
        result = 0

    if result_format > 0:
        st.write(f" λ = {result_format} mm")

else:
    st.title("What is LiDAR in simple words?")
    st.subheader(
        "Lidar, which stands for Light Detection and Ranging, is a remote sensing method that uses light in the form of a pulsed laser to measure ranges (variable distances) to the Earth.")

    # animation = load_lottie_url('https://assets10.lottiefiles.com/packages/lf20_oURJje.json')
    animation2 = load_lottie("lf30_editor_7edcypmc.json")
    st_lottie(animation2, height=200, key='2')



