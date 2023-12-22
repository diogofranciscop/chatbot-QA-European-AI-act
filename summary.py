from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def summarize_each_answer(answer):
    """
    Summarizes a single sentence by extracting important keywords.

    Args:
    answer (str): The sentence to be summarized.

    Returns:
    str: Summarized sentence based on keyword extraction.
    """
    stop_words = set(stopwords.words("english"))

    words = word_tokenize(answer.lower())

    words = [word for word in words if word.isalpha() and word not in stop_words]

    word_freq = Counter(words)

    summary_words = [word for word, _ in word_freq.most_common(5)] 

    summary_text = ' '.join(summary_words)

    return summary_text

#Uncomment to test.
#print(summarize_each_answer('EN 40 EN ( 3 ) ‘ small -scale provider ’ means a provider that is a micro or small enterprise within the meaning of Commission Recommendation 2003/361/EC61 ; ( 4 ) ‘ user ’ means any natural or legal person , public authority , agency or other body using an AI s ystem under its authority , except where the AI system is used in the course of a personal non -professional activity ; ( 5 ) ‘ authorised representative ’ means any natural or legal person established in the Union who has received a written mandate from a provid er of an AI system to , respectively , perform and carry out on its behalf the obligations and procedures established by this Regulation ; ( 6 ) ‘ importer ’ means any natural or legal person established in the Union that places on the market or puts into service an AI system that bears the name or trademark of a natural or legal person established outside the Union ; ( 7 ) ‘ distributor ’ means any natural or legal person in the supply chain , other than the provider or the importer , that makes an AI system available o n the Union market without affecting its properties ; ( 8 ) ‘ operator ’ means the provider , the user , the authorised representative , the importer and the distributor ; ( 9 ) ‘ placing on the market ’ means the first making available of an AI system on the Union market ; ( 10 ) ‘ making available on the market ’ means any supply of an AI system for distribution or use on the Union market in the course of a commercial activity , whether in return for payment or free of charge ; ( 11 ) ‘ putting into service ’ means the supply of an AI system for first use directly to the user or for own use on the Union market for its intended purpose ; ( 12 ) ‘ intended purpose ’ means the use for which an AI system is intended by the provider , including the specific context and conditions of use , as specified in the information supplied by the provider in the instructions for use , promotional or sales materials and statements , as well as in the technical documentation ; ( 13 ) ‘ reasonably foreseeable misuse ’ means the use of an AI system in a way tha t is not in accordance with its intended purpose , but which may result from reasonably foreseeable human behaviour or interaction with other systems ; ( 14 ) ‘ safety component of a product or system ’ means a component of a product or of a system which fulfils a safety function for that product or system or the failure or malfunctioning of which endangers the health and safety of persons or property ; ( 15 ) ‘ instructions for use ’ means the information provided by the provider to inform the user of in particular a n AI system ’ s intended purpose and proper use , inclusive of the specific geographical , behavioural or functional setting within which the high -risk AI system is intended to be used ; ( 16 ) ‘ recall of an AI system ’ means any measure aimed at achieving the ret urn to the provider of an AI system made available to users ; 61 Commission Recommendation of 6 May 2003 concerning the definition of micro , small and medium - sized enterprises ( OJ L 124 , 20.5.2003 , p. 36 ) .'))


