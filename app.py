import streamlit as st
import collections

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# Custom CSS for Styling
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
        text-shadow: 0px 2px 10px rgba(255, 215, 0, 0.3);
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
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .metric-label {
        font-size: 14px !important;
        font-weight: 900 !important;
        color: #FFD700 !important;
        margin-bottom: 3px;
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
        font-size: 16px !important;
    }
    .stButton button:hover {
        background-color: #334155 !important;
        border-color: #FFD700 !important;
        color: #FFD700 !important;
    }

    input[type="text"] {
        text-align: center !important;
        font-size: 18px !important;
        font-weight: bold !important;
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #3B82F6 !important;
    }
    
    div[data-baseweb="input"] {
        background-color: #1E293B !important;
        border-radius: 8px !important;
    }

    .pred-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        padding: 18px;
        border-radius: 14px;
        border: 2px solid #FFD700;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0px 6px 15px rgba(255, 215, 0, 0.2);
    }

    .history-card {
        background-color: #151C28;
        padding: 10px 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        border-left: 4px solid #FFD700;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #FFFFFF;
        font-size: 15px;
    }
    
    .win-text {
        color: #00E676 !important;
        font-weight: 900 !important;
    }

    .loss-text {
        color: #FF5252 !important;
        font-weight: 900 !important;
    }

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
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 14px; margin-top: -10px; margin-bottom: 20px;'>നിങ്ങളുടെ പ്രെഡിക്ഷനും ടാർഗറ്റും സുരക്ഷിതമായി കൈകാര്യം ചെയ്യാം</p>", unsafe_allow_html=True)

# ----------------- SESSION STATES FOR ACCESS & KEYS -----------------
if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123", "arun456"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["bosco123", "target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["bosco123"]

if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

# ----------------- MAIN SCREEN 3 LOGIN BOXES -----------------
if st.session_state.auth_role is None:
    st.markdown("### 🔐 ആക്സസ് തിരഞ്ഞെടുക്കുക (Access Portal)")
    
    tab1, tab2, tab3 = st.tabs(["👤 Normal Access", "🎯 Target Access", "🛠️ Admin Access"])
    
    with tab1:
        st.markdown("<b>സാധാരണ യൂസർ കീ നൽകുക:</b>", unsafe_allow_html=True)
        u_key_input = st.text_input("User Key Input", type="password", key="u_key_in", label_visibility="collapsed")
        if st.button("Login as User", use_container_width=True):
            if u_key_input in st.session_state.user_keys:
                st.session_state.auth_role = 'user'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ യൂസർ കീ!")

    with tab2:
        st.markdown("<b>ടാർഗറ്റ് ആക്സസ് കീ നൽകുക:</b>", unsafe_allow_html=True)
        t_key_input = st.text_input("Target Key Input", type="password", key="t_key_in", label_visibility="collapsed")
        if st.button("Login as Target", use_container_width=True):
            if t_key_input in st.session_state.target_keys:
                st.session_state.auth_role = 'target'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ ടാർഗറ്റ് കീ!")

    with tab3:
        st.markdown("<b>അഡ്മിൻ പാസ്‌വേഡ് നൽകുക:</b>", unsafe_allow_html=True)
        a_key_input = st.text_input("Admin Key Input", type="password", key="a_key_in", label_visibility="collapsed")
        if st.button("Login as Admin", use_container_width=True):
            if a_key_input in st.session_state.admin_keys:
                st.session_state.auth_role = 'admin'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ അഡ്മിൻ പാസ്‌വേഡ്!")
                
    st.stop()

if st.button("🚪 Logout / Switch Access"):
    st.session_state.auth_role = None
    st.rerun()

st.divider()

# =========================================================================
# 1. ADMIN ACCESS PANEL
# =========================================================================
if st.session_state.auth_role == 'admin':
    st.markdown("<h2 style='color: #FFD700;'>🛠️ Admin Control Panel</h2>", unsafe_allow_html=True)
    st.success("Admin Mode Active ✅")
    
    st.subheader("📋 നിലവിലുള്ള കീകൾ നിയന്ത്രിക്കുക")
    
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.write("👤 **User Keys:**", st.session_state.user_keys)
        new_u = st.text_input("പുതിയ യൂസർ കീ ചേർക്കുക:")
        if st.button("Add User Key"):
            if new_u and new_u not in st.session_state.user_keys:
                st.session_state.user_keys.append(new_u)
                st.success("ചേർത്തു!")
                st.rerun()
        rem_u = st.selectbox("ഒഴിവാക്കേണ്ട യൂസർ കീ:", ["-- Select --"] + st.session_state.user_keys, key="rem_u_sel")
        if st.button("Remove User Key") and rem_u != "-- Select --":
            st.session_state.user_keys.remove(rem_u)
            st.success("നീക്കം ചെയ്തു!")
            st.rerun()

    with col_a2:
        st.write("🎯 **Target Keys:**", st.session_state.target_keys)
        new_t = st.text_input("പുതിയ ടാർഗറ്റ് കീ ചേർക്കുക:")
        if st.button("Add Target Key"):
            if new_t and new_t not in st.session_state.target_keys:
                st.session_state.target_keys.append(new_t)
                st.success("ചേർത്തു!")
                st.rerun()
        rem_t = st.selectbox("ഒഴിവാക്കേണ്ട ടാർഗറ്റ് കീ:", ["-- Select --"] + st.session_state.target_keys, key="rem_t_sel")
        if st.button("Remove Target Key") and rem_t != "-- Select --":
            st.session_state.target_keys.remove(rem_t)
            st.success("നീക്കം ചെയ്തു!")
            st.rerun()

    st.stop()

# =========================================================================
# 2. TARGET ACCESS MODULE (Minimum ₹500 Wallet, Smart Skip & Daily Target)
# =========================================================================
elif st.session_state.auth_role == 'target':
    st.markdown("<h2 style='color: #FFD700; text-align: center;'>🎯 Target Profit & Wallet Tracker</h2>", unsafe_allow_html=True)
    
    if 'target_wallet' not in st.session_state: st.session_state.target_wallet = 500
    if 'starting_wallet' not in st.session_state: st.session_state.starting_wallet = 500
    if 'target_level' not in st.session_state: st.session_state.target_level = 1
    if 'target_wins' not in st.session_state: st.session_state.target_wins = 0
    if 'target_losses' not in st.session_state: st.session_state.target_losses = 0
    if 'target_history' not in st.session_state: st.session_state.target_history = []
    if 'target_history_details' not in st.session_state: st.session_state.target_history_details = []
    if 'target_pred' not in st.session_state: st.session_state.target_pred = None
    if 'target_is_skip' not in st.session_state: st.session_state.target_is_skip = False

    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 15px;'>💰 ഡെപ്പോസിറ്റ് ബാലൻസ് നൽകുക (മിനിമം ₹500):</p>", unsafe_allow_html=True)
    tw_col1, tw_col2, tw_col3 = st.columns([1, 2, 1])
    with tw_col2:
        t_wallet_input = st.text_input("Target Wallet Input", value=str(st.session_state.target_wallet), label_visibility="collapsed")
        if t_wallet_input.isdigit():
            val_tw = int(t_wallet_input)
            if val_tw >= 500:
                st.session_state.target_wallet = val_tw
                st.session_state.starting_wallet = val_tw
            else:
                st.warning("⚠️ മിനിമം ബാലൻസ് ₹500 അല്ലെങ്കിൽ അതിൽ കൂടുതലായിരിക്കണം!")

    goal_profit = int(st.session_state.starting_wallet * 0.20)
    current_profit = st.session_state.target_wallet - st.session_state.starting_wallet
    
    st.markdown(f"""
        <div class="pred-card">
            <div style="color: #38BDF8; font-size: 14px; font-weight: bold;">DAILY PROFIT TARGET STRATEGY</div>
            <div style="font-size: 22px; font-weight: 900; color: #FFD700; margin: 6px 0;">Target Profit: ₹{goal_profit}</div>
            <div style="color: #FFFFFF; font-size: 16px;">Current Profit Achieved: <b style="color: {'#00E676' if current_profit >= 0 else '#FF5252'};">₹{current_profit}</b></div>
        </div>
    """, unsafe_allow_html=True)

    if current_profit >= goal_profit:
        st.success(f"🎉 അഭിനന്ദനങ്ങൾ! ഇന്നത്തെ നിങ്ങളുടെ ടാർഗറ്റ് പ്രോഫിറ്റ് (₹{goal_profit}) വിജയകരമായി പൂർത്തിയായിരിക്കുന്നു!")

    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-box">
                <div class="metric-label">WINS 🟢</div>
                <div class="metric-val">{st.session_state.target_wins}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">LOSSES 🔴</div>
                <div class="metric-val">{st.session_state.target_losses}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Reset Target Data", use_container_width=True):
        st.session_state.target_wallet = 500
        st.session_state.starting_wallet = 500
        st.session_state.target_level = 1
        st.session_state.target_wins = 0
        st.session_state.target_losses = 0
        st.session_state.target_history = []
        st.session_state.target_history_details = []
        st.session_state.target_pred = None
        st.session_state.target_is_skip = False
        st.rerun()

    def handle_target_click(val):
        current_bs = "BIG" if val >= 5 else "SMALL"
        current_bs_short = "B" if val >= 5 else "S"
        status_str = "<span style='color:#94A3B8; font-weight:bold;'>➖ START</span>"
        
        base_unit = st.session_state.target_wallet / 255
        multipliers = [1, 2, 4, 8, 16, 32, 64, 128]
        bet_amt = max(1, round(base_unit * multipliers[st.session_state.target_level - 1]))

        if st.session_state.target_pred is not None:
            if not st.session_state.target_is_skip:
                if current_bs_short == st.session_state.target_pred:
                    st.session_state.target_wins += 1
                    status_str = "<span class='win-text'>🟢 WIN</span>"
                    st.session_state.target_wallet += bet_amt
                    st.session_state.target_level = 1
                else:
                    st.session_state.target_losses += 1
                    status_str = "<span class='loss-text'>🔴 LOSS</span>"
                    st.session_state.target_wallet = max(100, st.session_state.target_wallet - bet_amt)
                    st.session_state.target_level = st.session_state.target_level + 1 if st.session_state.target_level < 8 else 1
            else:
                status_str = "<span style='color:#38BDF8; font-weight:bold;'>🔄 SKIPPED</span>"

        st.session_state.target_history.append(current_bs_short)
        st.session_state.target_history_details.insert(0, {"num": val, "type": current_bs, "status": status_str})

        th = st.session_state.target_history

        if len(th) < 3:
            st.session_state.target_pred = None
            st.session_state.target_is_skip = False
        else:
            recent_four = th[-4:] if len(th) >= 4 else th
            is_choppy = (len(recent_four) == 4 and recent_four[0] != recent_four[1] and recent_four[1] != recent_four[2] and recent_four[2] != recent_four[3])
            is_heavy_repeat = (len(th) >= 3 and th[-1] == th[-2] == th[-3])

            st.session_state.target_is_skip = True if (is_choppy and st.session_state.target_level == 1 and len(th) % 2 == 0) else False

            is_alternating = (len(th) >= 4 and th[-1] != th[-2] and th[-2] != th[-3] and th[-3] != th[-4]) or (len(th) == 3 and th[-1] != th[-2] and th[-2] != th[-3])

            if is_alternating:
                next_pred = "S" if th[-1] == "B" else "B"
            elif is_heavy_repeat:
                next_pred = "S" if (th[-1] == "B" and st.session_state.target_level >= 3) else ("B" if st.session_state.target_level >= 3 else th[-1])
            else:
                recent_window = th[-6:] if len(th) >= 6 else th
                b_count, s_count = recent_window.count('B'), recent_window.count('S')
                next_pred = "B" if b_count > s_count else ("S" if s_count > b_count else ("S" if th[-1] == "B" else "B"))

            st.session_state.target_pred = next_pred

    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 15px; margin-top: 15px;'>വന്ന നമ്പർ തിരഞ്ഞെടുക്കുക:</p>", unsafe_allow_html=True)
    
    t_buttons = [
        (0, "0 (🟣🔴)", 5, "5 (🟢🟣)"),
        (1, "1 (🟢)",   6, "6 (🔴)"),
        (2, "2 (🔴)",   7, "7 (🟢)"),
        (3, "3 (🟢)",   8, "8 (🔴)"),
        (4, "4 (🔴)",   9, "9 (🟢)")
    ]
    for n1, l1, n2, l2 in t_buttons:
        col1, col2 = st.columns(2)
        with col1:
            if st.button(l1, key=f"t_btn_{n1}", use_container_width=True):
                handle_target_click(n1)
                st.rerun()
        with col2:
            if st.button(l2, key=f"t_btn_{n2}", use_container_width=True):
                handle_target_click(n2)
                st.rerun()

    if st.session_state.target_pred is not None:
        tp = st.session_state.target_pred
        tp_text = "⚠️ SMART SKIP (ഈ റൗണ്ട് വിടുക)" if st.session_state.target_is_skip else ("BIG 🟢" if tp == "B" else "SMALL 🔴")
        tp_color = "#38BDF8" if st.session_state.target_is_skip else ("#00E676" if tp == "B" else "#FF5252")
        
        base_unit_t = st.session_state.target_wallet / 255
        s_bet_t = max(1, round(base_unit_t * [1, 2, 4, 8, 16, 32, 64, 128][st.session_state.target_level - 1]))
        
        st.markdown(f"""
            <div class="pred-card">
                <div style="color: #94A3B8; font-size: 12px; font-weight: bold;">NEXT TARGET PREDICTION</div>
                <div style="font-size: 22px; font-weight: 900; color: {tp_color}; margin: 4px 0;">{tp_text}</div>
                <hr style="border-color: #334155; margin: 6px 0;">
                <div style="color: #38BDF8; font-size: 13px; font-weight: bold;">🛡️ Level {st.session_state.target_level}/8 (Win within 5 prioritized)</div>
                <div style="color: #FFFFFF; font-size: 16px; font-weight: 900; margin-top: 2px;">Suggested Bet: <span style="color: #FFD700;">₹{s_bet_t}</span></div>
                <div style="color: #E2E8F0; font-size: 14px; margin-top: 4px;">Live Wallet Balance: <b style="color: #FFD700;">₹{st.session_state.target_wallet}</b></div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    if st.session_state.target_history_details:
        st.markdown("<h3 style='color:#FFD700; font-size: 15px;'>📜 Target History Logs</h3>", unsafe_allow_html=True)
        for item in st.session_state.target_history_details[:10]:
            st.markdown(f"""
                <div class="history-card">
                    <span><b>Num: {item['num']}</b> ({item['type']})</span>
                    <span>{item['status']}</span>
                </div>
            """, unsafe_allow_html=True)

    st.stop()

# =========================================================================
# 3. NORMAL USER ACCESS MODULE (Original King Bosco Predictor)
# =========================================================================
if st.session_state.auth_role == 'user':
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

    st.markdown("<p style='text-align: center; font-weight: bold; color: #FFD700; font-size: 14px;'>💰 നിങ്ങളുടെ ഡെപ്പോസിറ്റ് ബാലൻസ് നൽകുക (₹):</p>", unsafe_allow_html=True)
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
        
        if st.ses
