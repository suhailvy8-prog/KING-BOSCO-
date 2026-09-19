import streamlit as st
import collections

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# VIP High-Contrast Style Setup (Removed all unwanted white backgrounds)
st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    .stApp { background-color: #0B0E14; color: #FFFFFF; }
    
    /* Metrics Styling - Fully Bold */
    div[data-testid="stMetricValue"] {
        font-size: 36px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 18px !important;
        font-weight: 900 !important;
        color: #FFD700 !important;
    }

    /* Custom Dark Buttons (Reset & Plus/Minus) */
    .stButton button {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 1px solid #334155 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }
    .stButton button:hover {
        background-color: #334155 !important;
        border-color: #FFD700 !important;
        color: #FFD700 !important;
    }

    /* Input Field Fix (Completely Dark & Clean) */
    input[type="text"] {
        text-align: center !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #3B82F6 !important;
    }
    
    div[data-baseweb="input"] {
        background-color: #1E293B !important;
        border-radius: 8px !important;
    }

    /* Prediction Card */
    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 22px;
        border-radius: 16px;
        border: 2px solid #FFD700;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0px 6px 15px rgba(255, 215, 0, 0.2);
    }

    /* History Logs Styling */
    .history-card {
        background-color: #151C28;
        padding: 12px 16px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 5px solid #FFD700;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #FFFFFF;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFD700; font-size: 28px;'>👑 KING BOSCO PREDICTOR</h1>", unsafe_allow_html=True)

# ----------------- ACCESS KEYS -----------------
ALLOWED_KEYS = ["JAI101", "JAI102", "VIP2026"]

st.sidebar.title("🔐 Access Control")
user_key = st.sidebar.text_input("Access Key നൽകുക:", type="password")

if user_key not in ALLOWED_KEYS:
    st.warning("🔒 ദയവായി ശരിയായ Access Key നൽകുക.")
    st.info("ആക്സസ് ലഭിക്കാൻ അഡ്മിനുമായി ബന്ധപ്പെടുക.")
    st.stop()

st.sidebar.success("✅ Access Granted!")

# ----------------- SESSION STATES -----------------
if 'history_details' not in st.session_state:
    st.session_state.history_details = []
if 'history' not in st.session_state:
    st.session_state.history = []
if 'num_history' not in st.session_state:
    st.session_state.num_history = []
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'losses' not in st.session_state:
    st.session_state.losses = 0
if 'last_prediction_bs' not in st.session_state:
    st.session_state.last_prediction_bs = None
if 'last_predicted_numbers' not in st.session_state:
    st.session_state.last_predicted_numbers = []
if 'current_num' not in st.session_state:
    st.session_state.current_num = 0

col1, col2 = st.columns(2)
col1.metric("WINS 🟢", st.session_state.wins)
col2.metric("LOSSES 🔴", st.session_state.losses)

st.write("")
if st.button("🔄 Reset Data", use_container_width=True):
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.last_prediction_bs = None
    st.session_state.last_predicted_numbers = []
    st.session_state.current_num = 0
    st.rerun()

st.divider()

# ----------------- NUMBER INPUT WITH +/- BUTTONS -----------------
st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക (0 - 9):</p>", unsafe_allow_html=True)

b_minus, b_input, b_plus = st.columns([1, 2, 1])

with b_minus:
    if st.button("➖", use_container_width=True):
        if st.session_state.current_num > 0:
            st.session_state.current_num -= 1
            st.rerun()

with b_input:
    num_str_input = st.text_input(
        "label_hidden", 
        value=str(st.session_state.current_num), 
        max_chars=1, 
        label_visibility="collapsed"
    )
    if num_str_input.isdigit():
        val_parsed = int(num_str_input)
        if 0 <= val_parsed <= 9:
            st.session_state.current_num = val_parsed

with b_plus:
    if st.button("➕", use_container_width=True):
        if st.session_state.current_num < 9:
            st.session_state.current_num += 1
            st.rerun()

st.write("")
submit_clicked = st.button("Submit Result", use_container_width=True, type="primary")

if submit_clicked:
    val = st.session_state.current_num
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"

    # Big/Small Win-Loss Check
    status_str = "➖ START"
    if st.session_state.last_prediction_bs is not None:
        if current_bs_short == st.session_state.last_prediction_bs:
            st.session_state.wins += 1
            status_str = "<span style='color:#00E676; font-weight:bold;'>🟢 WIN</span>"
        else:
            st.session_state.losses += 1
            status_str = "<span style='color:#FF5252; font-weight:bold;'>🔴 LOSS</span>"

    # Number Prediction Win Check
    num_win_str = ""
    if st.session_state.last_predicted_numbers:
        if val in st.session_state.last_predicted_numbers:
            num_win_str = " <span style='color:#00E676; font-size:13px; font-weight:bold;'>[🎯 Number Win]</span>"

    st.session_state.history.append(current_bs_short)
    st.session_state.num_history.append(val)
    
    st.session_state.history_details.insert(0, {
        "num": val,
        "type": current_bs,
        "status": status_str,
        "num_win": num_win_str
    })

    hist = st.session_state.history
    num_hist = st.session_state.num_history

    if len(hist) < 3:
        st.session_state.last_prediction_bs = None
        st.session_state.last_predicted_numbers = []
    else:
        last_three = "".join(hist[-3:])
        last_four = "".join(hist[-4:]) if len(hist) >= 4 else ""

        if last_four == "BBBB":
            next_pred = "S"
        elif last_four == "SSSS":
            next_pred = "B"
        elif last_three == "BBB":
            next_pred = "B"
        elif last_three == "SSS":
            next_pred = "S"
        else:
            recent_bs = hist[-5:]
            b_count = recent_bs.count('B')
            s_count = recent_bs.count('S')
            next_pred = "B" if b_count >= s_count else "S"

        st.session_state.last_prediction_bs = next_pred

        # Calculate likely numbers for next prediction
        num_counts = collections.Counter(num_hist[-15:])
        likely_nums = [n for n, c in num_counts.most_common(2)]
        st.session_state.last_predicted_numbers = likely_nums

        pred_text = "BIG 🟢" if next_pred == "B" else "SMALL 🔴"
        color_code = "#00E676" if next_pred == "B" else "#FF5252"

        st.markdown(f"""
            <div class="pred-card">
                <div style="color: #94A3B8; font-size: 14px; font-weight: bold;">NEXT PREDICTION</div>
                <div style="font-size: 38px; font-weight: 900; color: {color_code}; margin: 8px 0;">{pred_text}</div>
                <div style="color: #E2E8F0; font-size: 15px;">📊 Likely Numbers: <b style="color:#FFD700;">{likely_nums}</b></div>
            </div>
        """, unsafe_allow_html=True)

st.divider()

if st.session_state.history_details:
    st.markdown("<h3 style='color:#FFD700;'>📜 History Logs</h3>", unsafe_allow_html=True)
    for item in st.session_state.history_details[:10]:
        st.markdown(f"""
            <div class="history-card">
                <span><b>Number: {item['num']}</b> ({item['type']}){item.get('num_win', '')}</span>
                <span>{item['status']}</span>
            </div>
        """, unsafe_allow_html=True)
        
