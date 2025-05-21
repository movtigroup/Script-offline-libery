# Offline Python Package Installer & Virtual Environment Manager



This tool is a comprehensive offline package downloader and installer for Python. It allows you to:

- **Download packages offline:** Save the package files into a designated folder (`libay`).

- **Install packages offline:** Install packages from the offline folder without requiring an Internet connection.

- **Create a virtual environment:** Set up a Python virtual environment (`venv`) and install packages into it.

- **Run a Python script within the virtual environment:** (Windows only via PowerShell)

- **Select a desired Python version:** Choose from 3.9, 3.10, 3.11, or 3.12 to determine which package versions to install.

- **Platform-specific handling:** For Windows, the `uvloop` package is skipped (since it is intended for Linux).



## Features



- **Offline Download & Installation:** Avoid dependency on an active network connection.

- **Python Version Selection:** Choose which Python version’s library recommendations to use.

- **Virtual Environment Management:** Create and populate a virtual environment with your packages.

- **Cross-Platform:** Automatically detects Windows vs. Linux and adjusts package installation (e.g., skips `uvloop` for Windows).



## Requirements



- Python 3.9 or newer (the tool supports library versions for Python 3.9, 3.10, 3.11, and 3.12).

- Pip (usually included with Python).

- On Windows: PowerShell is required for running applications in the virtual environment.



## Usage



1. **Download the Script:**

   - Save the provided `installer.py` file to your working directory.



2. **Run the Script:**

   ```bash

   Python installer.py

   ```



3. **Select Options from the Menu:**

   - **Option 0:** Download packages offline. All package files will be saved into the `libay` folder.

   - **Option 1:** Check the downloaded content in the `libay` folder.

   - **Option 2:** Install the downloaded packages offline into your default Python environment.

   - **Option 3:** Create a virtual environment (`venv`) and install the packages into it.

   - **Option 4:** Run a Python script within the virtual environment (this opens a new PowerShell window on Windows).

   - **Option 5:** Set your desired Python version to use (choose between 3.9, 3.10, 3.11, or 3.12).

   - **Option q:** Quit the application.



4. **Follow the Prompts:**

   - The tool will display informative messages as it checks, downloads, and installs packages.  

   - When selecting the Python version or entering the path for a script, simply follow the on-screen instructions.



## Notes



- **uvloop Package:** This package is only applicable on Linux. On Windows, it will be automatically skipped when downloading and installing.

- **Offline Operation:** Ensure you first run the download (Option 0) before trying to install offline packages (Options 2 or 3).



## Contributing



Feel free to suggest improvements or contribute enhancements. Open an issue or submit a pull request on the project repository.



## License



Distributed under the MIT License. See `LICENSE` for more information.
