"""
Run poetry commands to create a poetry folder and to get in a string format the path of the newly created environment.
Use it as a new Python interpreter in VS Code.
"""

#######################
### IMPORT PACKAGES ###
#######################

import argparse
import subprocess
import os


############
### MAIN ###
############


def create_new_poetry_env(folder_destination: str, folder_name: str):
    """Run poetry commands to create a new poetry folder in a specified location and print the new environment name
    created for it. This can then be used as a new interpreter for your new project in VS Code.

    Parameters
    ----------
        folder_name (str):
            The name of the new poetry folder

    Returns
    --------
        str:
            The environment string to be copied and used in VSCode to activate the environment for the specific project
    """

    # Remove the current environment before creating a new one
    # Clearing out the existing Python virtual environment context to ensure that Poetry creates a fresh,
    # isolated environment for the new project, instead of accidentally reusing an existing one
    env = os.environ.copy()
    # Remove the VIRTUAL_ENV variable if it exists
    env.pop("VIRTUAL_ENV", None)
    # Clean the PATH (remove anything pointing to .venv/bin or other virtual envs)
    env["PATH"] = ":".join(
        p for p in env["PATH"].split(":") if ".venv" not in p and "virtualenv" not in p
    )

    # create the poetry folder structure
    create_poetry_folder = subprocess.run(
        f"poetry new {folder_name}",
        cwd=folder_destination,  # change folder destination
        shell=True,
        capture_output=True,
        encoding="utf-8",
    )

    # check where python3 is on your system: whereis works on ubuntu, use 'where python' on Windows
    where_is_python = (
        subprocess.check_output("whereis python3", shell=True, encoding="utf-8")
        .split(":")[1]
        .strip()
        .split(" ")[0]
    )

    # get the env address to be then used in VS Code
    poetry_env_address = subprocess.run(
        f"poetry env use {where_is_python}",
        shell=True,
        capture_output=True,
        encoding="utf-8",
        cwd=os.path.join(
            folder_destination, folder_name
        ),  # needed to cwd into the newly created folder
        env=env,
    )

    # print the newly creted environment to the console to be able to copy it into VS Code Select Interpreter
    print(poetry_env_address.stdout)


def main():
    # Create a parser
    parser = argparse.ArgumentParser(description="Create a new Poetry environment.")

    # add the two arguments that we need to define the destination path and the folder name
    parser.add_argument(
        "folder_destination", help="Destination path for the new folder"
    )
    parser.add_argument("folder_name", help="Name of the new project folder")

    # Creat the Namespace where the parameters will be stored. You can call them as args.<parameter_name>
    args = parser.parse_args()
    create_new_poetry_env(args.folder_destination, args.folder_name)
