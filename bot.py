import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from environment
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")


# Ensure API key is available
if not API_KEY:
    st.error("Error: GOOGLE_API_KEY is missing. Please check your .env file.")
    st.stop()

# Configure Gemini AI
genai.configure(api_key=API_KEY)

# Initialize AI Model
MODEL_NAME = "models/gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)
chat = model.start_chat(history=[])

# Allowed keywords for validation
ALLOWED_KEYWORDS = [
    "convert",
    "conversion",
    "kilometers",
    "miles",
    "meters",
    "centimeters",
    "millimeters",
    "inches",
    "feet",
    "yards",
    "nautical miles",
    "grams",
    "pounds",
    "kilograms",
    "ounces",
    "stones",
    "tons",
    "milligrams",
    "micrograms",
    "Celsius",
    "Fahrenheit",
    "Kelvin",
    "joules",
    "calories",
    "kilocalories",
    "kilojoules",
    "seconds",
    "minutes",
    "hours",
    "days",
    "weeks",
    "months",
    "years",
    "milliseconds",
    "microseconds",
    "watts",
    "kilowatts",
    "megawatts",
    "gigawatts",
    "horsepower",
    "degrees",
    "radians",
    "gradians",
    "liters",
    "milliliters",
    "gallons",
    "quarts",
    "pints",
    "cups",
    "fluid ounces",
    "tablespoons",
    "teaspoons",
    "bits",
    "bytes",
    "kilobytes",
    "megabytes",
    "gigabytes",
    "terabytes",
    "petabytes",
    "pascals",
    "atmospheres",
    "bars",
    "psi",
    "mmHg",
    "torr",
    "newtons",
    "dynes",
    "pound-force",
    "kilonewtons",
    "hertz",
    "kilohertz",
    "megahertz",
    "gigahertz",
    "meters per second",
    "kilometers per hour",
    "miles per hour",
    "knots",
]


# Function to generate unit conversion response
def bot_response(query):
    try:
        response = chat.send_message(query, stream=True)
        response_text = "".join(chunk.text for chunk in response)

        # Validate if response contains unit conversion keywords
        if any(keyword in response_text.lower() for keyword in ALLOWED_KEYWORDS):
            return response_text
        return "I can only perform unit conversions. Please ask about a unit."
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit UI Configuration
st.set_page_config(
    page_title="AI Unit Conversion System", page_icon="📐", layout="wide"
)

# Apply Custom CSS
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background: linear-gradient(135deg, #2c3e50 10%, #34495e 100%);


        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            padding: 10px;
        }
        .subheader {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .chat-container {
            padding: 20px;
            margin-bottom: 20px;
        }
        .user-msg {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .ai-msg {
            font-size: 16px;
            color: #333;
            background: #e3f2fd;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .history-container {
            max-height: 300px;
            overflow-y: auto;
            border-radius: 10px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .input-box {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    '<div class="title">🤖 AI Unit Conversion System</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="subheader">Convert Weight, Mass, Area, Volume, Speed, and more!</div>',
    unsafe_allow_html=True,
)

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "show_history" not in st.session_state:
    st.session_state["show_history"] = False

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

if "latest_response" not in st.session_state:
    st.session_state["latest_response"] = None


# Function to handle user input submission
def submit_input():
    if st.session_state["user_input"]:
        response = bot_response(st.session_state["user_input"])

        # Store in history
        st.session_state["chat_history"].append(
            {"query": st.session_state["user_input"], "response": response}
        )

        # Store latest response separately
        st.session_state["latest_response"] = {
            "query": st.session_state["user_input"],
            "response": response,
        }

    # Clear user input field
    st.session_state["user_input"] = ""


with st.expander("📜 View Supported Units"):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("### 🔹 Length")
        st.write("- Kilometers ↔ Miles")
        st.write("- Meters ↔ Feet")
        st.write("- Centimeters ↔ Inches")
        st.write("- Millimeters ↔ Inches")
        st.write("- Yards ↔ Meters")
        st.write("- Nautical Miles ↔ Miles")

    with col2:
        st.markdown("### ⚖️ Weight & Mass")
        st.write("- Grams ↔ Pounds")
        st.write("- Kilograms ↔ Ounces")
        st.write("- Stones ↔ Kilograms")
        st.write("- Tons ↔ Kilograms")
        st.write("- Milligrams ↔ Micrograms")

    with col3:
        st.markdown("### 🌡️ Temperature & Energy")
        st.write("- Celsius ↔ Fahrenheit")
        st.write("- Fahrenheit ↔ Celsius")
        st.write("- Kelvin ↔ Celsius")
        st.write("- Joules ↔ Calories")
        st.write("- Kilocalories ↔ Joules")
        st.write("- Kilojoules ↔ Calories")

    with col4:
        st.markdown("### ⏳ Time & Speed")
        st.write("- Seconds ↔ Minutes")
        st.write("- Minutes ↔ Hours")
        st.write("- Hours ↔ Days")
        st.write("- Days ↔ Weeks")
        st.write("- Weeks ↔ Months")
        st.write("- Months ↔ Years")
        st.write("- Milliseconds ↔ Microseconds")
        st.write("- Meters per Second ↔ Kilometers per Hour")
        st.write("- Miles per Hour ↔ Kilometers per Hour")
        st.write("- Knots ↔ Kilometers per Hour")

    with col5:
        st.markdown("### ⚡ Power, Pressure, & Digital Storage")
        st.write("- Watts ↔ Horsepower")
        st.write("- Kilowatts ↔ Megawatts")
        st.write("- Degrees ↔ Radians")
        st.write("- Pascals ↔ Atmospheres")
        st.write("- Bars ↔ PSI")
        st.write("- Bits ↔ Bytes")
        st.write("- Kilobytes ↔ Megabytes")
        st.write("- Gigabytes ↔ Terabytes")

# Toggle button for showing chat history
if st.button("📜 Show Chat History"):
    st.session_state["show_history"] = not st.session_state["show_history"]

# Display chat history if toggled on
if st.session_state["show_history"] and st.session_state["chat_history"]:
    st.markdown('<div class="history-container">', unsafe_allow_html=True)
    st.write("### 🔄 Chat History")
    for entry in reversed(st.session_state["chat_history"]):  # Show most recent first
        st.markdown(
            f'<div class="user-msg">👱🏻‍♂️ You: {entry["query"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="ai-msg">🤖 AI: {entry["response"]}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("---")

# Show latest response above input field
if st.session_state["latest_response"]:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="user-msg">👱🏻‍♂️ You: {st.session_state["latest_response"]["query"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="ai-msg">🤖 AI: {st.session_state["latest_response"]["response"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.text_input(
    "Please enter the unit you wish to convert:",
    key="user_input",
    on_change=submit_input,
    placeholder="e.g., Convert 10 miles to kilometers",
)
