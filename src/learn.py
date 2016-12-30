import numpy as np
# import pandas as pd
# import MySQLdb
# from learning.log import logger
# from learning.core.training_set.text_array import TextArray
# from learning.core.training_set.training_text import TrainingText
# from learning.core.nlang import Nlang
# from learning.config.config import Config
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from core.tagged_sentence_training_set import TaggedSentenceTrainingSet
# from sklearn.feature_extraction.text import CountVectorizer

# c = OneVsRestClassifier(SVC(kernel='linear', probability=True))
# tag_ids = [[1,2,3,4,5,6,7,8,9]]
# X = np.array([[1,0,1],[1,1,1],[0,0,1]])
# y = [[1,2],[3,4],[5,6]]
#
# binarizer = MultiLabelBinarizer().fit(tag_ids)
# binarized_y = binarizer.transform(y)
# estimator = c.fit(X, binarized_y)
#
# result = estimator.predict(X)
# print(result)
from core.text_array import TextArray

training_set = TaggedSentenceTrainingSet()
training_set.build()

# data = [
#         [[1, 3, 4], 1, 10, 0, 0, 0],
#         [[2, 3, 4, 5, 21], 0, 7, 22, 0, 0],
#         [[3, 4, 5, 6, 10], 0, 0, 6, 0, 20],
#        ]
#
# X = np.array([d[1:] for d in data])
# yvalues = np.array([d[0] for d in data])
# print(training_set.y)


# Create a binary array marking values as True or False
binarizer = MultiLabelBinarizer()
print('trainin set count: %s' % len(training_set.y))
print(training_set.y)
Y = binarizer.fit_transform(training_set.y)
# Y = binarizer.fit_transform(yvalues)
print(Y)

estimator = OneVsRestClassifier(SVC(kernel='linear'))
estimator.fit(training_set.x, Y)

joblib.dump(estimator, "models/estimator.pkl")
joblib.dump(training_set.body_array.vectorizer, "models/vectorizer.pkl")
joblib.dump(binarizer, "models/binarizer.pkl")