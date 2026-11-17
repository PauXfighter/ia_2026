import numpy as np


class Perceptron:

    """Perceptron classifier.

    Parameters
    ------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.

    Attributes
    -----------
    w_ : 1d-array
        Weights after fitting. w[0] = threshold
    errors_ : list
        Number of miss classifications in each epoch.

    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        self.w_ = None
        self.errors_ = []

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi.reshape(1, -1))[0])
                self.w_[0] += update
                self.w_[1:] += update * xi
                errors += (target - self.predict(xi.reshape(1, -1))[0])
            self.errors_.append(errors)
        return self

    def predict(self, X):
        z = np.dot(X, self.w_[1:]) + self.w_[0]
        return np.where(z >= 0.0, 1, -1)