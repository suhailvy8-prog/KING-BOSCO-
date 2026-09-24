import streamlit as st

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

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
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 KING BOSCO PREDICTOR</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #38bdf8; font-size: 16px;'>Access Key ලබා ගැනීමට অনুগ্রহ করে അഡ്മിനെ ബന്ധപ്പെടുക (Contact Admin for Access Key)</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #475569;'>", unsafe_allow_html=True)
    
    # Order: 1. User Section, 2. Admin Section, 3. Target Section
    tab_user, tab_admin, tab_target = st.tabs(["👤 1. User Access", "🛠️ 2. Admin Access", "🎯 3. Target Access"])
    
    with tab_user:
        st.markdown("### User Key നൽകി പ്രവേശിക്കുക")
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

    with tab_admin:
        st.markdown("### Admin Key നൽകി പ്രവേശിക്കുക")
        a_key_input = st.text_input("Enter Admin Key", type="password", key="login_a_key")
        if st.button("Login as Admin", use_container_width=True):
            if a_key_input in st.session_state.admin_keys:
                st.session_state.auth_role = 'admin'
                st.rerun()
            else:
                st.error("❌ തെറ്റായ അഡ്മിൻ പാസ്‌വേർഡ്!")

    with tab_target:
        st.markdown("### Target Key നൽകി പ്രവേശിക്കുക")
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
    
    st.stop()
    
