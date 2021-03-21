import nltk, string, re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

new_words = {
    'crushes': 10,
    'falls': -5,
    'crashes': -10,
    'beats': 5,
    'misses': -5,
    'trouble': -10,
    'falls': -100,
    'rises': 100,
}

vader = SentimentIntensityAnalyzer()
vader.lexicon.update(new_words)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def lemmatizer(text):
    wn = nltk.WordNetLemmatizer()
    text = [wn.lemmatize(word) for word in text]
    return text


def remove_punct(text):
    string.punctuation += "’“”"
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', ' ', text)
    return text


# remove punctuation, lowercase, stem
def normalize(text):
    return lemmatizer(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


def remove_stopwords(text):
    stopword = nltk.corpus.stopwords.words('english')
    stopword.extend(['u', 'ha', 'wa', 'im'])
    text = [word for word in text if word not in stopword]
    return text


def preprocess(text):
    text = re.sub('@[^\s]+', '', text)
    text = remove_punct(text)
    text = normalize(text)
    text = remove_stopwords(text)
    return text


def nltk_sentiment(sentence):
    sentence = preprocess(sentence)
    sentence = " ".join(y for y in sentence)
    sentiment = SentimentIntensityAnalyzer()
    score = sentiment.polarity_scores(sentence)
    return score


def average_sentiment(tweets):

    scores = []
    for tweet in tweets:
        score = nltk_sentiment(tweet)
        scores.append(score['compound'])
    return sum(scores) / len(scores)


# string_input = input("Enter a tweet: ")
# print(average_sentiment([string_input]))
