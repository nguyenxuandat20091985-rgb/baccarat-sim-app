import streamlit as st

# Cấu hình tối ưu hiển thị rực rỡ
st.set_page_config(page_title="TOOL BACCARAT VIP", layout="centered")

st.markdown("""
    <style>
    /* Nền tối sâu để nổi bật màu sắc */
    .main { background-color: #000000; }
    
    /* Định dạng nút nhấn siêu to */
    .stButton>button {
        height: 80px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        border: 2px solid #ffffff33 !important;
        color: white !important;
    }
    
    /* Màu sắc đặc trưng cho từng nút */
    div.stButton > button:first-child { background-color: #004dc2 !important; } /* CON - Xanh dương */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button { background-color: #c20000 !important; } /* CÁI - Đỏ */
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) button { background-color: #008000 !important; } /* HÒA - Xanh lá */
    
    /* Chấm Roadmap to rõ */
    .dot {
        height: 25px; width: 25px; border-radius: 50%;
        display: inline-block; margin: 3px;
        border: 2px solid #fff;
    }
    .status-box {
        background: #111; padding: 15px; border-radius: 15px;
        border: 2px solid #333; text-align: center; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state: st.session_state.history = []

# --- HIỂN THỊ DỰ ĐOÁN ---
st.markdown("<div class='status-box'>", unsafe_allow_html=True)
if len(st.session_state.history) > 0:
    # Logic soi cầu đơn giản
    p_count = st.session_state.history.count("CON")
    b_count = st.session_state.history.count("CÁI")
    advice = "CÁI (BANKER)" if b_count <= p_count else "CON (PLAYER)"
    adv_color = "#ff4b4b" if "CÁI" in advice else "#1c83e1"
    
    st.markdown(f"<h2 style='margin:0; color:white;'>AI DỰ BÁO:</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='margin:0; color:{adv_color}; font-size: 45px;'>{advice}</h1>", unsafe_allow_html=True)
else:
    st.markdown("<h2 style='color:gray;'>ĐANG ĐỢI DỮ LIỆU...</h2>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- NÚT BẤM TIẾNG VIỆT SIÊU TO ---
col1, col2, col3 = st.columns(3)
if col1.button("CON"): st.session_state.history.append("CON")
if col2.button("CÁI"): st.session_state.history.append("CÁI")
if col3.button("HÒA"): st.session_state.history.append("HÒA")

# --- LỊCH SỬ CẦU (ROADMAP CHẤM TRÒN TO) ---
st.write("")
roadmap_html = ""
for res in st.session_state.history[-18:]: # Hiện 18 ván gần nhất
    color = "#c20000" if res == "CÁI" else "#004dc2" if res == "CON" else "#008000"
    roadmap_html += f"<div class='dot' style='background-color:{color};'></div>"

st.markdown(f"<div style='background:#111; padding:10px; border-radius:10px; min-height:50px;'>{roadmap_html}</div>", unsafe_allow_html=True)

# --- NÚT RESET ---
st.write("")
if st.button("LÀM MỚI BÀN (RESET)", type="primary"):
    st.session_state.history = []
    st.rerun()
