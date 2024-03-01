#streamlit_user_input_on

import streamlit as st

def main():
    user_input = st.text_input(" ", value=" ")
    with open('website_text_content.txt', 'a', encoding='utf-8') as file:
        file.write(str(user_input+"\n"))
    with open('website_text_content.txt', 'r', encoding='utf-8') as file1:
        stryng = file1.read()
    st.text(stryng)

if __name__ == "__main__":
    main()
