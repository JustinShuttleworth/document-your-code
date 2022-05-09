import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format: str, language: str):
    """
    Calls an api that generates a random fact.

    Args:
        output_format: the return format of the fact. Choices: ["en", "de"]
        language: the language the fact will be returned in. Choices: ["html", "json", "txt", "md"]

    Returns:
        fact: random fact in your chosen language and output_format.
    """

    # check for supported language
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    # check for supported output format
    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    # send api get request for a random fact
    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    # check for a valid response code
    if response.status_code == 200:
        fact = response.json() if output_format == "json" else response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact


def test():
    print('hi')
    return 'world'