import streamlit as st

st.title("AI Web Scraper")

url = st.text_input("Enter the URL of the website to scrape:")

if st.button("Scrape Site:"):
    st.write("Scraping the website...")