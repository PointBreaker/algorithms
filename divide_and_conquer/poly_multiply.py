import numpy as np

roots_of_unities = lambda n: np.array([np.exp(2 * np.pi * 1j * i / n) for i in range(n)])
hyperceil = lambda x: int(2 ** np.ceil(np.log2(x)))

def fft(coeffs, roots):
    """
    args:
        coeffs (np.array): array of numbers representing the coefficients of a polynomial where coeffs[i]
                    is the coeffiecient of the term x^i
        roots (np.array): array containing the roots of unity [w_0, w_1, w_2, ..., w_{n-1}]
    return:
        List containing the results of evaluating the polynomial at the roots of unity
        [P(w_0), P(w_1), P(w_2), ...]
    """
    coeffs = np.array(coeffs)
    roots = np.array(roots)
    n = len(coeffs)
    assert n == hyperceil(n)
    if n == 1:
        return coeffs
    mid = n >> 1
    y_even = fft(coeffs[0:n:2], roots[0:n:2])
    y_odd = fft(coeffs[1:n:2], roots[0:n:2])
    high = y_even + roots[:mid] * y_odd
    low = y_even + roots[mid:] * y_odd
    y = np.concatenate((high, low), axis=0)
    return y

def ifft(vals, roots):
    """
    args:
        val (np.array): numpy array containing the results of evaluating the polynomial at the roots of unity
                    [P(w_0), P(w_1), P(w_2), ...]

        roots (np.array): numpy array containing the roots of unity [w_0, w_1, w_2, ..., w_{n-1}]

    return:
        List containing the results of evaluating the polynomial at the roots of unity. Can be a Python list
            or numpy array.
        [P(w_0), P(w_1), P(w_2), ...]
    """
    n = len(vals)
    assert n == hyperceil(n)
    return 1 / len(vals) * fft(vals, roots ** -1)

def pad(coeffs, to):
    """
    args:
        coeffs:List[] = list of numbers representing the coefficients of a polynomial where coeffs[i]
                    is the coeffiecient of the term x^i
        to:int = the final length coeffs should be after padding

    return:
        List of coefficients zero padded to length 'to'
    """
    res = np.append(coeffs, np.zeros(to - len(coeffs)))
    return res

round_complex_to_int = lambda lst: [round(x.real) for x in lst]
zero_pop = lambda lst: np.trim_zeros(lst, "b")


def poly_multiply(coeffs1, coeffs2):
    """
    args:
        coeffs1:List[] = list of numbers representing the coefficients of a polynomial where coeffs[i]
                    is the coeffiecient of the term x^i
        coeffs2:List[] = list of numbers representing the coefficients of a polynomial where coeffs[i]
                    is the coeffiecient of the term x^i

    return:
        List of coefficients corresponding to the product polynomial of the two inputs.
    """
    n = hyperceil(2 * max(len(coeffs1), len(coeffs2)) + 1)
    coeffs1 = pad(coeffs1, n)
    coeffs2 = pad(coeffs2, n)
    roots = roots_of_unities(n)
    val1 = fft(coeffs1, roots)
    val2 = fft(coeffs2, roots)
    val = val1 * val2
    return zero_pop(round_complex_to_int(ifft(val, roots)))


if __name__ == "__main__":
    print(poly_multiply([1, 1, 1, -1], [-1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1]))


