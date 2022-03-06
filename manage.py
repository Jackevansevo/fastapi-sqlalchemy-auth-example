#!/usr/bin/env python

import click
from subprocess import call
from sql_app.models import *


@click.group()
def cli() -> None:
    pass


@cli.command()
def runserver() -> None:
    call(["uvicorn", "sql_app.main:app", "--reload"])


@cli.command()
def shell() -> None:
    from IPython import embed

    embed(colors="neutral")


@cli.command()
def initdb() -> None:
    from sql_app.database import engine
    from sql_app.models import Base

    Base.metadata.create_all(bind=engine)
    click.echo("Initialized the database")


@cli.command()
def dropdb() -> None:

    from sql_app.database import engine
    from sql_app.models import Base

    Base.metadata.drop_all(bind=engine)
    click.echo("Dropped the database")


if __name__ == "__main__":
    cli()
