import streamlit as st
import collections

st.set_page_config(page_title="KING BOSCO PREDICTOR", page_icon="👑", layout="centered")

# Custom CSS for Professional Dark VIP Theme & Mobile Optimization
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    div[data-testid="stMetricValue"] { font-size: 26px; font-weight: bold; text-align: center; }
    
    /* Number Input Field Styling */
    input[type="text"] {
        text-align: center !important;
        font-size: 20px !important;
        font-weight: bold !important;
    }

    /* Prediction Card */
    .pred-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #334155;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
    }

    /* History Cards */
    .history-card {
        background-color: #1e293b;
        padding: 12px 16px;
        border-radius: 10px;
        margin-bottom: 8px;
        border-left: 5px solid #3b82f6;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #FFD700;'>👑 KING BOSCO PREDICTOR</h2>", unsafe_allow_html=True)

# ----------------- ACCESS KEYS LIST -----------------
# വേണ്ടാത്ത കീ ഇവിടുന്ന് ഡിലീറ്റ് ചെയ്യാം
ALLOWED_KEYS = [
    "JAI101",
    "JAI102",
    "VIP2026"
]

st.sidebar.title("🔐 Access Control")
user_key = st.sidebar.text_input("Access Key നൽകുക:", type="password")

if user_key not in ALLOWED_KEYS:
    st.warning("🔒 ദയവായി ശരിയായ Access Key നൽകുക.")
    st.info("ആക്സസ് ലഭിക്കാൻ അഡ്മിനുമായി ബന്ധപ്പെടുക.")
    st.stop()

st.sidebar.success("✅ Access Granted!")

# ----------------- MAIN LOGIC -----------------
if 'history_details' not in st.session_state:
    st.session_state.history_details = []
if 'history' not in st.session_state:
    st.session_state.history = []
if 'num_history' not in st.session_state:
    st.session_state.num_history = []
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'losses' not in st.session_state:
    st.session_state.losses = 0
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = None

col1, col2 = st.columns(2)
col1.metric("WINS 🟢", st.session_state.wins)
col2.metric("LOSSES 🔴", st.session_state.losses)

if st.button("🔄 Reset Data", use_container_width=True):
    st.session_state.history_details = []
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.last_prediction = None
    st.rerun()

st.divider()

# നമ്പർ എൻട്രി
num_input = st.text_input("വന്ന നമ്പർ നൽകുക (0 - 9):", value="", max_chars=1)

if st.button("Submit Result", use_container_width=True, type="primary"):
    if num_input.isdigit() and 0 <= int(num_input) <= 9:
        val = int(num_input)
        current_bs = "BIG" if val >= 5 else "SMALL"
        current_bs_short = "B" if val >= 5 else "S"

        status_str = ""
        if st.session_state.last_prediction is not None:
            if current_bs_short == st.session_state.last_prediction:
                st.session_state.wins += 1
                st.success("✨ WIN! ✨")
                status_str = "🟢 WIN"
            else:
                st.session_state.losses += 1
                st.error("❌ LOSS! ❌")
                status_str = "🔴 LOSS"

        st.session_state.history.append(current_bs_short)
        st.session_state.num_history.append(val)
        
        # ഹിസ്റ്ററി ലിസ്റ്റിലേക്ക് വരിവരിയായി ചേർക്കുന്നു
        st.session_state.history_details.insert(0, {
            "num": val,
            "type": current_bs,
            "status": status_str
        })

        hist = st.session_state.history
        num_hist = st.session_state.num_history

        if len(hist) < 3:
            st.info(f"കുറഞ്ഞത് {3 - len(hist)} ഡാറ്റ കൂടി നൽകുക...")
            st.session_state.last_prediction = None
        else:
            last_three = "".join(hist[-3:])
            last_four = "".join(hist[-4:]) if len(hist) >= 4 else ""

            if last_four == "BBBB":
                next_pred = "S"
            elif last_four == "SSSS":
                next_pred = "B"
            elif last_three == "BBB":
                next_pred = "B"
            elif last_three == "SSS":
                next_pred = "S"
            else:
                recent_bs = hist[-5:]
                b_count = recent_bs.count('B')
                s_count = recent_bs.count('S')
                next_pred = "B" if b_count >= s_count else "S"

            st.session_state.last_prediction = next_pred

            num_counts = collections.Counter(num_hist[-15:])
            likely_nums = [n for n, c in num_counts.most_common(2)]

            pred_text = "BIG 🟢" if next_pred == "B" else "SMALL 🔴"
            color_code = "#00E676" if next_pred == "B" else "#FF5252"

            st.markdown(f"""
                <div class="pred-card">
                    <div style="color: #94a3b8; font-size: 13px; text-transform: uppercase;">NEXT PREDICTION</div>
                    <div style="font-size: 34px; font-weight: 800; color: {color_code}; margin: 8px 0;">{pred_text}</div>
                    <div style="color: #cbd5e1; font-size: 14px;">📊 Likely Numbers: <b>{likely_nums}</b></div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("0 മുതൽ 9 വരെയുള്ള ഒരു നമ്പർ മാത്രം ടൈപ്പ് ചെയ്യുക.")

st.divider()

# അടിയ്ക്ക് അടിയായി ബോക്സുകളിൽ വരുന്ന ഹിസ്റ്ററി
if st.session_state.history_details:
    st.markdown("### 📜 History Logs")
    for item in st.session_state.history_details[:10]:
        st.markdown(f"""
            <div class="history-card">
                <span><b>Number: {item['num']}</b> ({item['type']})</span>
                <span><b>{item['status']}</b></span>
            </div>
        """, unsafe_allow_html=True)
        
