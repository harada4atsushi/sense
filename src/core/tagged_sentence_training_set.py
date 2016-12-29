import numpy as np
import pandas as pd
import MySQLdb
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.externals import joblib
# from .base import Base
# from learning.config.config import Config
# from learning.log import logger
# from learning.core.predict.tag import Tag
#
from core.text_array import TextArray


class TaggedSentenceTrainingSet:

    def __init__(self):
        host = 'localhost'
        dbname = 'sense'
        user = 'root'
        password = ''
        self.db = MySQLdb.connect(host=host, db=dbname, user=user, passwd=password, charset='utf8')

#         config = Config()
#         self.db = db
#         self.bot_id = bot_id
#         self.learning_parameter = learning_parameter
#         self.classfy_failed_answer_id = self.__find_classfy_failed_answer_id()
#         # self.binarizer = joblib.load("learning/models/%s/tag_model_labels.pkl" % config.env)  # TODO 共通化したい
#
    def build(self):
        sentences = pd.read_sql("select body, (select group_concat(id separator ',') from taggings where taggings.taggable_id = sentences.id) as tag_ids from sentences having tag_ids is not null;", self.db)
        body_array = TextArray(sentences['body'])
        self._x = body_array.to_vec(type='array')
        self._body_array = body_array

        self._y = sentences['tag_ids'].str.split(',')

    @property
    def body_array(self):
        return self._body_array

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
#
#
#
#     def __build_learning_training_messages(self):
#         data = pd.read_sql("select * from learning_training_messages where bot_id = %s;" % self.bot_id, self.db)
#         if self.learning_parameter.include_failed_data:
#             data_count = data['id'].count()
#             other_data = pd.read_sql("select * from learning_training_messages where bot_id <> %s and char_length(question) > 10 order by rand() limit %s;" % (self.bot_id, data_count), self.db)
#             other_data['answer_id'] = self.classfy_failed_answer_id
#             data = pd.concat([data, other_data])
#         logger.debug("data['id'].count(): %s" % data['id'].count())
#         # data = pd.read_csv('prototype_id.csv', encoding='SHIFT-JIS')
#         # logger.debug("data['question'].count(): %s" % data['question'].count())
#         return data
#
#     # HACK learning_training_messagesをクラスにするとリファクタリングできそう
#     def __extract_binarized_tag_vector(self, learning_training_messages):
#         tag_ids = learning_training_messages['tag_ids']
#         tag_ids[tag_ids.isnull()] = ','
#         tag_ids[tag_ids == ''] = ','
#         tag_ids = tag_ids.str.split(':')
#         logger.debug("tag_ids: %s" % list(tag_ids))
#
#         try:
#             logger.debug("self.binarizer.classes_: %s" % self.binarizer.classes_)
#             tag_vector = self.binarizer.transform(tag_ids)
#         except KeyError as e:
#             logger.error('タグ学習時に存在していなかったタグが含まれている可能性があります。python learn_tag.pyを実行してください。')
#             raise e
# #
#         logger.debug("tag_vector: %s" % tag_vector)
#         return tag_vector
#
#     def __find_classfy_failed_answer_id(self):
#         cursor = self.db.cursor()
#         cursor.execute("select id from answers where defined_answer_id = %s" % self.CLASSIFY_FAILED_ID)
#         return cursor.fetchone()[0]
