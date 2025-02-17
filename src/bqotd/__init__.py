def main() -> None:
    from pathlib import Path

    import ndjson
    from random import choice
    
    HERE = Path(__file__).parent

    with open(HERE / "quotes.json", "r") as file:
        quotes = ndjson.load(file)

    quote = choice(quotes)
    print(f"{quote['quote']}\n  ~ {quote['attribution']}, {quote['source']}\n")
