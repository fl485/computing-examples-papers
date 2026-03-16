import numpy as np
import pytest

def evals(A, B):
    return np.linalg.eigvalsh(A + B)

def test_working():
    A = np.diag([1.0, 2.0, 3.0])
    B = np.zeros((3, 3))
    result = evals(A, B)
    np.testing.assert_allclose(sorted(result), [1.0, 2.0, 3.0])

def test_zero_matrices():
    A = np.zeros((3, 3))
    B = np.zeros((3, 3))
    np.testing.assert_allclose(evals(A, B), np.zeros(3), atol=1e-12)

def test_scaling():
    rng = np.random.default_rng(3)
    M = rng.standard_normal((4, 4)); A = M + M.T
    N = rng.standard_normal((4, 4)); B = N + N.T
    c = 3.0
    np.testing.assert_allclose(evals(c*A, c*B), c * evals(A, B), rtol=1e-10)

