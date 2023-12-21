# Import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
#from streamlit_option_menu import option_menu
import pandas as pd  # read csv, df manipulation
st.set_page_config(page_title="Bytes and Bombs", page_icon="🚨", layout="centered")
st.markdown("<h2 style='color: #990000;'>The Internet and Cyber-Terrorism</h2>", unsafe_allow_html=True)
st.write("Not limited to real world actualities of radicalization, within the cyber sphere, terrorist aim to use "
         "cyber capabilities to further their ideological or political goals. This can include hacking into websites, "
         "launching distributed denial-of-service (DDoS) attacks and spreading propaganda. Cyber terrorists may "
         "target critical infrastructure, government systems, financial institutions, or any entity that does not "
         "align with their ideological or political objectives with the goal to cause disruption, fear, or economic "
         "damage. ")
st.write('The Security Brief, New Zealand article entitled "A brief history of cyber-threats — from 2000 to 2020" by '
         'Nick Forrester, provides a historical perspective on cyber-threats, "A brief history of cyber-threats — '
         'from 2000 to 2020" details the events and the increase in cyberattacks in different countries starting all '
         'the way from the early 2000’s entitling it the “Worm Era” he details the wave of prolific “worms” costing '
         'in over 100 billion dollars in damages and remediation costs to the information security industry  The '
         'notorious ILOVEYOU worm, unleashed in 2000, targeted Microsoft Outlook users, infecting 10% of '
         'internet-connected hosts within hours and causing up to 15 billion dollars in damages. Subsequent worms '
         'like CodeRed, Nimda, and Blaster exploited vulnerabilities in operating systems and network infrastructure '
         'as seen in the chart below. ')

# Data
data = {
    "Worm": ["CodeRed", "Code Red II", "Nimda", "SQL Slammer", "Blaster", "Welchia", "Sobig.F", "Sober", "Bagle", "MyDoom", "Netsky", "Sasser"],
    "Month": ["July 2001", "August 2001", "September 2001", "January 2003", "August 2003", "August 2003", "August 2003", "October 2003", "January 2004", "January 2004", "February 2004", "April 2004"]
}

df = pd.DataFrame(data)

# Chart
st.title("Worms of the Early 2000s")
chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y("Worm:N", title=None, sort='-x'),
    x=alt.X("Month:N", title="Month of Emergence"),
    color=alt.Color("Month:N", legend=None)
).properties(width=600, height=300)

st.altair_chart(chart, use_container_width=True)

st.write("Moving on the 2005-2013 era which was entitled the “Monetisation Era”, With the use of malvertising, spam, "
         "botnets, and trojans they terrorists were able to capitalize off this for money and profit instead of for "
         "notoriety. Spam, was initially used for spreading worms and eventually evolved into a monetized tool for "
         "online scams, particularly through coordinated campaigns like pharmacy spam. One notable development was "
         "the Storm botnet, renowned as the 'most powerful supercomputer,' designed for stealth and profit. The "
         "botnet employed advanced techniques, such as a distributed peer-to-peer model, fast-flux DNS, "
         "and polymorphism, setting a standard for future botnets. Additionally, the monetization era saw the rise of "
         "the Zeus/Zbot banking trojan, transforming from a banking trojan to a full-fledged crimeware kit. The "
         "leaked Zeus source code in 2011 spawned several variants, contributing to the era of crimeware-as-a-service "
         "to be capitalized off of.")
st.write("Lastly, in the Ransomware Era from 2013-2020, with estimated damages in the trillions of dollars, "
         "ransomware, most notably CryptoLocker  exploits vulnerabilities in IT defenses, utilizing encryption and "
         "cryptocurrency and double extortion. Cyber-criminals not only encrypt and steal data but also threaten to "
         "publish it unless a ransom is paid. No individual or industry is immune, and no single technology is "
         "foolproof against ransomware attacks.")
st.write("Below shows the region in which different crimes have been committed the most.")
import plotly.express as px
# Sample data (replace this with your actual data)
data = {
    'Region': ['Asia', 'Europe', 'North America', 'Middle East and Africa', 'Latin America'],
    'Server Access': [20, 26, 30, 18, 29],
    'Ransomware': [11, 12, 30, 12, 21],
    'Data Theft': [10, 10, 9, 14, 21],
}

# Create a stacked bar chart
fig = px.bar(
    data,
    x='Region',
    y=['Server Access', 'Ransomware', 'Data Theft'],
    title='Distribution of Cyber Attack Types by Region (2021)',
    labels={'value': 'Percentage'},
    height=500,
)

# Update layout for better visualization
fig.update_layout(barmode='stack', legend=dict(title_text='Attack Type'))

# Display the chart using Streamlit
st.plotly_chart(fig)

st.write("Additionally, some other cyber-attacks listed by New Jersey Gov. Including android malware that purposely "
         "targets android mobile devices mobile devices that causes a range of attacks from device disablement to "
         "data theft. Similarly, it is important to not iOS devices are not immune to malware as iOS devices "
         "including the macOS are subject to this threat. \nPayment processing systems are also targets for "
         "cybercriminals seeking to steal credit and debit card data.")
