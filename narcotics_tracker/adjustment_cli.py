"""Playing around with a command line interface for the Narcotics Tracker."""

import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    """Says Hello."""
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    """Says goodbye.

    Args:

        name (str): Who you're saying goodbye to.

        formal (bool): Set True for formal message.
    """
    if formal:
        print(f"Goodbye Mx. {name}. Have a good day.")
    else:
        print(f"Bye {name}.")


if __name__ == "__main__":
    app()
