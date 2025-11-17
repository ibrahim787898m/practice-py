import spacy
from tabulate import tabulate

def main():
    nlp = spacy.load("en_core_web_sm")
    dash()
    print("Welcome to a NLP programe made with Python using Spacy library.")
    dash()
    text = input("Write your text bellow to process different NLP operation: \n")
    dash()
    doc = nlp(text)
    while True:
        user_interface()
        user_input = input("Option(1 - 9): ")
        dash()
        if user_input == "1":
            print("Printing all tokens:\n")
            tokenization(doc)
            dash()
        elif user_input == "2":
            print("Printing Lingustic Annotations:\n")
            linguistical_annotation(doc)
            dash()
        elif user_input == "3":
            print("Printing lemmatization of all tokens:\n")
            lemmatization(doc)
            dash()
        elif user_input == "4":
            print("Detecting sentences in the given string and printing:\n")
            sentence_detection(doc)
            dash()
        elif user_input == "5":
            print("Printing POS, Tag and Explanation of all tokens:\n")
            pos_tagging(doc)
            dash()
        elif user_input == "6":
            print("Printing Named Entity Recognitions:\n")
            ner(doc)
            dash()
        elif user_input == "7":
            print("Detecting the stop words from the given string and removing them:\n")
            remove_stop_words(doc)
            dash()
        elif user_input == "8":
            print("Dependency Relationships:\n")
            dependency_parsing(doc)
            dash()
        elif user_input == "9":
            print("Thank you for using the program. Goodbye!")
            dash()
            break
        else:
            print("INVALID INPUT! TRY AGAIN.")
            dash()

def user_interface():
    print("Chose the operation you wanna process:\n")
    print("1. Tokenization")
    print("2. Linguistical annotation")
    print("3. Lemmatization")
    print("4. Sentence detection")
    print("5. POS tagging")
    print("6. Named Entity Recognition (NER)")
    print("7. Stop words removal")
    print("8. Dependency parsing")
    print("9. Exit the program")
    dash()

def tokenization(doc):
    for index, token in enumerate(doc, start=1):
        print(f"Token {index}: {token}")

def linguistical_annotation(doc):
    data = []
    for token in doc:
        data.append({"Token": token.text, "POS": token.pos_, "Lemma": token.lemma_, "Dependency": token.dep_, "Entity": token.ent_type_})

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
        data.append({"Entity": ent.text, "Type": ent.label_})

    print(tabulate(data, headers="keys", tablefmt="pipe"))

def remove_stop_words(doc):
    filtered_tokens = [token.text for token in doc if not token.is_stop]
    filtered_sent = " ".join(filtered_tokens)
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
