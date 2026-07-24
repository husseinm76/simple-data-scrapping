from sklearn.linear_model import LinearRegression
import  pickle

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


def train_model(rows):
    x,y = reshape_data_for_sklearn(rows)
    model = LinearRegression()
    model.fit(x,y)
    print('* Train Model : Successfully')
    return model

def save_model(model, model_file):

    with open(model_file,'wb') as file:
        pickle.dump(model, file)
    print('* Save Model : Successfully')

def load_model():
    pass

if __name__ == '__main__':

    from database import read_data

    rows = read_data('countries.db')
    model = train_model(rows)
    print(model.predict([[520]]))
