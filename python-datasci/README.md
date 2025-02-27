# {{ name }}
{% if __project_description__ %}
{{ __project_description__ }}
{% endif %}
## Introduction

This is a Renku project - basically a git repository with some
bells and whistles. You'll find we have already created some
useful things like `data` and `notebooks` directories and
a `Dockerfile`.

## {{ __template_id__ }} template

This project was created with the {{ __template_id__ }} template. It has the following things pre-configured:

###  Pre-installed packages

Common data-science packages come pre-installed in the template (listed in `requirements.txt`).

### Pre-commit

Pre-commit is installed and configured to format and lint code before every commit (see `.pre-commit-config.yaml`).
Whenever you commit code, pre-commit is set to run the following hooks on your code:

* trailing-whitespace: Trims whitespace at the end of lines.
* end-of-file-fixer: Removes empty lines at the end of file.
* check-ast: Checks if python code is valid.
* check-merge-conflict: Prevents commits with merge conflicts.
* [black](https://github.com/psf/black): Code formatting.
* [flake8](https://flake8.pycqa.org/en/latest/): Checks for problematic python code.
* [isort](https://github.com/PyCQA/isort): Sorts imports in python files.

If you try to commit code containing syntax errors or undefined variables, pre-commit will show the problems and prevent you from commit until you fix the issues.

If you wish to quickly commit incorrect code and ignore pre-commit's analysis, you can always run `git commit --no-verify`.

### Project structure

The project contains a basic directory structure (inspired from [cookiecutter data-science](https://drivendata.github.io/cookiecutter-data-science/).

```
 ├── data             # data files
 ├── notebooks        # jupyter notebooks
 └── src              # code
    ├── scripts       # command line scripts
    ├── tests         # unit tests
    └── project_name  # importable library
```
### Local package

The `src` folder contains a subdirectory with your project's name, which can be installed as a local "development" package (defined in `setup.py`) by running `pip install -e .`. Inside a Renku session, this package will already be available thanks to the `post-init.sh` script which is executed whenever starting a session. Once installed, code in this directory can be imported from anywhere using `import project_name`.

### Default Makefile recipes

A Makefile is also included. It contains basic recipes to install, test and lint the local package.

## Working with the project

The simplest way to start your project is right from the Renku
platform - just click on the `Sessions` tab and start a new session.
This will start an interactive session right in your browser.

To work with the project anywhere outside the Renku platform,
click the `Settings` tab where you will find the
git repo URLs - use `git` to clone the project on whichever machine you want.

### Changing interactive environment dependencies

Initially we install a very minimal set of packages to keep the images small.
However, you can add python and conda packages in `requirements.txt` and
`environment.yml` to your heart's content. If you need more fine-grained
control over your environment, please see [the documentation](https://renku.readthedocs.io/en/latest/user/advanced_interfaces.html#dockerfile-modifications).

## Project configuration

Project options can be found in `.renku/renku.ini`. In this
project there is currently only one option, which specifies
the default type of environment to open, in this case `/lab` for
JupyterLab. You may also choose `/tree` to get to the "classic" Jupyter
interface.

## Moving forward

Once you feel at home with your project, we recommend that you replace
this README file with your own project documentation! Happy data wrangling!
