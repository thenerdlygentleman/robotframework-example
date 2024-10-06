from typing import Optional
import typer
from typing_extensions import Annotated

from src.testsuite import TestSuite

app = typer.Typer()


@app.command()
def main(debug: Annotated[Optional[str], typer.Argument()] = False):
    TestSuite().run(debug=debug)


if __name__ == "__main__":
    app()
