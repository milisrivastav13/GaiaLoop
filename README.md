# 📌 Title:

🌍 *GaiaLoop – Environmental Sustainability Tracker*

# 👇🏻 Description:

*GaiaLoop* is a Streamlit app that helps users track daily activities and calculate their personal carbon footprint. Log transport, electricity, and diet habits, get eco-friendly suggestions, visualize CO₂ emissions with interactive charts, and review past entries. Built with Python, MySQL, Plotly, and bcrypt.




## 💡 Features:

🔒 Secure Authentication – Users can register and log in with passwords securely hashed using bcrypt.

📝 Comprehensive Activity Tracking – Log daily transport, electricity consumption, and dietary habits.

🌱 Carbon Footprint Calculation – Accurately estimate personal CO₂ emissions based on user inputs.

💡 Personalized Sustainability Recommendations – Receive actionable tips to reduce environmental impact.

📊 Data Visualization – Interactive charts display emissions by activity for clear insights.

🕒 Historical Data Management – Maintain and review past entries with timestamps for progress monitoring.

🗄️ Robust Database Integration – All user and activity data is securely stored in MySQL.

🖥️ User-Friendly Interface – Clean, responsive design optimized for both desktop and mobile devices.

## 🚀 How to Run:

1.Clone the repository

git clone https://github.com/milisrivastav13/gaialoop.git
cd gaialoop


2.Install dependencies

pip install -r requirements.txt


3.Set up MySQL Database

Create a database (e.g., gaialoop_db) in MySQL.

Update .streamlit/secrets.toml with your MySQL credentials:

[mysql]
host = "127.0.0.1"
user = "your_mysql_user"
password = "your_mysql_password"
database = "gaialoop_db"


4.Initialize the database tables

python db_setup.py


6.Run the Streamlit app

streamlit run app.py



## 🌐 Live Demo:

🔗 Click here to use MiliMind online:
https://github.com/milisrivastav13/GaiaLoop

## 📸 Screenshots:

![07923d5b-ee21-46a2-861b-a31fa9616fe4](https://github.com/user-attachments/assets/0fe5c898-5ee1-49b0-8acb-a4fa9920c002)

![c34ffad4-5c0e-4526-b788-82dd8b8e4d82](https://github.com/user-attachments/assets/3638c844-cf15-4c94-9ab3-1290c4cfa7ca)
![15b1977a-d97e-4269-aaae-beeacddca31d](https://github.com/user-attachments/assets/7f74d5ef-3646-4d20-9fe3-45d5eb146de0)

![aca974e1-c155-4d8b-b5c7-f9808e1110bc](https://github.com/user-attachments/assets/5a6aa5e4-4f03-4e7a-b275-ccb854aeead7)

![f792499b-8ab8-42f3-ad85-1ea9eda4f2c5](https://github.com/user-attachments/assets/bf51d0e0-080a-4530-8997-3d101cfea085)

![6c4d4711-c7d4-4f0b-9bb5-c64fe17ae5c7](https://github.com/user-attachments/assets/4e2e97b8-1983-48d1-8d8c-30fc113565f5)
![5373c219-abff-4cfa-a94a-45a9447119dd](https://github.com/user-attachments/assets/8ec97257-7bf5-4810-b7dd-1b34d4f84023)

![5220907f-2662-4794-9f32-0e6c3db37738](https://github.com/user-attachments/assets/fe2799b2-3273-4e45-b411-fb5f76c84b6f)
![9ca3fdef-d2d5-47e6-a29a-3f77adb1f201](https://github.com/user-attachments/assets/7608b70f-7ee1-4425-aa24-b9a1ab67fa70)
![75074a11-40bd-425b-9d5a-d7eafc3a5b41](https://github.com/user-attachments/assets/13c9e202-8731-4221-b9e6-a3a18e2005a8)

## 🛠️ Tech Stack:

🐍 Python – Core backend programming and calculations

💻 Streamlit – Interactive web app framework

🗄️ MySQL – Database for users & carbon footprint entries

🔒 bcrypt – Secure password hashing & authentication

📊 Pandas – Data manipulation and analysis

📈 Plotly – Interactive charts & visualizations

🎨 HTML / CSS – Custom styling within Streamlit for polished UI

🌐 Git & GitHub – Version control and repository management

☁️ Streamlit Cloud – Cloud deployment of the web app



## ❓ Frequently Asked Questions (FAQ):

Q1: 🌍 What is GaiaLoop?
A: GaiaLoop is an environmental sustainability tracker that helps users calculate their daily carbon footprint, track habits, and get eco-friendly suggestions.

Q2: 👥 Who can use this app?
A: Anyone interested in monitoring and reducing their carbon footprint. Users need to sign up and log in to track their activities.

Q3: ⚡ How is the carbon footprint calculated?
A: The app calculates carbon emissions based on daily transportation distance 🚗, electricity usage 💡, and diet type 🥗🍖.

Q4: 📊 Can I view my past entries?
A: Yes! GaiaLoop stores all entries in a secure MySQL database and displays them in an interactive chart.

Q5: 🔒 Is my data secure?
A: Absolutely. Passwords are hashed using bcrypt, and user data is stored securely in MySQL.

Q6: ☁️ Can I deploy GaiaLoop on my own server?
A: Yes! Clone the repository, set up the database, update secrets.toml, install dependencies, and run the app with Streamlit.

Q7: 🌐 Is there a live demo?
A: Yes! You can access it here on my git.

## 📝 Feedback:

I’d love to hear your thoughts on GaiaLoop!

Found a bug? 🐞 Open an issue on GitHub.

Have suggestions? 💡 Share your ideas or improvements.

Enjoyed the project? ⭐ Leave a comment or star the repo.

Your feedback helps me make GaiaLoop even better, more interactive, and impactful for everyone.

## 🚀 Future Enhancements:

📱 Mobile-Friendly UI: Improve responsiveness for phones and tablets.

📈 Advanced Analytics: Track trends over weeks/months with interactive dashboards.

🌐 Social Sharing: Allow users to share eco-achievements with friends.

🤖 AI Suggestions: Personalized tips using AI for more accurate carbon reduction.

🌿 Gamification: Rewards, badges, and challenges to motivate eco-friendly habits.

🔗 Integration: Connect with smart devices for automatic energy and transport tracking.
## 🙏 Acknowledgements:

This project was entirely developed by me, *Mili Srivastava*.
No external help was used — from planning to coding, designing, and testing, it’s completely my work.
Big thanks to my curiosity and persistence for making GaiaLoop possible! 🌱✨






## 👩‍💻 Author:

*Mili Srivastava* – Creator, Developer, and Designer of GaiaLoop

Conceptualized and developed GaiaLoop entirely from scratch.

Designed the interactive dashboard with intuitive visuals and real-time insights.

Implemented activity tracking, carbon calculations, and eco-friendly suggestions.

Passionate about AI, ML, DL, and creative coding.

Dedicated to building impactful and innovative projects that promote sustainability.

GitHub: milisrivastav13

LinkedIn: Mili Srivastava 🌟

