import streamlit as st
import datetime
import uuid

st.set_page_config(page_title="CYBER HACK v3.0 ⚡", page_icon="💻", layout="centered")

st.markdown("""
    <style>
    .main { background: #030712; }
    .stApp { background: #030712; color: #f3f4f6; font-family: monospace; }
    
    .app-header {
        text-align: center;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 28px !important;
        font-weight: 900 !important;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }

    .prediction-card {
        background: linear-gradient(135deg, #0f172a, #1e1b4b);
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #6366f1;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0px 0px 30px rgba(99, 102, 241, 0.3);
    }

    .hack-panel {
        background: #0f172a;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #334155;
        margin: 12px 0;
    }

    .admin-box {
        background: #180d2b;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #a855f7;
        margin: 12px 0;
    }

    .success-box {
        background: #064e3b;
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #34d399;
        text-align: center;
        margin: 15px 0;
    }

    .stButton button {
        background: #0f172a !important;
        color: #38bdf8 !important;
        border: 1px solid #3b82f6 !important;
        font-family: monospace !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        height: 52px !important;
        transition: all 0.25s ease;
    }
    .stButton button:hover {
        background: #3b82f6 !important;
        color: #030712 !important;
        box-shadow: 0px 0px 20px rgba(59, 130, 246, 0.6);
    }

    input[type="text"], input[type="password"] {
        text-align: center !important;
        font-size: 18px !important;
        font-family: monospace !important;
        background-color: #0f172a !important;
        color: #38bdf8 !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 10px !important;
    }

    .stat-card {
        background: #0f172a;
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-header'>[⚡ CYBER PREDICTIVE ENGINE ⚡]</div>", unsafe_allow_html=True)

if 'allowed_keys' not in st.session_state: st.session_state.allowed_keys = ["target123", "bosco456"]
if 'blocked_keys' not in st.session_state: st.session_state.blocked_keys = []
if 'bound_devices' not in st.session_state: st.session_state.bound_devices = {}
if 'auth_type' not in st.session_state: st.session_state.auth_type = None
if 'my_device_id' not in st.session_state: st.session_state.my_device_id = str(uuid.uuid4())

current_date_str = datetime.date.today().isoformat()
if 'last_reset_date' not in st.session_state: st.session_state.last_reset_date = current_date_str
if st.session_state.last_reset_date != current_date_str:
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.wallet_balance = 500
    st.session_state.initial_wallet = 500
    st.session_state.double_level = 1
    st.session_state.target_achieved = False
    st.session_state.last_reset_date = current_date_str

if 'history_details' not in st.session_state: st.session_state.history_details = []
if 'history' not in st.session_state: st.session_state.history = []
if 'wins' not in st.session_state: st.session_state.wins = 0
if 'losses' not in st.session_state: st.session_state.losses = 0
if 'initial_wallet' not in st.session_state: st.session_state.initial_wallet = 500
if 'wallet_balance' not in st.session_state: st.session_state.wallet_balance = 500
if 'double_level' not in st.session_state: st.session_state.double_level = 1
if 'target_achieved' not in st.session_state: st.session_state.target_achieved = False
    if st.session_state.auth_type is None:
    st.markdown("<div class='hack-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#38bdf8; text-align:center;'>🔐 SECURE TERMINAL LOGIN</h3>", unsafe_allow_html=True)
    
    login_option = st.selectbox("Select Auth Mode:", ["-- Select --", "User Access Key", "Admin Panel"])
    
    if login_option == "User Access Key":
        user_key = st.text_input("Enter Access Key:", type="password")
        if st.button("Authenticate User", use_container_width=True):
            if user_key in st.session_state.blocked_keys:
                st.error("[-] Access Denied: Key Blocked.")
            elif user_key in st.session_state.allowed_keys:
                if user_key in st.session_state.bound_devices and st.session_state.bound_devices[user_key] != st.session_state.my_device_id:
                    st.error("[-] Security Error: Key bound to another device.")
                    st.stop()
                st.session_state.bound_devices[user_key] = st.session_state.my_device_id
                st.session_state.auth_type = "user"
                st.rerun()
            else:
                st.error("[-] Invalid Access Key.")
                
    elif login_option == "Admin Panel":
        admin_pass = st.text_input("Enter Admin Password:", type="password")
        if st.button("Authenticate Admin", use_container_width=True):
            if admin_pass == "bosco123":
                st.session_state.auth_type = "admin"
                st.rerun()
            else:
                st.error("[-] Invalid Admin Password.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

if st.session_state.auth_type == "admin":
    st.markdown("<div class='admin-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#c084fc; text-align:center;'>🛠️ ADMIN COMMAND CENTER</h3>", unsafe_allow_html=True)
    for key in list(st.session_state.allowed_keys):
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: st.write(f"🔑 `{key}`")
        with c2:
            if key in st.session_state.blocked_keys:
                if st.button("Unblock", key=f"un_{key}"): st.session_state.blocked_keys.remove(key); st.rerun()
            else:
                if st.button("Block", key=f"bl_{key}"): st.session_state.blocked_keys.append(key); st.rerun()
        with c3:
            if st.button("Del", key=f"dl_{key}"): st.session_state.allowed_keys.remove(key); st.rerun()
    
    new_k = st.text_input("Add New Key:")
    if st.button("Inject Key", use_container_width=True) and new_k:
        if new_k not in st.session_state.allowed_keys: st.session_state.allowed_keys.append(new_k); st.rerun()
    
    if st.button("Logout Admin", use_container_width=True): st.session_state.auth_type = None; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

if st.session_state.auth_type == "user":
    if st.button("🚪 Terminate Session (Logout)"): st.session_state.auth_type = None; st.rerun()

st.divider()
def handle_number_click(val):
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"
    
    base_bet = 1
    opposite_bet = 2 * (2 ** (st.session_state.double_level - 1))
    total_investment = base_bet + opposite_bet
    
    is_opposite_win = True if val % 2 != 0 else False
    
    if is_opposite_win:
        st.session_state.wins += 1
        profit = opposite_bet - base_bet
        st.session_state.wallet_balance += profit
        net_change_str = f"<span style='color:#34d399; font-weight:bold;'>WIN (+₹{profit}) [{current_bs}]</span>"
        st.session_state.double_level = 1
    else:
        st.session_state.losses += 1
        st.session_state.wallet_balance -= total_investment
        net_change_str = f"<span style='color:#f87171; font-weight:bold;'>LOSS (-₹{total_investment}) [{current_bs}]</span>"
        if st.session_state.double_level < 8:
            st.session_state.double_level += 1
        else:
            st.session_state.double_level = 1

    profit_target = int(st.session_state.initial_wallet * 0.20)
    if st.session_state.wallet_balance >= (st.session_state.initial_wallet + profit_target):
        st.session_state.target_achieved = True

    st.session_state.history.append(current_bs_short)
    st.session_state.history_details.insert(0, {"num": val, "type": current_bs, "status": net_change_str})

if st.session_state.target_achieved:
    st.balloons()
    earned = int(st.session_state.initial_wallet * 0.20)
    st.markdown(f"""
        <div class='success-box'>
            <h2 style='color: #d1fae5;'>[+] TARGET PROFIT SECURED!</h2>
            <p>Initial: ₹{st.session_state.initial_wallet} | Profit: +₹{earned}</p>
            <p style='font-size: 20px; font-weight: bold;'>Final Balance: ₹{st.session_state.wallet_balance}</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 Restart Terminal Session", use_container_width=True):
        st.session_state.target_achieved = False
        st.session_state.history_details = []
        st.session_state.history = []
        st.session_state.wins = 0
        st.session_state.losses = 0
        st.session_state.double_level = 1
        st.rerun()
    st.stop()

st.markdown("<p style='text-align: center; color: #38bdf8;'>💰 WALLET CONFIGURATION (₹)</p>", unsafe_allow_html=True)
col_w1, col_w2, col_w3 = st.columns([1, 2, 1])
with col_w2:
    def update_w():
        w_str = st.session_state.w_input
        if w_str.isdigit() and int(w_str) >= 100:
            st.session_state.initial_wallet = int(w_str)
            st.session_state.wallet_balance = int(w_str)
    st.text_input("Wallet", value=str(st.session_state.wallet_balance), label_visibility="collapsed", key="w_input", on_change=update_w)

target_goal = st.session_state.initial_wallet + int(st.session_state.initial_wallet * 0.20)

st.markdown("<br>", unsafe_allow_html=True)
stat_c1, stat_c2 = st.columns(2)
with stat_c1:
    st.markdown(f"""
        <div class='stat-card' style='border-color: #34d399;'>
            <div style='color: #94a3b8; font-size: 13px;'>TOTAL WINS</div>
            <div style='color: #34d399; font-size: 26px; font-weight: bold;'>{st.session_state.wins} 🟢</div>
        </div>
    """, unsafe_allow_html=True)
with stat_c2:
    st.markdown(f"""
        <div class='stat-card' style='border-color: #f87171;'>
            <div style='color: #94a3b8; font-size: 13px;'>TOTAL LOSSES</div>
            <div style='color: #f87171; font-size: 26px; font-weight: bold;'>{st.session_state.losses} 🔴</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <div style='background: #0f172a; border: 1px solid #334155; padding: 12px; border-radius: 10px; text-align: center; margin-top: 12px;'>
        <span style='color: #94a3b8;'>Balance:</span> <b style='color: #34d399;'>₹{st.session_state.wallet_balance}</b> &nbsp;|&nbsp; 
        <span style='color: #94a3b8;'>Target:</span> <b style='color: #38bdf8;'>₹{target_goal}</b>
    </div>
""", unsafe_allow_html=True)

if st.button("🔄 System Manual Reset", use_container_width=True):
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.double_level = 1
    st.rerun()

st.divider()

curr_opposite = 2 * (2 ** (st.session_state.double_level - 1))
last_result = st.session_state.history[-1] if st.session_state.history else "B"

if last_result == "B":
    pred_display = f"ബിഗ് - 1 &nbsp;|&nbsp; സ്മോൾ - {curr_opposite}"
else:
    pred_display = f"സ്മോൾ - 1 &nbsp;|&nbsp; ബിഗ് - {curr_opposite}"

st.markdown(f"""
    <div class='prediction-card'>
        <div style='color: #94a3b8; font-size: 13px; margin-bottom: 8px; letter-spacing: 1px;'>🎯 NEXT PREDICTION SIGNAL</div>
        <div style='color: #f8fafc; font-size: 24px; font-weight: 900; margin: 12px 0; text-transform: uppercase;'>{pred_display}</div>
        <div style='color: #38bdf8; font-size: 13px; margin-top: 8px;'>ട്രെൻഡ് അനുസരിച്ച് തുക കൃത്യമായി ഫോളോ ചെയ്യുക</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #38bdf8;'>INPUT RECENT RESULT NUMBER:</p>", unsafe_allow_html=True)
top_cols = st.columns(5)
for i, (n, b) in enumerate([(0, "🟣🔴"), (1, "🟢"), (2, "🔴"), (3, "🟢"), (4, "🔴")]):
    with top_cols[i]:
        if st.button(f"{n}\n{b}", key=f"b_{n}", use_container_width=True): handle_number_click(n); st.rerun()

bot_cols = st.columns(5)
for i, (n, b) in enumerate([(5, "🟢🟣"), (6, "🔴"), (7, "🟢"), (8, "🔴"), (9, "🟢")]):
    with bot_cols[i]:
        if st.button(f"{n}\n{b}", key=f"b_{n}", use_container_width=True): handle_number_click(n); st.rerun()

st.markdown("<h3 style='color: #38bdf8; text-align: center; font-size: 16px; margin-top: 25px;'>[ EXECUTION HISTORY ]</h3>", unsafe_allow_html=True)
if not st.session_state.history_details:
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px;'>No logs recorded.</p>", unsafe_allow_html=True)
else:
    for item in st.session_state.history_details[:8]:
        st.markdown(f"""
            <div style='background: #0f172a; border-left: 3px solid #6366f1; padding: 10px 14px; border-radius: 8px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center;'>
                <span style='color: #e2e8f0;'>Num: <b>{item['num']}</b> ({item['type']})</span>
                <span>{item['status']}</span>
            </div>
        """, unsafe_allow_html=True)
        
