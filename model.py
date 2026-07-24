from sklearn.linear_model import LinearRegression

def model_exist(model_file):
    import os
    return(os.path.exists(model_file))

def reshape_data_for_sklearn(rows):

    x = []
    y = []

    for row in rows:
        population = row[3]
        area = row[4]

        x.append([population])
        y.append(area)
    
    return x,y


def train_model(X,Y):

    model = LinearRegression()
    model.fit(X,Y)
    return model

def save_model():
    pass

def load_model():
    pass