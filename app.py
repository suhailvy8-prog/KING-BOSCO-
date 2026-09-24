import streamlit as st
import random

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# Custom CSS for Professional Dark & Colorful UI
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #0B0E14, #1a1c29); }
    .stApp { background: linear-gradient(135deg, #0B0E14, #1a1c29); color: #FFFFFF; }
    .app-title {
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FF4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 28px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
    }
    .sub-text {
        text-align: center;
        color: #38bdf8;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 15px;
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
    .custom-box {
        background: linear-gradient(135deg, #1e1b4b, #311042);
        border: 2px solid #a855f7;
        padding: 20px;
        border-radius: 15px;
        color: #FFFFFF;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
        margin-bottom: 20px;
    }
    .prediction-display {
        background: linear-gradient(135deg, #065f46, #047857);
        border: 3px solid #34d399;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        color: #FFFFFF;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0 0 25px rgba(52, 211, 153, 0.5);
        margin: 15px 0;
    }
    .stat-box-win {
        background: linear-gradient(135deg, #065f46, #047857);
        border: 2px solid #34d399;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #FFFFFF;
    }
    .stat-box-loss {
        background: linear-gradient(135deg, #7f1d1d, #991b1b);
        border: 2px solid #f87171;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #FFFFFF;
    }
    .dark-data-box {
        background-color: #111827;
        border: 2px solid #4f46e5;
        padding: 15px;
        border-radius: 12px;
        color: #34d399;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Session states initialization
if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["bosco123"]
if 'used_keys' not in st.session_state:
    st.session_state.used_keys = set()
if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

# User Section States
if 'user_level' not in st.session_state:
    st.session_state.user_level = 1
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 1000.0
if 'custom_bet' not in st.session_state:
    st.session_state.custom_bet = 10.0
if 'win_count' not in st.session_state:
    st.session_state.win_count = 0
if 'loss_count' not in st.session_state:
    st.session_state.loss_count = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = "നമ്പർ തിരഞ്ഞെടുത്ത് പ്രെഡിക്ഷൻ എടുക്കുക"

# ==================== 1. LOGIN PAGE ====================
if st.session_state.auth_role is None:
    st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>Access Key ലഭിക്കാൻ അഡ്മിനെ ബന്ധപ്പെടുക</div>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #475569;'>", unsafe_allow_html=True)
    
    tab_user, tab_admin, tab_target = st.tabs(["👤 1. User Access", "🛠️ 2. Admin Access", "🎯 3. Target Access"])
    
    with tab_user:
        st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
        st.markdown("### 👤 User Key നൽകി പ്രവേശിക്കുക")
        u_key_input = st.text_input("Enter User Key", type="password", key="login_u_key")
        if st.button("Login as User", use_container_width=True):
            if u_key_input in st.session_state.user_keys:
                if u_key_input in st.session_state.used_keys:
                    st.error("❌ ഈ കീ ഇതിനകം ഉപയോഗിച്ചതാണ്!")
                else:
                    st.session_state.used_keys.add(u_key_input)
                    st.session_state.auth_role = 'user'
                    st.rerun()
            else:
                st.error("❌ തെറ്റായ യൂസർ കീ!")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_admin:
        st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
        st.markdown("### 🛠️ Admin Access (bosco123)")
        a_key_input = st.text_input("Enter Admin Key", type="password", key="login_a_key")
        if st.button("Login as Admin", use_container_width=True):
            if a_key_input in st.session_state.admin_keys:
                st.session_state.auth_role = 'admin'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ അഡ്മിൻ കീ!")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_target:
        st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
        st.markdown("### 🎯 Target Key നൽകി പ്രവേശിക്കുക")
        t_key_input = st.text_input("Enter Target Key", type="password", key="login_t_key")
        if st.button("Login as Target", use_container_width=True):
            if t_key_input in st.session_state.target_keys:
                if t_key_input in st.session_state.used_keys:
                    st.error("❌ ഈ ടാർഗറ്റ് കീ ഇതിനകം ഉപയോഗിച്ചതാണ്!")
                else:
                    st.session_state.used_keys.add(t_key_input)
                    st.session_state.auth_role = 'target'
                    st.rerun()
            else:
                st.error("❌ തെറ്റായ ടാർഗറ്റ് കീ!")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.stop()

# ==================== 2. ADMIN PANEL SECTION ====================
if st.session_state.auth_role == 'admin':
    st.markdown("<div class='app-title'>🛠️ KING BOSCO ADMIN PANEL</div>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #475569;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
        st.subheader("➕ പുതിയ കീ ചേർക്കുക")
        new_key_type = st.selectbox("Key Type", ["User Key", "Target Key"])
        new_key_val = st.text_input("Enter New Key Value")
        
        if st.button("Add Key", use_container_width=True):
            if new_key_val:
                if new_key_type == "User Key":
                    if new_key_val not in st.session_state.user_keys:
                        st.session_state.user_keys.append(new_key_val)
                        st.success(f"✅ User Key '{new_key_val}' വിജയകരമായി ചേർത്തു!")
                    else:
                        st.warning("⚠️ ഈ കീ നിലവിലുണ്ട്!")
                else:
                    if new_key_val not in st.session_state.target_keys:
                        st.session_state.target_keys.append(new_key_val)
                        st.success(f"✅ Target Key '{new_key_val}' വിജയകരമായി ചേർത്തു!")
                    else:
                        st.warning("⚠️ ഈ കീ നിലവിലുണ്ട്!")
            else:
                st.error("❌ ദയവായി കീ നൽകുക!")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
        st.subheader("🗑️ കീ ബ്ലോക്ക് ചെയ്യുക / നീക്കം ചെയ്യുക")
        all_keys_list = st.session_state.user_keys + st.session_state.target_keys
        key_to_remove = st.selectbox("Select Key to Block/Delete", all_keys_list if all_keys_list else ["No Keys Available"])
        
        if st.button("Block/Delete Key", use_container_width=True):
            if key_to_remove in st.session_state.user_keys:
                st.session_state.user_keys.remove(key_to_remove)
                if key_to_remove in st.session_state.used_keys:
                    st.session_state.used_keys.remove(key_to_remove)
                st.success(f"🚫 User Key '{key_to_remove}' ബ്ലോക്ക് ചെയ്തു!")
                st.rerun()
            elif key_to_remove in st.session_state.target_keys:
                st.session_state.target_keys.remove(key_to_remove)
                if key_to_remove in st.session_state.used_keys:
                    st.session_state.used_keys.remove(key_to_remove)
                st.success(f"🚫 Target Key '{key_to_remove}' ബ്ലോക്ക് ചെയ്തു!")
                st.rerun()
            else:
                st.error("❌ കീ കണ്ടെത്താൻ കഴിഞ്ഞില്ല!")
        st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🚪 Logout Admin", use_container_width=True):
        st.session_state.auth_role = None
        st.rerun()
        
    st.stop()

# ==================== 3. USER SECTION ====================
if st.session_state.auth_role == 'user':
    st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>User Section - 8 Level Smart Prediction Plan</div>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #475569;'>", unsafe_allow_html=True)
    
    # 1. Win / Loss Count Side-by-Side Boxes
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.markdown(f"<div class='stat-box-win'>✅ WIN Count: {st.session_state.win_count}</div>", unsafe_allow_html=True)
    with col_stat2:
        st.markdown(f"<div class='stat-box-loss'>❌ LOSS Count: {st.session_state.loss_count}</div>", unsafe_allow_html=True)
    
    st.write("")
    
    # 2. Wallet & Custom Bet Input
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.markdown(f"<div class='dark-data-box' style='padding: 10px;'>💰 Wallet: ₹ {st.session_state.wallet_balance}</div>", unsafe_allow_html=True)
    with col_w2:
        st.session_state.custom_bet = st.number_input("Custom Bet Amount", min_value=1.0, value=float(st.session_state.custom_bet), step=10.0)

    # Current Level & Bet Amount
    current_active_bet = st.session_state.custom_bet * (2 ** (st.session_state.user_level - 1))
    st.markdown(f"<div class='dark-data-box'>📈 നിലവിലെ ലെവൽ: Level {st.session_state.user_level} / 8 &nbsp;|&nbsp; 💵 ബെറ്റ് തുക: ₹ {current_active_bet}</div>", unsafe_allow_html=True)

    # 3. PREDICTION DISPLAY (Mugalilayittu)
    st.markdown(f"<div class='prediction-display'>{st.session_state.last_prediction}</div>", unsafe_allow_html=True)

    # 4. Number Grid (0 to 9 with colors)
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.subheader("🔢 0 മുതൽ 9 വരെയുള്ള നമ്പറുകൾ തിരഞ്ഞെടുക്കുക")
    
    cols_n = st.columns(5)
    selected_numbers = []
    
    num_colors = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899", "#06b6d4", "#84cc16", "#eab308", "#6366f1"]
    
    for i in range(10):
        with cols_n[i % 5]:
            if st.checkbox(f"Num {i}", key=f"grid_num_{i}"):
                selected_numbers.append(i)

    st.markdown("</div>", unsafe_allow_html=True)

    # Prediction Action Button
    if st.button("🔮 പ്രെഡിക്ഷൻ പരിശോധിക്കുക (Get Prediction)", use_container_width=True):
        if len(selected_numbers) == 0:
            st.warning("⚠️ ദയവായി ഏതെങ്കിലും നമ്പറുകൾ തിരഞ്ഞെടുക്കൂ!")
        else:
            total_sum = sum(selected_numbers)
            if len(selected_numbers) >= 3 and all(n == selected_numbers[0] for n in selected_numbers):
                st.session_state.last_prediction = "⚠️ SKIP (ട്രെൻഡ് വ്യക്തമല്ല)"
            else:
                res = "BIG 🟢" if total_sum % 2 != 0 else "SMALL 🔴"
                st.session_state.last_prediction = f"🎯 ഫലം: {res} (Level {st.session_state.user_level})"
                st.session_state.history.append(f"Level {st.session_state.user_level} -> {res}")
            st.rerun()

    # Win / Loss Control Buttons for Level Progression
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🟢 WIN (വിൻ അടിച്ചു)", use_container_width=True):
            st.session_state.wallet_balance += current_active_bet
            st.session_state.win_count += 1
            st.session_state.user_level = 1  # Reset to Level 1 on Win
            st.success("🎉 വിജയം! ലെവൽ 1 ലേക്ക് റീസെറ്റ് ചെയ്തു.")
            st.rerun()
            
    with col_btn2:
        if st.button("🔴 LOSS (ലോസ് അടിച്ചു)", use_container_width=True):
            st.session_state.wallet_balance -= current_active_bet
            st.session_state.loss_count += 1
            if st.session_state.user_level < 8:
                st.session_state.user_level += 1  # Move to next level
                st.warning(f"⚠️ ലോസ്! അടുത്ത ലെവലിലേക്ക് ഉയർന്നു: Level {st.session_state.user_level}")
            else:
                st.error("🚨 മാക്സിമം ലെവൽ 8 എത്തി! വീണ്ടും ലെവൽ 1 ലേക്ക് മാറ്റുന്നു.")
                st.session_state.user_level = 1
            st.rerun()

    # History Section
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.subheader("📜 പ്രെഡിക്ഷൻ ഹിസ്റ്ററി (History)")
    if st.session_state.history:
        for h in reversed(st.session_state.history[-5:]):
            st.write(f"• {h}")
    else:
        st.write("ഇതുവരെ ഹിസ്റ്ററി ഒന്നുമില്ല.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚪 Logout User", use_container_width=True):
        st.session_state.auth_role = None
        st.rerun()
        
    st.stop()
                        
