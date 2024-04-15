import numpy as np
from numpy.linalg import inv


class LinearLeastSquare:
    def __init__(self):
        self.W = None

    def fit(self, X_train, Y_train):
        # train
        # W = (X.T * X)^-1 * X.T * Y
        # W = inv(X.T @ X) @ X.T @ Y
        self.W = inv(X_train.T @ X_train) @ X_train.T @ Y_train

    def predict(self, X_test):
        Y_pred = X_test @ self.W

        return Y_pred
    
    def evaluate(self, X_test, Y_test):
        pass

