import streamlit as st
import datetime
import uuid

st.set_page_config(page_title="PRO SKIP MASTER 🎯", page_icon="⚡", layout="centered")

# Custom CSS Theme
st.markdown("""
    <style>
    .main { background: #07090E; }
    .stApp { background: #07090E; color: #F8FAFC; }
    
    .app-header {
        text-align: center;
        background: linear-gradient(90deg, #00F2FE, #4FACFE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 28px !important;
        font-weight: 900 !important;
        margin-bottom: 12px;
    }

    .skip-warning-panel {
        background: linear-gradient(135deg, #7f1d1d, #450a0a);
        padding: 24px;
        border-radius: 18px;
        border: 3px solid #EF4444;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0px 8px 30px rgba(239, 68, 68, 0.4);
    }

    .game-panel {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        padding: 22px;
        border-radius: 18px;
        border: 2px solid #00F2FE;
        margin: 15px 0;
        box-shadow: 0px 8px 25px rgba(0, 242, 254, 0.15);
    }

    .admin-panel-box {
        background: linear-gradient(135deg, #4c0519, #1f1218);
        padding: 24px;
        border-radius: 20px;
        border: 2px solid #fb7185;
        margin: 15px 0;
    }

    .grand-success-box {
        background: linear-gradient(135deg, #065f46, #022c22);
        padding: 30px;
        border-radius: 22px;
        border: 3px solid #10B981;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0px 10px 35px rgba(16, 185, 129, 0.4);
    }

    .stButton button {
        background: linear-gradient(135deg, #1e293b, #0f172a) !important;
        color: #00F2FE !important;
        border: 2px solid #00F2FE !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        height: 50px !important;
        font-size: 16px !important;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: #00F2FE !important;
        color: #07090E !important;
        transform: translateY(-2px);
    }

    input[type="text"], input[type="password"] {
        text-align: center !important;
        font-size: 18px !important;
        font-weight: bold !important;
        background-color: #0f172a !important;
        color: #00F2FE !important;
        border: 2px solid #00F2FE !important;
        border-radius: 10px !important;
    }

    .history-item-row {
        background: #0f172a;
        padding: 12px 16px;
        border-radius: 10px;
        margin-bottom: 8px;
        border-left: 5px solid #00F2FE;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-header'>⚡ PRO SKIP MASTER ⚡</div>", unsafe_allow_html=True)

# Access Control & Session States Initialization
if 'allowed_keys' not in st.session_state:
    st.session_state.allowed_keys = ["target123", "bosco456", "rahul789"]
if 'blocked_keys' not in st.session_state:
    st.session_state.blocked_keys = []
if 'bound_devices' not in st.session_state:
    st.session_state.bound_devices = {}
if 'auth_type' not in st.session_state:
    st.session_state.auth_type = None
if 'logged_in_key' not in st.session_state:
    st.session_state.logged_in_key = None
if 'my_device_id' not in st.session_state:
    st.session_state.my_device_id = str(uuid.uuid4())

# Midnight Reset Check (12:00 AM Reset Only)
current_date_str = datetime.date.today().isoformat()
if 'last_reset_date' not in st.session_state:
    st.session_state.last_reset_date = current_date_str

if st.session_state.last_reset_date != current_date_str:
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.wallet_balance = 500
    st.session_state.initial_wallet = 500
    st.session_state.double_level = 1
    st.session_state.target_achieved = False
    st.session_state.last_reset_date = current_date_str

# Game States
if 'history_details' not in st.session_state: st.session_state.history_details = []
if 'history' not in st.session_state: st.session_state.history = []
if 'num_history' not in st.session_state: st.session_state.num_history = []
if 'wins' not in st.session_state: st.session_state.wins = 0
if 'losses' not in st.session_state: st.session_state.losses = 0
if 'initial_wallet' not in st.session_state: st.session_state.initial_wallet = 500
if 'wallet_balance' not in st.session_state: st.session_state.wallet_balance = 500
if 'double_level' not in st.session_state: st.session_state.double_level = 1
if 'target_achieved' not in st.session_state: st.session_state.target_achieved = False
    # Login Screen Component
if st.session_state.auth_type is None:
    st.markdown("<div class='game-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00F2FE; text-align:center;'>🔐 ആക്സസ് ടൈപ്പ് തിരഞ്ഞെടുക്കുക</h3>", unsafe_allow_html=True)
    
    login_option = st.selectbox("ലോഗിൻ വിഭാഗം തിരഞ്ഞെടുക്കുക:", ["-- Select --", "User Login", "Admin Login"])
    
    if login_option == "User Login":
        user_input_key = st.text_input("User Access Key നൽകുക:", type="password")
        if st.button("Login as User", use_container_width=True):
            if user_input_key in st.session_state.blocked_keys:
                st.error("❌ ഈ കീ അഡ്മിൻ ബ്ലോക്ക് ചെയ്തിരിക്കുന്നു!")
            elif user_input_key in st.session_state.allowed_keys:
                if user_input_key in st.session_state.bound_devices:
                    if st.session_state.bound_devices[user_input_key] != st.session_state.my_device_id:
                        st.error("❌ ഈ കീ മറ്റൊരു ഡിവൈസിൽ രജിസ്റ്റർ ചെയ്തതാണ്!")
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

# Admin Control Panel
if st.session_state.auth_type == "admin":
    st.markdown("<div class='admin-panel-box'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#fb7185; text-align: center;'>🛠️ ADMIN CONTROL PANEL</h2>", unsafe_allow_html=True)
    
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

# Logout Option for User
if st.session_state.auth_type == "user":
    if st.button("🚪 Logout"):
        st.session_state.auth_type = None
        st.session_state.logged_in_key = None
        st.rerun()

st.divider()
def handle_number_click(val):
    current_bs = "BIG" if val >= 5 else "SMALL"
    current_bs_short = "B" if val >= 5 else "S"
    
    is_skip_zone = False
    if len(st.session_state.history) >= 3:
        last_three = st.session_state.history[-3:]
        if all(x == current_bs_short for x in last_three):
            is_skip_zone = True

    current_double_bet = 2 ** (st.session_state.double_level - 1)
    fixed_bet = 1
    round_investment = fixed_bet + current_double_bet
    
    if is_skip_zone:
        st.session_state.losses += 1
        st.session_state.wallet_balance -= round_investment
        status_str = f"<span style='color:#EF4444; font-weight:900;'>🔴 LOSS (SKIPPED ZONE)</span>"
        st.session_state.double_level = 1 
    else:
        st.session_state.wins += 1
        st.session_state.wallet_balance += current_double_bet 
        status_str = f"<span style='color:#10B981; font-weight:900;'>🟢 WIN ({current_bs})</span>"
        if st.session_state.double_level < 8:
            st.session_state.double_level += 1
        else:
            st.session_state.double_level = 1

    profit_target = int(st.session_state.initial_wallet * 0.20)
    target_goal_amount = st.session_state.initial_wallet + profit_target

    if st.session_state.wallet_balance >= target_goal_amount:
        st.session_state.target_achieved = True

    st.session_state.history.append(current_bs_short)
    st.session_state.num_history.append(val)
    st.session_state.history_details.insert(0, {"num": val, "type": current_bs, "status": status_str})

# Target Achieved Section
if st.session_state.target_achieved:
    st.balloons()
    profit_earned = int(st.session_state.initial_wallet * 0.20)
    st.markdown(f"""
        <div class="grand-success-box">
            <h1 style="color: #6EE7B7; font-size: 30px; font-weight: 900;">🌟 TARGET ACHIEVED SUCCESSFULLY! 🌟</h1>
            <h3 style="color: #F8FAFC; margin-top: 10px; font-size: 18px;">ഇന്നത്തെ പ്രോഫിറ്റ് ടാർഗറ്റ് പൂർത്തിയായി!</h3>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 12px; margin-top: 15px; border: 1px solid #10B981;">
                <p style="color: #CBD5E1; font-size: 15px; margin: 4px 0;">Initial Wallet: <b>₹{st.session_state.initial_wallet}</b></p>
                <p style="color: #34D399; font-size: 17px; margin: 4px 0;">Profit Earned: <b>+₹{profit_earned}</b></p>
                <p style="color: #F8FAFC; font-size: 20px; font-weight: 900; margin: 4px 0;">Final Wallet: ₹{st.session_state.wallet_balance}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 New Session Start", use_container_width=True):
        st.session_state.target_achieved = False
        st.session_state.history_details = []
        st.session_state.history = []
        st.session_state.num_history = []
        st.session_state.wins = 0
        st.session_state.losses = 0
        st.session_state.double_level = 1
        st.rerun()
    st.stop()

# Wallet Input & Controls
st.markdown("<p style='text-align: center; font-weight: bold; color: #00F2FE; font-size: 16px;'>💰 വാലറ്റ് ബാലൻസ് നൽകുക (₹):</p>", unsafe_allow_html=True)
w_col1, w_col2, w_col3 = st.columns([1, 2, 1])
with w_col2:
    def update_wallet():
        val_str = st.session_state.wallet_box_input
        if val_str.isdigit() and int(val_str) >= 100:
            new_val = int(val_str)
            st.session_state.initial_wallet = new_val
            st.session_state.wallet_balance = new_val

    st.text_input("Wallet", value=str(st.session_state.wallet_balance), label_visibility="collapsed", key="wallet_box_input", on_change=update_wallet)

fixed_profit_target = int(st.session_state.initial_wallet * 0.20)
target_goal_amount = st.session_state.initial_wallet + fixed_profit_target

st.markdown(f"""
    <div style="background: #0f172a; border: 2px solid #00F2FE; border-radius: 12px; padding: 12px; text-align: center; margin: 15px 0;">
        <span style="color: #00F2FE; font-weight: bold; font-size: 15px;">🟢 Live Wallet: </span>
        <span style="color: #34D399; font-weight: 900; font-size: 20px;">₹{st.session_state.wallet_balance}</span> 
        <span style="color: #94A3B8; font-size: 13px;">(Target: ₹{target_goal_amount})</span>
    </div>
""", unsafe_allow_html=True)

if st.button("🔄 Manual Reset Data", use_container_width=True, key="reset_btn"):
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.double_level = 1
    st.session_state.target_achieved = False
    st.rerun()

st.divider()

st.markdown("<p style='text-align: center; font-weight: bold; color: #00F2FE; font-size: 16px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)
cols_top = st.columns(5)
nums_top = [(0, "0", "🟣 🔴"), (1, "1", "🟢"), (2, "2", "🔴"), (3, "3", "🟢"), (4, "4", "🔴")]
for idx, (num_val, num_str, badge) in enumerate(nums_top):
    with cols_top[idx]:
        if st.button(f"{num_str}\n{badge}", key=f"btn_{num_val}", use_container_width=True):
            handle_number_click(num_val)
            st.rerun()

cols_bottom = st.columns(5)
nums_bottom = [(5, "5", "🟢 🟣"), (6, "6", "🔴"), (7, "7", "🟢"), (8, "8", "🔴"), (9, "9", "🟢")]
for idx, (num_val, num_str, badge) in enumerate(nums_bottom):
    with cols_bottom[idx]:
        if st.button(f"{num_str}\n{badge}", key=f"btn_{num_val}", use_container_width=True):
            handle_number_click(num_val)
            st.rerun()

# 4-Streak Skip Logic Check
if st.session_state.history:
    last_type = st.session_state.history[-1]
    curr_double = 2 ** (st.session_state.double_level - 1)
    
    is_skip = False
    if len(st.session_state.history) >= 4:
        last_four = st.session_state.history[-4:]
        if all(x == last_four[0] for x in last_four):
            is_skip = True

    if is_skip:
        st.markdown("""
            <div class="skip-warning-panel">
                <h2 style="color: #FCA5A5; font-size: 24px; font-weight: 900; margin: 0;">⚠️ SKIP ! SKIP ! SKIP ! ⚠️</h2>
                <p style="color: #FEE2E2; font-size: 15px; margin-top: 8px;">തുടർച്ചയായി 4 പ്രാവശ്യം ഒരേ ഫലം വന്നതിനാൽ ഇപ്പോൾ ഗെയിം **സ്കിപ്പ്** ചെയ്യുക!</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        if last_type == "S":
            s_bet_text = "Small-ൽ ₹1 (Fixed)"
            b_bet_text = f"Big-ൽ ₹{curr_double} (Double)"
        else:
            b_bet_text = "Big-ൽ ₹1 (Fixed)"
            s_bet_text = f"Small-ൽ ₹{curr_double} (Double)"

        st.markdown(f"""
            <div class="game-panel">
                <div style="color: #94A3B8; font-size: 12px; font-weight: bold; letter-spacing: 1px;">NEXT BET RECOMMENDATION</div>
                <div style="font-size: 18px; font-weight: 900; color: #00F2FE; margin: 6px 0;">👉 {s_bet_text} &nbsp;|&nbsp; {b_bet_text}</div>
                <div style="color: #CBD5E1; font-size: 13px;">Current Level: <b>Level {st.session_state.double_level}</b></div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<h3 style='color: #00F2FE; text-align: center; margin-top: 20px;'>📜 History</h3>", unsafe_allow_html=True)
if not st.session_state.history_details:
    st.markdown("<p style='text-align: center; color: #94A3B8;'>ഇതുവരെ ഗെയിം ഹിസ്റ്ററി ഒന്നുമില്ല.</p>", unsafe_allow_html=True)
else:
    for item in st.session_state.history_details[:10]:
        st.markdown(f"""
            <div class="history-item-row">
                <div><b>Number:</b> {item['num']} ({item['type']})</div>
                <div>{item['status']}</div>
            </div>
        """, unsafe_allow_html=True)
        
