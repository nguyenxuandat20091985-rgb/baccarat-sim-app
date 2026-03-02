import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Baccarat Pro - Realtime Tool", layout="wide")

# Khởi tạo bộ nhớ tạm cho phiên chơi
if 'history' not in st.session_state:
    st.session_state.history = []
if 'balance' not in st.session_state:
    st.session_state.balance = 0.0

st.title("🚀 AI Baccarat Real-time Predictor")
st.write("Nhập kết quả thực tế từ bàn chơi để nhận dự đoán.")

# Layout chính: 2 cột
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🎮 Nhập kết quả")
    c1, c2, c3 = st.columns(3)
    if c1.button("P (Player)", use_container_width=True):
        st.session_state.history.append("P")
    if c2.button("B (Banker)", use_container_width=True):
        st.session_state.history.append("B")
    if c3.button("T (Tie)", use_container_width=True):
        st.session_state.history.append("T")
    
    if st.button("Xóa ván cuối"):
        if st.session_state.history: st.session_state.history.pop()
    if st.button("Reset phiên chơi", type="primary"):
        st.session_state.history = []

with col2:
    st.subheader("📊 Phân tích & Dự đoán")
    if len(st.session_state.history) > 0:
        # Thuật toán dự đoán đơn giản: Theo đuôi (Trend following)
        last_result = st.session_state.history[-1]
        next_bet = "Player" if last_result == "P" else "Banker"
        if last_result == "T": next_bet = "Đợi ván sau"
        
        st.success(f"🔥 Gợi ý ván tiếp theo: **{next_bet}**")
        
        # Hiển thị Roadmap đơn giản
        st.write("Lịch sử cầu:")
        roadmap_str = " ➡️ ".join([f"[{res}]" for res in st.session_state.history[-10:]])
        st.info(roadmap_str)
    else:
        st.warning("Hãy nhập ít nhất 1 ván để bắt đầu dự đoán.")

# Phần quản lý vốn (Money Management)
st.divider()
st.subheader("💰 Quản lý vốn Martingale")
base_money = st.number_input("Tiền cược cơ sở (VND)", value=10000)

# Tính toán mức cược dựa trên chuỗi thua
lose_count = 0
for res in reversed(st.session_state.history):
    # Giả định chiến thuật là đánh theo đuôi, nếu kết quả ngược lại là thua
    if len(st.session_state.history) < 2: break
    # Đây là logic minh họa cho chuỗi thua
    break 

current_bet = base_money * (2 ** lose_count)
st.metric("Lệnh cược tiếp theo", f"{current_bet:,} VND")

st.caption("Lưu ý: Tool dựa trên xác suất thống kê. Không có gì là 100%. Hãy chơi có trách nhiệm!")
