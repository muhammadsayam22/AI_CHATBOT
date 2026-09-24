import os

import streamlit as st
from google import genai

# صفحہ کی سیٹنگ
st.set_page_config(page_title="مجھ سے بات کریں - AI Chat", page_icon="🤖")

st.title("🤖 میرا پہلا AI چیٹ بوٹ")
st.write("پائথন، اسٹریملٹ اور گوگل جیمنی (Gemini) کی مدد سے بنایا گیا ہے۔")

# اپنی گوگل API Key پرائیویٹ میں GEMINI_API_KEY میں رکھیں
API_KEY = os.environ.get("GEMINI_API_KEY", "your_api_key_here")

if API_KEY == "your_api_key_here" or not API_KEY:
    st.warning("براہ کرم کوڈ کے اندر اپنی اصلی Google Gemini API Key درج کریں۔")
else:
    client = genai.Client(api_key=API_KEY)

    if "chat_history" not in st.session_state:
        st.session_state.chat = client.chats.create(model="gemini-3.6-flash")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("یہاں اپنا سوال لکھیں..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("سوچ رہا ہے..."):
                try:
                    response = st.session_state.chat.send_message(user_input)
                    bot_reply = response.text
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                except Exception as e:
                    st.error(e)