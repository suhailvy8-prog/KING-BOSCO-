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

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)

if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123", "arun456"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["bosco123", "target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["bosco123"]
if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

if st.session_state.auth_role is None:
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

if st.button("🚪 Logout"):
    st.session_state.auth_role = None
    st.rerun()

st.divider()

if st.session_state.auth_role == 'admin':
    st.markdown("<h2>🛠️ Admin Control Panel</h2>", unsafe_allow_html=True)
    st.write("👤 User Keys:", st.session_state.user_keys)
    st.write("🎯 Target Keys:", st.session_state.target_keys)
    st.stop()

elif st.session_state.auth_role == 'target':
    st.markdown("<h2 style='text-align: center;'>🎯 Target Profit & Wallet Tracker</h2>", unsafe_allow_html=True)
    if 'target_wallet' not in st.session_state: st.session_state.target_wallet = 500
    if 'target_level' not in st.session_state: st.session_state.target_level = 1
    if 'target_wins' not in st.session_state: st.session_state.target_wins = 0
    if 'target_losses' not in st.session_state: st.session_state.target_losses = 0
    if 'target_history' not in st.session_state: st.session_state.target_history = []
    if 'target_history_details' not in st.session_state: st.session_state.target_history_details = []
    if 'target_pred' not in st.session_state: st.session_state.target_pred = None
    if 'target_is_skip' not in st.session_state: st.session_state.target_is_skip = False

    tw = st.text_input("Wallet Balance (Min 500):", value=str(st.session_state.target_wallet))
    if tw.isdigit() and int(tw) >= 500:
        st.session_state.target_wallet = int(tw)

    st.markdown(f"**Wins:** {st.session_state.target_wins} | **Losses:** {st.session_state.target_losses}")

    def handle_target_click(val):
        cb = "BIG" if val >= 5 else "SMALL"
        cbs = "B" if val >= 5 else "S"
        status = "➖ START"
        base = st.session_state.target_wallet / 255
        mults = [1, 2, 4, 8, 16, 32, 64, 128]
        bet = max(1, round(base * mults[st.session_state.target_level - 1]))

        if st.session_state.target_pred is not None and not st.session_state.target_is_skip:
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

    cols = st.columns(2)
    nums = [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9")]
    for i, (n, label) in enumerate(nums):
        with cols[i % 2]:
            if st.button(label, key=f"t_{n}", use_container_width=True):
                handle_target_click(n)
                st.rerun()

    if st.session_state.target_pred:
        st.info(f"Next Prediction: {st.session_state.target_pred} | Level: {st.session_state.target_level}")
    st.stop()

if st.session_state.auth_role == 'user':
    st.markdown("<h2 style='text-align: center;'>👑 King Bosco Predictor</h2>", unsafe_allow_html=True)
    if 'history' not in st.session_state: st.session_state.history = []
    if 'wins' not in st.session_state: st.session_state.wins = 0
    if 'losses' not in st.session_state: st.session_state.losses = 0
    if 'last_pred' not in st.session_state: st.session_state.last_pred = None

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
        
