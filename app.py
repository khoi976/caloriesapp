import streamlit as st
from PIL import Image

# Giao diện tiêu đề
st.title("🍱 Ứng dụng Phân Tích Calo Món Ăn")
st.write("Tải ảnh món ăn để phân tích lượng calo, protein và tinh bột.")

# Upload ảnh
uploaded_file = st.file_uploader("📷 Tải ảnh món ăn (jpg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh món ăn đã chọn", use_column_width=True)

    # Giả lập phân tích món ăn (sau này có thể thay bằng AI thật)
    st.subheader("📊 Kết quả phân tích (giả lập)")
    st.markdown("🔥 **Calo:** 640 kcal")
    st.markdown("🍗 **Protein:** 32g")
    st.markdown("🍚 **Carbohydrates:** 78g")

    st.success("✅ Phân tích hoàn tất!")
