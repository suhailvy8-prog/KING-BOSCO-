import streamlit as st
import collections

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    .stApp { background-color: #0B0E14; color: #FFFFFF; }
    
    .app-title {
        text-align: center;
        color: #FFD700;
        font-size: 26px !important;
        font-weight: 900 !important;
        margin-bottom: 10px;
    }

    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin: 10px 0;
    }
    .metric-box {
        flex: 1;
        background-color: #1E293B;
        border: 2px solid #334155;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    
    input[type="text"] {
        text-align: center !important;
        font-size: 18px !important;
        font-weight: bold !important;
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #3B82F6 !important;
    }
    
    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 15px;
        border-radius: 12px;
        border: 2px solid #FFD700;
        text-align: center;
        margin: 10px 0;
    }

    .history-card {
        background-color: #151C28;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
        border-left: 4px solid #FFD700;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #FFFFFF;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)

# ----------------- SESSION STATE FOR ACCESS KEYS -----------------
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]

# ----------------- SIDEBAR ACCESS & ADMIN CONTROL -----------------
st.sidebar.title("🔐 Access Control")
user_key = st.sidebar.text_input("Access Key:", type="password")

st.sidebar.divider()
st.sidebar.subheader("🛠️ Admin Settings")
admin_pass = st.sidebar.text_input("Admin Password:", type="password")
admin_logged_in = (admin_pass == "bosco123")

if admin_logged_in:
    st.sidebar.success("Admin Mode Active ✅")
    new_key_to_add = st.sidebar.text_input("പുതിയ കീ ചേർക്കുക:")
    if st.sidebar.button("Add Key"):
        if new_key_to_add and new_key_to_add not in st.session_state.allowed_keys:
            st.session_state.allowed_keys.append(new_key_to_add)
            st.sidebar.success("ചേർത്തു!")
            st.rerun()

if user_key in st.session_state.allowed_keys or admin_logged_in:
    st.sidebar.success("✅ Access Granted!")
else:
    st.sidebar.warning("🔒 ദയവായി ശരിയായ Access Key നൽകുക.")
    st.stop()

if 'history_details' not in st.session_state: st.session_state.history_details = []
if 'history' not in st.session_state: st.session_state.history = []
if 'num_history' not in st.session_state: st.session_state.num_history = []
if 'wins' not in st.session_state: st.session_state.wins = 0
if 'losses' not in st.session_state: st.session_state.losses = 0
if 'last_prediction_bs' not in st.session_state: st.session_state.last_prediction_bs = None
if 'last_predicted_numbers' not in st.session_state: st.session_state.last_predicted_numbers = []
if 'wallet_balance' not in st.session_state: st.session_state.wallet_balance = 5000
if 'current_level' not in st.session_state: st.session_state.current_level = 1
if 'is_skip' not in st.session_state: st.session_state.is_skip = False

wallet_input = st.text_input("Wallet Balance (₹):", value=str(st.session_state.wallet_balance))
if wallet_input.isdigit():
    if int(wallet_input) > 0: st.session_state.wallet_balance = int(wallet_input)

st.markdown(f"""
    <div class="metric-container">
        <div class="metric-box">
            <div style="color: #FFD700; font-weight: bold; font-size: 14px;">WINS 🟢</div>
            <div style="font-size: 20px; font-weight: bold;">{st.session_state.wins}</div>
        </div>
        <div class="metric-box">
            <div style="color: #FFD700; font-weight: bold; font-size: 14px;">LOSSES 🔴</div>
            <div style="font-size: 20px; font-weight: bold;">{st.session_state.losses}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

if st.button("🔄 Reset Data", use_container_width=True):
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.last_prediction_bs = None
    st.session_state.current_level = 1
    st.session_state.is_skip = False
    st.rerun()

def handle_number_click(val):
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"
    status_str = "<span>➖ START</span>"
    
    if st.session_state.last_prediction_bs is not None:
        if not st.session_state.is_skip:
            if current_bs_short == st.session_state.last_prediction_bs:
                st.session_state.wins += 1
                status_str = "<span style='color:#00E676; font-weight:bold;'>🟢 WIN</span>"
                st.session_state.current_level = 1
            else:
                st.session_state.losses += 1
                status_str = "<span style='color:#FF5252; font-weight:bold;'>🔴 LOSS</span>"
                st.session_state.current_level = st.session_state.current_level + 1 if st.session_state.current_level < 8 else 1
        else:
            status_str = "<span style='color:#38BDF8; font-weight:bold;'>🔄 SKIPPED</span>"

    st.session_state.history.append(current_bs_short)
    st.session_state.num_history.append(val)
    st.session_state.history_details.insert(0, {"num": val, "type": current_bs, "status": status_str})

    hist = st.session_state.history
    num_hist = st.session_state.num_history

    if len(hist) >= 3:
        st.session_state.last_prediction_bs = "B" if hist[-1] == "S" else "S"
        st.session_state.last_predicted_numbers = [n for n, c in collections.Counter(num_hist[-12:]).most_common(2)]

st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; margin-top: 15px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)

# 0 to 4 buttons row
cols1 = st.columns(5)
for idx, num_val in enumerate(range(5)):
    with cols1[idx]:
        if st.button(str(num_val), key=f"btn_{num_val}", use_container_width=True):
            handle_number_click(num_val)
            st.rerun()

# 5 to 9 buttons row
cols2 = st.columns(5)
for idx, num_val in enumerate(range(5, 10)):
    with cols2[idx]:
        if st.button(str(num_val), key=f"btn_{num_val}", use_container_width=True):
            handle_number_click(num_val)
            st.rerun()

if st.session_state.last_prediction_bs is not None:
    pred_text = "BIG 🟢" if st.session_state.last_prediction_bs == "B" else "SMALL 🔴"
    base_unit = st.session_state.wallet_balance / 255
    multipliers = [1, 2, 4, 8, 16, 32, 64, 128]
    suggested_bet = max(1, round(base_unit * multipliers[st.session_state.current_level - 1]))

    st.markdown(f"""
        <div class="pred-card">
            <div style="font-size: 14px; color: #94A3B8; font-weight: bold;">NEXT PREDICTION</div>
            <div style="font-size: 24px; font-weight: bold; color: #00E676; margin: 5px 0;">{pred_text}</div>
            <div style="font-size: 13px; color: #38BDF8;">Level {st.session_state.current_level}/8 | Bet: ₹{suggested_bet}</div>
        </div>
    """, unsafe_allow_html=True)

if st.session_state.history_details:
    st.markdown("<h4 style='color:#FFD700; font-size: 16px;'>History Logs</h4>", unsafe_allow_html=True)
    for item in st.session_state.history_details[:5]:
        st.markdown(f"""
            <div class="history-card">
                <span>Num: {item['num']} ({item['type']})</span>
                <span>{item['status']}</span>
            </div>
        """, unsafe_allow_html=True)
        
