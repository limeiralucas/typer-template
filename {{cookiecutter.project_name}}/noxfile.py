"""Nox Configuration File

This module is used to configure multiple sessions for nox.
Such as linting, static typing checking and executing tests agains multiple
Python versions.
"""

import nox

PYTHON_VERSIONS = ["3.8", "3.11"]

nox.needs_version = ">=2022.11.21"
nox.options.reuse_existing_virtualenvs = True


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Executes tests agains multiple Python versions"""
    session.run("poetry", "install", external=True)
    session.run("pytest")


@nox.session
def mypy(session):
    """Executes static type checking"""
    session.run("poetry", "install", external=True)
    session.run("mypy", ".")


@nox.session
def lint(session):
    """Executes linting agains main module and config files using pylint and black"""
    session.run("poetry", "install", external=True)
    session.run("black", ".")
    session.run("isort", "--profile", "black", ".")
    session.run("pylint", "{{cookiecutter.project_name}}")
    session.run("pylint", "noxfile.py")
