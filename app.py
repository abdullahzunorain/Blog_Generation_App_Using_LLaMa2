import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
# import gradio as gr
from groq import Groq
import os

key = os.getenv("groq_api")
client = Groq(api_key = key)

## Function To get response from LLAma 2 model

# def getLLamaresponse(input_text,no_words,blog_style):

#     ## LLama2 model
#     llm=CTransformers(model="llama3-8b-8192",   # model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
#                       model_type='llama',
#                       config={'max_new_tokens':256,
#                               'temperature':0.01})
    
#     # llm = client.chat.completions.create(model="llama3-8b-8192",   # model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
#     #                   model_type='llama',
#     #                   config={'max_new_tokens':256,
#     #                           'temperature':0.01})
    
#     ## Prompt Template

#     template="""
#         Write a blog for {blog_style} job profile for a topic {input_text}
#         within {no_words} words.
#             """
    
#     prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
#                           template=template)
    
#     ## Generate the ressponse from the LLama 2 model
#     response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
#     print(response)
#     return response



def getLLamaresponse(input_text, no_words, blog_style):
    # Define the prompt using the PromptTemplate
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)
    formatted_prompt = prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    
    # Call the Groq client to generate a response
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": formatted_prompt}],
        max_tokens=256,
        temperature=0.01
    )

    # Print the response to inspect its structure
    print(response)  # Add this line to see the response structure

    # Extract the response content based on its structure
    # Adjust the access based on what you see in the print statement
    if response and 'choices' in response and len(response.choices) > 0:
        return response.choices[0].message['content']
    else:
        return "No response generated."





st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
