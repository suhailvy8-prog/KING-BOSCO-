import streamlit as st
import collections

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    .stApp { background-color: #0B0E14; color: #FFFFFF; }
    
    .app-title {
        text-align: center;
        color: #FFD700;
        font-size: 34px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
        margin-bottom: 20px;
        text-shadow: 0px 2px 10px rgba(255, 215, 0, 0.3);
    }

    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin: 15px 0;
    }
    .metric-box {
        flex: 1;
        background-color: #1E293B;
        border: 2px solid #334155;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .metric-label {
        font-size: 16px !important;
        font-weight: 900 !important;
        color: #FFD700 !important;
        margin-bottom: 5px;
    }
    .metric-val {
        font-size: 32px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
    }

    .stButton button {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #334155 !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        height: 50px !important;
        font-size: 18px !important;
    }
    .stButton button:hover {
        background-color: #334155 !important;
        border-color: #FFD700 !important;
        color: #FFD700 !important;
    }

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

    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 22px;
        border-radius: 16px;
        border: 2px solid #FFD700;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0px 6px 15px rgba(255, 215, 0, 0.2);
    }

    .history-card {
        background-color: #151C28;
        padding: 14px 16px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 5px solid #FFD700;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #FFFFFF;
        font-size: 17px;
    }
    
    .win-text {
        color: #00E676 !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 8px rgba(0, 230, 118, 0.4);
    }

    .loss-text {
        color: #FF5252 !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 8px rgba(255, 82, 82, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)

# ----------------- SESSION STATE FOR ACCESS KEYS -----------------
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]

# ----------------- SIDEBAR ACCESS & ADMIN CONTROL -----------------
st.sidebar.title("🔐 Access Control")

user_key = st.sidebar.text_input("നിങ്ങളുടെ Access Key നൽകുക:", type="password")

st.sidebar.divider()
st.sidebar.subheader("🛠️ Admin Settings")
admin_pass = st.sidebar.text_input("Admin Password:", type="password")

admin_logged_in = (admin_pass == "bosco123")

if admin_logged_in:
    st.sidebar.success("Admin Mode Active ✅")
    st.sidebar.write("നിലവിലെ ആക്സസ് കീകൾ:")
    st.sidebar.write(st.session_state.allowed_keys)
    
    new_key_to_add = st.sidebar.text_input("പുതിയ കീ ചേർക്കുക:")
    if st.sidebar.button("Add Key"):
        if new_key_to_add and new_key_to_add not in st.session_state.allowed_keys:
            st.session_state.allowed_keys.append(new_key_to_add)
            st.sidebar.success(f"'{new_key_to_add}' ചേർത്തു!")
            st.rerun()
            
    key_to_remove = st.sidebar.selectbox("ഒഴിവാക്കേണ്ട കീ:", ["-- Select --"] + st.session_state.allowed_keys)
    if st.sidebar.button("Remove Key") and key_to_remove != "-- Select --":	
        st.session_state.allowed_keys.remove(key_to_remove)
        st.sidebar.success(f"'{key_to_remove}' നീക്കം ചെയ്തു!")
        st.rerun()

if user_key in st.session_state.allowed_keys or admin_logged_in:
    st.sidebar.success("✅ Access Granted!")
else:
    st.warning("🔒 ദയവായി ശരിയായ Access Key നൽകുക.")
    st.stop()

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
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 5000
if 'current_level' not in st.session_state:
    st.session_state.current_level = 1
if 'is_skip' not in st.session_state:
    st.session_state.is_skip = False

# ----------------- WALLET INPUT -----------------
st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 18px;'>💰 നിങ്ങളുടെ ഡെപ്പോസിറ്റ് ബാലൻസ് നൽകുക (₹):</p>", unsafe_allow_html=True)
wallet_col1, wallet_col2, wallet_col3 = st.columns([1, 2, 1])
with wallet_col2:
    wallet_input = st.text_input("Wallet Input", value=str(st.session_state.wallet_balance), label_visibility="collapsed")
    if wallet_input.isdigit():
        val_w = int(wallet_input)
        if val_w > 0:
            st.session_state.wallet_balance = val_w

st.write("")

# ----------------- WINS & LOSSES -----------------
st.markdown(f"""
    <div class="metric-container">
        <div class="metric-box">
            <div class="metric-label">WINS 🟢</div>
            <div class="metric-val">{st.session_state.wins}</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">LOSSES 🔴</div>
            <div class="metric-val">{st.session_state.losses}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# ----------------- RESET BUTTON -----------------
if st.button("🔄 Reset Data", use_container_width=True):
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.last_prediction_bs = None
    st.session_state.last_predicted_numbers = []
    st.session_state.current_level = 1
    st.session_state.is_skip = False
    st.rerun()

st.write("")

# Function to handle number selection with Dynamic Trend, Repeat & Smart Skip Logic
def handle_number_click(val):
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"

    status_str = "<span style='color:#94A3B8; font-weight:bold;'>➖ START</span>"
    
    if st.session_state.last_prediction_bs is not None:
        if not st.session_state.is_skip:
            if current_bs_short == st.session_state.last_prediction_bs:
                st.session_state.wins += 1
                status_str = "<span class='win-text'>🟢 WIN</span>"
                st.session_state.current_level = 1  # Reset on Win (Within 5 levels preferred)
            else:
                st.session_state.losses += 1
                status_str = "<span class='loss-text'>🔴 LOSS</span>"
                if st.session_state.current_level < 8:
                    st.session_state.current_level += 1  # Max up to Level 8
                else:
                    st.session_state.current_level = 1  # Reset after Level 8
        else:
            status_str = "<span style='color:#38BDF8; font-weight:bold;'>🔄 SKIPPED</span>"

    num_win_str = ""
    if st.session_state.last_predicted_numbers:
        if val in st.session_state.last_predicted_numbers:
            num_win_str = " <span style='color:#00E676; font-size:13px; font-weight:900;'>[🎯 Number Win]</span>"

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
        st.session_state.is_skip = False
    else:
        recent_four = hist[-4:] if len(hist) >= 4 else hist
        
        is_choppy = False
        if len(recent_four) == 4 and recent_four[0] != recent_four[1] and recent_four[1] != recent_four[2] and recent_four[2] != recent_four[3]:
            is_choppy = True

        is_heavy_repeat = False
        if len(hist) >= 3 and hist[-1] == hist[-2] == hist[-3]:
            is_heavy_repeat = True

        if is_choppy and st.session_state.current_level == 1 and len(hist) % 2 == 0:
            st.session_state.is_skip = True
        else:
            st.session_state.is_skip = False

        is_alternating = False
        if len(hist) >= 4:
            if hist[-1] != hist[-2] and hist[-2] != hist[-3] and hist[-3] != hist[-4]:
                is_alternating = True
        elif len(hist) == 3:
            if hist[-1] != hist[-2] and hist[-2] != hist[-3]:
                is_alternating = True

        if is_alternating:
            next_pred = "S" if hist[-1] == "B" else "B"
        elif is_heavy_repeat:
            if st.session_state.current_level >= 3:
                next_pred = "S" if hist[-1] == "B" else "B"
            else:
                next_pred = hist[-1]
        else:
            recent_window = hist[-6:] if len(hist) >= 6 else hist
            b_count = recent_window.count('B')
            s_count = recent_window.count('S')
            
            if b_count > s_count:
                next_pred = "B"
            elif s_count > b_count:
                next_pred = "S"
            else:
                next_pred = "S" if hist[-1] == "B" else "B"

        st.session_state.last_prediction_bs = next_pred

        num_counts = collections.Counter(num_hist[-12:])
        likely_nums = [n for n, c in num_counts.most_common(2)]
        st.session_state.last_predicted_numbers = likely_nums

# ----------------- CIRCULAR GRID BUTTONS UI (0 to 9) -----------------
st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 18px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)

cols_top = st.columns(5)
nums_top = [
    (0, "0", "🟣 🔴"),
    (1, "1", "🟢"),
    (2, "2", "🔴"),
    (3, "3", "🟢"),
    (4, "4", "🔴")
]

for idx, (num_val, num_str, badge) in enumerate(nums_top):
    with cols_top[idx]:
        if st.button(f"{num_str}\n{badge}", key=f"btn_{num_val}", use_container_width=True):
            handle_number_click(num_val)
            st.rerun()

cols_bottom = st.columns(5)
nums_bottom = [
    (5, "5", "🟢 🟣"),
    (6, "6", "🔴"),
    (7, "7", "🟢"),
    (8, "8", "🔴"),
    (9, "9", "🟢")
]

for idx, (num_val, num_str, badge) in enumerate(nums_bottom):
    with cols_bottom[idx]:
        if st.button(f"{num_str}\n{badge}", key=f"btn_{num_val}", use_container_width=True):
            handle_number_click(num_val)
            st.rerun()

st.write("")

# ----------------- DISPLAY PREDICTION CARD -----------------
if st.session_state.last_prediction_bs is not None:
    next_pred = st.session_state.last_prediction_bs
    likely_nums = st.session_state.last_predicted_numbers

    if st.session_state.is_skip:
        pred_text = "⚠️ SMART SKIP (ഈ റൗണ്ട് സുരക്ഷിതമായി വിടുക)"
        color_code = "#38BDF8"
    else:
        pred_text = "BIG 🟢" if next_pred == "B" else "SMALL 🔴"
        color_code = "#00E676" if next_pred == "B" else "#FF5252"

    base_unit = st.session_state.wallet_balance / 255
    multipliers = [1, 2, 4, 8, 16, 32, 64, 128]
    current_multiplier = multipliers[st.session_state.current_level - 1]
    suggested_bet = max(1, round(base_unit * current_multiplier))

    st.markdown(f"""
        <div class="pred-card">
            <div style="color: #94A3B8; font-size: 14px; font-weight: bold;">NEXT PREDICTION</div>
            <div style="font-size: 32px; font-weight: 900; color: {color_code}; margin: 8px 0;">{pred_text}</div>
            <div style="color: #E2E8F0; font-size: 15px; margin-bottom: 6px;">📊 Likely Numbers: <b style="color:#FFD700;">{likely_nums}</b></div>
            <hr style="border-color: #334155; margin: 10px 0;">
            <div style="color: #38BDF8; font-size: 16px; font-weight: bold;">
                🛡️ 8-Level Plan | Level {st.session_state.current_level}/8 (Win within 5 prioritized)
            </div>
            <div style="color: #FFFFFF; font-size: 20px; font-weight: 900; margin-top: 4px;">
                Suggested Bet: <span style="color: #FFD700;">₹{suggested_bet}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    if len(st.session_state.history) < 3:
        st.info(f"കുറഞ്ഞത് {3 - len(st.session_state.history)} ഡാറ്റ കൂടി നൽകുക...")

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
