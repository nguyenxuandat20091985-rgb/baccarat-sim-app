import streamlit as st
import pandas as pd

st.set_page_config(page_title="PRO BACCARAT PREDICTOR 2026", layout="wide")

# Giao diện Dark Mode chuyên nghiệp
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; font-weight: bold; }
    .stMetric { background-color: #1f2937; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state: st.session_state.history = []

st.title("🛡️ PRO BACCARAT PREDICTOR v2.0")
st.write("Dữ liệu nhập trực tiếp từ bàn chơi Real-time")

# Khu vực hiển thị Roadmap chuyên nghiệp
def draw_roadmap(history):
    if not history: return ""
    return " ".join([f"<span style='color:{'#ff4b4b' if x=='B' else '#31333f' if x=='T' else '#1c83e1'}; font-size:24px;'>●</span>" for x in history])

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⌨️ Nhập lệnh")
    c1, c2, c3 = st.columns(3)
    if c1.button("PLAYER", type="secondary"): st.session_state.history.append("P")
    if c2.button("BANKER", type="primary"): st.session_state.history.append("B")
    if c3.button("TIE"): st.session_state.history.append("T")
    
    if st.button("🔄 Reset bàn mới"): st.session_state.history = []
    st.info(f"Tổng ván đã nhập: {len(st.session_state.history)}")

with col2:
    st.subheader("📈 Phân tích AI & Cầu")
    st.markdown(draw_roadmap(st.session_state.history[-20:]), unsafe_allow_html=True)
    
    if len(st.session_state.history) > 2:
        # Thuật toán soi cầu giả lập chuyên nghiệp
        last = st.session_state.history[-1]
        p_count = st.session_state.history.count("P")
        b_count = st.session_state.history.count("B")
        
        # Dự đoán dựa trên xu hướng (Trend)
        advice = "BANKER" if b_count < p_count else "PLAYER"
        confidence = min(abs(p_count - b_count) * 20 + 50, 98)
        
        st.success(f"🎯 Gợi ý lệnh: **{advice}** | Độ tin cậy: **{confidence}%**")
        
        # Quản lý vốn theo Step (Giống hình anh gửi)
        step = (len([x for x in st.session_state.history if x != st.session_state.history[-1]]) % 5) + 1
        st.metric("Mức cược hiện tại (Martin Step)", f"Bước {step}")
    else:
        st.warning("Đang chờ dữ liệu bàn chơi...")

st.divider()
st.caption("Cảnh báo: Mọi thuật toán chỉ mang tính chất tham khảo dựa trên thống kê. Hãy quản lý vốn chặt chẽ.")
