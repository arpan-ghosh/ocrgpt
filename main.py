import dbutils
from lib.utility import DATABRICKS_FILE_LOCATION, copy_sourcefile, debug_print
import openai
from PIL import Image
import pytesseract

OPENAI_API_KEY = "INSERT_API_KEY_HERE"

openai.organization = "org-87S7CpTnHb0kAdCaM9m5NorN"
openai.api_key = OPENAI_API_KEY
openai.Model.list()

def get_image():
    image_file_location = "/tmp/question_screenshot_example"
    return image_file_location

def ocr_to_text(image):
    raw_text = pytesseract.image_to_string(Image.open(DATABRICKS_FILE_LOCATION))
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
    chunks = ocr_to_text(get_image())
    question = parse_question(chunks)
    ask_chatgpt(question)
