import os.path

pytest_plugins = [
    'data_driven',
]


def pytest_configure(config):
    mypy_source_root = os.path.dirname(os.path.abspath(__file__))
    if os.getcwd() != mypy_source_root:
        os.chdir(mypy_source_root)


# This function name is special to pytest.  See
# http://doc.pytest.org/en/latest/writing_plugins.html#initialization-command-line-and-configuration-hooks
def pytest_addoption(parser) -> None:
    parser.addoption('--bench', action='store_true', default=False,
                     help='Enable the benchmark test runs')
    group = parser.getgroup('mypy')
    group.addoption('--mypy-verbose', action='count',
                    help='Set the verbose flag when creating mypy Options')
    group.addoption('--mypyc-showc', action='store_true', default=False,
                    help='Display C code on mypyc test failures')
