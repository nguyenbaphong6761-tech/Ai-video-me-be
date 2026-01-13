import streamlit as st
from openai import OpenAI

# =============================
# CẤU HÌNH TRANG
# =============================
st.set_page_config(
    page_title="AI Tool Xây Kênh Mẹ & Bé",
    page_icon="👶",
    layout="centered"
)

st.title("👶 AI TOOL TẠO KỊCH BẢN & PROMPT VIDEO MẸ & BÉ")
st.write("Dành cho xây kênh nội dung dài hạn (TikTok / Reels / Shorts)")

# =============================
# NHẬP API KEY
# =============================
api_key = st.text_input(
    "🔑 Nhập OpenAI API Key",
    type="password",
    help="Lấy tại https://platform.openai.com"
)

if not api_key:
    st.warning("Vui lòng nhập API Key để tiếp tục")
    st.stop()

client = OpenAI(api_key=api_key)

# =============================
# INPUT NGƯỜI DÙNG
# =============================
age_range = st.selectbox(
    "👶 Độ tuổi của bé",
    [
        "1–3 tháng",
        "3–6 tháng",
        "6–12 tháng"
    ]
)

content_type = st.selectbox(
    "🎯 Mục tiêu nội dung",
    [
        "Xây kênh dài hạn",
        "Chia sẻ kiến thức",
        "Video trải nghiệm thực tế",
        "Video review sản phẩm"
    ]
)

tone = st.selectbox(
    "🎨 Giọng điệu",
    [
        "Nhẹ nhàng – ấm áp",
        "Chuyên gia – đáng tin cậy",
        "Gần gũi – đời thường"
    ]
)

brand = st.text_input(
    "🏷️ Thương hiệu (không bắt buộc)",
    placeholder="Ví dụ: Fatzbaby, Pigeon, Chicco..."
)

# =============================
# TẠO PROMPT AI
# =============================
def build_prompt():
    brand_text = f"Lồng ghép thương hiệu {brand} một cách tự nhiên." if brand else ""

    return f"""
Bạn là chuyên gia nội dung ngành mẹ & bé tại Việt Nam.

Hãy tạo:
1. KỊCH BẢN VIDEO (30–45 giây, chia cảnh rõ ràng)
2. PROMPT TẠO VIDEO AI (dán vào CapCut / Vivideo / HeyGen)

Thông tin:
- Độ tuổi bé: {age_range}
- Mục tiêu nội dung: {content_type}
- Giọng điệu: {tone}
{brand_text}

Yêu cầu:
- An toàn cho trẻ sơ sinh
- Ngôn từ tích cực, không gây lo lắng
- Phù hợp xây kênh lâu dài
- Có thể dùng cho TikTok / Reels / Shorts

Trình bày đúng cấu trúc:
=== KỊCH BẢN VIDEO ===
=== PROMPT VIDEO AI ===
"""

# =============================
# NÚT TẠO NỘI DUNG
# =============================
if st.button("🚀 TẠO KỊCH BẢN & PROMPT"):
    with st.spinner("AI đang tạo nội dung..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia marketing và nội dung mẹ & bé."},
                {"role": "user", "content": build_prompt()}
            ],
            temperature=0.7
        )

        result = response.choices[0].message.content

    st.success("✅ Hoàn thành!")
    st.markdown(result)

    st.download_button(
        label="📥 Tải nội dung (.txt)",
        data=result,
        file_name="kich_ban_va_prompt_video_me_va_be.txt",
        mime="text/plain"
    )
