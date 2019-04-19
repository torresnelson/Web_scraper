#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

from typing import List, Tuple


def remove_newline(text: str) -> str:
    return text.replace("\n\n", "\n")


def get_links() -> List[str]:
    with open("lista", "r") as f:
        return f.read().split("\n")


def scrape_link(link: str) -> Tuple[str, str]:
    print(f"Scraping {link}...")

    src = requests.get(link)
    src.encoding = "UTF-8"
    soup = BeautifulSoup(src.text, "lxml")
    general_results = soup.body.find(
        "div",
        id="columna_resultados_generales"
        )
    conjugations = soup.body.find(
        "div",
        id="columna_resultados_conjugaciones"
        )
    general_results = general_results.text.split(")")[1]
    conjugations = conjugations.text.split(")")[1]
    return general_results, conjugations


def get_words() -> None:
    words = ""
    for link in get_links():
        general_results, conjugations = scrape_link(link)
        words += f"{remove_newline(general_results)}"\
            f"{remove_newline(conjugations)}"

        with open("spanish_words.txt", "w") as f:
            f.write(words)

        print("--- Ready ---")


if __name__ == "__main__":
    get_words()
