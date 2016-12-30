# from learning.log import logger
# from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.externals import joblib
# from learning.core.nlang import Nlang
# from learning.config.config import Config
# from learning.core.training_set.training_text import TrainingText
# from learning.core.training_set.text_array import TextArray
from core.model_not_exists_error import ModelNotExistsError
from core.text_array import TextArray


class Document:

    def __init__(self, sentences):
        self._sentences = sentences

    def tag(self):
        try:
            estimator = joblib.load("models/estimator.pkl")
            vectorizer = joblib.load('models/vectorizer.pkl')
            binarizer = joblib.load('models/binarizer.pkl')
        except IOError:
            raise ModelNotExistsError()

        text_array = TextArray(self._sentences, vectorizer=vectorizer)
        features = text_array.to_vec()
        tags = estimator.predict(features.toarray())
        self._tags = binarizer.inverse_transform(tags)
        return self._tags

        # tagged_sentences =  np.c_[self._sentences, self._tags]
        # print(tagged_sentences)
        # return tagged_sentences


# #
#     def predict(self, X, return_type='id'):
#         if len(X) == 0:
#             return []
#         body_array = TextArray(X, vocabulary=self.vocabulary)
#         result = self.estimator.predict(body_array.to_vec())
#         logger.debug("predicted_tag_ids: %s" % result)
#         logger.debug("inversed_predicted_tag_ids: %s" % self.binarizer.inverse_transform(result))
#
#         if return_type == 'id':
#             result = self.binarizer.inverse_transform(result)
#
#         return result
#
#     def binarize(self, tag_ids):
#         return self.binarizer.transform(tag_ids)
