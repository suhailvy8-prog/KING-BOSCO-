import streamlit as st
import collections

st.set_page_config(page_title="JAI CLUB PRO", page_icon="🎯", layout="centered")

st.markdown("<h2 style='text-align: center; color: #2E7D32;'>🎯 JAI CLUB PRO PREDICTOR</h2>", unsafe_allow_html=True)

# ----------------- ACCESS KEYS LIST -----------------
ALLOWED_KEYS = [
    "JAI101",
    "JAI102",
    "VIP2026"
]

st.sidebar.title("🔐 Access Control")
user_key = st.sidebar.text_input("നിങ്ങളുടെ Access Key നൽകുക:", type="password")

if user_key not in ALLOWED_KEYS:
    st.warning("🔒 ദയവായി ശരിയായ Access Key നൽകുക.")
    st.info("നിങ്ങൾക്ക് ആക്സസ് ഇല്ലെങ്കിൽ അഡ്മിനുമായി ബന്ധപ്പെടുക.")
    st.stop()

st.sidebar.success("✅ Access Granted!")

# ----------------- MAIN TOOL LOGIC -----------------
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

if st.button("🔄 Reset All Data"):
    st.session_state.history = []
    st.session_state.num_history = []
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.last_prediction = None
    st.rerun()

st.divider()

num_input = st.number_input("വന്ന നമ്പർ നൽകുക (0 - 9):", min_value=0, max_value=9, step=1)

if st.button("Submit Result"):
    val = int(num_input)
    current_bs = "B" if val >= 5 else "S"

    if st.session_state.last_prediction is not None:
        if current_bs == st.session_state.last_prediction:
            st.session_state.wins += 1
            st.success("✨ WIN! ✨")
        else:
            st.session_state.losses += 1
            st.error("❌ LOSS! ❌")

    st.session_state.history.append(current_bs)
    st.session_state.num_history.append(val)

    hist = st.session_state.history
    num_hist = st.session_state.num_history

    if len(hist) < 3:
        st.info(f"കുറഞ്ഞത് {3 - len(hist)} ഡാറ്റ കൂടി നൽകുക...")
        st.session_state.last_prediction = None
    else:
        last_three = "".join(hist[-3:])
        last_four = "".join(hist[-4:]) if len(hist) >= 4 else ""

        # 5-Level Safe Logic
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
        st.markdown(f"### NEXT PREDICTION: **{pred_text}**")
        st.write(f"📊 **Likely Numbers (0-9):** {likely_nums}")

st.divider()
st.caption("History: " + " -> ".join(st.session_state.history[-10:]))
