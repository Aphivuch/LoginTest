import streamlit as st

# --- ตั้งค่าหน้าเว็บให้มีช่องรับข้อมูล (มาแทน input) ---
ID = st.text_input("User_ID: ")
Password = st.text_input("Password: ", type="password")

# --- เติมปุ่มกดตามที่ต้องการ ---
if st.button("เข้าสู่ระบบ"):

    # โครงสร้าง Logic if-elif-else ดั้งเดิมของคุณเป๊ะๆ
    if ID == "Account1" and Password == "pass1":
        st.write(f"Login Successful User {ID}")

    elif ID == "Account2" and Password == "pass2":
        st.write(f"Login Successful User {ID}")

    elif ID == "Account3" and Password == "pass3":
        st.write(f"Login Successful User {ID}")

    elif ID == "Account4" and Password == "pass4":
        st.write(f"Login Successful User {ID}")

    else:
        st.write(f"Login Failed User {ID} - Please try again.")