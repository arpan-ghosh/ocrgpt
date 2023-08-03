import dbutils
from PIL import Image
import pytesseract
import openai
import pprint

openai.organization = "org-87S7CpTnHb0kAdCaM9m5NorN"
OPENAI_API_KEY = "INSERT_API_KEY_HERE"
openai.api_key = OPENAI_API_KEY
openai.Model.list()

uploaded_file = "/FileStore/tables/question_screenshot_example.PNG"

def debug_print(value):
    pprint.PrettyPrinter().pprint(value)

def get_image():
    image_file_location = "/tmp/question_screenshot_example"
    return image_file_location

#Copy from Databricks Community Edition DBFS to accessible /tmp directory
def copy_sourcefile():
    dbutils.fs.cp(uploaded_file, "file:///tmp/question_screenshot_example")

def ocr_to_text(image):
    raw_text = pytesseract.image_to_string(Image.open(file_location))
    chunks = raw_text.split('\n')
    debug_print(raw_text)
    return chunks

def clean_question(question):
    return question.lstrip('0123456789.- ')

def parse_question(chunks):
    question = clean_question(chunks[0])
    debug_print(question)
    return question

def ask_chatgpt(question):
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

    debug_print(response)

if __name__ == "__main__":
    copy_sourcefile()
    data = ocr_to_text(get_image())
    question = parse_question(chunks)
    ask_chatgpt(question)
