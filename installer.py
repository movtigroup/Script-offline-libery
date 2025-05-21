#!/usr/bin/env python3
import os
import sys
import subprocess

# Define packages with recommended versions based on the selected Python version.
# Note: For Windows, the "uvloop" package will be skipped since it is only required on Linux.
PACKAGES = {
    "aiofiles": {"3.9": "0.7.0", "3.10": "0.8.0", "3.11": "latest", "3.12": "latest"},
    "aiohttp": {"3.9": "3.8.1", "3.10": "3.8.3", "3.11": "latest", "3.12": "latest"},
    "aiomysql": {"3.9": "0.0.21", "3.10": "0.1.0", "3.11": "latest", "3.12": "latest"},
    "asyncmy": {"3.9": "0.2.7", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "cachetools": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "cython": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "fastapi": {"3.9": "0.68.0", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "gunicorn": {"3.9": "20.0.4", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "httptools": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "lxml": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "mysql-connector-python": {"3.9": "8.0.25", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "pydantic": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "python-multipart": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "pytz": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "schedule": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "slowapi": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "sqlalchemy": {"3.9": "1.3.23", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "uvicorn": {"3.9": "0.15.0", "3.10": "0.16.0", "3.11": "latest", "3.12": "latest"},
    "uvloop": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "httpx": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "numpy": {"3.9": "1.19.5", "3.10": "1.21.0", "3.11": "latest", "3.12": "latest"},
    "pandas": {"3.9": "1.1.5", "3.10": "1.3.0", "3.11": "latest", "3.12": "latest"},
    "matplotlib": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "tqdm": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
    "asyncio": {"3.9": "latest", "3.10": "latest", "3.11": "latest", "3.12": "latest"},
}

# Directory for offline package downloads and virtual environment folder.
LIB_DIR = "libay"
VENV_DIR = "venv"

# Global variable for the selected Python version (default is the system's version).
SELECTED_PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}"

def get_recommended_version(package):
    """Return the recommended version for a package based on the selected Python version."""
    return PACKAGES.get(package, {}).get(SELECTED_PYTHON_VERSION, "latest")

def set_python_version():
    """Allow the user to set the desired Python version (3.9, 3.10, 3.11, or 3.12)."""
    global SELECTED_PYTHON_VERSION
    print("Please enter your desired Python version (e.g., 3.9, 3.10, 3.11, or 3.12):")
    version_input = input("Python version: ").strip()
    if version_input not in ["3.9", "3.10", "3.11", "3.12"]:
        print("Invalid version entered. Please choose from 3.9, 3.10, 3.11, or 3.12.")
    else:
        SELECTED_PYTHON_VERSION = version_input
        print(f"Selected Python version: {SELECTED_PYTHON_VERSION}")
        print(f"Checking and downloading the best libraries for Python {SELECTED_PYTHON_VERSION}...\n")

def offline_download_packages():
    """Download packages offline according to the selected Python version."""
    print(f"Selected Python version: {SELECTED_PYTHON_VERSION}")
    print("Checking and downloading the best suitable libraries offline...")
    if not os.path.exists(LIB_DIR):
        os.makedirs(LIB_DIR)
        print(f"Folder '{LIB_DIR}' created.")
    else:
        print(f"Folder '{LIB_DIR}' exists.")

    for package in PACKAGES.keys():
        # Skip the uvloop package on Windows.
        if package.lower() == "uvloop" and sys.platform == "win32":
            print("On Windows: 'uvloop' is not required. Skipping download.")
            continue
        recommended_version = get_recommended_version(package)
        package_spec = f"{package}=={recommended_version}" if recommended_version != "latest" else package
        if not any(f.lower().startswith(package.lower() + "-") for f in os.listdir(LIB_DIR)):
            print(f"Downloading {package_spec}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "download", package_spec, "--dest", LIB_DIR])
            except subprocess.CalledProcessError as e:
                print(f"Error downloading {package_spec}: {e}")
        else:
            print(f"{package_spec} has already been downloaded.")
    print("Offline package download process completed.\n")

def check_downloaded_packages():
    """List the downloaded package files in the LIB_DIR folder."""
    if not os.path.exists(LIB_DIR):
        print(f"Folder '{LIB_DIR}' does not exist. Please run the download option first.\n")
        return
    files = os.listdir(LIB_DIR)
    if files:
        print(f"Downloaded files in '{LIB_DIR}':")
        for f in files:
            print(" - " + f)
    else:
        print(f"No files found in '{LIB_DIR}'.")
    print()

def offline_install_packages():
    """Install the packages offline from the LIB_DIR folder."""
    if not os.path.exists(LIB_DIR):
        print(f"Folder '{LIB_DIR}' does not exist. Please run the download option first.\n")
        return
    print(f"Selected Python version: {SELECTED_PYTHON_VERSION}")
    print("Installing packages offline...")
    for package in PACKAGES.keys():
        if package.lower() == "uvloop" and sys.platform == "win32":
            print("On Windows: 'uvloop' is not required. Skipping installation.")
            continue
        recommended_version = get_recommended_version(package)
        package_spec = f"{package}=={recommended_version}" if recommended_version != "latest" else package
        print(f"Installing {package_spec}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-index", "--find-links", LIB_DIR, package_spec])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_spec}: {e}")
    print("Offline installation of packages completed.\n")

def create_virtual_environment():
    """Create a virtual environment and install packages into it according to the selected Python version."""
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment '{VENV_DIR}'...")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
            print(f"Virtual environment '{VENV_DIR}' created.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            return
    else:
        print(f"Virtual environment '{VENV_DIR}' already exists.")
    
    # Determine the pip path in the virtual environment:
    pip_path = os.path.join(VENV_DIR, "Scripts", "pip") if sys.platform == "win32" else os.path.join(VENV_DIR, "bin", "pip")
    print("Installing packages into the virtual environment...")
    for package in PACKAGES.keys():
        if package.lower() == "uvloop" and sys.platform == "win32":
            print("On Windows: 'uvloop' is not required. Skipping installation in the virtual environment.")
            continue
        recommended_version = get_recommended_version(package)
        package_spec = f"{package}=={recommended_version}" if recommended_version != "latest" else package
        print(f"Installing {package_spec} in virtual environment...")
        try:
            subprocess.check_call([pip_path, "install", "--no-index", "--find-links", LIB_DIR, package_spec])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_spec} in virtual environment: {e}")
    print("Virtual environment setup completed.\n")

def run_app_in_venv():
    """
    Run a Python script in the virtual environment using PowerShell (Windows only):
      1. Change directory to the launcher's directory.
      2. Activate the virtual environment.
      3. Change directory to the application directory and run the Python file.
    """
    app_path = input("Please enter the full path to the Python file to run:\n").strip()
    if not os.path.exists(app_path):
        print("The entered path does not exist.\n")
        return
    app_path = os.path.abspath(app_path)
    app_dir = os.path.dirname(app_path)
    app_file = os.path.basename(app_path)
    launcher_dir = os.path.dirname(os.path.abspath(__file__))
    activation_script = os.path.join(launcher_dir, VENV_DIR, "Scripts", "Activate.ps1")
    
    if not os.path.exists(activation_script):
        print(f"Activation script not found at {activation_script}.\n")
        return
    
    cmd = (
        f"cd '{launcher_dir}'; "
        f"& '{activation_script}'; "
        f"cd ../; "
        f"cd '{app_dir}'; "
        f"python '{app_file}'"
    )
    
    try:
        subprocess.Popen(["powershell", "-NoExit", "-Command", cmd], creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("A new PowerShell window has been opened to run the application.\n")
    except Exception as e:
        print("Error running the application in virtual environment:", e)

def print_menu():
    print("""
=== Offline Python Package Installer & Virtual Environment Manager ===

Please choose an option:
0. Download packages offline to 'libay'
1. Check downloaded packages in 'libay'
2. Install packages offline from 'libay'
3. Create virtual environment ('venv') and install packages into it
4. Run a Python script in the virtual environment (PowerShell)
5. Set desired Python version (3.9, 3.10, 3.11, 3.12)
q. Quit
""")

def main():
    while True:
        print_menu()
        choice = input("Your choice: ").strip()
        if choice == "0":
            offline_download_packages()
        elif choice == "1":
            check_downloaded_packages()
        elif choice == "2":
            offline_install_packages()
        elif choice == "3":
            create_virtual_environment()
        elif choice == "4":
            run_app_in_venv()
        elif choice == "5":
            set_python_version()
        elif choice.lower() == "q":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
