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
        padding: 15px;
        border-radius: 12px;
        color: #FFFFFF;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Session states initialization
if 'user_keys' not in st.session_state:
    st.session_state.user_keys = ["bosco123", "rahul123"]
if 'target_keys' not in st.session_state:
    st.session_state.target_keys = ["target999"]
if 'admin_keys' not in st.session_state:
    st.session_state.admin_keys = ["admin123"]
if 'used_keys' not in st.session_state:
    st.session_state.used_keys = set()
if 'auth_role' not in st.session_state:
    st.session_state.auth_role = None

# Login Page Structure
if st.session_state.auth_role is None:
    st.markdown("<div class='app-title'>👑 KING BOSCO PREDICTOR</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>Access Key ലഭിക്കാൻ അഡ്മിനെ ബന്ധപ്പെടുക (Contact Admin for Access Key)</div>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #475569;'>", unsafe_allow_html=True)
    
    # Order: 1. User Section, 2. Admin Section, 3. Target Section
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
        st.markdown("### 🛠️ Admin Key നൽകി പ്രവേശിക്കുക")
        a_key_input = st.text_input("Enter Admin Key", type="password", key="login_a_key")
        if st.button("Login as Admin", use_container_width=True):
            if a_key_input in st.session_state.admin_keys:
                st.session_state.auth_role = 'admin'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ അഡ്മിൻ പാസ്‌വേർഡ്!")
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
    
