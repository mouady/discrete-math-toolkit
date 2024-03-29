from pytest import approx
from src.recursion import *

# Recursions

basic_first_grade = HomogenousRecursion((1, 2), [Case(0, 1)])
double = HomogenousRecursion((1, 2, -1), [Case(0, 0), Case(1, 1)])
fibonacci = HomogenousRecursion((1, 1, 1), [Case(0, 0), Case(1, 1)])
random = HomogenousRecursion((1, -2, 1), [Case(0, 0), Case(1, 1)])

# Grade Function


def test_grade_1(benchmark):
    grade = benchmark(basic_first_grade.grade)
    assert grade == 1


def test_grade_2(benchmark):
    grade = benchmark(fibonacci.grade)
    assert grade == 2

# Solve Function


def test_solve_grade1(benchmark):
    res = benchmark(basic_first_grade.solve)
    assert res == RecursionSolution(1, None, 1, 2, None, None)


def test_solve_grade2_double_root(benchmark):
    res = benchmark(double.solve)
    assert res == RecursionSolution(2, True, 0, 1, 1, None)


def test_solve_grade2_different_root(benchmark):
    res = benchmark(fibonacci.solve)
    assert res == RecursionSolution(
        grade=2,
        double_root=False,
        coefficient0=approx(1/sqrt(5)),
        coefficient1=approx(-1/sqrt(5)),
        root0=approx((1+sqrt(5))/2),
        root1=approx((1-sqrt(5))/2))

# Solve for n Function


def test_solve_for_n_grade1(benchmark):
    res = benchmark(basic_first_grade.solve_for_n, 4)
    assert res == 16


def test_solve_for_n_grade2_double_root(benchmark):
    res = benchmark(double.solve_for_n, 3)
    assert res == 3


def test_solve_for_n_grade2_different_root(benchmark):
    res = benchmark(fibonacci.solve_for_n, 7)
    assert res == approx(13)


def test_solve_for_n_random(benchmark):
    res = benchmark(random.solve_for_n, 4)
    assert res == approx(-12)
