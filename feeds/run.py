import argparse
import logging
import sys

from code_challenge.api.config_file import ConfigFile
from code_challenge.api.graphql_reader import GraphQLReader
from feeds.feed_y import FeedY


def config_log():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    root.addHandler(handler)


def main():
    parser = argparse.ArgumentParser("feed")
    parser.add_argument("ticker")
    parser.add_argument("-H", "--host")
    parser.add_argument("-e", "--endpoint")
    parser.add_argument("-t", "--token")
    args = parser.parse_args()

    config_log()

    config_file = ConfigFile()
    settings = config_file.read()
    if args.host:
        settings.host = args.host
    if args.endpoint:
        settings.endpoint = args.endpoint
    if args.token:
        settings.token = args.token
    config_file.write(settings)

    reader = GraphQLReader(settings)
    feed = FeedY(reader)
    feed.fill(args.ticker)


if __name__ == "__main__":
    main()
