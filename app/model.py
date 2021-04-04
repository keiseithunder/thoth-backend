import pickle

class Model:

    @staticmethod
    def predict(text):
      tfidf = None
      model = None
      with open('spam_model/text_classifier', 'rb') as spam_detection_model:
          model = pickle.load(spam_detection_model)
      with open('spam_model/TfidfTransformer', 'rb') as tfidfTransformer:
          tfidf = pickle.load(tfidfTransformer)
      transform = tfidf.transform(text)
      return model.predict(transform)

