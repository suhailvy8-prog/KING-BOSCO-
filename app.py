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

# ----------------- SESSION STATES FOR ACCESS & KEYS -----------------
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["target123", "boscotarget"]
    
if 'active_sessions' not in st.session_state:
    st.session_state.active_sessions = {}

if 'auth_type' not in st.session_state:
    st.session_state.auth_type = None  # Can be 'user', 'target', or 'admin'
if 'logged_in_key' not in st.session_state:
    st.session_state.logged_in_key = None

# User Session States
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

# Target Session States
if 'target_history_details' not in st.session_state:
    st.session_state.target_history_details = []
if 'target_history' not in st.session_state:
    st.session_state.target_history = []
if 'target_num_history' not in st.session_state:
    st.session_state.target_num_history = []
if 'target_wins' not in st.session_state:
    st.session_state.target_wins = 0
if 'target_losses' not in st.session_state:
    st.session_state.target_losses = 0
if 'target_last_prediction_bs' not in st.session_state:
    st.session_state.target_last_prediction_bs = None
if 'target_last_predicted_numbers' not in st.session_state:
    st.session_state.target_last_predicted_numbers = []
if 'target_wallet_balance' not in st.session_state:
    st.session_state.target_wallet_balance = 500
if 'target_current_level' not in st.session_state:
    st.session_state.target_current_level = 1
if 'target_is_skip' not in st.session_state:
    st.session_state.target_is_skip = False

if 'client_session_id' not in st.session_state:
    st.session_state.client_session_id = str(uuid.uuid4())

if st.session_state.logged_in_key and st.session_state.auth_type in ["user", "target"]:
    current_key = st.session_state.logged_in_key
    if st.session_state.active_sessions.get(current_key) != st.session_state.client_session_id:
        st.session_state.auth_type = None
        st.session_state.logged_in_key = None
        st.warning("⚠️ ഈ കീ ഇപ്പോൾ മറ്റൊരു ഡിവൈസിൽ ഉപയോഗത്തിലാണ്! അതിനാൽ ഇവിടെ നിന്ന് ലോഗ് ഔട്ട് ആയിരിക്കുന്നു.")

# ----------------- FIRST STEP: ACCESS / LOGIN SCREEN -----------------
if st.session_state.auth_type is None:
    st.markdown("<div class='pred-card'>", unsafe_allow_html=True)
    st.markdown("<h3>🔐 ആക്സസ് ടൈപ്പ് തിരഞ്ഞെടുക്കുക</h3>", unsafe_allow_html=True)
    
    login_option = st.selectbox("ലോഗിൻ വിഭാഗം തിരഞ്ഞെടുക്കുക:", ["-- Select --", "User Login", "Target Login", "Admin Login"])
    
    if login_option == "User Login":
        user_input_key = st.text_input("User Access Key നൽകുക:", type="password")
        if st.button("Login as User", use_container_width=True):
            if user_input_key in st.session_state.allowed_keys:
                if user_input_key in st.session_state.active_sessions and st.session_state.active_sessions[user_input_key] != st.session_state.client_session_id:
                    st.error("❌ ഈ കീ നിലവിൽ വേറെയൊരു ഫോണിൽ ആക്ടീവ് ആണ്!")
                else:
                    st.session_state.active_sessions[user_input_key] = st.session_state.client_session_id
                    st.session_state.auth_type = "user"
                    st.session_state.logged_in_key = user_input_key
                    st.success("User Access Granted! ✅")
                    st.rerun()
            else:
                st.error("❌ തെറ്റായ User Key!")
                
    elif login_option == "Target Login":
        target_input_key = st.text_input("Target Access Key നൽകുക:", type="password")
        if st.button("Login as Target", use_container_width=True):
            if target_input_key in st.session_state.target_keys:
                if target_input_key in st.session_state.active_sessions and st.session_state.active_sessions[target_input_key] != st.session_state.client_session_id:
                    st.error("❌ ഈ ടാർഗറ്റ് കീ നിലവിൽ വേറെയൊരു ഫോണിൽ ആക്ടീവ് ആണ്!")
                else:
                    st.session_state.active_sessions[target_input_key] = st.session_state.client_session_id
                    st.session_state.auth_type = "target"
                    st.session_state.logged_in_key = target_input_key
                    st.success("Target Access Granted! ✅")
                    st.rerun()
            else:
                st.error("❌ തെറ്റായ Target Key!")
                
    elif login_option == "Admin Login":
        admin_input_pass = st.text_input("Admin Password നൽകുക:", type="password")
        if st.button("Login as Admin", use_container_width=True):
            if admin_input_pass == "bosco123":
                st.session_state.auth_type = "admin"
                st.success("Admin Login Success! ✅")
                st.rerun()
            else:
                st.error("❌ തെറ്റായ Admin Password!")
                
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ----------------- ADMIN PANEL -----------------
if st.session_state.auth_type == "admin":
    st.markdown("<div class='pred-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#FFD700;'>🛠️ KING BOSCO ADMIN PANEL</h2>", unsafe_allow_html=True)
    
    tab_u, tab_t = st.tabs(["👤 User Keys Management", "🎯 Target Keys Management"])
    
    with tab_u:
        st.write("<b>നിലവിലെ യൂസർ കീകൾ:</b>", unsafe_allow_html=True)
        st.write(st.session_state.allowed_keys)
        
        new_u_key = st.text_input("പുതിയ യൂസർ കീ ചേർക്കുക:")
        if st.button("Add User Key", use_container_width=True):
            if new_u_key and new_u_key not in st.session_state.allowed_keys:
                st.session_state.allowed_keys.append(new_u_key)
                st.success(f"✅ User Key '{new_u_key}' ചേർത്തു!")
                st.rerun()
                
        rem_u_key = st.selectbox("ബ്ലോക്ക് ചെയ്യേണ്ട യൂസർ കീ:", ["-- Select --"] + st.session_state.allowed_keys, key="rem_u")
        if st.button("Block/Delete User Key", use_container_width=True) and rem_u_key != "-- Select --":
            if rem_u_key in st.session_state.active_sessions:
                del st.session_state.active_sessions[rem_u_key]
            st.session_state.allowed_keys.remove(rem_u_key)
            st.success(f"🚫 User Key '{rem_u_key}' ബ്ലോക്ക് ചെയ്തു!")
            st.rerun()

    with tab_t:
        st.write("<b>നിലവിലെ ടാർഗറ്റ് കീകൾ:</b>", unsafe_allow_html=True)
        st.write(st.session_state.target_keys)
        
        new_t_key = st.text_input("പുതിയ ടാർഗറ്റ് കീ ചേർക്കുക:")
        if st.button("Add Target Key", use_container_width=True):
            if new_t_key and new_t_key not in st.session_state.target_keys:
                st.session_state.target_keys.append(new_t_key)
                st.success(f"✅ Target Key '{new_t_key}' ചേർത്തു!")
                st.rerun()
                
        rem_t_key = st.selectbox("ബ്ലോക്ക് ചെയ്യേണ്ട ടാർഗറ്റ് കീ:", ["-- Select --"] + st.session_state.target_keys, key="rem_t")
        if st.button("Block/Delete Target Key", use_container_width=True) and rem_t_key != "-- Select --":
            if rem_t_key in st.session_state.active_sessions:
                del st.session_state.active_sessions[rem_t_key]
            st.session_state.target_keys.remove(rem_t_key)
            st.success(f"🚫 Target Key '{rem_t_key}' ബ്ലോക്ക് ചെയ്തു!")
            st.rerun()

    st.write("")
    if st.button("🚪 Logout Admin", use_container_width=True):
        st.session_state.auth_type = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =========================================================================
# ----------------- 1. USER SECTION (UNTOUCHED / AS IT IS) ----------------
# =========================================================================
if st.session_state.auth_type == "user":
    col_head1, col_head2 = st.columns([4, 1])
    with col_head2:
        if st.button("🚪 Logout", key="logout_user"):
            if st.session_state.logged_in_key in st.session_state.active_sessions:
                del st.session_state.active_sessions[st.session_state.logged_in_key]
            st.session_state.auth_type = None
            st.session_state.logged_in_key = None
            st.rerun()

    st.divider()

    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 18px;'>💰 നിങ്ങളുടെ ഡെപ്പോസിറ്റ് ബാലൻസ് നൽകുക (₹):</p>", unsafe_allow_html=True)
    wallet_col1, wallet_col2, wallet_col3 = st.columns([1, 2, 1])
    with wallet_col2:
        wallet_input = st.text_input("Wallet Input", value=str(st.session_state.wallet_balance), label_visibility="collapsed", key="w_inp_user")
        if wallet_input.isdigit():
            val_w = int(wallet_input)
            if val_w > 0:
                st.session_state.wallet_balance = val_w

    st.write("")

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

    if st.button("🔄 Reset Data", use_container_width=True, key="reset_user"):
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
        if st.session_state.last_predicted_numbers:
            if val in st.session_state.last_predicted_numbers:
                num_win_str = " <span style='color:#00E676; font-size:13px; font-weight:900;'>[🎯 Number Win]</span>"

        st.session_state.history.append(current_bs_short)
        st.session_state.num_history.append(val)
        
        st.session_state.history_details.insert(0, {
            "num": val, "type": current_bs, "status": status_str, "num_win": num_win_str
        })

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

    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 18px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)

    cols_top = st.columns(5)
    nums_top = [(0, "0", "🟣 🔴"), (1, "1", "🟢"), (2, "2", "🔴"), (3, "3", "🟢"), (4, "4", "🔴")]
    for idx, (num_val, num_str, badge) in enumerate(nums_top):
        with cols_top[idx]:
            if st.button(f"{num_str}\n{badge}", key=f"btn_u_{num_val}", use_container_width=True):
                handle_number_click_user(num_val)
                st.rerun()

    cols_bottom = st.columns(5)
    nums_bottom = [(5, "5", "🟢 🟣"), (6, "6", "🔴"), (7, "7", "🟢"), (8, "8", "🔴"), (9, "9", "🟢")]
    for idx, (num_val, num_str, badge) in enumerate(nums_bottom):
        with cols_bottom[idx]:
            if st.button(f"{num_str}\n{badge}", key=f"btn_u_{num_val}", use_container_width=True):
                handle_number_click_user(num_val)
                st.rerun()

    st.write("")

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
                    🛡️ 8-Level Plan | Level {st.session_state.current_level}/8
                </div>
                <div style="color: #FFFFFF; font-size: 20px; font-weight: 900; margin-top: 4px;">
                    Suggested Bet: <span style="color: #FFD700;">₹{suggested_bet}</span>
                </div>
            </div
