import streamlit as st
import collections
import uuid

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# Custom CSS for Vibrant & Colorful UI Styling
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #07090E, #111827); }
    .stApp { background: linear-gradient(135deg, #07090E, #111827); color: #FFFFFF; }
    
    .app-title {
        text-align: center;
        background: linear-gradient(90deg, #FFD700, #FF4500, #00E676, #38BDF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 38px !important;
        font-weight: 900 !important;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
        text-shadow: 0px 4px 20px rgba(255, 215, 0, 0.4);
    }

    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin: 20px 0;
    }
    .metric-box {
        flex: 1;
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 2px solid #3B82F6;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(59, 130, 246, 0.25);
    }
    .metric-label {
        font-size: 16px !important;
        font-weight: 900 !important;
        color: #38BDF8 !important;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    .metric-val {
        font-size: 34px !important;
        font-weight: 900 !important;
        color: #00E676 !important;
        text-shadow: 0px 0px 10px rgba(0, 230, 118, 0.4);
    }

    .stButton button {
        background: linear-gradient(135deg, #1E293B, #334155) !important;
        color: #FFFFFF !important;
        border: 2px solid #FFD700 !important;
        font-weight: bold !important;
        border-radius: 14px !important;
        height: 55px !important;
        font-size: 18px !important;
        box-shadow: 0px 4px 15px rgba(255, 215, 0, 0.2);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #334155, #1E293B) !important;
        border-color: #00E676 !important;
        color: #00E676 !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(0, 230, 118, 0.4);
    }

    input[type="text"], input[type="password"] {
        text-align: center !important;
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #1E293B !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 12px !important;
    }

    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 25px;
        border-radius: 20px;
        border: 3px solid #FFD700;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0px 10px 30px rgba(255, 215, 0, 0.3);
    }

    .history-card {
        background: linear-gradient(135deg, #151C28, #1E293B);
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 12px;
        border-left: 6px solid #FFD700;
        border-right: 2px solid #334155;
        border-top: 2px solid #334155;
        border-bottom: 2px solid #334155;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #FFFFFF;
        font-size: 17px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.4);
    }
    
    .win-text {
        color: #00E676 !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 8px rgba(0, 230, 118, 0.5);
    }

    .loss-text {
        color: #FF5252 !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 8px rgba(255, 82, 82, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR 👑</div>", unsafe_allow_html=True)

# ----------------- SESSION STATES -----------------
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]
if 'active_sessions' not in st.session_state:
    st.session_state.active_sessions = {}
if 'auth_type' not in st.session_state:
    st.session_state.auth_type = None
if 'logged_in_key' not in st.session_state:
    st.session_state.logged_in_key = None

# User States
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

if 'client_session_id' not in st.session_state:
    st.session_state.client_session_id = str(uuid.uuid4())

# ----------------- FUNCTIONS -----------------
def handle_number_click_user(val):
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"
    status_str = "<span style='color:#38BDF8; font-weight:bold;'>➖ START</span>"
    
    if st.session_state.last_prediction_bs is not None:
        if not st.session_state.is_skip:
            if current_bs_short == st.session_state.last_prediction_bs:
                st.session_state.wins += 1
                status_str = "<span class='win-text'>🟢 WIN</span>"
                st.session_state.current_level = 1  
            else:
                st.session_state.losses += 1
                status_str = "<span class='loss-text'>🔴 LOSS</span>"
                if st.session_state.current_level < 8:
                    st.session_state.current_level += 1  
                else:
                    st.session_state.current_level = 1  
        else:
            status_str = "<span style='color:#FFD700; font-weight:bold;'>🔄 SKIPPED</span>"

    num_win_str = ""
    if st.session_state.last_predicted_numbers and val in st.session_state.last_predicted_numbers:
        num_win_str = " <span style='color:#00E676; font-size:13px; font-weight:900;'>[🎯 Number Win]</span>"

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
        is_choppy = len(recent_four) == 4 and recent_four[0] != recent_four[1] and recent_four[1] != recent_four[2] and recent_four[2] != recent_four[3]
        is_heavy_repeat = len(hist) >= 3 and hist[-1] == hist[-2] == hist[-3]

        if is_choppy and st.session_state.current_level == 1 and len(hist) % 2 == 0:
            st.session_state.is_skip = True
        else:
            st.session_state.is_skip = False

        is_alternating = len(hist) >= 4 and hist[-1] != hist[-2] != hist[-3] != hist[-4]
        if is_alternating:
            next_pred = "S" if hist[-1] == "B" else "B"
        elif is_heavy_repeat:
            next_pred = "S" if (hist[-1] == "B" and st.session_state.current_level >= 3) else ("B" if st.session_state.current_level >= 3 else hist[-1])
        else:
            recent_window = hist[-6:] if len(hist) >= 6 else hist
            b_count = recent_window.count('B')
            s_count = recent_window.count('S')
            next_pred = "B" if b_count > s_count else ("S" if s_count > b_count else ("S" if hist[-1] == "B" else "B"))

        st.session_state.last_prediction_bs = next_pred
        num_counts = collections.Counter(num_hist[-12:])
        st.session_state.last_predicted_numbers = [n for n, c in num_counts.most_common(2)]

# ----------------- LOGIN SCREEN -----------------
if st.session_state.auth_type is None:
    st.markdown("<div class='pred-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #FFD700;'>🔐 ആക്സസ് ടൈപ്പ് തിരഞ്ഞെടുക്കുക</h3>", unsafe_allow_html=True)
    
    login_option = st.selectbox("ലോഗിൻ വിഭാഗം തിരഞ്ഞെടുക്കുക:", ["-- Select --", "User Login", "Admin Login"])
    
    if login_option == "User Login":
        user_input_key = st.text_input("User Access Key നൽകുക:", type="password")
        if st.button("Login as User", use_container_width=True):
            if user_input_key in st.session_state.allowed_keys:
                st.session_state.auth_type = "user"
                st.session_state.logged_in_key = user_input_key
                st.rerun()
            else:
                st.error("❌ തെറ്റായ User Key!")
                
    elif login_option == "Admin Login":
        admin_input_pass = st.text_input("Admin Password നൽകുക:", type="password")
        if st.button("Login as Admin", use_container_width=True):
            if admin_input_pass == "bosco123":
                st.session_state.auth_type = "admin"
                st.rerun()
            else:
                st.error("❌ തെറ്റായ Admin Password!")
                
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ----------------- ADMIN PANEL -----------------
if st.session_state.auth_type == "admin":
    st.markdown("<div class='pred-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#FFD700;'>🛠️ ADMIN PANEL</h2>", unsafe_allow_html=True)
    
    st.write("### 👤 Allowed User Keys")
    st.write(st.session_state.allowed_keys)
    new_u = st.text_input("New User Key:")
    if st.button("Add User Key", use_container_width=True) and new_u:
        if new_u not in st.session_state.allowed_keys:
            st.session_state.allowed_keys.append(new_u)
            st.success("Key successfully added!")
            st.rerun()

    if st.button("🚪 Logout Admin", use_container_width=True):
        st.session_state.auth_type = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# Logout button for User
if st.session_state.auth_type == "user":
    if st.button("🚪 Logout"):
        st.session_state.auth_type = None
        st.session_state.logged_in_key = None
        st.rerun()

st.divider()

# ----------------- USER SECTION -----------------
if st.session_state.auth_type == "user":
    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 18px;'>💰 നിങ്ങളുടെ ഡെപ്പോസിറ്റ് ബാലൻസ് നൽകുക (₹):</p>", unsafe_allow_html=True)
    wallet_col1, wallet_col2, wallet_col3 = st.columns([1, 2, 1])
    with wallet_col2:
        wallet_input = st.text_input("Wallet Input", value=str(st.session_state.wallet_balance), label_visibility="collapsed", key="u_wallet_box")
        if wallet_input.isdigit() and int(wallet_input) > 0:
            st.session_state.wallet_balance = int(wallet_input)

    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-box">
                <div class="metric-label">WINS 🟢</div>
                <div class="metric-val">{st.session_state.wins}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">LOSSES 🔴</div>
                <div class="metric-val" style="color: #FF5252 !important; text-shadow: 0px 0px 10px rgba(255, 82, 82, 0.4);">{st.session_state.losses}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Reset Data", use_container_width=True, key="u_reset"):
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

    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 18px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)
    cols_top = st.columns(5)
    nums_top = [(0, "0", "🟣 🔴"), (1, "1", "🟢"), (2, "2", "🔴"), (3, "3", "🟢"), (4, "4", "🔴")]
    for idx, (num_val, num_str, badge) in enumerate(nums_top):
        with cols_top[idx]:
            if st.button(f"{num_str}\n{badge}", key=f"u_btn_{num_val}", use_container_width=True):
                handle_number_click_user(num_val)
                st.rerun()

    cols_bottom = st.columns(5)
    nums_bottom = [(5, "5", "🟢 🟣"), (6, "6", "🔴"), (7, "7", "🟢"), (8, "8", "🔴"), (9, "9", "🟢")]
    for idx, (num_val, num_str, badge) in enumerate(nums_bottom):
        with cols_bottom[idx]:
            if st.button(f"{num_str}\n{badge}", key=f"u_btn_{num_val}", use_container_width=True):
                handle_number_click_user(num_val)
                st.rerun()

    if st.session_state.last_prediction_bs is not None:
        next_pred = st.session_state.last_prediction_bs
        likely_nums = st.session_state.last_predicted_numbers
        pred_text = "⚠️ SMART SKIP (ഈ റൗണ്ട് സുരക്ഷിതമായി വിടുക)" if st.session_state.is_skip else ("BIG 🟢" if next_pred == "B" else "SMALL 🔴")
        color_code = "#38BDF8" if st.session_state.is_skip else ("#00E676" if next_pred == "B" else "#FF5252")

        base_unit = st.session_state.wallet_balance / 255
        multipliers = [1, 2, 4, 8, 16, 32, 64, 128]
        suggested_bet = max(1, round(base_unit * multipliers[st.session_state.current_level - 1]))

        st.markdown(f"""
            <div class="pred-card">
                <div style="color: #38BDF8; font-size: 15px; font-weight: bold; letter-spacing: 1px;">NEXT PREDICTION</div>
                <div style="font-size: 34px; font-weight: 900; color: {color_code}; margin: 10px 0; text-shadow: 0px 0px 15px rgba(255,255,255,0.2);">{pred_text}</div>
                <div style="color: #E2E8F0; font-size: 16px; margin-bottom: 8px;">📊 Likely Numbers: <b style="color:#FFD700; font-size: 18px;">{likely_nums}</b></div>
                <hr style="border-color: #334155; margin: 12px 0;">
                <div style="color: #38BDF8; font-size: 16px; font-weight: bold;">🛡️ 8-Level Plan | Level {st.session_state.current_level}/8</div>
                <div style="color: #FFFFFF; font-size: 22px; font-weight: 900; margin-top: 6px;">Suggested Bet: <span style="color: #FFD700; text-shadow: 0px 0px 10px rgba(255,215,0,0.5);">₹{suggested_bet}</span></div>
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
            
