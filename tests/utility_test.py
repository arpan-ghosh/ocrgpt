from lib.utility import debug_print, extract_question_and_answers_periods
from tests.data.utility_data import QUESTION_ONE_LINE_TEXT

def test_extract_question_and_answers_periods():
    question, answers = extract_question_and_answers_periods(QUESTION_ONE_LINE_TEXT)
    assert question == 'Which of the following is not a valid SQL type?'
    assert answers == ['FLOAT', 'NUMERIC', 'DECIMAL', 'CHARACTER']

