import pprint
import re

def debug_print(value):
    pprint.PrettyPrinter().pprint(value)

def read_file(source_file):
    with open(source_file, 'r', encoding='utf8') as file:
        data = file.read()
        debug_print(data)
        return data

def parse_question_answer_parentheses(question_text):
    questions = re.split(r'\n\s*\n', question_text) #splits the questions into a list assuming there is no empty lines inside each question
    question_answers = []

    for question in questions:
        if question != None and 'a. ': #extra check to make sure that this a question
            statement = re.findall(r'[^(]+', question)[0].replace('\n', ' ').rstrip()
            print(statement)
            # option_a = re.findall(r'\(a\)[^(]+', question)[0].replace('\n', ' ').rstrip()
            # option_b = re.findall(r'\(b\)[^(]+', question)[0].replace('\n', ' ').rstrip()
            # option_c = re.findall(r'\(c\)[^(]+', question)[0].replace('\n', ' ').rstrip()
            # option_d = re.findall(r'\(d\)[^(]+', question)[0].replace('\n', ' ').rstrip()
            option_a = re.findall(r'\(a\)[^(]+', question)
            option_b = re.findall(r'\(b\)[^(]+', question)
            option_c = re.findall(r'\(c\)[^(]+', question)
            option_d = re.findall(r'\(d\)[^(]+', question)
            question_answers.append({
                'statement': statement.rstrip(),
                'options': [option_a, option_b, option_c, option_d]
            })

    debug_print(question_answers)
    return question_answers

def extract_question_and_answers_periods(question_text):
    # Define the regular expression patterns for question and answers
    question_pattern = r"\d+\)\s+(.*)\n"
    answer_pattern = r"[a-d]\.\s*(\w+)"

    # Find the question using the regular expression
    question_match = re.search(question_pattern, question_text)
    if question_match:
        question = question_match.group(1).strip()
    else:
        question = None

    # Find all matches for answers using the regular expression
    answer_matches = re.findall(answer_pattern, question_text)

    # Return the question and the list of answers
    return question, answer_matches
