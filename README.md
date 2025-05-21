# Offline Python Package Installer & Virtual Environment Manager



This tool is a comprehensive offline package downloader and installer for Python projects. It allows you to:



- **Download packages offline**: Save package files into a designated folder (`libay`).

- **Install packages offline**: Install packages from the offline folder without requiring an Internet connection.

- **Create a virtual environment**: Set up a Python virtual environment (`venv`) and install packages into it.

- **Run a Python script within the virtual environment**: Opens a new terminal window (PowerShell on Windows or gnome-terminal on Linux) and runs your script.

- **Select a desired Python version**: Choose from 3.9, 3.10, 3.11, 3.12, or 3.13 to determine which package versions to install.

- **Platform-specific handling**: On Windows, the `uvloop` package is automatically skipped as it is intended only for Linux.



## Features



- **Offline Download & Installation**: Operate without a constant network connection.

- **Python Version Selection**: Set the desired Python version for package recommendations.

- **Virtual Environment Management**: Create and populate a development environment with your specified packages.

- **Cross-Platform**: Automatically detects Windows vs. Linux and adjusts the execution method.



## Requirements



- Python 3.9 or newer (the tool supports library versions for Python 3.9, 3.10, 3.11, 3.12, and 3.13).

- Pip (usually included with Python).

- On Windows: PowerShell is required for running applications in the virtual environment.

- On Linux: A terminal emulator such as **gnome-terminal** is assumed for launching the script in a new window.



## Usage



1. **Download the Script Files:**

   - Save `installer.py` and `packages.py` to your working directory.

   - Refer to this `README.md` for usage instructions.



2. **Run the Installer:**

   ```bash

   Python installer.py

   ```



3. **Select Options from the Menu:**

    - **Option 0:** Download packages offline into the `libay` folder.

    - **Option 1:** List the files downloaded in `libay`.

    - **Option 2:** Install the downloaded packages offline.

    - **Option 3:** Create a virtual environment (`venv`) and install packages into it.

    - **Option 4:** Run a Python script within the virtual environment (opens a new terminal window).

    - **Option 5:** Set your desired Python version (choose between 3.9, 3.10, 3.11, 3.12, or 3.13).

    - **Option q:** Quit the application.



4. **Follow the Prompts:**

    - The tool displays informative messages as it processes your selections.

    - When setting the Python version or providing a file path, follow the on-screen instructions.



## Notes



- **uvloop Package**: This package is intended only for Linux. In Windows environments, it will be skipped automatically.

- **Terminal Emulation on Linux**: This script currently uses **gnome-terminal** to launch a new terminal window. Adjust the `run_app_in_venv()` function if you use a different terminal emulator.



## Contributing



Feel free to submit issues or pull requests for further improvements.



## License



Distributed under the MIT License. See `LICENSE` for further details.
