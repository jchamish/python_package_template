"""
Main executor
"""

from python_package_name.classes import Person


def main() -> None:
    """
    Main Executor and Dispatcher
    """
    joseph_chamish = Person("Joseph Chamish", 24)
    matthew_freeman = Person("Matthew Freeman", 29)

    print(joseph_chamish == matthew_freeman)  # Expect False


if __name__ == "__main__":
    # Do not add anything else here, all code should be handled in functions/methods
    main()
