import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Mẹ & Bé", layout="centered")
st.title("🤱 AI tạo kịch bản mẹ & bé")

st.write("👉 Nhập API key và bấm nút để test")

api_key = st.text_input("OpenAI API Key", type="password")

if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

topic = st.text_input(
    "Chủ đề video",
    "Chăm sóc bé 1–3 tháng tuổi"
)

if st.button("TẠO KỊCH BẢN"):
    with st.spinner("AI đang tạo nội dung..."):
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia chăm sóc mẹ và bé."},
                {"role": "user", "content": f"Viết kịch bản video 30 giây về: {topic}"}
            ]
        )

        st.success("Hoàn thành")
        st.write(res.choices[0].message.content)
