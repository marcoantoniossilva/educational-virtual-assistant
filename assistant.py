import speech_recognition as sr
from nltk import word_tokenize, corpus
import json

# Assistant configuration
CORPUS_LANGUAGE = "portuguese"
DATA_FILE = "data.json"
LANGUAGE_SPEAKS = "pt-BR"


def initialize():
    global assistant_name
    global recognizer
    global stop_words
    global formulas

    recognizer = sr.Recognizer()
    stop_words = set(corpus.stopwords.words(CORPUS_LANGUAGE))

    with open(DATA_FILE, "r", encoding="utf8") as data_file_stm:
        data = json.load(data_file_stm)

        assistant_name = data["assistant-name"]
        formulas = data["formulas"]

        data_file_stm.close()


def recognize_question():
    global recognizer

    question = None

    with sr.Microphone() as audio_source:
        recognizer.adjust_for_ambient_noise(audio_source)

        print("Pergunte-me sobre alguma fórmula...")

        speaks = recognizer.listen(audio_source)

        try:
            question = recognizer.recognize_google(speaks, language=LANGUAGE_SPEAKS)
        except sr.UnknownValueError:
            pass

    return question


def eliminate_stop_words(tokens):
    global stop_words

    filtered_tokens = []
    for token in tokens:
        if token not in stop_words:
            filtered_tokens.append(token)

    return filtered_tokens


def tokenizate_question(question):
    global assistant_name

    formula = None
    variant = None

    tokens = word_tokenize(question, CORPUS_LANGUAGE)
    if tokens:
        tokens = eliminate_stop_words(tokens)

        if len(tokens) >= 4:
            if assistant_name == tokens[0].lower():
                print(tokens)
                formula = tokens[3].lower()
                if len(tokens) >= 5:
                    variant = tokens[4].lower()

    return formula, variant


def validate_question(formula, variant):
    global formulas

    valid = False
    composed = False

    if formula:
        for verified_formula in formulas:
            if formula == verified_formula["name"]:
                valid = True
                if variant:
                    if variant in verified_formula["variant"]:
                        composed = True
                        break

    return valid, composed


def execute_question_composed(formula, variant):
    print("1 você quer saber: ", formula, variant)
    
def execute_question(formula):
    print("2 você quer saber: ", formula)


if __name__ == "__main__":
    initialize()

    keep_listening = True
    while keep_listening:
        try:
            question = recognize_question()
            if question:
                formula, variant = tokenizate_question(question)
                valid, composed = validate_question(formula, variant)
                if valid and composed:
                    execute_question_composed(formula, variant)
                else:
                    if valid:
                        execute_question(formula)
                    else:
                        print("Não entendi a fórmula que deseja aprender, repita por favor...")
        except KeyboardInterrupt:
            print("bye!")
            keep_listening = False
