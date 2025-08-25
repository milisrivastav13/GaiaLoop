import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import bcrypt, base64
import mysql.connector

from carbon_calc import calculate_carbon
from suggestions import eco_suggestions
from db_setup import init_db

# ✅ Must be at top
st.set_page_config(page_title="GaiaLoop", page_icon="🌱", layout="centered")

# ✅ Initialize DB
init_db()

# ----------------- Logo -----------------
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64_of_image("image.png")

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 24px; margin-bottom: 10px;">
        <div style="width: 240px; height: 130px; 
                    border-radius: 60% / 40%; 
                    overflow: hidden; 
                    border: 4px solid #ffffff; 
                    box-shadow: 0 0 12px white, 0 0 24px #00e676; background:#0b1715;">
            <img src="data:image/png;base64,{logo_base64}" 
                 style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <h1 style="color: #00e676; 
                   text-shadow: 0 0 8px rgba(0,230,118,0.6), 
                                0 0 15px rgba(0,230,118,0.8); 
                   margin: 0;">
            🌍 GaiaLoop - Environmental Sustainability Tracker
        </h1>
    </div>
""", unsafe_allow_html=True)

# ----------------- Chart Theme -----------------
pio.templates["gaialoop_theme"] = pio.templates["plotly_dark"]
pio.templates["gaialoop_theme"].layout.update({
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "font": {"family": "Trebuchet MS", "color": "#f5f5f5"},
    "title": {"x": 0.5, "xanchor": "center", "font": {"color": "#00e676"}},
    "xaxis": {"gridcolor": "rgba(255,255,255,0.1)", "zerolinecolor": "#80d8ff"},
    "yaxis": {"gridcolor": "rgba(255,255,255,0.1)", "zerolinecolor": "#80d8ff"},
    "colorway": ["#00e676", "#80d8ff", "#00bfa5", "#ffab40"],
})
pio.templates.default = "gaialoop_theme"

# ----------------- CSS -----------------
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0d1b1e, #1b2e2a);
        color: #f5f5f5;
        font-family: "Trebuchet MS", sans-serif;
    }
    [data-testid="stSidebar"] {
        background: #102520 !important;
        color: #e0f2f1 !important;
    }
    h1, h2, h3 {
        color: #00e676 !important;
        text-shadow: 0 0 8px rgba(0, 230, 118, 0.6);
        font-weight: bold;
    }
    .stSlider > div {
        background: rgba(0, 230, 118, 0.2) !important;
        border-radius: 8px;
        padding: 5px;
    }
    .stButton button {
        background: linear-gradient(90deg, #00e676, #00bfa5);
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #80d8ff, #00e676);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- DB Helper -----------------
def get_connection():
    conn = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
    return conn

# ----------------- Auth Functions -----------------
def create_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    if cursor.fetchone():
        conn.close()
        return False  # email exists

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                       (name, email, hashed))
        conn.commit()
        return True
    except mysql.connector.Error:
        return False
    finally:
        conn.close()

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()
    conn.close()
    if row and bcrypt.checkpw(password.encode(), row[0].encode() if isinstance(row[0], str) else row[0]):
        return True
    return False

def save_entry(user_email, data, carbon_value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (user_email, data, carbon_value) VALUES (%s, %s, %s)", 
                   (user_email, data, carbon_value))
    conn.commit()
    conn.close()

def get_entries(user_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT data, carbon_value, created_at FROM entries WHERE user_email=%s", (user_email,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# ----------------- Sidebar -----------------
menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Signup":
    st.subheader("Create a New Account")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        if create_user(name, email, password):
            st.success("✅ Account created! Please login.")
        else:
            st.error("⚠️ Email already exists or error occurred.")

elif choice == "Login":
    st.subheader("Login to Your Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(email, password):
            st.success(f"🌱 Welcome {email}")
            st.session_state["user"] = email
        else:
            st.error("❌ Invalid credentials")

# ----------------- Main App -----------------
if "user" in st.session_state:
    st.subheader("Track your habits, reduce your footprint, and stay eco-smart 💡🌿")
    st.caption("Close the loop. Protect Gaia.")

    st.header("Enter Your Daily Activities")
    transport = st.number_input("Distance traveled (km)", min_value=0)
    electricity = st.number_input("Electricity used (kWh)", min_value=0)
    diet = st.selectbox("Diet Type", ["Vegan", "Vegetarian", "Non-Vegetarian"])
    diet_map = {"Vegan": 0, "Vegetarian": 1, "Non-Vegetarian": 2}

    if st.button("Calculate Carbon Footprint"):
        carbon = calculate_carbon(transport, electricity, diet_map[diet])
        st.metric(label="Estimated Carbon Footprint (kg CO₂/day)", value=carbon)

        # Save entry
        save_entry(st.session_state["user"], 
                   f"Transport: {transport} km, Electricity: {electricity} kWh, Diet: {diet}", 
                   carbon)

        st.subheader("Eco-Friendly Suggestions")
        for tip in eco_suggestions(transport, electricity, diet_map[diet]):
            st.write("✅", tip)

        df = pd.DataFrame({
            "Activity": ["Transport", "Electricity", "Diet"],
            "CO2 (kg)": [transport*0.21, electricity*0.92, [2, 3.5, 5][diet_map[diet]]]
        })
        fig = px.bar(df, x="Activity", y="CO2 (kg)", color="CO2 (kg)", title="CO₂ Emissions by Activity")
        st.plotly_chart(fig)

    # ----------------- Show User History -----------------
    st.subheader("📊 My Past Entries")
    history = get_entries(st.session_state["user"])
    if history:
        df = pd.DataFrame(history, columns=["Activity Data", "Carbon Value", "Date"])
        st.dataframe(df)
    else:
        st.info("No entries yet. Start tracking your carbon footprint!")

