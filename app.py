import streamlit as st

st.set_page_config(page_icon=":material:Speed:")

st.subheader("Demo app for non emoji icons")

with st.chat_message("user", avatar=":material:AddCircle:"):
    st.write("Hello from USER 👋")

with st.chat_message("ai", avatar=":material:DirectionsBike:"):
    st.write("Hello from AI 👋")

with st.chat_message("ai"):
    st.write("Hello from AI default👋")

with st.chat_message("user"):
    st.write("Hello from User default👋")

with st.chat_message("ai", avatar="🛑"):
    st.write("Hello from AI 👋")

with st.chat_message("user", avatar="💚"):
    st.write("Hello from USER 👋")

st.success("This is a success message", icon=":material:ThreeDRotation:")
st.warning("This is a warning message", icon=":material:FourK:")
st.info("This is a purely informational message", icon="ℹ️")


left, right = st.columns(2)
with left:
    my_button = st.button("Show toast with custom icon")
    if my_button:
        st.toast("Your edited image was saved!" * 30, icon="😍")
        st.toast("Your edited image was saved!" * 30, icon=":material:AlarmAdd:")

with right:
    st.button("Rerun app to see a favicon")
