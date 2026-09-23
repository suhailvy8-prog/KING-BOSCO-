import streamlit as st

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    .stApp { background-color: #0B0E14; color: #FFFFFF; }
    .app-title {
        text-align: center;
        color: #FFD700;
        font-size: 28px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
        margin-bottom: 15px;
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
    .metric-label {
        font-size: 14px !important;
        font-weight: 900 !important;
        color: #FFD700 !important;
    }
    .metric-val {
        font-size: 24px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
    }
    .stButton button {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #334155 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 45px !important;
    }
    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 18px;
        border-radius: 14px;
        border: 2px solid #FFD700;
        text-align: center;
        margin: 12px 0;
    }
    .history-card {
        background-color: #151C28;
        padding: 10px 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        border-left: 4px solid #FFD700;
        display: flex;
        justify-content: space-between;
        color: #FFFFFF;
    }
    .win-text { color: #00E676 !important; font-weight: 900 !important; }
    .loss-text { color: #FF5252 !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# Session States initialization
if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123", "arun456"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["bosco123", "target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["bosco123"]
if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

# Authentication Screen
if st.session_state.auth_role is None:
    st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
    st.markdown("### 🔐 ആക്സസ് തിരഞ്ഞെടുക്കുക")
    tab1, tab2, tab3 = st.tabs(["👤 User Access", "🎯 Target Access", "🛠️ Admin Access"])
    
    with tab1:
        u_key_input = st.text_input("User Key", type="password", key="u_key_in")
        if st.button("Login as User", use_container_width=True):
            if u_key_input in st.session_state.user_keys:
                st.session_state.auth_role = 'user'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ യൂസർ കീ!")

    with tab2:
        t_key_input = st.text_input("Target Key", type="password", key="t_key_in")
        if st.button("Login as Target", use_container_width=True):
            if t_key_input in st.session_state.target_keys:
                st.session_state.auth_role = 'target'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ ടാർഗറ്റ് കീ!")

    with tab3:
        a_key_input = st.text_input("Admin Key", type="password", key="a_key_in")
        if st.button("Login as Admin", use_container_width=True):
            if a_key_input in st.session_state.admin_keys:
                st.session_state.auth_role = 'admin'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ അഡ്മിൻ പാസ്‌വേഡ്!")
    st.stop()

# Top Bar with Title and Small Logout Door Icon
col_title, col_logout = st.columns([0.85, 0.15])
with col_title:
    st.markdown("<div class='app-title' style='text-align: left; margin-bottom: 0;'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
with col_logout:
    if st.button("🚪", help="Logout", use_container_width=True):
        st.session_state.auth_role = None
        st.rerun()

st.divider()

# ================= ADMIN SECTION =================
if st.session_state.auth_role == 'admin':
    st.markdown("<h2>🛠️ Admin Control Panel</h2>", unsafe_allow_html=True)
    
    st.markdown("### 👤 User Keys Management")
    new_u_key = st.text_input("New User Key Add ചെയ്യുക", key="new_u")
    if st.button("Add User Key"):
        if new_u_key and new_u_key not in st.session_state.user_keys:
            st.session_state.user_keys.append(new_u_key)
            st.success(f"User key '{new_u_key}' successfully added!")
            st.rerun()
            
    st.write("നിലവിലുള്ള User Keys:", st.session_state.user_keys)
    del_u_key = st.selectbox("ബ്ലോക്ക്/ഡിലീറ്റ് ചെയ്യേണ്ട User Key തിരഞ്ഞെടുക്കുക", ["--Select--"] + st.session_state.user_keys, key="del_u")
    if st.button("Remove User Key") and del_u_key != "--Select--":
        st.session_state.user_keys.remove(del_u_key)
        st.success(f"User key '{del_u_key}' removed!")
        st.rerun()

    st.markdown("---")
    st.markdown("### 🎯 Target Keys Management")
    new_t_key = st.text_input("New Target Key Add ചെയ്യുക", key="new_t")
    if st.button("Add Target Key"):
        if new_t_key and new_t_key not in st.session_state.target_keys:
            st.session_state.target_keys.append(new_t_key)
            st.success(f"Target key '{new_t_key}' successfully added!")
            st.rerun()
            
    st.write("നിലവിലുള്ള Target Keys:", st.session_state.target_keys)
    del_t_key = st.selectbox("ബ്ലോക്ക്/ഡിലീറ്റ് ചെയ്യേണ്ട Target Key തിരഞ്ഞെടുക്കുക", ["--Select--"] + st.session_state.target_keys, key="del_t")
    if st.button("Remove Target Key") and del_t_key != "--Select--":
        st.session_state.target_keys.remove(del_t_key)
        st.success(f"Target key '{del_t_key}' removed!")
        st.rerun()

# ================= TARGET SECTION =================
elif st.session_state.auth_role == 'target':
    st.markdown("<h2>🎯 Target Profit & Wallet Tracker</h2>", unsafe_allow_html=True)
    
    if 'target_wallet' not in st.session_state: st.session_state.target_wallet = 500
    if 'target_level' not in st.session_state: st.session_state.target_level = 1
    if 'target_wins' not in st.session_state: st.session_state.target_wins = 0
    if 'target_losses' not in st.session_state: st.session_state.target_losses = 0
    if 'target_history' not in st.session_state: st.session_state.target_history = []
    if 'target_history_details' not in st.session_state: st.session_state.target_history_details = []
    if 'target_pred' not in st.session_state: st.session_state.target_pred = None

    # Wallet Display Box (Big & Stylish)
    st.markdown(f"""
        <div class='metric-container'>
            <div class='metric-box'>
                <div class='metric-label'>WALLET BALANCE</div>
                <div class='metric-val'>₹ {st.session_state.target_wallet}</div>
            </div>
            <div class='metric-box'>
                <div class='metric-label'>CURRENT LEVEL</div>
                <div class='metric-val'>Lvl {st.session_state.target_level}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"**Wins:** <span style='color:#00E676; font-weight:bold;'>{st.session_state.target_wins}</span> | **Losses:** <span style='color:#FF5252; font-weight:bold;'>{st.session_state.target_losses}</span>", unsafe_allow_html=True)

    # Next Prediction Display Card
    pred_display = st.session_state.target_pred if st.session_state.target_pred else "WAITING..."
    pred_full = "BIG (5-9)" if pred_display == "B" else ("SMALL (0-4)" if pred_display == "S" else "WAITING FOR 3 INPUTS")
    st.markdown(f"""
        <div class='pred-card'>
            <div style='font-size: 14px; color: #FFD700; font-weight: bold;'>NEXT PREDICTION</div>
            <div style='font-size: 28px; font-weight: 900; color: #FFFFFF;'>{pred_full}</div>
        </div>
    """, unsafe_allow_html=True)

    def handle_target_click(val):
        cb = "BIG" if val >= 5 else "SMALL"
        cbs = "B" if val >= 5 else "S"
        base = st.session_state.target_wallet / 255
        mults = [1, 2, 4, 8, 16, 32, 64, 128]
        bet = max(1, round(base * mults[st.session_state.target_level - 1]))

        status = "➖ START"
        if st.session_state.target_pred is not None:
            if cbs == st.session_state.target_pred:
                st.session_state.target_wins += 1
                status = "🟢 WIN"
                st.session_state.target_wallet += bet
                st.session_state.target_level = 1
            else:
                st.session_state.target_losses += 1
                status = "🔴 LOSS"
                st.session_state.target_wallet = max(100, st.session_state.target_wallet - bet)
                st.session_state.target_level = st.session_state.target_level + 1 if st.session_state.target_level < 8 else 1

        st.session_state.target_history.append(cbs)
        st.session_state.target_history_details.insert(0, {"num": val, "type": cb, "status": status})
        th = st.session_state.target_history

        if len(th) >= 3:
            st.session_state.target_pred = "S" if th[-1] == "B" else "B"
        else:
            st.session_state.target_pred = None

    st.markdown("### ቁഖ്യകൾ തിരഞ്ഞെടുക്കുക (0-9)")
    cols = st.columns(2)
    nums = [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9")]
    for i, (n, label) in enumerate(nums):
        with cols[i % 2]:
            if st.button(label, key=f"t_{n}", use_container_width=True):
                handle_target_click(n)
                st.rerun()

    # History Display
    st.markdown("### 📊 ഹിസ്റ്ററി")
    if st.session_state.target_history_details:
        for item in st.session_state.target_history_details[:10]:
            st_color = "win-text" if "WIN" in item['status'] else ("loss-text" if "LOSS" in item['status'] else "")
            st.markdown(f"""
                <div class='history-card'>
                    <div>നമ്പർ: <b>{item['num']}</b> ({item['type']})</div>
                    <div class='{st_color}'>{item['status']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("ഇതുവരെ ഹിസ്റ്ററി ഒന്നുമില്ല.")

# ================= USER SECTION =================
elif st.session_state.auth_role == 'user':
    st.markdown("<h2>👑 King Bosco Predictor</h2>", unsafe_allow_html=True)
    
    if 'history' not in st.session_state: st.session_state.history = []
    if 'wins' not in st.session_state: st.session_state.wins = 0
    if 'losses' not in st.session_state: st.session_state.losses = 0
    if 'last_pred' not in st.session_state: st.session_state.last_pred = None

    st.markdown(f"**Wins:** {st.session_state.wins} | **Losses:** {st.session_state.losses}")

    def handle_click(val):
        cbs = "B" if val >= 5 else "S"
        if st.session_state.last_pred:
            if cbs == st.session_state.last_pred:
                st.session_state.wins += 1
            else:
                st.session_state.losses += 1
        st.session_state.history.append(cbs)
        if len(st.session_state.history) >= 3:
            st.session_state.last_pred = "S" if st.session_state.history[-1] == "B" else "B"

    cols = st.columns(2)
    for n in range(10):
        with cols[n % 2]:
            if st.button(str(n), key=f"u_{n}", use_container_width=True):
                handle_click(n)
                st.rerun()
                
    if st.session_state.last_pred:
        st.success(f"Prediction: {st.session_state.last_pred}")
        
