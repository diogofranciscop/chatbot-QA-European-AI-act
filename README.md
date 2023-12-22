# chatbot-QA-European-AI-act
This chatbot aims to provide answers to questions related to the European AI Act. It utilizes text processing techniques on a provided PDF document to answer user queries about the act.
How It Works:
- PDF Text Extraction: The chatbot reads a PDF file containing the European AI Act.
- Text Preprocessing: It preprocesses the text by dividing it into sentences, cleaning and organizing them.
- Keyword Matching: The chatbot identifies keywords in both the user's question and the preprocessed sentences.
- Answer Retrieval: If the number of matching keywords exceeds a predefined threshold, the relevant sentences are returned as answers.

To run the chatbot, simply execute 'interfaceQA.py'. 

There are a couple of customizable features available:

- Targeted Analysis: By default, the chatbot analyzes only the articles within the PDF using pre-defined settings. To modify this behavior, you can alter the analysis scope by calling the 'extract_text_PDF' function. For a comprehensive analysis of the entire PDF content, use: extract_text_PDF('PDF', divide=False).

- Adjust Sensitivity: The chatbot's responsiveness can modified in the 'common' variable within the 'find_answer' function.

- Summary: Presently, the chatbot returns the original text. To generate a summarized version of the sentence, uncomment line 125 in 'preprocess.py'. Please note that this summary currently displays only the keywords present in the sentence. Wasn't able to optimize it yet.
