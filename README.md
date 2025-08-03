# Poetry CLI App

This is a CLI tool to automatically create a new Poetry-based Python project and Poetry environment — even if you're not inside a virtual environment.

### 👇 1. Clone the repo

```
git clone https://github.com/alessandro-maccario/poetry-cli-app.git
```

### 📦 2. Install `pipx` (if not already installed - Recommended)

This tool is meant to be used globally via [`pipx`](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/), which creates isolated virtual environments for each CLI application and puts them on your system `PATH`.

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

(Restart your terminal or reload your shell config to ensure pipx is available.)

### 3. ⚙️ Build your package

Inside this project folder, run:

```
poetry build
```

This will create a .whl and .tar.gz in the dist/ folder.

### 4. 🪛 Install the CLI with pipx

Run:
```
pipx install dist/<your-package-name-version>.whl
```

Example:
```
pipx install dist/poetry_cli_app-0.1.0-py3-none-any.whl
```

In your terminal, you should now see:

```
These apps are now globally available
    - poetry_cli_app
done! ✨ 🌟 ✨
```

### 5. ▶️ Use the CLI
Once installed, you can run the tool globally from any location:

```
poetry_cli_app <folder_destination> <folder_name>
```

Example:
```
poetry_cli_app /home/<username>/dev my-new-poetry-project
```

### 6. ℹ️ View the help:

```
poetry_cli_app --help
```

This will show available options and arguments.

### 7. ❌ Remove the package

```
pipx uninstall poetry_cli_app
```


#### References
 - [Installing stand alone command line tools](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/)
 - [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)