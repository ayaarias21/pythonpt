import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd
import altair as alt
#from streamlit_option_menu import option_menu
import pandas as pd  # read csv, df manipulation
st.set_page_config(page_title="Bytes and Bombs", page_icon="🚨", layout="centered")
#pip install streamlit to instsall streamlit.io
def introduction_page():
    st.markdown("<h2 style='color: #990000;'>Bytes and Bombs: The Internet and Cyber-Terrorism</h2>",
                unsafe_allow_html=True)
    st.sidebar.success("")

    image_url = "https://media.giphy.com/media/oYQ9HRm5Mo7VXeMNVR/giphy.gif"
    st.image(image_url, caption='Image from > https://giphy.com/gifs/glitch-error-basic-oYQ9HRm5Mo7VXeMNVR',
             use_column_width=True)

    st.markdown("<h2 style='color: #990000;'>Introduction</h2>", unsafe_allow_html=True)


    st.write(
        "Although terrorism can have various definitions, it is consistently associated with a negative connotation. "
        "The Nacos Definition states: 'Terrorism is political violence or the threat of violence by groups or "
        "individuals who deliberately target noncombatants to influence the behavior and actions of targeted publics "
        "and governments.' ")
    st.write(
        "I urge everyone to critically examine this definition and identify its shortcomings. However, "
        "it is important to note that it is genuinely impossible to formulate or enforce international law without a "
        "standardized definition. In many cases, the lack of a uniform definition leads to loopholes due to the "
        "differing interpretations of each country.")
    st.write(
        'According to Brian Michael Jenkins, in his work "The Study of Terrorism: Definitional Problems," the term '
        '"terrorism" is described as "a fad word used promiscuously and often applied to a variety of acts of '
        'violence which are not strictly limited.... terrorism is what the bad guys do" (Jenkins), does an excellent '
        'job of highlighting the issue of definitional challenges and the varying definitions that can come with an '
        'unspecified and non-meticulous reality of the term.')
    st.write(
        'An example of the failure of getting the definition “right” would be the US State Department characterizes '
        'it as "politically motivated violence perpetrated against noncombatant targets by subnational groups or '
        'clandestine agents, usually intended to influence an audience." While this definition serves as an attempt '
        'to capture what they believe to be terrorism, it is full of contradictions and complexities.')
    st.write(
        'One inherent challenge lies in the subjectivity of the term "politically motivated violence." What '
        'constitutes political motivation can vary widely, subject to individual or group perspectives. Additionally, '
        'the specification of "noncombatant targets" adds another layer of complexity. The distinction between '
        'combatants and noncombatants is not always clear, particularly in modern conflicts where the lines between '
        'these categories can blur. This ambiguity may lead to contradictions in the application of the definition. ')
    st.write(
        'While this describes terrorism on a broader range, like these many different definitions, cyber-terrorism '
        'too has not universally accepted definition. According to the text entitled “Understanding Cyber Terrorism '
        'from Motivational Perspectives”, by Yunos, Z, and S Sulaman, for an attack to be labeled as cyber terrorism, '
        'it must have a motivational component, result in death and/or large-scale destruction, and be politically '
        'motivated. The aim is to cause grave harm, severe economic damage, or extreme financial harm. Including this '
        'it is stated that there are three key elements must be satisfied to constitute cyber terrorism, '
        'including politically motivated cyber-attacks leading to death or bodily injury, cyber attacks causing fear '
        'and physical harm, and serious attacks targeting critical information infrastructures such as financial, '
        'energy, transportation, and government operations. ')

def loading_animation():
    st.title("Bytes and Bombs")
    st.write("This project delves into the challenges of defining terrorism and the evolution of cyber-threats, "
             "highlighting the complex nature of radicalization and counter terrorism efforts. "
             )
    user_name = "Ayanna Bailey- Arias"
    st.write(f"{user_name}")

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text(f"Loading... {i + 1}%")
        time.sleep(0.1)

    progress_bar.empty()
    status_text.empty()

    # Clear the entire page after animation
    st.empty()

    # Display the introduction page
    introduction_page()

def main():
    loading_animation()

if __name__ == "__main__":
    main()

