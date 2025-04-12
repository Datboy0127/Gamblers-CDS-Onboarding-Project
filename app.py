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

    st.subheader("Supervised Learning")
    st.write("""In this project, we used historical NBA game data to predict the total wins for each team in a season based on performance statistics:
	•	Points per game (avg_pts)
	•	Field goal percentage (avg_fg_pct)
	•	Assists per game (avg_ast)
	•	Rebounds per game (avg_reb)""")

    st.subheader("KNN")
    st.write("""How does a k-NN work? : KNN finds the k closests data points by distance (neighbors) and averages the target values of those neighbors to predict the target values for the validation set.
    """)
    st.write("""What’s the tradeoff between making k smaller or larger? : Making K larger decreases the MSE, due to better generalization, however smaller K allows for more specificity but is prone to overfitting.
""")
    st.write("""What happens when you reduce the number of input features? : Reducing features hurts performance overall, likely because of less data, so the model is too generalized, which hurts accuracy.
""")
    st.write("""What happens when you normalize your input data? If it’s already normalized, what happens when you scale your input data to different proportions? : No change, since KNN depends on distance, the scaling does not change the relative distance between data points.""")

    st.subheader("SVR")
    st.write("""SVR fits a close-to-linear function that stays within margins of truth values of training data. 
""")
    st.write("""It is similar to LR in that both try to make predictions for problems with linear output. However, it can use kernels for higher-dimensional data.
1. Linear kernel
- For linearly separable data,
- Behaves like LR
2. Polynomial kernel
- Higher dimensional polynomial space
- Curves for complex data
3. Rbf Radial Basis Function
- Infinite dimensional spaces
- Non-linear relationships
""")
    st.write(""" A larger C results in a tighter margin, as there is a larger penalty for errors, which can result in overfitting. This is seen across all Kernels, but RBF is displayed below. Larger gamma values do not seem to improve performance, there seems to be a sweet spot where the margins are just right and error is minimized (on our data), which can be found with hyperparameter tuning. The increase in MSE as gamma increases is likely due to overfitting, as gamma determines how tight the model fits around data.
""")

    st.subheader("DTR")
    st.write("""It splits data into regions to predict the continuous value recursively and reducing MSE. Each node makes a decision based on a feature value range and each leaf contains average target value for the data in the group.
""")
    st.write("""With a low max depth, the model underfits, with a high max depth, the model overfits.
""")
    st.write("""With less features, there can be less noise, which may help accuracy by improving generalization. However if the feature is important then accuracy can be lost.
""")
    st.write("""Don't need normalization, so distortion has no effect. This is because the trees split based on thresholds instead of specific values or distances.
""")

    st.subheader("Comparison")
    st.write("""Which k-NN, SVR, or DT performed the best? Why do you think that model had low validation loss? : Out of the models, KNN performed the best, with lowest MSE and KNN was able to identify localized patterns within clusters of wins / losses in the data. Whereas the other two must find larger trends.
""")
    st.write("""Compare the tradeoffs between using a k-NN, SVR, or DT classifier. Hypothesize in what settings each would outperform the other two. : Some trade offs:
1. KNN doesn’t require training, so it will be fastest
2. Decision tree is fastest, as the tree is built and requires few resources to follow
3. Generally depends on data, but probably KNN since it works with localized points
4. Generally depends on data, but probably also KNN since it works with localized points and can also work with larger clusters to minimize loss. Since SVR has many hyperparameters it's also possible it can be made to be better at validation (generalization)
""")