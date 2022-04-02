import pickle


def load_model(path):
    return pickle.load(open(path, "rb"))


def save_model(model, path):
    pickle.dump(model, open(path, "wb"))
