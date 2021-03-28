import pickle

class Model:
    __model = None
    __tfidfTransformer = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Model.__model == None and Model.__tfidfTransformer == None:
            Model()
        return Model.__model

    def __init__(self):
        """ Virtually private constructor. """
        if Model.__model != None and Model.__tfidfTransformer != None:
            raise Exception("Something went wrong") 
        else:
            with open('spam_model/text_classifier', 'rb') as spam_detection_model:
                Model.__model = pickle.load(spam_detection_model)
            with open('spam_model/TfidfTransformer', 'rb') as tfidfTransformer:
                Model.__tfidfTransformer = pickle.load(tfidfTransformer)

    @staticmethod
    def predict(text):
      transform = Model.__tfidfTransformer.transform([text])
      return Model.__model.predict(transform)

