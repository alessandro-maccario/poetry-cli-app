A small poetry cli app: the main goal is to run the cli poetry app instead of manually running all the commands in order to create a poetry environment.

On `Ubuntu`:
What you usually do manually to create a poetry environment is as follows (in the CLI):
1. poetry new <folder-name>
2. whereis python3
3. `cd` into the newly created <folder-name> folder and then `poetry env use /usr/bin/python3`. You should then see an output similar to the following: `Creating virtualenv poetry-cli-app-9d0BHpKN-py3.12 in /home/m/.cache/pypoetry/virtualenvs`
`Using virtualenv: /home/m/.cache/pypoetry/virtualenvs/poetry-cli-app-9d0BHpKN-py3.12`
4. In VSCode, at this point, you press `CTRL+P`, then `Python: Select Interpreter`, then `Enter Interpreter Path` and you should insert the `path` given in point 3. that is available after the _Using virtualenv:_. It contains the path to the current virtual environment connected to your newly created project folder.

