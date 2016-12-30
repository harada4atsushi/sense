from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

from core.document import Document
from core.tagged_sentence_training_set import TaggedSentenceTrainingSet
from core.text_array import TextArray

X = [
    'こんにちは！',
    'こんにちは、君は誰なの？',
    'こんばんは',
    '撤収しました！ お疲れ様でした！',
    'おっけーです'
]

# estimator = joblib.load("models/estimator.pkl")
# vectorizer = joblib.load('models/vectorizer.pkl')
# binarizer = joblib.load('models/binarizer.pkl')
#
# text_array = TextArray(X, vectorizer=vectorizer)
# features = text_array.to_vec()
# print(features.toarray())
#
# result = estimator.predict(features.toarray())
# print(result)
#
# print(binarizer.inverse_transform(result))

result = Document(X).tag()
