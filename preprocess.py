import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from summary import *


def extract_text_PDF(pdf_name,divide=True):
    """
    Extracts specific sections from a PDF file.

    Args:
    pdf_name (str): Path to the PDF file.
    divide (boolean): if True the text is divided in 3
    Returns:
    tuple: Tuple containing text from first pages, last pages, and articles 
    or 
    all text
    """
    
    pdfFileObj =  open(pdf_name,'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    num_pages = len(pdfReader.pages)

    first_pages=''
    last_pages = ''
    articles = ''
    all_text = ''
    #For dividing the document into first pages, last pages and the pages with articles
    if divide == True:
        for page in range(num_pages):
            if page <=90 and page >= 38:
                articles += pdfReader.pages[page].extract_text()
            elif page <= 96:
                first_pages += pdfReader.pages[page].extract_text()
            else:
                last_pages += pdfReader.pages[page].extract_text()

        return first_pages, last_pages,  articles
    else:
        for page in range(num_pages):
            all_text += pdfReader.pages[page].extract_text()
        return all_text

def preprocess_text(text):
    """
    Preprocess the text at the sentence level.

    Args:
    text (str): Input text containing multiple sentences.

    Returns:
    tuple: Tuple containing preprocessed sentences and a mapping of original sentences to their preprocessed versions.
    """
    sentences = sent_tokenize(text)
    preprocessed_sentences = []
    original_sentences = {} 

    for sentence in sentences:
        # Tokenize and preprocess the sentence
        words = word_tokenize(sentence)
        original_words = [word for word in words] 
        words = [word.lower() for word in words if word.isalpha()]
        stop_words = set(stopwords.words("english"))
        words = [word for word in words if word not in stop_words]
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in words]

        # Save both preprocessed and original sentence
        preprocessed_sentence = " ".join(stemmed_words)
        preprocessed_sentences.append(preprocessed_sentence)
        original_sentences[preprocessed_sentence] = " ".join(original_words) 

    return preprocessed_sentences, original_sentences

def preprocess_sentences(text):
    """
    Preprocesses a string by tokenizing, converting to lowercase, removing stopwords, and stemming words.

    Args:
    text (str): Input string.

    Returns:
    list: List of preprocessed words.
    """
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return words


def find_answers(question):
    """
    Searches for answers within a given PDF document based on a provided question.

    Args:
    question (str): The question for which answers are sought within the PDF document.

    Returns:
    list or str: A list of formatted answers if found; a descriptive message otherwise.
    """
    question_words = preprocess_sentences(question)
    first_pages, last_pages, articles = extract_text_PDF('The-AI-Act.pdf')
    preprocessed_sentences, original_sentences = preprocess_text(articles)
    matching_original_sentences = []

    answer_number = 1
    # Change this value for a more precise answer or for a mor ample answer
    common = 4
    for idx, sentence in enumerate(preprocessed_sentences):
        sentence_words = preprocess_sentences(sentence)

        # Check for similarity between question and sentence
        common_words = set(question_words).intersection(sentence_words)
        if len(common_words) > common: 
            matched_original_sentence = original_sentences[sentence]  
            
            #Uncomment to see answers summarized by keywords
            #formatted_answer = f"Answer {answer_number}: {summarize_each_answer(matched_original_sentence)}"
            formatted_answer = f"Answer {answer_number}: {matched_original_sentence}"
            matching_original_sentences.append(formatted_answer)
            answer_number += 1  

    if not matching_original_sentences:
        return "I couldn't find an answer."
    
    combined_answers = "\n".join(matching_original_sentences)

    return combined_answers

#To test without the interface run this script without the above coments.
#question = 'What are the contextual expansions in the application of Regulation (EU) 2019/1020 regarding economic operators and products within the scope of the regulation?'
#print(find_answers(question))
