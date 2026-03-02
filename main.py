import streamlit as st

# Ép giao diện về mức tối giản nhất có thể
st.set_page_config(page_title="TOOL GỠ", layout="centered")

st.markdown("""
    <style>
    /* Xóa bỏ mọi khoảng trắng thừa của Streamlit */
    .block-container { padding: 5px !important; }
    header, footer { visibility: hidden; }
    
    /* Nút bấm siêu to, chiếm trọn chiều ngang, không lo bị kẹt */
    .stButton>button {
        width: 100% !important;
        height: 70px !important;
        font-size: 25px !important;
        font-weight: 900 !important;
        color: white !important;
        border: 2px solid #fff !important;
        margin-bottom: 5px !important;
        display: block !important;
    }
    
    /* Màu sắc cực mạnh để nhìn xuyên thấu */
    div.stButton > button:first-child { background-color: #0033ff !important; } /* CON */
    div[data-testid="stHorizontalBlock"] + div .stButton > button { background-color: #ff0000 !important; } /* CÁI */
    
    .ai-box {
        background: yellow; color: black; 
        text-align: center; font-size: 30px; 
        font-weight: bold; border-radius: 10px;
        padding: 10px; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'h' not in st.session_state: st.session_state.h = []

# --- DÒNG DỰ ĐOÁN SIÊU TO ---
if len(st.session_state.h) > 0:
    p = st.session_state.h.count("P")
    b = st.session_state.h.count("B")
    txt = "ĐÁNH: CÁI" if b <= p else "ĐÁNH: CON"
    st.markdown(f"<div class='ai-box'>{txt}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='ai-box'>NHẬP CẦU ĐI</div>", unsafe_allow_html=True)

# --- NÚT BẤM DẠNG CỘT DỌC ĐỂ KHÔNG BỊ TRÀN ---
if st.button("CON (PLAYER)"): st.session_state.h.append("P")
if st.button("CÁI (BANKER)"): st.session_state.h.append("B")

col1, col2 = st.columns(2)
with col1:
    if st.button("HÒA"): st.session_state.h.append("T")
with col2:
    if st.button("XOÁ"): 
        if st.session_state.h: st.session_state.h.pop()
        st.rerun()

if st.button("RESET BÀN MỚI", type="primary"):
    st.session_state.h = []
    st.rerun()

st.write(f"Số ván đã nhập: {len(st.session_state.h)}")
