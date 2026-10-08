import streamlit as st
import datetime
import uuid

st.set_page_config(page_title="CYBER HACK v2.0 ⚡", page_icon="💻", layout="centered")

# Professional Hacking Tool Theme (Matrix Dark & Neon Green/Red)
st.markdown("""
    <style>
    .main { background: #030712; }
    .stApp { background: #030712; color: #4ade80; font-family: monospace; }
    
    .app-header {
        text-align: center;
        background: linear-gradient(90deg, #22c55e, #10b981, #065f46);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 26px !important;
        font-weight: 900 !important;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }

    .hack-panel {
        background: #0b0f19;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #22c55e;
        margin: 12px 0;
        box-shadow: 0px 0px 15px rgba(34, 197, 94, 0.15);
    }

    .skip-alert-panel {
        background: #18080a;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #ef4444;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0px 0px 20px rgba(239, 68, 68, 0.3);
    }

    .admin-box {
        background: #110c1d;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #a855f7;
        margin: 12px 0;
    }

    .success-box {
        background: #022c22;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #10b981;
        text-align: center;
        margin: 15px 0;
    }

    .stButton button {
        background: #030712 !important;
        color: #22c55e !important;
        border: 1px solid #22c55e !important;
        font-family: monospace !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        height: 48px !important;
        transition: all 0.2s ease;
    }
    .stButton button:hover {
        background: #22c55e !important;
        color: #030712 !important;
        box-shadow: 0px 0px 10px #22c55e;
    }

    input[type="text"], input[type="password"] {
        text-align: center !important;
        font-size: 16px !important;
        font-family: monospace !important;
        background-color: #0b0f19 !important;
        color: #22c55e !important;
        border: 1px solid #22c55e !important;
        border-radius: 8px !important;
    }

    .stat-card {
        background: #0b0f19;
        border: 1px solid #1f2937;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-header'>[⚡ CYBER PREDICTIVE HACK v2.0 ⚡]</div>", unsafe_allow_html=True)

# Session States
if 'allowed_keys' not in st.session_state: st.session_state.allowed_keys = ["target123", "bosco456"]
if 'blocked_keys' not in st.session_state: st.session_state.blocked_keys = []
if 'bound_devices' not in st.session_state: st.session_state.bound_devices = {}
if 'auth_type' not in st.session_state: st.session_state.auth_type = None
if 'my_device_id' not in st.session_state: st.session_state.my_device_id = str(uuid.uuid4())

# Midnight Reset Check
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
    # Login Screen
if st.session_state.auth_type is None:
    st.markdown("<div class='hack-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#22c55e; text-align:center;'>🔐 SECURE TERMINAL LOGIN</h3>", unsafe_allow_html=True)
    
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

# Admin Panel
if st.session_state.auth_type == "admin":
    st.markdown("<div class='admin-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#a855f7; text-align:center;'>🛠️ ADMIN COMMAND CENTER</h3>", unsafe_allow_html=True)
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
    
    is_skip_zone = False
    if len(st.session_state.history) >= 3:
        if all(x == current_bs_short for x in st.session_state.history[-3:]):
            is_skip_zone = True

    # Dual Betting Logic: ₹1 Fixed Bet + ₹(current_double) Double Bet
    fixed_bet = 1
    current_double_bet = 2 ** (st.session_state.double_level - 1)
    total_investment = fixed_bet + current_double_bet
    
    if is_skip_zone:
        st.session_state.losses += 1
        st.session_state.wallet_balance -= total_investment
        net_change_str = f"<span style='color:#ef4444; font-weight:bold;'>🔴 LOSS (-₹{total_investment}) [SKIPPED]</span>"
        st.session_state.double_level = 1
    else:
        # Win scenario: Fixed bet (₹1) wins, Double bet wins/recovers net profit
        net_profit = current_double_bet - fixed_bet
        st.session_state.wins += 1
        st.session_state.wallet_balance += net_profit
        net_change_str = f"<span style='color:#22c55e; font-weight:bold;'>🟢 WIN (+₹{net_profit}) [{current_bs}]</span>"
        if st.session_state.double_level < 8:
            st.session_state.double_level += 1
        else:
            st.session_state.double_level = 1

    profit_target = int(st.session_state.initial_wallet * 0.20)
    if st.session_state.wallet_balance >= (st.session_state.initial_wallet + profit_target):
        st.session_state.target_achieved = True

    st.session_state.history.append(current_bs_short)
    st.session_state.history_details.insert(0, {"num": val, "type": current_bs, "status": net_change_str})

# Target Achieved Screen
if st.session_state.target_achieved:
    st.balloons()
    earned = int(st.session_state.initial_wallet * 0.20)
    st.markdown(f"""
        <div class='success-box'>
            <h2 style='color: #34d399;'>[+] TARGET PROFIT SECURED!</h2>
            <p>Initial: ₹{st.session_state.initial_wallet} | Profit: +₹{earned}</p>
            <p style='font-size: 18px; font-weight: bold;'>Final Balance: ₹{st.session_state.wallet_balance}</p>
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

# Wallet Input & Stats Bar
st.markdown("<p style='text-align: center; color: #22c55e;'>💰 WALLET CONFIGURATION (₹)</p>", unsafe_allow_html=True)
col_w1, col_w2, col_w3 = st.columns([1, 2, 1])
with col_w2:
    def update_w():
        w_str = st.session_state.w_input
        if w_str.isdigit() and int(w_str) >= 100:
            st.session_state.initial_wallet = int(w_str)
            st.session_state.wallet_balance = int(w_str)
    st.text_input("Wallet", value=str(st.session_state.wallet_balance), label_visibility="collapsed", key="w_input", on_change=update_w)

target_goal = st.session_state.initial_wallet + int(st.session_state.initial_wallet * 0.20)

# Side-by-Side Win & Loss Statistics Dashboard
st.markdown("<br>", unsafe_allow_html=True)
stat_c1, stat_c2 = st.columns(2)
with stat_c1:
    st.markdown(f"""
        <div class='stat-card' style='border-color: #22c55e;'>
            <div style='color: #9ca3af; font-size: 12px;'>TOTAL WINS</div>
            <div style='color: #22c55e; font-size: 22px; font-weight: bold;'>{st.session_state.wins} 🟢</div>
        </div>
    """, unsafe_allow_html=True)
with stat_c2:
    st.markdown(f"""
        <div class='stat-card' style='border-color: #ef4444;'>
            <div style='color: #9ca3af; font-size: 12px;'>TOTAL LOSSES</div>
            <div style='color: #ef4444; font-size: 22px; font-weight: bold;'>{st.session_state.losses} 🔴</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <div style='background: #0b0f19; border: 1px solid #22c55e; padding: 10px; border-radius: 8px; text-align: center; margin-top: 10px;'>
        <span style='color: #9ca3af;'>Balance:</span> <b style='color: #34d399;'>₹{st.session_state.wallet_balance}</b> &nbsp;|&nbsp; 
        <span style='color: #9ca3af;'>Target:</span> <b style='color: #60a5fa;'>₹{target_goal}</b>
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

# 4-Streak Skip Logic & Prediction Recommendation Engine
if st.session_state.history:
    last_t = st.session_state.history[-1]
    curr_bet = 2 ** (st.session_state.double_level - 1)
    
    is_skip = False
    if len(st.session_state.history) >= 4 and all(x == st.session_state.history[-4] for x in st.session_state.history[-4:]):
        is_skip = True

    if is_skip:
        st.markdown("""
            <div class='skip-alert-panel'>
                <h3 style='color: #fca5a5; margin:0;'>⚠️ WARNING: 4-STREAK SKIP ZONE DETECTED!</h3>
                <p style='color: #fee2e2; font-size: 13px; margin-top:5px;'>പാറ്റേൺ ലോക്ക് ആയിരിക്കുന്നു. നിലവിൽ ബെറ്റിംഗ് ഒഴിവാക്കുക (SKIP).</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        s_txt = "Small: ₹1 (Fixed)" if last_t != "S" else f"Small: ₹{curr_bet} (Double)"
        b_txt = "Big: ₹1 (Fixed)" if last_t != "B" else f"Big: ₹{curr_bet} (Double)"
        st.markdown(f"""
            <div class='hack-panel'>
                <div style='color: #9ca3af; font-size: 11px;'>RECOMMENDED ACTION (LEVEL {st.session_state.double_level})</div>
                <div style='color: #22c55e; font-size: 15px; font-weight: bold; margin-top: 4px;'>👉 {s_txt} &nbsp;|&nbsp; {b_txt}</div>
            </div>
        """, unsafe_allow_html=True)

# Input Buttons Panel
st.markdown("<p style='text-align: center; color: #22c55e;'>INPUT RECENT RESULT NUMBER:</p>", unsafe_allow_html=True)
top_cols = st.columns(5)
for i, (n, b) in enumerate([(0, "🟣🔴"), (1, "🟢"), (2, "🔴"), (3, "🟢"), (4, "🔴")]):
    with top_cols[i]:
        if st.button(f"{n}\n{b}", key=f"b_{n}", use_container_width=True): handle_number_click(n); st.rerun()

bot_cols = st.columns(5)
for i, (n, b) in enumerate([(5, "🟢🟣"), (6, "🔴"), (7, "🟢"), (8, "🔴"), (9, "🟢")]):
    with bot_cols[i]:
        if st.button(f"{n}\n{b}", key=f"b_{n}", use_container_width=True): handle_number_click(n); st.rerun()

# History Feed with Plus/Minus Amounts
st.markdown("<h3 style='color: #22c55e; text-align: center; font-size: 16px; margin-top: 15px;'>[ EXECUTION HISTORY ]</h3>", unsafe_allow_html=True)
if not st.session_state.history_details:
    st.markdown("<p style='text-align: center; color: #4b5563; font-size: 13px;'>No logs recorded.</p>", unsafe_allow_html=True)
else:
    for item in st.session_state.history_details[:8]:
        st.markdown(f"""
            <div style='background: #0b0f19; border-left: 3px solid #22c55e; padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center;'>
                <span style='color: #d1d5db;'>Num: <b>{item['num']}</b> ({item['type']})</span>
                <span>{item['status']}</span>
            </div>
        """, unsafe_allow_html=True)
