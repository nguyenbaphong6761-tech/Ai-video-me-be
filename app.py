import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Video Mẹ & Bé", layout="centered")
st.title("🤱 AI Tạo Kịch Bản + Ảnh Video Mẹ & Bé")

api_key = st.text_input("🔑 Nhập OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    topic = st.text_area(
        "📌 Nhập chủ đề video",
        "Chăm sóc bé 1–3 tháng tuổi ngủ ngon ban đêm"
    )

    if st.button("🚀 Tạo kịch bản & hình ảnh"):
        with st.spinner("AI đang xử lý..."):

            # 1️⃣ Tạo kịch bản + prompt ảnh
            script_prompt = f"""
            Viết:
            1. Kịch bản video ngắn 30–45s cho chủ đề: {topic}
            2. Prompt tạo ảnh minh họa cho video (phong cách dễ thương, thực tế)

            Trình bày rõ ràng.
            """

            script_res = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là chuyên gia nội dung mẹ và bé."},
                    {"role": "user", "content": script_prompt}
                ]
            )

            result_text = script_res.choices[0].message.content
            st.subheader("📜 KỊCH BẢN & PROMPT")
            st.markdown(result_text)

            # 2️⃣ Prompt ảnh đơn giản (có thể nâng cấp sau)
            image_prompt = f"""
            A realistic, warm illustration of a baby 1-3 months old,
            Vietnamese family style, soft light, clean home,
            vertical 9:16, high quality
            """

            image = client.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="1024x1024"
            )

            st.subheader("🖼️ ẢNH MINH HỌA")
            st.image(image.data[0].url)

        st.success("✅ Hoàn thành")
else:
    st.info("👉 Vui lòng nhập OpenAI API Key để bắt đầu")
