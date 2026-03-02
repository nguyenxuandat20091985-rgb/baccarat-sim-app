import streamlit as st

st.set_page_config(page_title="GỠ VỐN BACCARAT", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000; }
    /* Nút bấm dàn ngang, cực gọn để không che màn hình */
    .stButton>button {
        height: 60px !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        border-radius: 10px !important;
        color: white !important;
        margin-bottom: 0px !important;
    }
    /* Màu sắc rực rỡ nhất */
    div.stButton > button:first-child { background-color: #0055ff !important; border: 2px solid white !important; } /* CON */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button { background-color: #ff0000 !important; border: 2px solid white !important; } /* CÁI */
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) button { background-color: #00aa00 !important; border: 2px solid white !important; } /* HÒA */
    
    .predict-text {
        text-align: center; color: yellow; font-size: 28px; 
        font-weight: bold; background: #222; border-radius: 10px; padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state: st.session_state.history = []

# --- DỰ ĐOÁN SIÊU GỌN ---
if len(st.session_state.history) > 0:
    p_count = st.session_state.history.count("CON")
    b_count = st.session_state.history.count("CÁI")
    advice = "CÁI" if b_count <= p_count else "CON"
    st.markdown(f"<div class='predict-text'>ĐÁNH: {advice}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='predict-text'>NHẬP CẦU ĐÊ...</div>", unsafe_allow_html=True)

# --- 3 NÚT DÀN HÀNG NGANG ---
st.write("")
c1, c2, c3 = st.columns(3)
if c1.button("CON"): st.session_state.history.append("CON")
if c2.button("CÁI"): st.session_state.history.append("CÁI")
if c3.button("HÒA"): st.session_state.history.append("HÒA")

# --- NÚT RESET NHỎ ---
if st.button("RESET", type="primary"):
    st.session_state.history = []
    st.rerun()
