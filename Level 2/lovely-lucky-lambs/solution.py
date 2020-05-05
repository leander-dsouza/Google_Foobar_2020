from math import sqrt,log
def solution(total_lambs):

    phi = (1+sqrt(5))/2  # golden search ratio
    tau = (1-sqrt(5))/2  # equal to 1/phi
    eps = pow(10, -10)

    max_hunchmen = int(round(log((total_lambs + 1) * sqrt(5)+eps, phi))) - 2
    Fib_num = int(round((pow(phi, max_hunchmen+2)-pow(tau, max_hunchmen+2))/sqrt(5)))
    if total_lambs+1 < Fib_num:
        max_hunchmen -= 1

    min_hunchmen = int(log((total_lambs + 1), 2))

    return max_hunchmen - min_hunchmen
