import streamlit as st

# --- จัดหน้าเว็บให้อยู่ตรงกลางและดูเป็นระบบ ---
# ใช้ st.container เพื่อตีกรอบให้เป็นสัดส่วน ไม่กระจัดกระจาย
with st.container(border=True):
    # ช่องรับข้อมูลแบบกระชับ
    ID = st.text_input("User_ID: ")
    Password = st.text_input("Password: ", type="password")

    # ปุ่มกดแบบ Primary (จะขึ้นสีเด่นขึ้นมา ไม่ทื่อเหมือนเดิม)
    submit_button = st.button("เข้าสู่ระบบ", type="primary", use_container_width=True)

# --- ส่วนของการประมวลผล Logic ของคุณเป๊ะๆ ---
if submit_button:
    # สร้างกล่องข้อความแจ้งเตือนด้านล่างเพื่อความสวยงาม
    with st.container():
        if ID == "Account1" and Password == "pass1":
            st.success(f"Login Successful User {ID}")

        elif ID == "Account2" and Password == "pass2":
            st.success(f"Login Successful User {ID}")

        elif ID == "Account3" and Password == "pass3":
            st.success(f"Login Successful User {ID}")

        elif ID == "Account4" and Password == "pass4":
            st.success(f"Login Successful User {ID}")

        else:
            st.error(f"Login Failed User {ID} - Please try again.")