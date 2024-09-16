import doctest
from gematriapy import gematria


# Discover all doctests in the package
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(gematria))
    return tests
