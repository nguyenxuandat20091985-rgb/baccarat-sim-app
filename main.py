import streamlit as st
import numpy as np

# Thiết lập giao diện tối giản nhất cho cửa sổ nhỏ
st.set_page_config(page_title="MINI AI Baccarat", layout="centered")

st.markdown("""
    <style>
    /* Ép giao diện cực gọn */
    .block-container { padding: 10px !important; }
    .stButton>button { height: 40px; font-size: 14px !important; margin-bottom: 5px; }
    .stMetric { padding: 5px !important; }
    h2, h3 { font-size: 18px !important; margin-bottom: 10px !important; text-align: center; }
    .roadmap-container { 
        display: flex; flex-wrap: wrap; gap: 3px; 
        background: #111; padding: 8px; border-radius: 5px;
    }
    .dot { height: 12px; width: 12px; border-radius: 50%; }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state: st.session_state.history = []

# --- GIAO DIỆN MINI ---
st.markdown("### 🤖 AI PREDICT")

# Dự đoán siêu gọn
if len(st.session_state.history) > 0:
    p_count = st.session_state.history.count("P")
    b_count = st.session_state.history.count("B")
    advice = "BANKER" if b_count <= p_count else "PLAYER"
    color = "#ef4444" if advice == "BANKER" else "#3b82f6"
    st.markdown(f"<h2 style='color: {color}; margin: 0;'>{advice}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h4 style='text-align:center;'>WAIT...</h4>", unsafe_allow_html=True)

# Nút bấm dàn hàng ngang cho tiết kiệm diện tích
c1, c2, c3 = st.columns(3)
if c1.button("P"): st.session_state.history.append("P")
if c2.button("B"): st.session_state.history.append("B")
if c3.button("T"): st.session_state.history.append("T")

# Roadmap mini
roadmap_html = "".join([f"<div class='dot' style='background:{'#ef4444' if x=='B' else '#3b82f6' if x=='P' else '#10b981'};'></div>" for x in st.session_state.history[-24:]])
st.markdown(f"<div class='roadmap-container'>{roadmap_html}</div>", unsafe_allow_html=True)

# Nút Reset nhỏ
if st.button("RESET", type="primary"):
    st.session_state.history = []
    st.rerun()
