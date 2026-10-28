import sys
import time

import requests

SERVER_URL = "http://server:8000/api/message"
MAX_ATTEMPTS = 10
REQUEST_TIMEOUT = 3
RETRY_DELAY = 1


def colorful_print(text: str) -> None:
    colors = [
        "\033[91m",
        "\033[92m",
        "\033[93m",
        "\033[94m",
        "\033[95m",
    ]
    reset = "\033[0m"

    for index, character in enumerate(text):
        color = colors[index % len(colors)]
        sys.stdout.write(color + character + reset)
        sys.stdout.flush()
        time.sleep(0.03)

    print()


def get_server_message() -> str:
    last_error = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = requests.get(
                SERVER_URL,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            return response.json()["message"]
        except requests.RequestException as error:
            last_error = error
            print(
                f"Сервер ещё не готов: попытка "
                f"{attempt}/{MAX_ATTEMPTS}",
                file=sys.stderr,
            )

            if attempt < MAX_ATTEMPTS:
                time.sleep(RETRY_DELAY)

    raise RuntimeError(
        "Не удалось получить ответ сервера"
    ) from last_error


if __name__ == "__main__":
    colorful_print(get_server_message())
