from sklearn.linear_model import LinearRegression

def model_exist(model_file):
    import os
    return(os.path.exists(model_file))


def train_model(X,Y):

    model = LinearRegression()
    model.fit(X,Y)
    return model

def save_model():
    pass

def load_model():
    pass