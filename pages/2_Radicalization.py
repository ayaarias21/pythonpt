import streamlit as st
import time
import pandas as pd
import altair as alt
#from streamlit_option_menu import option_menu
import pandas as pd  # read csv, df manipulation

st.set_page_config(page_title="Bytes and Bombs", page_icon="🚨", layout="centered")
st.markdown("<h2 style='color: #990000;'>Radicalization</h2>", unsafe_allow_html=True)

article_intro = """
The article entitled “Rethinking Online Radicalization” by Joe Whittaker does an excellent job at challenging 
the understanding of online radicalization by arguing against the separation between the “online” and “offline” realms. 
The article suggests both domains are inseparable, and we should understand the ontological nature of it and by doing 
this adopting a broader range of factors beyond online communication technologies when studying radicalization.
"""

article_main = """
The article refers to various models and theories proposed by scholars to explain the dynamics of online radicalization, 
emphasizing the potential for individuals to be exposed to extremist propaganda, engage in deviant behaviors, and form 
online communities that facilitate radicalization. When trying to theorize the process of online and offline dynamics, 
the article acknowledges the ambiguity of the term online radicalization and suggests that scholars should move beyond 
the narrow focus on online radicalization. It recommends considering the wider information environment while avoiding 
theories that exclusively explain how online radicalization works and advocates for holistic theories that consider 
individuals' predispositions, stressors, engagement with their environment, and systemic factors.
"""

police_text = """
In correlation to this, the text by the International Association of Chiefs Police, entitled 
“Online Radicalization to Violent Extremism,” briefly touches on the topic highlighting the process by which individuals 
are exposed to extremist ideologies and gradually move from mainstream beliefs toward more extreme views. Online media, 
particularly social networks like Facebook, Twitter, and YouTube, play a significant role in this process. The text 
emphasizes that the factors influencing radicalization vary from person to person, and the process itself can be dynamic, 
with individuals moving back and forth between stages. This also leads into different perspectives.
"""

# Displaying the content using Streamlit
st.write(article_intro)
st.write(article_main)
st.write(police_text)

st.markdown("Firstly, the social perspective and the induvial focus; The concept of radicalization usually emphasizes "
            "the psychological factors, and the effect online platforms and social media have on the induvial "
            "constantly this rhetoric of construed violent beliefs. Group dynamics also play an important in this "
            "first perspective because not only can the group influence tend to pull individuals towards extremist "
            "ideologies, but the engagement also associated with the mind of interaction and sense of belonging "
            "become an intense pull factor towards those ideas")
st.write("The psychological perspective such as individual vulnerabilities due to grievances and confirmation bias, "
         "wherein individuals seek information aligning with their existing beliefs, contributes to the reinforcement "
         "of radical ideologies act as factors for this perspective however, the line can become misconstrued for "
         "example, the horrific crimes Anders Breivik committed, the question of mental health became a key topic in "
         "his trail, although sentenced to 21 years, the question still remains of mental health as strategic factor "
         "for mitigated legal consequences or for public sympathy.")
st.write("Another less widely looked at perspective is the political perspective where an individual's ideologies are "
         "fueled by key factors including but not limited, to their socio-political and economic conditions marked by "
         "discrimination, inequality, and the use of propaganda. ")

# Import necessary libraries

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
data_altair = {
    "Worm": ["CodeRed", "Code Red II", "Nimda", "SQL Slammer", "Blaster", "Welchia", "Sobig.F", "Sober", "Bagle", "MyDoom", "Netsky", "Sasser"],
    "Month": ["July 2001", "August 2001", "September 2001", "January 2003", "August 2003", "August 2003", "August 2003", "October 2003", "January 2004", "January 2004", "February 2004", "April 2004"]
}

df_altair = pd.DataFrame(data_altair)

# Chart
chart_altair = alt.Chart(df_altair).mark_bar().encode(
    y=alt.Y("Worm:N", title=None, sort='-x'),
    x=alt.X("Month:N", title="Month of Emergence"),
    color=alt.Color("Month:N", legend=None)
).properties(width=600, height=300)

# Display the Altair chart
st.altair_chart(chart_altair, use_container_width=True)


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

# Data
data_altair = {
    'Region': ['Asia', 'Europe', 'North America', 'Middle East and Africa', 'Latin America'],
    'Server Access': [20, 26, 30, 18, 29],
    'Ransomware': [11, 12, 30, 12, 21],
    'Data Theft': [10, 10, 9, 14, 21],
}

df_altair = pd.DataFrame(data_altair)

# Melt the DataFrame to make it tidy for Altair
df_melted = df_altair.melt('Region', var_name='Attack Type', value_name='Count')

# Stacked bar chart with Altair
chart_altair = alt.Chart(df_melted).mark_bar().encode(
    x='Region:N',
    y='Count:Q',
    color='Attack Type:N',
    order=alt.Order('Attack Type:N', sort='ascending'),
    tooltip=['Region:N', 'Count:Q']
).properties(height=500)

# Display the Altair chart
st.altair_chart(chart_altair, use_container_width=True)

st.write("Additionally, some other cyber-attacks listed by New Jersey Gov. Including android malware that purposely "
         "targets android mobile devices mobile devices that causes a range of attacks from device disablement to "
         "data theft. Similarly, it is important to not iOS devices are not immune to malware as iOS devices "
         "including the macOS are subject to this threat. \nPayment processing systems are also targets for "
         "cybercriminals seeking to steal credit and debit card data.")
# Import necessary libraries
