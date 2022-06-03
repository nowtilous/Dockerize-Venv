import argparse


def main():
    args = parse_args()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to venv root')
    return parser.parse_args()


if __name__ == "__main__":
    main()
