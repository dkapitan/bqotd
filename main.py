import click
import ndjson
from random import choice


with open("quotes.json", "r") as file:
    quotes = ndjson.load(file)

@click.command()
def bqotd():
    quote = choice(quotes)
    print(f"{quote['quote']}\n  ~ {quote['attribution']}, {quote['source']}")


if __name__ == "__main__":
    bqotd()