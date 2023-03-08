# this is an example script from class 6 on Wednesday 8.3

# load packages
import spacy
# initialize spacy
nlp = spacy.load("en_core_web_lg")

def main():
    text = "This is a string"
    doc = nlp(text)
    for token in doc:
        print(token.text)

if __name__=="__main__":
    main()