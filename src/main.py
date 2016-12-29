import numpy as np
# import pandas as pd
# import MySQLdb
# from learning.log import logger
# from learning.core.training_set.text_array import TextArray
# from learning.core.training_set.training_text import TrainingText
# from learning.core.nlang import Nlang
# from learning.config.config import Config
# from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
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


data = [
        [[1 , 2, 3, 4], 1, 10, 0, 0, 0],
        [[2 , 3, 4, 5], 0, 7, 22, 0, 0],
        [[3 , 4, 5, 6], 0, 0, 6, 0, 20],
       ]

X = np.array([d[1:] for d in data])
yvalues = np.array([d[0] for d in data])

# Create a binary array marking values as True or False
from sklearn.preprocessing import MultiLabelBinarizer
binarizer = MultiLabelBinarizer()
Y = binarizer.fit_transform(yvalues)

clf = OneVsRestClassifier(SVC(kernel='poly'))
clf.fit(X, Y)
result = clf.predict(X) # predict on a new X

print(binarizer.inverse_transform(result))


