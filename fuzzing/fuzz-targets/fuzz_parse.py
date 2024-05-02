import atheris
import sys
from io import BytesIO

with atheris.instrument_imports():
    import feedparser


def TestOneInput(data):
    feedparser.parse(BytesIO(data))


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
