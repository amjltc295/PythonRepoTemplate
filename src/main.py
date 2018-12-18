import argparse

from logging_config import logger


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input_path', type=str, help='Input data path'
    )
    parser.add_argument(
        '-o', '--output_path', type=str, help='Output data path'
    )
    args = parser.parse_args()
    return args


def main(args):
    logger.info(args)


if __name__ == "__main__":
    args = parse_args()
    main(args)
