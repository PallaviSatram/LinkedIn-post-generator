import streamlit as st
from  few_shot import FewShotPosts
from post_generator import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
  st.title("LinkedIn Post Generator")
  col1, col2, col3 = st.columns(3)
  fs = FewShotPosts()
  with col1:
    sel_tag = st.selectbox("Topic", options=fs.get_tags())

  with col2:
    sel_len = st.selectbox("Length", options=length_options)

  with col3:
    sel_lang = st.selectbox("Language", options=language_options)
  if st.button("Generate"):
    post = generate_post(sel_tag, sel_len, sel_lang)
    st.write(post)

if __name__ == "__main__":
  main()