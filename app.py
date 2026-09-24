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

# Session States Initialization
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["bosco1234", "rahul123", "arun456", "vipin789"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["target123", "boscotarget"]
    
if 'active_sessions' not in st.session_state:
    st.session_state.active_sessions = {}

if 'auth_type' not in st.session_state:
    st.session_state.auth_type = None
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
        st.warning("⚠️ ഈ കീ ഇപ്പോൾ മറ്റൊരു ഡിവൈസിൽ ഉപയോഗത്തിലാണ്!")

# Login Screen
if st.session_state.auth_type is None:
    st.markdown("<div class='pred-card'>", unsafe_allow_html=True)
    st.markdown("<h3>🔐 ആക്സസ് ടൈപ്പ് തിരഞ്ഞെടുക്കുക</h3>", unsafe_allow_html=True)
    
    login_option = st.selectbox("ലോഗിൻ വിഭാഗം തിരഞ്ഞെടുക്കുക:", ["-- Select --", "User Login", "Target Login", "Admin Login"])
    
    if login_option == "User Login":
        user_input_key = st.text_input("User Access Key നൽകുക:", type="password")
        if st.button("Login as User", use_container_width=True):
            if user_input_key in st.session_state.allowed_keys:
                st.session_state.active_sessions[user_input_key] = st.session_state.client_session_id
                st.session_state.auth_type = "user"
                st.session_state.logged_in_key = user_input_key
                st.rerun()
            else:
                st.error("❌ തെറ്റായ User Key!")
                
    elif login_option == "Target Login":
        target_input_key = st.text_input("Target Access Key നൽകുക:", type="password")
        if st.button("Login as Target", use_container_width=True):
            if target_input_key in st.session_state.target_keys:
                st.session_state.active_sessions[target_input_key] = st.session_state.client_session_id
                st.session_state.auth_type = "target"
                st.session_state.logged_in_key = target_input_key
                st.rerun()
            else:
                st.error("❌ തെറ്റായ Target Key!")
                
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

# Admin Panel
if st.session_state.auth_type == "admin":
    st.markdown("<div class='pred-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#FFD700;'>🛠️ ADMIN PANEL</h2>", unsafe_allow_html=True)
    
    tab_u, tab_t = st.tabs(["👤 User Keys", "🎯 Target Keys"])
    
    with tab_u:
        st.write(st.session_state.allowed_keys)
        new_u = st.text_input("New User Key:")
        if st.button("Add User", use_container_width=True) and new_u:
            st.session_state.allowed_keys.append(new_u)
            st.rerun()
            
    with tab_t:
        st.write(st.session_state.target_keys)
        new_t = st.text_input("New Target Key:")
        if st.button("Add Target", use_container_width=True) and new_t:
            st.session_state.target_keys.append(new_t)
            st.rerun()

    if st.button("🚪 Logout Admin", use_container_width=True):
        st.session_state.auth_type = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# User Section (Full Featured)
if st.session_state.auth_type == "user":
    col_head1, col_head2 = st.columns([4, 1])
    with col_head2:
        if st.button("🚪 Logout", key="logout_user"):
            st.session_state.auth_type = None
            st.rerun()

    st.divider()
    wallet_input = st.text_input("Wallet Input", value=str(st.session_state.wallet_balance), key="w_inp_user")
    if wallet_input.isdigit():
        st.session_state.wallet_balance = int(wallet_input)

    st.markdown(f"**Wins:** {st.session_state.wins} | **Losses:** {st.session_state.losses}")
    
    def handle_number_click_user(val):
        curr_bs = "B" if val >= 5 else "S"
        st.session_state.history.append(curr_bs)
        st.session_state.num_history.append(val)
        st.session_state.history_details.insert(0, {"num": val, "type": "BIG" if val>=5 else "SMALL", "status": "OK"})
        if len(st.session_state.history) >= 3:
            st.session_state.last_prediction_bs = "B" if st.session_state.history[-1] == "S" else "S"

    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            if st.button(str(i), key=f"u_{i}", use_container_width=True):
                handle_number_click_user(i)
                st.rerun()

    if st.session_state.last_prediction_bs:
        st.info(f"Prediction: {st.session_state.last_prediction_bs}")

# Target Section (Enhanced with Target Requirements)
elif st.session_state.auth_type == "target":
    col_t1, col_t2 = st.columns([4, 1])
    with col_t2:
        if st.button("🚪 Logout", key="logout_target"):
            st.session_state.auth_type = None
            st.rerun()

    st.markdown("<h3 style='color: #38BDF8;'>🎯 TARGET DASHBOARD</h3>", unsafe_allow_html=True)
    st.divider()

    target_wallet_input = st.text_input("Target Wallet (Min 500):", value=str(st.session_state.target_wallet_balance), key="tw_inp")
    if target_wallet_input.isdigit():
        val_tw = int(target_wallet_input)
        if val_tw >= 500:
            st.session_state.target_wallet_balance = val_tw
        else:
            st.warning("⚠️ കുറഞ്ഞത് ₹500 എങ്കിലും നൽകുക!")

    st.markdown(f"**Wins:** {st.session_state.target_wins} | **Losses:** {st.session_state.target_losses}")

    def handle_number_click_target(val):
        curr_bs = "B" if val >= 5 else "S"
        st.session_state.target_history.append(curr_bs)
        st.session_state.target_num_history.append(val)
        st.session_state.target_history_details.insert(0, {"num": val, "type": "BIG" if val>=5 else "SMALL", "status": "OK"})
        if len(st.session_state.target_history) >= 3:
            st.session_state.target_last_prediction_bs = "B" if st.session_state.target_history[-1] == "S" else "S"

    cols_t = st.columns(5)
    for i in range(10):
        with cols_t[i % 5]:
            if st.button(str(i), key=f"t_{i}", use_container_width=True):
                handle_number_click_target(i)
                st.rerun()

    if st.session_state.target_last_prediction_bs:
        base_unit = st.session_state.target_wallet_balance / 255
        suggested_bet = max(1, round(base_unit))
        st.markdown(f"""
            <div class="pred-card">
                <div style="font-size: 24px; color: #FFD700;">Target Prediction: {st.session_state.target_last_prediction_bs}</div>
                <div>Suggested Bet: ₹{suggested_bet}</div>
            </div>
        """, unsafe_allow_html=True)
        
