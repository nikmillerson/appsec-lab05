import typer


def main(
    name: str,
    lastname: str = typer.Option(
        "",
        help="Фамилия пользователя.",
    ),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Использовать формальное приветствие.",
    ),
) -> None:
    """
    Говорит "Привет" пользователю, опционально используя фамилию
    и формальный стиль.
    """
    # Здесь либо привет, либо добрый день можно выбрать.
    if formal:
        full_name = f"{name} {lastname}".strip()
        print(f"Добрый день, {full_name}!")
    else:
        print(f"Привет, {name}!")


# Запускаю приложение как консольное
if __name__ == "__main__":
    typer.run(main)
