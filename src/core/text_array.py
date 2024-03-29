from sklearn.feature_extraction.text import TfidfVectorizer

from core.nlang import Nlang


class TextArray:
    def __init__(self, data, vocabulary=None, vectorizer=None):
        self.data = data
        self._vocabulary = vocabulary
        self._vectorizer = vectorizer

    def to_vec(self, type=None):
        vectorizer = self.__build_vectorizer()
        feature_vectors = vectorizer.transform(self.__splited_data())
        if type == 'array':
            feature_vectors = feature_vectors.toarray()
        return feature_vectors

    def __build_vectorizer(self):
        if self._vectorizer is not None:
            return self._vectorizer

        if self._vocabulary is None:
            self._vectorizer = TfidfVectorizer(norm=None)
            # vectorizer = TfidfVectorizer(norm='l2', max_df=0.1, min_df=1)
            # vectorizer = TfidfVectorizer(min_df=1, max_df=100)
            # vectorizer = CountVectorizer()
            self._vectorizer.fit(self.__splited_data())
            self._vocabulary = self._vectorizer.get_feature_names()
        else:
            # vectorizer = CountVectorizer(vocabulary=self.vocabulary)
            self._vectorizer = TfidfVectorizer(vocabulary=self.vocabulary, norm=None)
        return self._vectorizer

    def __splited_data(self):
        splited_data = []
        for datum in self.data:
            splited_data.append(Nlang.split(datum))
        return splited_data

    # def __is_bigger_than_min_tfidf(self, term, terms, tfidfs):
    #     if tfidfs[terms.index(term)] > 0.01:
    #         return True
    #     return False

    # TODO vectorizerをpklするならvacabularyは不要な気がする
    @property
    def vocabulary(self):
        return self._vocabulary

    @property
    def vectorizer(self):
        return self._vectorizer
