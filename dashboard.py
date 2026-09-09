import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

# --- Header ---
st.title("📊 AI Data Analyst Agent")
st.markdown("""
Upload a CSV file and ask questions about your data!
*Powered by OpenAI and PandasAI*
""")

# --- Sidebar ---
with st.sidebar:
    st.header("Configuration")
    
    # Try to get key from env, otherwise ask user
    env_key = os.getenv("OPENAI_API_KEY")
    api_key = st.text_input("OpenAI API Key", value=env_key if env_key else "", type="password")
    
    if not api_key:
        st.warning("⚠️ Please provide an API Key to proceed.")
        
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# --- Main Logic ---
if uploaded_file is not None and api_key:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())
        
        # Initialize LLM
        llm = OpenAI(api_token=api_key)
        sdf = SmartDataframe(df, config={"llm": llm})
        
        # Chat Interface
        st.write("### Ask a Question")
        query = st.text_area("What would you like to know?", placeholder="e.g., Plot the distribution of Sales, or What is the average profit?")
        
        if st.button("Generate Answer"):
            if query:
                with st.spinner("Analyzing..."):
                    try:
                        response = sdf.chat(query)
                        
                        st.success("Analysis Complete!")
                        
                        # PandasAI returns different types based on result
                        # If it's a plot path (string ending in .png), display it
                        # If it's a dataframe, display it
                        # If it's a number/string, write it
                        
                        # Check for chart (PandasAI usually saves charts to ./exports/charts and returns path or None)
                        # We can inspect the response type
                        
                        if isinstance(response, str) and response.endswith(".png"):
                             st.image(response)
                        elif isinstance(response, pd.DataFrame):
                             st.dataframe(response)
                        else:
                             st.write(response)
                             
                        # Explicitly try to show the plot if one was generated in the background
                        # PandasAI creates a generic plot in the backend sometimes
                        if plt.get_fignums():
                            st.pyplot(plt.gcf())
                            plt.clf()

                    except Exception as e:
                        st.error(f"AI Error: {e}")
            else:
                st.warning("Please enter a question.")

    except Exception as e:
        st.error(f"Error reading file: {e}")

elif uploaded_file is None:
    st.info("👆 Please upload a CSV file to begin.")
    
    if st.button("Use Sample Data"):
        # Create a sample CSV for the user to download/use
        data = {
            'Date': pd.date_range(start='1/1/2023', periods=10),
            'Product': ['Widget A', 'Widget B', 'Widget C', 'Widget A', 'Widget B', 'Widget C', 'Widget A', 'Widget B', 'Widget C', 'Widget A'],
            'Sales': [100, 150, 80, 120, 160, 90, 110, 140, 85, 130],
            'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'North', 'South']
        }
        df_sample = pd.DataFrame(data)
        df_sample.to_csv("sample_sales.csv", index=False)
        st.success("Created 'sample_sales.csv'! Drag and drop it into the uploader.")
        st.dataframe(df_sample)

