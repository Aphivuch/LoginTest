import streamlit as st

# --- 🎨 ตั้งค่าหน้าเว็บ (Config) ---
st.set_page_config(page_title="Corporate Login System", page_icon="🏢", layout="wide")

# --- 🖌️ Custom CSS เพื่อให้ทุกอย่างอยู่ตรงกลางและใหญ่ขึ้น ---
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        font-size: 20px;
        padding: 15px;
    }
    .stButton > button {
        height: 3em;
        font-size: 20px !important;
        background-color: #004aad !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_stdio=True)

# --- 📐 จัด Layout กึ่งกลาง ---
# ใช้ columns 3 ช่อง (สัดส่วน 1:2:1) เพื่อให้เนื้อหาหลักอยู่ในช่องกลางที่กว้างกว่า
col1, col2, col3 = st.columns([1, 1.5, 1])

with col2:
    # 1. เพิ่มรูปสัญลักษณ์ (Logo/Symbol)
    # ใช้รูปสัญลักษณ์จากระบบที่ดูเป็นทางการ
    st.image("http://googleusercontent.com/image_collection/image_retrieval/7053439828386315202", width=150)

    st.title("ระบบเข้าสู่ระบบส่วนกลาง")
    st.write("โปรดระบุข้อมูลประจำตัวของคุณเพื่อเข้าสู่ระบบพิมพ์เขียว")

    # 2. สร้างกล่อง Login (ใหญ่และอยู่ตรงกลาง)
    with st.container(border=True):
        ID = st.text_input("User_ID:")
        Password = st.text_input("Password:", type="password")

        # ปุ่มกดขยายเต็มความกว้าง
        submit_button = st.button("LOG IN", use_container_width=True)

    # --- 🧠 Logic การตรวจสอบ (ดั้งเดิมของคุณ) ---
    if submit_button:
        if ID == "Account1" and Password == "pass1":
            st.success(f"🔓 Login Successful: ยินดีต้อนรับ User {ID}")
            st.balloons()

        elif ID == "Account2" and Password == "pass2":
            st.success(f"🔓 Login Successful: ยินดีต้อนรับ User {ID}")
            st.balloons()

        elif ID == "Account3" and Password == "pass3":
            st.success(f"🔓 Login Successful: ยินดีต้อนรับ User {ID}")
            st.balloons()

        elif ID == "Account4" and Password == "pass4":
            st.success(f"🔓 Login Successful: ยินดีต้อนรับ User {ID}")
            st.balloons()

        else:
            st.error(f"❌ Login Failed: User {ID if ID else 'Unknown'} - โปรดตรวจสอบข้อมูลอีกครั้ง")

# --- ส่วนท้าย (Footer) ---
st.markdown("---")
st.caption("© 2026 Your Company Name - Corporate Login Blueprint")