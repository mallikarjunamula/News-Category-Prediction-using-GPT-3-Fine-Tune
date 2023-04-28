import streamlit as st
import openai
openai.api_key ='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'

st.header("News Category Prediction using FineTuned GPT-3 Model")
news_text  = st.text_area("Enter News Text")
button = st.button("Generate Category")

def test_gpt3(text):
  response = openai.Completion.create(
    model="davinci:ft-personal-2023-03-16-06-36-32",
    prompt=f"Determine Category of the given news.\n\n{text}\n\nCategory:",
    max_tokens=5,
    temperature=0,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=[" END"]
  )
  st.write(response)
  return response['choices'][0]['text']

if button and news_text:
    with st.spinner("Generating Category!..."):
        reply = test_gpt3(news_text)
    st.write(reply)