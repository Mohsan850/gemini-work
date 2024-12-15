from  dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()
api_key=os.environ.get("GEMNAI_API_KEY")
genai.configure(api_key=api_key)
model_name = "gemini-1.5-flash"
model=genai.GenerativeModel(model_name)
response = model.generate_content(input("type any thing"))
print(response.text)
