import dbutils
from PIL import Image
import pytesseract
import openai

openai.organization = "org-87S7CpTnHb0kAdCaM9m5NorN"
OPENAI_API_KEY = "INSERT_API_KEY_HERE"
openai.api_key = OPENAI_API_KEY
openai.Model.list()

uploaded_file = "/FileStore/tables/question_screenshot_example.PNG"

#Copy from Databricks Community Edition DBFS to accessible /tmp directory
dbutils.fs.cp(uploaded_file, "file:///tmp/question_screenshot_example")

# File location and type
file_location = "/tmp/question_screenshot_example"
raw_text = pytesseract.image_to_string(Image.open(file_location))
chunks = raw_text.split('\n')
print(raw_text)

question = chunks[0]
question = question.lstrip('0123456789.- ')
print(question)

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=question,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response)