def main() -> None:
    from pathlib import Path

    import ndjson
    from random import choice
    
    HERE = Path(__file__).parent

    with open(HERE / "quotes.json", "r") as file:
        quotes = ndjson.load(file)

    quote = choice(quotes)
    if quote.get("source") and quote.get("attribution"):
        print(f"{quote['quote']}\n  ~ {quote['attribution']}, {quote['source']}\n")
    if quote.get("attribution") and not quote.get("source") :
        print(f"{quote['quote']}\n  ~ {quote['attribution']}")
    if quote.get("source") and not quote.get("attribution"):
        print(f"{quote['quote']}\n  ~ {quote['source']}\n")