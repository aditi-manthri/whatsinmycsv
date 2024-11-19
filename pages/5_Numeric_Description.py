import streamlit as st
import pandas as pd

st.set_page_config(page_title="Numeric Description", page_icon="✨", layout="wide")

# Load CSS styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.markdown("<h1 class='custom-sub'>Numeric Description</h1>", unsafe_allow_html=True)
    
    # Access data from session state
    if 'data' in st.session_state:
        data = st.session_state['data']
        
        # Display summary statistics for numerical columns
        st.markdown("### Summary Statistics for Numerical Columns")
        st.write(data.describe())
    else:
        st.write("No data available.")

if __name__ == "__main__":
    main()