import items


def test_stdout(capsys):
    with capsys.disabled():
        version = items.__version__
        print("\nitems " + version)
