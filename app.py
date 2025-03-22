import streamlit as st
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Kalshi-House Arbitrage",
    page_icon="📈",
    layout="wide"
)

# Navigation
page = st.sidebar.radio("Navigation", ["Home", "About Us", "Project Details"])

if page == "Home":
    # Title Section
    st.title("🏆 Kalshi-House Arbitrage")
    st.subheader("Group Name: Gamblers")
    st.write("**Team Members:**")
    st.write("- Sucheer Maddury")
    st.write("- Ronald Feng")
    st.write("- Leo Qian")
    st.write("- Aydan Gerber")
    
    st.markdown("---")
    
    # Project Introduction
    st.header("About Us")
    st.write("""
    **Members:**
    Sucheer: **Major:** Mathematics and Computer Science

    **Hometown:** San Jose, CA

    **Bio:** I’m studying Math & CS in Arts. I enjoy playing poker and other card games, badminton, and exploring Ithaca.

    **Natural habitat:** room

    **Hobby I never had time to do:** I want to learn pool/billiards

    **Values:** efficient time management, commitment, curiosity

    **Life Goal:** Go to the casino

    **CDS Stake:** I want to understand ML at a deep level and how it can be used to solve problems.
    
    Ronald: Hi, I am Ronald and I am majoring in CS and Math in the Arts and Sciences. I am passionate about many things such as soccer, cello, and working on fun projects!

    **Major/Minors: CS, Math**

    **Hometown: Scarsdale, NY**

    **My natural habitat**: Sleeping

    **A cool thing I did this semester**: I rock climbed for the first time in Outdoor Odyssey

    **A hobby I always wanted to try out but never had the time to**: Archery

    **My biggest values**: Persistance, kindness

    🌱 **A personal life goal of mine**: Reach 70k trophies in Brawl Stars

    🎯 **My stake in CDS**: I want to work on interesting projects and meet passionate team members

    Leo: **Major:** Computer Science

    **Hometown:** Lexington, MA

    **Bio:** I’m studying CS in Engineering. I like working out, playing Roblox and horror games, and hanging out with friends. My favorite sports are swimming, skiing, volleyball, and running.

    **Natural habitat:** watching horror movies in ckb lounge (but i live in jameson)

    **Hobby I never had time to do:** i want to learn boxing and rock climbing

    **Values:** excellence in my work and exploring anything that interests me (either topics, places, or relationships), commitment to my team

    **Life Goal:** have money

    **CDS Stake:** I want to collaboratively discover applications of ds/ai/ml and their applications in different fields

    Aydan: 1. **Pronouns**: He/Him
    2. **Major/Minors: Information Science, Concentration in Data Science, Minor in Business**
    3. **Hometown:Westchester, NY**
    4. **My natural habitat**: Statler library, Gates hall
    5. **A cool thing I did this semester**: I climbed on top of Mann library
    6. **A hobby I always wanted to try out but never had the time to**: Guitar
    7. **My biggest values**: Optimism
    8. **A personal life goal of mine**: Bench 225
    9. 🎯 **My stake in CDS**: I want to have a community of like-minded people who I enjoy working with.
    """)
    
    st.image("images/SucheerHeadshot.jpeg", caption="Sucheer Maddury")
    st.image("images/ronald_headshot.png", caption="Ronald Feng")
    st.image("images/leo_headshot.png", caption="Leo Qian")
    st.image("images/aydan_headshot.png", caption="Aydan Gerber")

elif page == "Project Details":
    st.header("Project Details")
    
    st.subheader("Introduction")
    st.write("""
    Our project is about analyzing user-priced lines on betting websites and comparing them to housed markets to try and find alpha. The theory behind this is that arbitrage always exists because housed markets are more efficient than user-priced lines. In practice, liquidity can be a significant concern. Regardless, our main dataset is taken from Kalshi via their API. Our goal is to use market structures to try and make profitable trades on Kalshi, potentially using data from sites like DraftKings or FanDuel in the process.
    """)

    st.subheader("Data Manipulation")
    st.write("""
    1. Our first step was using the Kalshi API to access all markets from all time
    2. We then used keywords as well as ticker filters to extract sports-related lines from the total data
    3. We used pandas to create feature columns for the spread and other market structure features
    4. We cleaned the data of all invalid rows
    """)

    st.subheader("Visualization")
    st.image("images/kalshi_snapshot.png", width=600)
    st.image("images/confusion.png", width=600)
    st.image("images/ROC.png", width=600)
    st.image("images/PRC.png", width=600)
    st.image("images/feature_importances.png", width=600)

    st.subheader("Frontend")
    st.write("""
    Most likely, we will begin with a simple Terminal User Interface (TUI), as our input data format is relatively simple. As our frontend development progresses, it is likely that we will implement a simple web app framework, potentially via Flask so the user can input files. The frontend is used so that the user can input a variety of data and get a betting amount according to their portfolio (Kelly criterion).
    """)

    st.subheader("CI")
    st.write("""
    We are using the Python Application workflow to manage our code. Current tests are not always passing because there are spare files in the Github that we will need to clean. 
    """)