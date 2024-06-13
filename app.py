import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import time

# Load the environment variables
load_dotenv()

# Get the HuggingFace API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]

def get_huggingface_response(input_text, no_words, blog_style):
    # Calling the model
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=1000, temperature=0.7, token=HUGGINGFACEHUB_API_TOKEN)

    # Prompt
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
            
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'], template=template)
    
    # Chain
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    
    # Get the response
    response = llm_chain.run(blog_style=blog_style, input_text=input_text, no_words=no_words)
    return response

# Page title
st.title("📚 WordWeaver: The Blog Generator ✒️")

# Sidebar for user inputs
st.sidebar.header("Input Parameters ✍️")

# Dropdown for selecting blog style in sidebar
blog_style = st.sidebar.selectbox(
    "Choose the blog style 🌟",
    ["Technical", "Lifestyle", "Travel", "Food", "Fitness", "Finance", "Education", "Health", "Entertainment", "Career"]
)

# Text input for custom blog topic in sidebar
input_text = st.sidebar.text_input("Enter the blog topic 📚")

# Slider for number of words in sidebar
no_words = st.sidebar.slider("Select the number of words 📏", min_value=50, max_value=1000, step=50, value=150)

# Generate blog button in sidebar
if st.sidebar.button("Generate Blog 🚀"):
    if input_text and no_words and blog_style:
        with st.spinner("Generating blog... ⏳"):
            response = get_huggingface_response(input_text, no_words, blog_style)
            time.sleep(3)  # Simulating processing time
        st.success("Blog generated successfully! 🎉")
        st.markdown("### 📝 Generated Blog:")
        st.markdown(response)
    else:
        st.sidebar.write("Please fill in all the fields ❗")

# Footer
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p>Made by Sathyam A 🕺🏽</p>
    </div>
""", unsafe_allow_html=True)
