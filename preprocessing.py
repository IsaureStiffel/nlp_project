from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def preprocess_text(text):
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    # Tokenization
    tokens = word_tokenize(text)
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in tokens if word.isalnum()]
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    # Lemmatization using WordNetLemmatizer
    words = [stemmer.stem(word) for word in words]
    
    return ' '.join(words)

def remove_freqwords(text: str, freq_words: list) -> str:
    cleaned_text = " ".join([word for word in text.split() if word not in freq_words])
    return cleaned_text

def remove_rarewords(text: str, rare_words: list) -> str:
    cleaned_text = " ".join([word for word in text.split() if word not in rare_words])
    return cleaned_text