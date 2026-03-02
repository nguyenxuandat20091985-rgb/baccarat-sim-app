import streamlit as st

# Cấu hình siêu gọn cho cửa sổ nhỏ
st.set_page_config(page_title="GỠ NỢ 2026", layout="centered")

st.markdown("""
    <style>
    /* Xóa sạch khoảng trống thừa */
    .block-container { padding: 0px !important; }
    header, footer { visibility: hidden; }
    
    /* Dòng AI dự đoán cực to màu Vàng rực */
    .ai-display {
        background-color: #000;
        color: #ffff00;
        text-align: center;
        font-size: 35px !important;
        font-weight: 900;
        padding: 15px;
        border-bottom: 3px solid #ffff00;
        margin-bottom: 10px;
    }
    
    /* Nút bấm khổng lồ, xếp dọc để không bao giờ bị kẹt */
    .stButton>button {
        width: 100% !important;
        height: 90px !important;
        font-size: 30px !important;
        font-weight: bold !important;
        color: white !important;
        border: 3px solid #fff !important;
        margin-bottom: 8px !important;
    }
    
    /* Màu sắc thực chiến */
    div.stButton > button:first-child { background-color: #0044ff !important; } /* CON */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) button { background-color: #ee0000 !important; } /* CÁI */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) button { background-color: #008800 !important; } /* HÒA */
    </style>
    """, unsafe_allow_html=True)

if 'h' not in st.session_state: st.session_state.h = []

# --- DÒNG DỰ ĐOÁN ĐẬP VÀO MẮT ---
if len(st.session_state.h) > 0:
    p = st.session_state.h.count("P")
    b = st.session_state.h.count("B")
    # Thuật toán AI cơ bản: Đánh vào bên đang yếu hơn (soi cầu nghiêng)
    advice = "CÁI" if b <= p else "CON"
    st.markdown(f"<div class='ai-display'>ĐÁNH: {advice}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='ai-display'>NHẬP CẦU</div>", unsafe_allow_html=True)

# --- NÚT BẤM DỌC - CHỐNG TRÀN MÀN HÌNH ---
if st.button("CON (PLAYER)"): 
    st.session_state.h.append("P")
    st.rerun()

if st.button("CÁI (BANKER)"): 
    st.session_state.h.append("B")
    st.rerun()

if st.button("HÒA (TIE)"): 
    st.session_state.h.append("T")
    st.rerun()

# Nút chức năng nhỏ bên dưới
col1, col2 = st.columns(2)
with col1:
    if st.button("XOÁ VÁN"): 
        if st.session_state.h: st.session_state.h.pop()
        st.rerun()
with col2:
    if st.button("RESET"): 
        st.session_state.h = []
        st.rerun()

st.write(f"Đã nhập: {len(st.session_state.h)} ván")
