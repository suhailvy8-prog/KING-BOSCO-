import streamlit as st
import collections
import uuid

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

    input[type="text"], input[type="password"] {
        text-align: center !important;
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #3B82F6 !important;
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
    }

    .loss-text {
        color: #FF5252 !important;
        font-size: 18px !important;
        font-weight: 900 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)

# ----------------- SESSION STATES -----------------
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]
if 'blocked_keys' not in st.session_state:
    st.session_state.blocked_keys = []  # ബ്ലോക്ക് ചെയ്ത കീകളുടെ ലിസ്റ്റ്
if 'bound_devices' not in st.session_state:
    st.session_state.bound_devices = {}  # {key: unique_device_id}
if 'auth_type' not in st.session_state:
    st.session_state.auth_type = None
if 'logged_in_key' not in st.session_state:
    st.session_state.logged_in_key = None

if 'my_device_id' not in st.session_state:
    st.session_state.my_device_id = str(uuid.uuid4())

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

# ----------------- FUNCTIONS -----------------
def handle_number_click_user(val):
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
                if st.session_state.current_level < 8:
                    st.session_state.current_level += 1  
                else:
                    st.session_state.current_level = 1  
        else:
            status_str = "<span style='color:#38BDF8; font-weight:bold;'>🔄 SKIPPED</span>"

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
        
        recent_five = hist[-5:] if len(hist) >= 5 else hist
        is_long_streak = len(recent_five) >= 5 and all(x == recent_five[0] for x in recent_five)

        if is_choppy or is_long_streak:
            st.session_state.is_skip = True
        else:
            st.session_state.is_skip = False

        is_alternating = len(hist) >= 4 and hist[-1] != hist[-2] != hist[-3] != hist[-4]
        is_heavy_repeat = len(hist) >= 3 and hist[-1] == hist[-2] == hist[-3]

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
    st.markdown("<h3>🔐 ആക്സസ് ടൈപ്പ് തിരഞ്ഞെടുക്കുക</h3>", unsafe_allow_html=True)
    
    login_option = st.selectbox("ലോഗിൻ വിഭാഗം തിരഞ്ഞെടുക്കുക:", ["-- Select --", "User Login", "Admin Login"])
    
    if login_option == "User Login":
        user_input_key = st.text_input("User Access Key നൽകുക:", type="password")
        if st.button("Login as User", use_container_width=True):
            if user_input_key in st.session_state.blocked_keys:
                st.error("❌ ഈ കീ അഡ്മിൻ ബ്ലോക്ക് ചെയ്തിരിക്കുന്നു!")
            elif user_input_key in st.session_state.allowed_keys:
                if user_input_key in st.session_state.bound_devices:
                    if st.session_state.bound_devices[user_input_key] != st.session_state.my_device_id:
                        st.error("❌ ഈ കീ മറ്റൊരു ഡിവൈസിൽ രജിസ്റ്റർ ചെയ്തതാണ്! ഈ ഡിവൈസിൽ ഇത് വർക്ക് ചെയ്യുകയില്ല.")
                        st.stop()
                else:
                    st.session_state.bound_devices[user_input_key] = st.session_state.my_device_id

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
    
    st.write("### 👤 Allowed User Keys & Control")
    
    for key in list(st.session_state.allowed_keys):
        col_k1, col_k2, col_k3 = st.columns([2, 1, 1])
        with col_k1:
            is_blocked = key in st.session_state.blocked_keys
            status_label = "🔴 (Blocked)" if is_blocked else ("🔒 (Bound)" if key in st.session_state.bound_devices else "🔓 (Active)")
            st.write(f"🔑 `{key}` {status_label}")
        with col_k2:
            is_blocked = key in st.session_state.blocked_keys
            if is_blocked:
                if st.button("🟢 Unblock", key=f"unblock_{key}"):
                    st.session_state.blocked_keys.remove(key)
                    st.success(f"'{key}' അൺബ്ലോക്ക് ചെയ്തു!")
                    st.rerun()
            else:
                if st.button("⛔ Block", key=f"block_{key}"):
                    st.session_state.blocked_keys.append(key)
                    st.warning(f"'{key}' ബ്ലോക്ക് ചെയ്തു!")
                    st.rerun()
        with col_k3:
            if st.button("🗑️ Remove", key=f"del_{key}"):
                st.session_state.allowed_keys.remove(key)
                if key in st.session_state.bound_devices:
                    del st.session_state.bound_devices[key]
                if key in st.session_state.blocked_keys:
                    st.session_state.blocked_keys.remove(key)
                st.success(f"'{key}' നീക്കം ചെയ്തു!")
                st.rerun()

    st.divider()
    new_u = st.text_input("New User Key:")
    if st.button("Add User Key", use_container_width=True) and new_u:
        if new_u not in st.session_state.allowed_keys:
            st.session_state.allowed_keys.append(new_u)
            st.success("Key successfully added!")
            st.rerun()
        else:
            st.warning("ഈ കീ ഇതിനകം നിലവിലുണ്ട്!")

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
                <div class="metric-val">{st.session_state.losses}</div>
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
                <div style="color: #94A3B8; font-size: 14px; font-weight: bold;">NEXT PREDICTION</div>
                <div style="font-size: 32px; font-weight: 900; color: {color_code}; margin: 8px 0;">{pred_text}</div>
                <div style="color: #E2E8F0; font-size: 15px; margin-bottom: 6px;">📊 Likely Numbers: <b style="color:#FFD700;">{likely_nums}</b></div>
                <hr style="border-color: #334155; margin: 10px 0;">
                <div style="color: #38BDF8; font-size: 16px; font-weight: bold;">🛡️ 8-Level Plan | Level {st.session_state.current_level}/8</div>
                <div style="color: #FFFFFF; font-size: 20px; font-weight: 900; margin-top: 4px;">Suggested Bet: <span style="color: #FFD700;">₹{suggested_bet}</span></div>
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
            
