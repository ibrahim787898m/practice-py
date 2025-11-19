import spacy
from tabulate import tabulate

def main():
    nlp = spacy.load("en_core_web_sm")
    header()
    user_input_text(nlp)

def header():
    dash()
    print("NLP Program - Process text using spaCy library")
    dash()

def user_input_text(nlp):
    while True:
        text = input("Enter text to analyze (or 'quit' to exit):\n").strip()
        if text.lower() == 'quit':
            dash()
            print("Thank you for using the program. Goodbye!")
            dash()
            break
        if not text:
            print("Error: Please enter some text.")
            dash()
            continue
        doc = nlp(text)
        dash()
        print("Processed Text:")
        print(f"{text}")
        dash()
        result = operations_menu(doc, nlp)
        if result == "exit":
            break

def operations_menu(doc, nlp):
    while True:
        print("Choose an operation:\n")
        print("  1. Tokenization")
        print("  2. Linguistic Annotation")
        print("  3. Lemmatization")
        print("  4. Sentence Detection")
        print("  5. POS Tagging")
        print("  6. Named Entity Recognition")
        print("  7. Stop Words Removal")
        print("  8. Dependency Parsing")
        print("  9. Analyze New Text")
        print("  0. Exit")
        dash()
        result = operations(doc, nlp)
        if result == "new_text":
            return "new_text"
        elif result == "exit":
            return "exit"

def operations(doc, nlp):
    user_input = input("Option: ").strip()
    dash()
    if user_input == "1":
        print("Printing Tokens:\n")
        tokenization(doc)
        dash()
    elif user_input == "2":
        print("Printing Linguistical Annotations of all tokens:\n")
        linguistical_annotation(doc)
        dash()
    elif user_input == "3":
        print("Printing lemmatization of all tokens:\n")
        lemmatization(doc)
        dash()
    elif user_input == "4":
        print("Printing Sentences:\n")
        sentence_detection(doc)
        dash()
    elif user_input == "5":
        print("Printing POS Tags:\n")
        pos_tagging(doc)
        dash()
    elif user_input == "6":
        print("Printing Named Entities:\n")
        ner(doc)
        dash()
    elif user_input == "7":
        print("Printing text after removing stop words:\n")
        remove_stop_words(doc)
        dash()
    elif user_input == "8":
        print("Printing Dependency Parsing:\n")
        dependency_parsing(doc)
        dash()
    elif user_input == "9":
        print("Exiting to main menu to analyze new text.")
        dash()
        return "new_text"
    elif user_input == "0":
        print("Exiting program. Goodbye!")
        dash()
        return "exit"
    else:
        print("Invalid option. Please choose a valid operation.")
        dash()
    return None

def tokenization(doc):
    for index, token in enumerate(doc, start=1):
        print(f"Token {index}: {token}")

def linguistical_annotation(doc):
    data = []
    for token in doc:
        data.append({"Token": token.text, "POS": token.pos_, "Lemma": token.lemma_, "Dependency": token.dep_, "Entity": token.ent_type_ if token.ent_type_ else "-"})

    print(tabulate(data, headers="keys", tablefmt="pipe"))

def lemmatization(doc):
    data = []
    for index, token in enumerate(doc, start=1):
        data.append({"Token": token.text, "Lemma": token.lemma_})

    print(tabulate(data, headers="keys", tablefmt="pipe"))

def sentence_detection(doc):
    for index, sent in enumerate(doc.sents, start=1):
        print(f"{index}: {sent}")

def pos_tagging(doc):
    data = []
    for token in doc:
        data.append({"Token": token.text, "POS": token.pos_, "Tag": token.tag_, "Detail": spacy.explain(token.tag_)})

    print(tabulate(data, headers="keys", tablefmt="pipe"))

def ner(doc):
    data = []
    for ent in doc.ents:
        data.append({"Entity": ent.text, "Label": ent.label_, "Explanation": spacy.explain(ent.label_)})

    if not data:
        print("No named entities found.")
        return

    print(tabulate(data, headers="keys", tablefmt="pipe"))

def remove_stop_words(doc):
    filtered_tokens = [token.text for token in doc if not token.is_stop]
    filtered_sent = " ".join(filtered_tokens)
    if not filtered_sent:
        print("All words are stop words; no text remains after removal.")
        return
    
    print(f"Original Text: {doc.text}")
    print(f"Text after stop word removal: {filtered_sent}")

def dependency_parsing(doc):
    data = []
    for token in doc:
        data.append({"TOKEN": token.text, "DEP": token.dep_, "HEAD": token.head, "POS": token.pos_})
        
    print(tabulate(data, headers="keys", tablefmt="pipe"))

def dash():
    print("=" * 100)

if __name__ == "__main__":
    main()