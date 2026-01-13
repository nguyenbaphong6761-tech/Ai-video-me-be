import streamlit as st
from openai import OpenAI
from openai import PermissionDeniedError

st.set_page_config(page_title="AI Mẹ & Bé", layout="centered")
st.title("🤱 AI Tạo Kịch Bản Mẹ & Bé")

api_key = st.text_input("🔑 OpenAI API Key", type="password")

if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

topic = st.text_input(
    "📌 Chủ đề video",
    "Chăm sóc bé 1–3 tháng tuổi ngủ ngon ban đêm"
)

if st.button("🚀 Tạo nội dung"):

    with st.spinner("AI đang xử lý..."):

        # ===== TEXT =====
        text_res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia chăm sóc mẹ và bé."},
                {"role": "user", "content": f"Viết kịch bản video 30–45s về: {topic}"}
            ]
        )

        st.subheader("📜 KỊCH BẢN VIDEO")
        st.markdown(text_res.choices[0].message.content)

        # ===== IMAGE (CÓ TRY/EXCEPT) =====
        st.subheader("🖼️ ẢNH MINH HỌA")

        try:
            img = client.images.generate(
                model="gpt-image-1",
                prompt="A warm, realistic photo of a 1-3 month old baby sleeping peacefully, Vietnamese family, soft light",
                size="1024x1024"
            )
            st.image(img.data[0].url, use_container_width=True)

        except PermissionDeniedError:
            st.warning(
                "⚠️ Tài khoản OpenAI của bạn chưa được cấp quyền IMAGE API.\n\n"
                "👉 App vẫn chạy bình thường.\n"
                "👉 Bạn có thể dùng prompt này để tạo ảnh bằng Leonardo / Bing / DALL·E web."
            ) API Key",
    type="password",
    placeholder="sk-..."
)

if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

# ================== NHẬP CHỦ ĐỀ ==================
topic = st.text_input(
    "📌 Chủ đề video",
    "Chăm sóc bé 1–3 tháng tuổi ngủ ngon ban đêm"
)

# ================== NÚT CHẠY ==================
if st.button("🚀 Tạo kịch bản & hình ảnh"):

    with st.spinner("AI đang xử lý, vui lòng chờ..."):

        # ---------- 1. TẠO KỊCH BẢN ----------
        script_prompt = f"""
        Viết kịch bản video ngắn 30–45 giây cho chủ đề:
        {topic}

        Phong cách:
        - Dễ hiểu
        - Dành cho cha mẹ có con nhỏ
        - Thân thiện, tích cực
        """

        text_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Bạn là chuyên gia chăm sóc mẹ và bé."
                },
                {
                    "role": "user",
                    "content": script_prompt
                }
            ]
        )

        script_text = text_response.choices[0].message.content

        st.subheader("📜 KỊCH BẢN VIDEO")
        st.markdown(script_text)

        # ---------- 2. TẠO ẢNH ----------
        image_prompt = (
            "A warm, realistic photo of a 1-3 month old baby sleeping peacefully, "
            "Vietnamese family, soft natural light, clean home, "
            "vertical portrait, high quality"
        )

        image_response = client.images.generate(
            model="gpt-image-1",
            prompt=image_prompt,
            size="1024x1024"
        )

        st.subheader("🖼️ ẢNH MINH HỌA")
        st.image(image_response.data[0].url, use_container_width=True)

    st.success("✅ Hoàn thành! Bạn có thể dùng nội dung này để làm video.")
