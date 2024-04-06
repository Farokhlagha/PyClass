import numpy as np

class KNN:
    def __init__(self, K):
        self.K = K

    # training
    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

    def predict(self, X): # x:fruit X:fruits
        Y = []
        for x in X:
            distances = []
            for x_train in self.X_train:
                d = self.euclidean_distance(x, x_train)
                distances.append(d)

            
            nearest_neighbors = np.argsort(distances)[0:self.K]  # argsort:index of aaray # fruit 189th
            result = np.bincount(self.Y_train[nearest_neighbors])  # bincount: count number of array 0:2  1:3
            y = np.argmax(result)
            Y.append(y) 
        return Y
    
    def evaluate(self, X, Y):
        Y_pred = self.predict(X)
        accuracy = np.sum(Y_pred == Y) / len(Y)
        return accuracy 