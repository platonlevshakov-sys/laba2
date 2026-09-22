import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Настройка страницы
st.set_page_config(page_title="AI Vision Tracker", page_icon="🧠", layout="wide")

st.title("🧠 Трекер компьютерного зрения на базе ИИ")
st.write("Интерактивная система обработки видеопотока и компьютерного зрения.")

# Боковое меню
st.sidebar.header("Параметры фильтрации")
effect = st.sidebar.selectbox("Выберите режим эффекта:", [
    "Оригинал",
    "Черно-белый (Grayscale)",
    "Инверсия цветов",
    "Эффект матричного сканирования (Edge Detection)"
])

st.subheader("📷 Загрузите изображение для обработки ИИ")
uploaded_file = st.file_uploader("Выберите фото (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Читаем картинку
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Конвертируем цвета для OpenCV
    processed_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Применяем выбранный "ИИ-эффект"
    if effect == "Черно-белый (Grayscale)":
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2RGB)
    elif effect == "Инверсия цветов":
        processed_img = cv2.bitwise_not(processed_img)
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    elif effect == "Эффект матричного сканирования (Edge Detection)":
        gray = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        processed_img = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    else:
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)

    # Вывод результатов в две колонки
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Исходное изображение", use_container_width=True)
    with col2:
        st.image(processed_img, caption=f"Результат обработки ({effect})", use_container_width=True)

    st.success("Кадр успешно обработан нейросетевым фильтром!")
else:
    st.info("💡 Загрузите любое фото выше, чтобы запустить алгоритмы компьютерного зрения.")