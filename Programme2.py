from scipy.linalg import cho_factor, cho_solve, cholesky
import numpy as np
A = np.array([[32, -0.1, -0.2, -0.3, 0.4, 0.7],
              [-0.1, 7, -0.3, 0.5, 0.7, 2],
              [-0.2, -0.3, 10, 0.6, 0.8, 5],
              [-0.3, 0.5, 0.6, 15, 0.9, 6],
              [0.4, 0.7, 0.8, 0.9, 20, 7],
              [0.7, 2, 5, 6, 7, 21]])
B = np.array([1, 2, 3, 4, 5, 6])
C = cho_factor(A)
D = np.triu(A)
E = np.tril(A)
F = cholesky(A)
G = cho_solve(C, B)
print("\n Macierz pierwsza [A] : \n\n", A, "\n")
print("Macierz druga [B] : \n\n", B, "\n")
print("Macierz trójkątna krawędź górna : \n\n", D, "\n")
print("Macierz trójkątna krawędź dolna : \n\n", E, "\n")
print("Rozkład Choleskiego : \n\n", F, "\n")
print("Rozwiązanie : \n\n", G, "\n")
