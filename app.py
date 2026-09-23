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
        font-size: 22px !important;
        font-weight: 900 !important;
        margin-bottom: 8px;
    }

    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 6px;
        margin: 6px 0;
    }
    .metric-box {
        flex: 1;
        background-color: #1E293B;
        border: 2px solid #334155;
        border-radius: 6px;
        padding: 5px;
        text-align: center;
    }
    .metric-label {
        font-size: 11px !important;
        font-weight: 900 !important;
        color: #FFD700 !important;
    }
    .metric-val {
        font-size: 18px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
    }

    input[type="text"] {
        text-align: center !important;
        font-size: 14px !important;
        font-weight: bold !important;
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #3B82F6 !important;
    }
    
    div[data-baseweb="input"] {
        background-color: #1E293B !important;
        border-radius: 6px !important;
    }

    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 10px;
        border-radius: 8px;
        border: 2px solid #FFD700;
        text-align: center;
        margin: 6px 0;
    }

    .history-card {
        background-color: #151C28;
        padding: 6px 8px;
        border-radius: 6px;
        margin-bottom: 4px;
        border-left: 3px solid #FFD700;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #FFFFFF;
        font-size: 12px;
    }
    
    .win-text { color: #00E676 !important; font-weight: 900 !important; }
    .loss-text { color: #FF5252 !important; font-weight: 900 !important; }

    /* Strict mobile fitting without horizontal scroll or vertical stacking */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 4px !important;
    }
    [data-testid="column"] {
        width: 50% !important;
        flex: 1 1 50% !important;
        min-width: 0 !important;
        max-width: 50% !important;
        padding: 0 !important;
    }
    
    /* Compact buttons to fit phone screen width perfectly */
    .stButton > button {
        width: 100% !important;
        font-size: 13px !important;
        padding: 5px 2px !important;
        border-radius: 5px !important;
        white-space: nowrap !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)

if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]

st.sidebar.title("🔐 Access Control")
user_key = st.sidebar.text_input("നിങ്ങളുടെ Access Key നൽകുക:", type="password")

st.sidebar.divider()
st.sidebar.subheader("🛠️ Admin Settings")
admin_pass = st.sidebar.text_input("Admin Password:", type="password")
admin_logged_in = (admin_pass == "bosco123")

if admin_logged_in:
    st.sidebar.success("Admin Mode Active ✅")
    st.sidebar.write(st.session_state.allowed_keys)
    new_key_to_add = st.sidebar.text_input("പുതിയ കീ ചേർക്കുക:")
    if st.sidebar.button("Add Key"):
        if new_key_to_add and new_key_to_add not in st.session_state.allowed_keys:
            st.session_state.allowed_keys.append(new_key_to_add)
            st.rerun()
    key_to_remove = st.sidebar.selectbox("ഒഴിവാക്കേണ്ട കീ:", ["-- Select --"] + st.session_state.allowed_keys)
    if st.sidebar.button("Remove Key") and key_to_remove != "-- Select --":    
        st.session_state.allowed_keys.remove(key_to_remove)
        st.rerun()

if user_key in st.session_state.allowed_keys or admin_logged_in:
    st.sidebar.success("✅ Access Granted!")
else:
    st.warning("🔒 ദയവായി ശരിയായ Access Key നൽകുക.")
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

st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 13px;'>💰 ബാലൻസ് നൽകുക (₹):</p>", unsafe_allow_html=True)
wallet_col1, wallet_col2, wallet_col3 = st.columns([1, 2, 1])
with wallet_col2:
    wallet_input = st.text_input("Wallet Input", value=str(st.session_state.wallet_balance), label_visibility="collapsed")
    if wallet_input.isdigit():
        val_w = int(wallet_input)
        if val_w > 0: st.session_state.wallet_balance = val_w

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

def handle_number_click(val):
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"
    status_str = "<span style='color:#94A3B8; font-weight:bold;'>➖ START</span>"
    
    if st.session_state.last_prediction_bs is not None:
        if not st.session_state.is_skip:
            if current_bs_short == st.session_state.last_prediction_bs:
                st.session_state.wins += 1
                status_str = "<span class='win-text'>🟢 WIN</span>"
                st.session_state.current_level = 1
            else:
                st.session_state.losses += 1
                status_str = "<span class='loss-text'>🔴 LOSS</span>"
                st.session_state.current_level = st.session_state.current_level + 1 if st.session_state.current_level < 8 else 1
        else:
            status_str = "<span style='color:#38BDF8; font-weight:bold;'>🔄 SKIPPED</span>"

    num_win_str = ""
    if st.session_state.last_predicted_numbers and val in st.session_state.last_predicted_numbers:
        num_win_str = " <span style='color:#00E676; font-size:10px; font-weight:900;'>[🎯 Win]</span>"

    st.session_state.history.append(current_bs_short)
    st.session_state.num_history.append(val)
    st.session_state.history_details.insert(0, {"num": val, "type": current_bs, "status": status_str, "num_win": num_win_str})

    hist = st.session_state.history
    num_hist = st.session_state.num_history

    if len(hist) < 3:
        st.session_state.last_prediction_bs = None
        st.session_state.last_predicted_numbers = []
        st.session_state.is_skip = False
    else:
        recent_four = hist[-4:] if len(hist) >= 4 else hist
        is_choppy = (len(recent_four) == 4 and recent_four[0] != recent_four[1] and recent_four[1] != recent_four[2] and recent_four[2] != recent_four[3])
        is_heavy_repeat = (len(hist) >= 3 and hist[-1] == hist[-2] == hist[-3])

        st.session_state.is_skip = True if (is_choppy and st.session_state.current_level == 1 and len(hist) % 2 == 0) else False

        is_alternating = (len(hist) >= 4 and hist[-1] != hist[-2] and hist[-2] != hist[-3] and hist[-3] != hist[-4]) or (len(hist) == 3 and hist[-1] != hist[-2] and hist[-2] != hist[-3])

        if is_alternating:
            next_pred = "S" if hist[-1] == "B" else "B"
        elif is_heavy_repeat:
            next_pred = "S" if (hist[-1] == "B" and st.session_state.current_level >= 3) else ("B" if st.session_state.current_level >= 3 else hist[-1])
        else:
            recent_window = hist[-6:] if len(hist) >= 6 else hist
            b_count, s_count = recent_window.count('B'), recent_window.count('S')
            next_pred = "B" if b_count > s_count else ("S" if s_count > b_count else ("S" if hist[-1] == "B" else "B"))

        st.session_state.last_prediction_bs = next_pred
        st.session_state.last_predicted_numbers = [n for n, c in collections.Counter(num_hist[-12:]).most_common(2)]

st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 13px; margin-top: 6px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)

buttons_info = [
    (0, "0 (🟣🔴)", 5, "5 (🟢🟣)"),
    (1, "1 (🟢)",   6, "6 (🔴)"),
    (2, "2 (🔴)",   7, "7 (🟢)"),
    (3, "3 (🟢)",   8, "8 (🔴)"),
    (4, "4 (🔴)",   9, "9 (🟢)")
]

for num1, label1, num2, label2 in buttons_info:
    col1, col2 = st.columns(2)
    with col1:
        if st.button(label1, key=f"btn_{num1}", use_container_width=True):
            handle_number_click(num1)
            st.rerun()
    with col2:
        if st.button(label2, key=f"btn_{num2}", use_container_width=True):
            handle_number_click(num2)
            st.rerun()

st.write("")

if st.session_state.last_prediction_bs is not None:
    next_pred = st.session_state.last_prediction_bs
    likely_nums = st.session_state.last_predicted_numbers
    pred_text = "⚠️ SMART SKIP (ഈ റൗണ്ട് വിടുക)" if st.session_state.is_skip else ("BIG 🟢" if next_pred == "B" else "SMALL 🔴")
    color_code = "#38BDF8" if st.session_state.is_skip else ("#00E676" if next_pred == "B" else "#FF5252")

    base_unit = st.session_state.wallet_balance / 255
    suggested_bet = max(1, round(base_unit * [1, 2, 4, 8, 16, 32, 64, 128][st.session_state.current_level - 1]))

    st.markdown(f"""
        <div class="pred-card">
            <div style="color: #94A3B8; font-size: 11px; font-weight: bold;">NEXT PREDICTION</div>
            <div style="font-size: 20px; font-weight: 900; color: {color_code}; margin: 2px 0;">{pred_text}</div>
            <div style="color: #E2E8F0; font-size: 12px; margin-bottom: 2px;">📊 Likely Numbers: <b style="color:#FFD700;">{likely_nums}</b></div>
            <hr style="border-color: #334155; margin: 4px 0;">
            <div style="color: #38BDF8; font-size: 11px; font-weight: bold;">🛡️ Level {st.session_state.current_level}/8</div>
            <div style="color: #FFFFFF; font-size: 14px; font-weight: 900; margin-top: 1px;">Suggested Bet: <span style="color: #FFD700;">₹{suggested_bet}</span></div>
        </div>
    """, unsafe_allow_html=True)
else:
    if len(st.session_state.history) < 3:
        st.info(f"കുറഞ്ഞത് {3 - len(st.session_state.history)} ഡാറ്റ കൂടി നൽകുക...")

st.divider()

if st.session_state.history_details:
    st.markdown("<h3 style='color:#FFD700; font-size: 14px;'>📜 History Logs</h3>", unsafe_allow_html=True)
    for item in st.session_state.history_details[:10]:
        st.markdown(f"""
            <div class="history-card">
                <span><b>Num: {item['num']}</b> ({item['type']}){item.get('num_win', '')}</span>
                <span>{item['status']}</span>
            </div>
        """, unsafe_allow_html=True)
    
