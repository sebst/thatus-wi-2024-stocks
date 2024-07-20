import os
from string import Template
import tomllib

import yfinance as yf


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_symbols():
    with open(os.path.join(SCRIPT_DIR, "../config/config.toml"), "rb") as f:
        config = tomllib.load(f)
    symbols = config["symbols"]
    sorted_symbols = sorted(symbols)
    return sorted_symbols


def get_symbol_md(symbol):
    with open(os.path.join(SCRIPT_DIR, "templates/partials/symbol.md")) as f:
        template = Template(f.read())
    return template.substitute(symbol=symbol)


def get_symbol_toc(symbol):
    return f"- [{symbol}](#{symbol})"


def update_readme(symbols):
    with open(os.path.join(SCRIPT_DIR, "templates/README.md")) as f:
        template = Template(f.read())
    symbols_md = "\n".join([get_symbol_md(symbol) for symbol in symbols])
    toc = "\n".join([get_symbol_toc(symbol) for symbol in symbols])
    readme = template.substitute(symbols_md=symbols_md, toc=toc)
    with open(os.path.join(SCRIPT_DIR, "../README.md"), "w") as f:
        f.write(readme)


def main():
    symbols = get_symbols()
    update_readme(symbols)


if __name__ == "__main__":
    main()
