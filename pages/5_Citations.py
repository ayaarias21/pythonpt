# Import necessary libraries
import streamlit as st

#from streamlit_option_menu import option_menu
import pandas as pd  # read csv, df manipulation
st.set_page_config(page_title="Bytes and Bombs", page_icon="🚨", layout="centered")
# Import necessary libraries
st.markdown("<h2 style='color: #990000;'>Citations</h2>",
            unsafe_allow_html=True)
st.write("Wasburn, Philo C. J’]ournal of Political & Military Sociology 31, no. 1 (2003): 157–59. (http://www.jstor.org/stable/45294377)") #how to include a link
st.write("Yunos, Z, and S Sulaman. “Understanding Cyber Terrorism from Motivational Perspectives.” Journal of Information Warfare 16, no. 4 (2017): 1–13(https://www.jstor.org/stable/26504114.)") #how to include a link
st.write("Jacobsen, Colin, and Daniel Maier-Katkin. “Breivik’s Sanity: Terrorism, Mass Murder, and the Insanity Defense.” Human Rights Quarterly 37, no. 1 (2015): 137–5(http://www.jstor.org/stable/24518277.)") #how to include a linkst.write("Whittaker, Joe. “Rethinking Online Radicalization.” Perspectives on Terrorism 16, no. 4(2022): 27–40(https://www.jstor.org/stable/27158150)") #how to include a link
st.write(" Clarke, Richard A. “The Risk of Cyber War And Cyber Terrorism.” Journal of International Affairs 70, no. 1 (2016): 179–81.(https://www.jstor.org/stable/90012602)") #how to include a link
st.write("(https://securitybrief.co.nz/story/a-brief-history-of-cyber-threats-from-2000-to-2020)") #how to include a link
st.write("(https://www.nj.gov/njoem/mitigation/pdf/2019/mit2019_section5-16_Cyber_Attack.pdf)") #how to include a link #how to include a link
st.write("Drent, Margriet, Kees Homan, and Dick Zandee. “Case Study Cyber Security.” Civil-Military Capacities for European Security. Clingendael Institute, 2013.(http://www.jstor.org/stable/resrep05404.8.)") #how to include a link
st.write("Henry, Shawn, and Aaron F. Brantly. “Countering the Cyber Threat.” The Cyber Defense Review 3, no. 1 (2018): 47–56.(http://www.jstor.org/stable/26427375)") #how to include a link
st.write("ICT Cyber Desk. “Trends in Countering Cyber-Terrorism.” Analysis of Cyber Trends 2016, International Institute for Counter-Terrorism (ICT), 2016, pp. 17–19. JSTOR,](http://www.jstor.org/stable/resrep09459.7)")
st.write("Georgia, Holmer, “Countering Violent Extremism: A Peacebuilding Perspective”(https://www.usip.org/sites/default/files/SR336-Countering%20Violent%20Extremism-A%20Peacebuilding%20Perspective.pdf )")
st.write("Islam, Md. Didarul. “De-Radicalisation of Terrorists: Theoretical Analysis and Case Studies.” Counter Terrorist Trends and Analyses 11, no. 5 (2019): 6–12.(https://www.jstor.org/stable/26631540.)")





html_code = """
<style>
  @keyframes rotate {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #000;
  }

  .police-light {
    font-size: 4em;
    animation: rotate 1s linear infinite, stopRotate 2s linear forwards;
    color: #00f; /* Blue color for police light */
  }

  @keyframes stopRotate {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>

<div class="police-light">🚨</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
st.write("Thanks for reading!")

