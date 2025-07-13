import streamlit as st
from scraper import scrape
from scraper import splitdom , clean , extract_content

st.title("Web Scraper")

url = st.text_input("Enter the url")

if st.button("Scrape"):
    st.write("Running")
    
    domc = scrape(url)
    
    body = extract_content(url)
    cleaned = clean(body)

    st.session_state.domc = cleaned

    with st.expander("View Content"):
        st.text_area("content",cleaned,height=300)

if "domc" in st.session_state:

    parsed = st.text_area("describe what you want to parse")

    if st.button("Parse Content"):
        if parsed:
            st.write("Loading")

            chunks = splitdom(st.session_state.domc)
