import streamlit as st
import pandas as pd
import numpy as np

# Tối ưu giao diện Mobile & Dark Mode
st.set_page_config(page_title="VIP BACCARAT AI 2026", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #050a12; color: #e0e0e0; }
    .stButton>button { 
        border-radius: 8px; height: 50px; font-weight: 800; 
        border: 1px solid #333; transition: 0.3s;
    }
    .stMetric { background-color: #111827; border: 1px solid #1f2937; border-radius: 12px; padding: 15px; }
    .roadmap-dot {
        height: 18px; width: 18px; border-radius: 50%; display: inline-block;
        margin: 2px; border: 2px solid rgba(255,255,255,0.1);
    }
    .status-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 20px; border-radius: 15px; border-left: 5px solid #3b82f6; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state: st.session_state.history = []
if 'balance_history' not in st.session_state: st.session_state.balance_history = [0]

# --- TIÊU ĐỀ ---
st.markdown("<h2 style='text-align: center; color: #3b82f6;'>💎 VIP BACCARAT PREDICTOR</h2>", unsafe_allow_html=True)

# --- KHU VỰC DỰ ĐOÁN (TRUNG TÂM) ---
with st.container():
    st.markdown("<div class='status-card'>", unsafe_allow_html=True)
    if len(st.session_state.history) > 0:
        # Thuật toán AI giả lập: Soi cầu bệt/cầu nghiêng
        p_count = st.session_state.history.count("P")
        b_count = st.session_state.history.count("B")
        advice = "BANKER" if b_count <= p_count else "PLAYER"
        color = "#ef4444" if advice == "BANKER" else "#3b82f6"
        
        st.markdown(f"<h3 style='text-align: center; margin:0;'>AI DỰ ĐOÁN VÁN TIẾP</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: {color}; margin:10px 0;'>{advice}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; opacity: 0.7;'>Độ tin cậy: {min(50 + len(st.session_state.history)*2, 97)}%</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align: center;'>ĐANG CHỜ DỮ LIỆU...</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- NHẬP KẾT QUẢ (GỌN GÀNG) ---
cols = st.columns(3)
if cols[0].button("PLAYER", type="secondary"): 
    st.session_state.history.append("P")
    st.session_state.balance_history.append(st.session_state.balance_history[-1] + np.random.uniform(-1, 1.5))
if cols[1].button("BANKER", type="primary"): 
    st.session_state.history.append("B")
    st.session_state.balance_history.append(st.session_state.balance_history[-1] + np.random.uniform(-1, 1.5))
if cols[2].button("TIE"): 
    st.session_state.history.append("T")

# --- ROADMAP & BIỂU ĐỒ ---
st.write("---")
tab1, tab2 = st.tabs(["📊 ROADMAP", "📈 BIẾN ĐỘNG"])

with tab1:
    roadmap_html = ""
    for res in st.session_state.history[-36:]: # Hiển thị 36 ván gần nhất
        color = "#ef4444" if res == "B" else "#3b82f6" if res == "P" else "#10b981"
        roadmap_html += f"<span class='roadmap-dot' style='background-color:{color};'></span>"
    st.markdown(f"<div style='background:#111827; padding:15px; border-radius:10px;'>{roadmap_html}</div>", unsafe_allow_html=True)

with tab2:
    # Vẽ biểu đồ hình sin giống hình Store
    st.line_chart(st.session_state.balance_history, height=200)

# --- NÚT PHỤ ---
st.write("")
if st.button("🔄 LÀM MỚI BÀN CHƠI"):
    st.session_state.history = []
    st.session_state.balance_history = [0]
    st.rerun()
