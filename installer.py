#!/usr/bin/env python3
import os
import sys
import subprocess
from packages import PACKAGES  # Import the packages dictionary from packages.py

# Directories for offline package downloads and virtual environment.
LIB_DIR = "libay"
VENV_DIR = "venv"

# Global variable for the selected Python version (default is the system’s version).
SELECTED_PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}"

def get_recommended_version(package):
    """Return the recommended version for a package based on the selected Python version."""
    return PACKAGES.get(package, {}).get(SELECTED_PYTHON_VERSION, "latest")

def set_python_version():
    """Allow the user to set the desired Python version (3.9, 3.10, 3.11, 3.12, or 3.13)."""
    global SELECTED_PYTHON_VERSION
    print("Please enter your desired Python version (e.g., 3.9, 3.10, 3.11, 3.12, or 3.13):")
    version_input = input("Python version: ").strip()
    if version_input not in ["3.9", "3.10", "3.11", "3.12", "3.13"]:
        print("Invalid version entered. Please choose from 3.9, 3.10, 3.11, 3.12, or 3.13.")
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
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "download", package_spec, "--dest", LIB_DIR]
                )
            except subprocess.CalledProcessError as e:
                print(f"Error downloading {package_spec}: {e}")
        else:
            print(f"{package_spec} has already been downloaded.")
    print("Offline package download process completed.\n")

def check_downloaded_packages():
    """List the downloaded package files in the offline library folder."""
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
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--no-index", "--find-links", LIB_DIR, package_spec]
            )
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_spec}: {e}")
    print("Offline installation of packages completed.\n")

def create_virtual_environment():
    """Create a virtual environment and install packages into it based on the selected Python version."""
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
    
    # Determine the pip path in the virtual environment.
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
            subprocess.check_call(
                [pip_path, "install", "--no-index", "--find-links", LIB_DIR, package_spec]
            )
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_spec} in virtual environment: {e}")
    print("Virtual environment setup completed.\n")

def run_app_in_venv():
    """
    Run a Python script in the virtual environment in a new terminal window.
    
    For Windows, this uses PowerShell. For Linux, it attempts to open a new gnome-terminal.
    """
    app_path = input("Please enter the full path to the Python file to run:\n").strip()
    if not os.path.exists(app_path):
        print("The entered path does not exist.\n")
        return
    app_path = os.path.abspath(app_path)
    app_dir = os.path.dirname(app_path)
    app_file = os.path.basename(app_path)
    launcher_dir = os.path.dirname(os.path.abspath(__file__))
    
    if sys.platform == "win32":
        # Windows: use PowerShell.
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
            subprocess.Popen(
                ["powershell", "-NoExit", "-Command", cmd],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            print("A new PowerShell window has been opened to run the application.\n")
        except Exception as e:
            print("Error running the application in virtual environment:", e)
    else:
        # Linux: attempt to open a new terminal (using gnome-terminal as an example).
        venv_activate = os.path.join(launcher_dir, VENV_DIR, "bin", "activate")
        # Build a command that activates the venv, changes directory, runs the app, and holds the terminal open.
        linux_cmd = f"bash -c 'source \"{venv_activate}\"; cd \"{app_dir}\"; python \"{app_file}\"; exec bash'"
        try:
            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", linux_cmd])
            print("A new terminal window has been opened to run the application.\n")
        except Exception as e:
            print("Error launching the application in a new terminal window on Linux:", e)

def print_menu():
    print("""
=== Offline Python Package Installer & Virtual Environment Manager ===

Please choose an option:
0. Download packages offline to 'libay'
1. Check downloaded packages in 'libay'
2. Install packages offline from 'libay'
3. Create virtual environment ('venv') and install packages into it
4. Run a Python script in the virtual environment (New terminal window)
5. Set desired Python version (3.9, 3.10, 3.11, 3.12, or 3.13)
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
