import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from Perceptron import Perceptron

# Generació del conjunt de mostres
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, n_repeated=0,
                           n_classes=2, n_clusters_per_class=1, class_sep=1.25,
                           random_state=0)

y[y == 0] = -1  # La nostra implementació esta pensada per tenir les classes 1 i -1.


perceptron = Perceptron()
perceptron.fit(X, y)  # Ajusta els pesos
y_prediction = perceptron.predict(X)  # Prediu

#  Resultats
plt.figure(1)
plt.scatter(X[:, 0], X[:, 1], c=y_prediction)  # Mostram el conjunt de mostres el color indica la classe

# ---------- AFEGIT: recta de divisió sobre la mateixa figura ----------
w0, w1, w2 = perceptron.w_
print("Pesos (w0, w1, w2):", perceptron.w_)

# Frontera: w0 + w1*x1 + w2*x2 = 0  ->  x2 = -(w0 + w1*x1) / w2
plt.axline((0, -w0 / w2), (1, -(w0 + w1) / w2), color='k', label='Recta de divisió')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Perceptron: mostres i recta de divisió')
plt.legend()

# ---------- AFEGIT: errors per època ----------
plt.figure(2)
plt.plot(range(1, len(perceptron.errors_) + 1), perceptron.errors_, marker='o')
plt.xlabel('Època')
plt.ylabel('Errors de classificació')
plt.title('Convergència del perceptron')

# ---------- AFEGIT: precisió ----------
accuracy = np.mean(y_prediction == y)
print(f"Precisió sobre el conjunt d'entrenament: {accuracy * 100:.1f}%")

plt.show()