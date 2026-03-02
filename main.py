import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Baccarat Simulator - Kỹ thuật vs May rủi", layout="wide")

st.title("🎰 Baccarat Strategy Simulator")
st.write("Công cụ mô phỏng để kiểm chứng xác suất thực tế.")

# Sidebar cấu hình
st.sidebar.header("Cấu hình mô phỏng")
init_balance = st.sidebar.number_input("Vốn ban đầu ($)", value=1000)
base_bet = st.sidebar.number_input("Tiền cược cơ sở ($)", value=10)
num_games = st.sidebar.slider("Số lượng ván chơi", 10, 1000, 100)
strategy = st.sidebar.selectbox("Chiến thuật", ["Đánh đều tay", "Gấp thếp (Martingale)"])

def simulate_baccarat(init_balance, base_bet, num_games, strategy):
    balance = init_balance
    history = []
    current_bet = base_bet
    
    # Tỷ lệ thực tế: Banker thắng ~45.8%, Player ~44.6%, Tie ~9.6%
    # (Loại bỏ Tie để đơn giản hóa, Banker/Player gần như 50/50 nhưng Banker mất phế)
    
    for i in range(num_games):
        if balance < current_bet:
            break
            
        win = random.choice([True, False]) # Mô phỏng tung đồng xu
        
        if win:
            # Nếu thắng, Banker thường chỉ ăn 0.95 (trừ phế 5%)
            balance += current_bet * 0.95 
            status = "Thắng"
            if strategy == "Gấp thếp (Martingale)":
                current_bet = base_bet
        else:
            balance -= current_bet
            status = "Thua"
            if strategy == "Gấp thếp (Martingale)":
                current_bet *= 2 # Thua thì gấp đôi
                
        history.append({"Ván": i+1, "Kết quả": status, "Tiền cược": current_bet, "Số dư": balance})
        
    return pd.DataFrame(history)

if st.button("Bắt đầu mô phỏng"):
    df = simulate_baccarat(init_balance, base_bet, num_games, strategy)
    
    # Hiển thị biểu đồ
    st.line_chart(df.set_index("Ván")["Số dư"])
    
    # Thống kê
    col1, col2 = st.columns(2)
    col1.metric("Số dư cuối cùng", f"{df['Số dư'].iloc[-1]:.2f} $")
    col2.metric("Lợi nhuận", f"{df['Số dư'].iloc[-1] - init_balance:.2f} $")
    
    st.write("### Chi tiết lịch sử ván đấu")
    st.dataframe(df)

st.info("💡 Lưu ý kỹ thuật: Anh sẽ thấy khi dùng 'Gấp thếp', biểu đồ có vẻ đi lên nhưng chỉ cần 1 chuỗi thua dài, số dư sẽ rơi thẳng xuống đáy (cháy túi).")
