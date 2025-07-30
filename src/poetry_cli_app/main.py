"""
Run poetry commands to create a poetry folder and to get in a string format the path of the newly created environment.
Use it as a new Python interpreter in VS Code.
"""

#######################
### IMPORT PACKAGES ###
#######################

import subprocess
import os

############
### MAIN ###
############


def poetry_env(folder_destination: str, folder_name: str):
    """Run poetry commands to create a new poetry folder in a specified location

    Parameters
    ----------
        folder_name (str):
            The name of the new poetry folder

    Returns
    --------
        str: _description_
    """

    # change the directory to the directoy destination first
    # os.chdir(os.path.abspath(os.path.expanduser(folder_destination)))

    # Step 1: Copy current environment
    env = os.environ.copy()

    # Step 2: Remove the VIRTUAL_ENV variable if it exists
    env.pop("VIRTUAL_ENV", None)

    # Step 3: Clean the PATH (remove anything pointing to .venv/bin or other virtual envs)
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

    # check where python3 is
    where_is_python = (
        subprocess.check_output("whereis python3", shell=True, encoding="utf-8")
        .split(":")[1]
        .strip()
        .split(" ")[0]
    )
    # print(where_is_python)

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

    # print the output to console
    print(poetry_env_address.stdout)


if "__name__" == "__main__":
    path_to_new_poetry_folder = input(
        "Set the path to the newly created poetry folder:\n"
    )
    poetry_folder_name = input("Folder name:\n")
    poetry_env(
        folder_destination=path_to_new_poetry_folder,
        folder_name=f"{poetry_folder_name}",
    )
