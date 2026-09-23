import streamlit as st

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #0B0E14, #1a1c29); }
    .stApp { background: linear-gradient(135deg, #0B0E14, #1a1c29); color: #FFFFFF; }
    .app-title {
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FF4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 26px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
    }
    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin: 10px 0;
    }
    .metric-box {
        flex: 1;
        background: linear-gradient(135deg, #1e1b4b, #311042);
        border: 2px solid #a855f7;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
    }
    .metric-label {
        font-size: 11px !important;
        font-weight: 900 !important;
        color: #f43f5e !important;
    }
    .metric-val {
        font-size: 18px !important;
        font-weight: 900 !important;
        color: #38bdf8 !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
        color: #FFFFFF !important;
        border: 2px solid #60a5fa !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        height: 48px !important;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.4);
    }
    .stButton button:active, .stButton button:focus {
        border: 2px solid #FFD700 !important;
        color: #FFD700 !important;
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
    }
    .pred-card {
        background: linear-gradient(135deg, #312e81, #581c87);
        padding: 20px;
        border-radius: 16px;
        border: 2px solid #fbbf24;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0 6px 20px rgba(251, 191, 36, 0.4);
    }
    .history-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 10px 14px;
        border-radius: 10px;
        margin-bottom: 8px;
        border-left: 5px solid #10b981;
        display: flex;
        justify-content: space-between;
        color: #FFFFFF;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    .custom-box {
        background-color: #1e293b;
        border: 1px solid #475569;
        padding: 12px;
        border-radius: 10px;
        color: #38bdf8;
        font-family: monospace;
        margin-bottom: 10px;
    }
    .win-text { color: #10b981 !important; font-weight: 900 !important; }
    .loss-text { color: #f43f5e !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# State Management for Keys & Used Keys
if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123", "arun456"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["bosco123", "target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["bosco123"]
if 'used_keys' not in st.session_state:
    st.session_state.used_keys = set()

if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

if st.session_state.auth_role is None:
    st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
    st.markdown("### 🔐 Aakhas തിരഞ്ഞെടുക്കുക")
    tab1, tab2, tab3 = st.tabs(["👤 User Access", "🎯 Target Access", "🛠️ Admin Access"])
    
    with tab1:
        u_key_input = st.text_input("User Key", type="password", key="u_key_in")
        if st.button("Login as User", use_container_width=True):
            if u_key_input in st.session_state.user_keys:
                if u_key_input in st.session_state.used_keys:
                    st.error("❌ Ee key ithinakam upayogichathanu!")
                else:
                    st.session_state.used_keys.add(u_key_input)
                    st.session_state.auth_role = 'user'
                    st.rerun()
            else:
                st.error("❌ Thettaya user key!")

    with tab2:
        t_key_input = st.text_input("Target Key", type="password", key="t_key_in")
        if st.button("Login as Target", use_container_width=True):
            if t_key_input in st.session_state.target_keys:
                if t_key_input in st.session_state.used_keys:
                    st.error("❌ Ee key ithinakam upayogichathanu!")
                else:
                    st.session_state.used_keys.add(t_key_input)
                    st.session_state.auth_role = 'target'
                    st.rerun()
            else:
                st.error("❌ Thettaya target key!")

    with tab3:
        a_key_input = st.text_input("Admin Key", type="password", key="a_key_in")
        if st.button("Login as Admin", use_container_width=True):
            if a_key_input in st.session_state.admin_keys:
                st.session_state.auth_role = 'admin'
                st.rerun()
            else:
                st.error("❌ Thettaya admin password!")
    st.stop()

# Top Bar with Title and Small Logout Icon (🚪)
col_title, col_logout = st.columns([0.85, 0.15])
with col_title:
    st.markdown("<div class='app-title' style='text-align: left;'>👑 KING BOSCO</div>", unsafe_allow_html=True)
with col_logout:
    if st.button("🚪", help="Logout", use_container_width=True):
        st.session_state.auth_role = None
        st.rerun()

st.divider()

# ================= ADMIN SECTION =================
if st.session_state.auth_role == 'admin':
    st.markdown("<h2>🛠️ Admin Control Panel</h2>", unsafe_allow_html=True)
    
    st.markdown("### 👤 User Keys Management")
    new_u_key = st.text_input("New User Key Add cheyyuka", key="new_u")
    if st.button("Add User Key"):
        if new_u_key and new_u_key not in st.session_state.user_keys:
            st.session_state.user_keys.append(new_u_key)
            st.success("User key successfully added!")
            st.rerun()
            
    st.markdown("Nilavilulla User Keys:")
    u_keys_str = ", ".join(st.session_state.user_keys)
    st.markdown(f"<div class='custom-box'>{u_keys_str}</div>", unsafe_allow_html=True)
    
    del_u_key = st.selectbox("Block/Delete cheyyenda User Key", ["--Select--"] + st.session_state.user_keys, key="del_u")
    if st.button("Remove User Key") and del_u_key != "--Select--":
        st.session_state.user_keys.remove(del_u_key)
        if del_u_key in st.session_state.used_keys:
            st.session_state.used_keys.remove(del_u_key)
        st.success("User key removed!")
        st.rerun()

    st.markdown("---")
    st.markdown("### 🎯 Target Keys Management")
    new_t_key = st.text_input("New Target Key Add cheyyuka", key="new_t")
    if st.button("Add Target Key"):
        if new_t_key and new_t_key not in st.session_state.target_keys:
            st.session_state.target_keys.append(new_t_key)
            st.success("Target key successfully added!")
            st.rerun()
            
    st.markdown("Nilavilulla Target Keys:")
    t_keys_str = ", ".join(st.session_state.target_keys)
    st.markdown(f"<div class='custom-box'>{t_keys_str}</div>", unsafe_allow_html=True)
    
    del_t_key = st.selectbox("Block/Delete cheyyenda Target Key", ["--Select--"] + st.session_state.target_keys, key="del_t")
    if st.button("Remove Target Key") and del_t_key != "--Select--":
        st.session_state.target_keys.remove(del_t_key)
        if del_t_key in st.session_state.used_keys:
            st.session_state.used_keys.remove(del_t_key)
        st.success("Target key removed!")
        st.rerun()

# ================= TARGET SECTION (With Number Buttons & Predictions & Wallet Updates) =================
elif st.session_state.auth_role == 'target':
    st.markdown("<h2>🎯 Target Profit & Wallet Tracker (500 ➡️ 600)</h2>", unsafe_allow_html=True)
    
    if 'target_wallet' not in st.session_state: st.session_state.target_wallet = 500
    if 'target_level' not in st.session_state: st.session_state.target_level = 1
    if 'target_wins' not in st.session_state: st.session_state.target_wins = 0
    if 'target_losses' not in st.session_state: st.session_state.target_losses = 0
    if 'target_history' not in st.session_state: st.session_state.target_history = []
    if 'target_history_details' not in st.session_state: st.session_state.target_history_details = []
    if 'target_pred' not in st.session_state: st.session_state.target_pred = None

    if st.session_state.target_wallet >= 600:
        st.success("🎉 Lakshyam vijayichirikkunnu! Target 600 reached. Wallet reset cheyyunnu!")
        st.session_state.target_wallet = 500
        st.session_state.target_level = 1
        st.session_state.target_pred = None
        st.session_state.target_history = []
        st.session_state.target_history_details = []
        st.rerun()

    manual_t_wal = st.number_input("Wallet balance mattuka", min_value=-5000, value=int(st.session_state.target_wallet), step=50, key="manual_t_input")
    if manual_t_wal != st.session_state.target_wallet:
        st.session_state.target_wallet = manual_t_wal
        st.session_state.target_level = 1
        st.rerun()

    base = st.session_state.target_wallet / 255 if st.session_state.target_wallet != 0 else 2.0
    mults = [1, 2, 4, 8, 16, 32, 64, 128]
    current_bet = max(1, round(base * mults[st.session_state.target_level - 1]))

    st.markdown(f"""
        <div class='metric-container'>
            <div class='metric-box'>
                <div class='metric-label'>WALLET BALANCE</div>
                <div class='metric-val'>₹ {st.session_state.target_wallet} / ₹ 600</div>
            </div>
            <div class='metric-box'>
                <div class='metric-label'>8-LEVEL PLAN BET</div>
                <div class='metric-val'>₹ {current_bet} (Lvl {st.session_state.target_level})</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='metric-container'>
            <div class='metric-box'>
                <div class='metric-label'>WINS</div>
                <div class='metric-val' style='color:#10b981;'>{st.session_state.target_wins}</div>
            </div>
            <div class='metric-box'>
                <div class='metric-label'>LOSSES</div>
                <div class='metric-val' style='color:#f43f5e;'>{st.session_state.target_losses}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    pred_display = st.session_state.target_pred if st.session_state.target_pred else "WAITING..."
    pred_full = "BIG (5-9)" if pred_display == "B" else ("SMALL (0-4)" if pred_display == "S" else "WAITING FOR 3 INPUTS")
    st.markdown(f"""
        <div class='pred-card'>
            <div style='font-size: 13px; color: #fbbf24; font-weight: bold;'>NEXT PREDICTION</div>
            <div style='font-size: 32px; font-weight: 900; color: #FFFFFF; margin: 10px 0;'>{pred_full}</div>
            <div style='font-size: 14px; color: #38bdf8;'>8-Level Plan | Level <b>{st.session_state.target_level}</b> | Bet: <b>₹ {current_bet}</b></div>
        </div>
    """, unsafe_allow_html=True)

    def handle_target_click(val):
        cb = "BIG" if val >= 5 else "SMALL"
        cbs = "B" if val >= 5 else "S"
        bet = current_bet

        if st.session_state.target_pred is not None:
            if cbs == st.session_state.target_pred:
                st.session_state.target_wins += 1
                status = "🟢 WIN"
                st.session_state.target_wallet += bet
                st.session_state.target_level = 1
            else:
                st.session_state.target_losses += 1
                status = "🔴 LOSS"
                st.session_state.target_wallet -= bet
                st.session_state.target_level = st.session_state.target_level + 1 if st.session_state.target_level < 8 else 1
        else:
            if len(st.session_state.target_history) > 0:
                st.session_state.target_losses += 1
                status = "🔴 LOSS"
                st.session_state.target_wallet -= bet
                st.session_state.target_level = st.session_state.target_level + 1 if st.session_state.target_level < 8 else 1
            else:
                status = "➖ START"

        st.session_state.target_history.append(cbs)
        st.session_state.target_history_details.insert(0, {"num": val, "type": cb, "status": status})
        th = st.session_state.target_history

        if len(th) >= 3:
            st.session_state.target_pred = "S" if th[-1] == "B" else "B"
        else:
            st.session_state.target_pred = None

    st.markdown("### Numbers theranjedukkuka (0-9)")
    nums_t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in nums_t:
        if st.button(str(n), key=f"t_{n}", use_container_width=True):
            handle_target_click(n)
            st.rerun()

    st.markdown("### 📊 History")
    if st.session_state.target_history_details:
        for item in st.session_state.target_history_details[:10]:
            st_color = "win-text" if "WIN" in item['status'] else ("loss-text" if "LOSS" in item['status'] else "")
            st.markdown(f"""
                <div class='history-card'>
                    <div>Number: <b>{item['num']}</b> ({item['type']})</div>
                    <div class='{st_color}'>{item['status']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Ithuvare history onnumilla.")

# ================= USER SECTION =================
elif st.session_state.auth_role == 'user':
    st.markdown("<h2>👑 King Bosco Predictor</h2>", unsafe_allow_html=True)
    
    if 'user_wallet' not in st.session_state: st.session_state.user_wallet = 500
    if 'user_history' not in st.session_state: st.session_state.user_history = []
    if 'user_history_details' not in st.session_state: st.session_state.user_history_details = []
    if 'user_wins' not in st.session_state: st.session_state.user_wins = 0
    if 'user_losses' not in st.session_state: st.session_state.user_losses = 0
    if 'user_level' not in st.session_state: st.session_state.user_level = 1
    if 'user_pred' not in st.session_state: st.session_state.user_pred = None

    manual_u_wal = st.number_input("Wallet balance mattuka", min_value=-5000, value=int(st.session_state.user_wallet), step=50, key="manual_u_input")
    if manual_u_wal != st.session_state.user_wallet:
        st.session_state.user_wallet = manual_u_wal
        st.session_state.user_level = 1
        st.rerun()

    base_u = st.session_state.user_wallet / 255 if st.session_state.user_wallet != 0 else 2.0
    mults_u = [1, 2, 4, 8, 16, 32, 64, 128]
    current_u_bet = max(1, round(base_u * mults_u[st.session_state.user_level - 1]))

    st.markdown(f"""
        <div class='metric-container'>
            <div class='metric-box'>
                <div class='metric-label'>WALLET BALANCE</div>
                <div class='metric-val'>₹ {st.session_state.user_wallet}</div>
            </div>
            <div class='metric-box'>
                <div class='metric-label'>8-LEVEL PLAN BET</div>
                <div class='metric-val'>₹ {current_u_bet} (Lvl {st.session_state.user_level})</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='metric-container'>
            <div class='metric-box'>
                <div class='metric-label'>WINS</div>
                <div class='metric-val' style='color:#10b981;'>{st.session_state.user_wins}</div>
            </div>
            <div class='metric-box'>
                <div class='metric-label'>LOSSES</div>
                <div class='metric-val' style='color:#f43f5e;'>{st.session_state.user_losses}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    pred_display_u = st.session_state.user_pred if st.session_state.user_pred else "WAITING..."
    pred_full_u = "BIG (5-9)" if pred_display_u == "B" else ("SMALL (0-4)" if pred_display_u == "S" else "WAITING FOR 3 INPUTS")
    st.markdown(f"""
        <div class='pred-card'>
            <div style='font-size: 13px; color: #fbbf24; font-weight: bold;'>NEXT PREDICTION</div>
            <div style='font-size: 32px; font-weight: 900; color: #FFFFFF; margin: 10px 0;'>{pred_full_u}</div>
            <div style='font-size: 14px; color: #38bdf8;'>8-Level Plan | Level <b>{st.session_state.user_level}</b> | Bet: <b>₹ {current_u_bet}</b></div>
        </div>
    """, unsafe_allow_html=True)

    def handle_user_click(val):
        cb = "BIG" if val >= 5 else "SMALL"
        cbs = "B" if val >= 5 else "S"
        bet = current_u_bet

        if st.session_state.user_pred is not None:
            if cbs == st.session_state.user_pred:
                st.session_state.user_wins += 1
                status = "🟢 WIN"
                st.session_state.user_wallet += bet
                st.session_state.user_level = 1
            else:
                st.session_state.user_losses += 1
                status = "🔴 LOSS"
                st.session_state.user_wallet -= bet
                st.session_state.user_level = st.session_state.user_level + 1 if st.session_state.user_level < 8 else 1
        else:
            if len(st.session_state.user_history) > 0:
                st.session_state.user_losses += 1
                status = "🔴 LOSS"
                st.session_state.user_wallet -= bet
                st.session_state.user_level = st.session_state.user_level + 1 if st.session_state.user_level < 8 else 1
            else:
                status = "➖ START"

        st.session_state.user_history.append(cbs)
        st.session_state.user_history_details.insert(0, {"num": val, "type": cb, "status": status})
        th_u = st.session_state.user_history

        if len(th_u) >= 3:
            st.session_state.user_pred = "S" if th_u[-1] == "B" else "B"
        else:
            st.session_state.user_pred = None

    st.markdown("### Numbers theranjedukkuka (0-9)")
    nums_u = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in nums_u:
        if st.button(str(n), key=f"u_{n}", use_container_width=True):
            handle_user_click(n)
            st.rerun()

    st.markdown("### 📊 History")
    if st.session_state.user_history_details:
        for item in st.session_state.user_history_details[:10]:
            st_color = "win-text" if "WIN" in item['status'] else ("loss-text" if "LOSS" in item['status'] else "")
            st.markdown(f"""
                <div class='history-card'>
                    <div>Number: <b>{item['num']}</b> ({item['type']})</div>
                    <div class='{st_color}'>{item['status']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Ithuvare history onnumilla.")
            
