import streamlit as st

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# Custom CSS for Dark, Colorful & Attractive UI
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #0B0E14, #1a1c29); }
    .stApp { background: linear-gradient(135deg, #0B0E14, #1a1c29); color: #FFFFFF; }
    .app-title {
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FF4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 30px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
    }
    .sub-text {
        text-align: center;
        color: #38bdf8;
        font-size: 14px;
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
    .stButton button:active, .stButton button:focus {
        border: 2px solid #FFD700 !important;
        color: #FFD700 !important;
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
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
    </style>
""", unsafe_allow_html=True)

# Session states initialization
if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["bosco123"]  # Admin key as requested
if 'used_keys' not in st.session_state:
    st.session_state.used_keys = set()
if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

# ==================== 1. LOGIN PAGE ====================
if st.session_state.auth_role is None:
    st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>Access Key ലഭിക്കാൻ അഡ്മിനെ ബന്ധപ്പെടുക (Contact Admin for Access Key)</div>", unsafe_allow_html=True)
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
    
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.subheader("📊 നിലവിലുള്ള കീകളുടെ വിവരങ്ങൾ")
    st.write("**User Keys:**", st.session_state.user_keys)
    st.write("**Target Keys:**", st.session_state.target_keys)
    st.write("**Used/Active Keys:**", list(st.session_state.used_keys))
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚪 Logout Admin", use_container_width=True):
        st.session_state.auth_role = None
        st.rerun()
        
    st.stop()
    
