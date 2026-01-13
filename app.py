import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Video Mẹ & Bé", layout="centered")
st.title("🤱 AI xây kênh Video Mẹ & Bé")

api_key = st.text_input("🔑 OpenAI API Key", type="password")

if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

topic = st.text_input(
    "📌 Chủ đề video",
    "Bé 1–3 tháng tuổi ngủ hay giật mình ban đêm"
)

if st.button("🚀 Tạo kịch bản + prompt video"):

    with st.spinner("AI đang tạo nội dung..."):

        prompt = f"""
        Hãy tạo nội dung cho video TikTok/Reels về chủ đề: {topic}

        Trả về theo cấu trúc sau:

        1. HOOK 3 GIÂY ĐẦU (1 câu ngắn, đánh vào nỗi lo cha mẹ)
        2. KỊCH BẢN 30–45 GIÂY (chia từng câu ngắn)
        3. CHECKLIST / TIP NGẮN (3 ý)
        4. CTA NHẸ (không bán hàng)
        5. PROMPT TẠO ẢNH (cho Leonardo / Bing Image)
        6. PROMPT DỰNG VIDEO (cho CapCut / Pika, mô tả cảnh)

        Ngôn ngữ: tiếng Việt, dễ hiểu, thân thiện.
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia nội dung mẹ & bé và marketing video ngắn."},
                {"role": "user", "content": prompt}
            ]
        )

        st.success("✅ Hoàn thành")

        st.markdown(res.choices[0].message.content)
