import numpy as np
from gevent.server import StreamServer
from mprpc import RPCServer
from sklearn.externals import joblib
from core.document import Document
from core.log import logger


class Server(RPCServer):
    STATUS_CODE_SUCCESS = 1
    # STATUS_CODE_MODEL_NOT_EXISTS = 101
    #
    # def reply(self, bot_id, context, body, learning_parameter_attributes):
    #     learning_parameter = LearningParameter(learning_parameter_attributes)
    #     # X = list(context)
    #     # X.append(body)
    #     # HACK かっこを二重にしないとなぜかprobabilityが下がる(要調査)
    #     X = np.array([body])
    #     predict_results = {}
    #     status_code = self.STATUS_CODE_SUCCESS
    #
    #     try:
    #         predict_results = Reply(bot_id, learning_parameter).predict(X)
    #         logger.debug(predict_results)
    #         # if answer_id is not None:
    #         #     answer_id = float(answer_id)
    #     except ModelNotExistsError:
    #         status_code = self.STATUS_CODE_MODEL_NOT_EXISTS
    #
    #     result = {
    #         'status_code': status_code,
    #         # 'results':  [{'probability': 0.99974810633704125, 'answer_id': 20}, {'probability': 4.8263524435402245e-05, 'answer_id': 2092}, {'probability': 3.8650944875454533e-06, 'answer_id': 2065}, {'probability': 3.3403655454494557e-06, 'answer_id': 2128}, {'probability': 3.2779455165232719e-06, 'answer_id': 2298}, {'probability': 3.2096909894687076e-06, 'answer_id': 57}, {'probability': 2.770086869426734e-06, 'answer_id': 2030}, {'probability': 2.4034569493278136e-06, 'answer_id': 2314}, {'probability': 2.4034569493267467e-06, 'answer_id': 2337}, {'probability': 2.3194390806239406e-06, 'answer_id': 2047}]
    #
    #         'results': predict_results,
    #     }
    #     return result
    #     # return { 'status_code': status_code, 'answer_id': answer_id }
    #
    # def learn(self, bot_id, learning_parameter_attributes):
    #     learning_parameter = LearningParameter(learning_parameter_attributes)
    #     evaluator = Bot(bot_id, learning_parameter).learn()
    #     return {
    #         'accuracy': evaluator.accuracy,
    #         'precision': evaluator.precision,
    #         'recall': evaluator.recall,
    #         'f1': evaluator.f1,
    #     }
    #
    # def learn_tag_model(self):
    #     LearnTag().learn()
    #     return { 'status_code': self.STATUS_CODE_SUCCESS }
    #
    def predict(self, sentences):
        tags = Document(np.array(sentences)).tag()
        logger.debug("tags: %s" % tags)
        return {
            'status_code': self.STATUS_CODE_SUCCESS,
            'tags': tags
        }


server = StreamServer(('127.0.0.1', 6000), Server())
server.serve_forever()
