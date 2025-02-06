
# Codewar API

## Overview

**Codewar API** is a command-line tool designed to interact with the Codewars API. Its main goal is to help users fetch, update, and manage their Codewars kata (challenge) solutions. The tool provides several commands to:

- Set your Codewars username.
- Define your working directory.
- Fetch the list of completed kata by the user.
- Retrieve detailed information about each kata.
- Automatically create and update a structured folder system for kata files.
- Synchronize the workspace with a Git repository.

## Features

- **User Configuration:**  
  Configure your Codewars username and workspace directory via CLI commands (`set_user` and `set_dir`).

- **Fetch Kata:**  
  Retrieve a list of completed kata IDs using the Codewars API and save them to a JSON file.

- **Update Kata:**  
  For each fetched kata, obtain detailed information (including name, difficulty, URL, and description) and generate a Python file with a header docstring containing this metadata.

- **Workspace Setup:**  
  Create a main folder structure that organizes kata files by their difficulty level (e.g., folders named "1 kyu" through "7 kyu").

- **Git Integration:**  
  Automate Git operations such as repository initialization, staging changes, committing, pulling updates, and pushing changes to a remote repository.

## Technologies and Libraries

- **Python 3.x:** The project is written in Python.
- **PyYAML:** Used for reading and writing YAML configuration files (see `settings.yaml`).
- **Requests:** Utilized for making HTTP requests to the Codewars API.
- **Custom Modules:**  
  - **CLI Command Handling:** Managed by a custom CLI class that parses and executes commands.
  - **Configuration Management:** Uses `ConfigManager` to load and save settings.
  - **Folder Management:** Automatically creates and organizes folders and files based on kata details.
  - **Git Tools:** Executes Git commands via subprocess calls.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/NelexstarMain/Codewar_api.git
   cd Codewar_api
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The project uses a YAML configuration file (`settings.yaml`) with the following settings:

- `commit_prefix`: A prefix for Git commit messages (default: `'Codewars: Kata Solution'`).
- `default_branch`: The default Git branch (default: `main`).
- `root_directory`: The base directory for the workspace (set via CLI command `set_dir` if currently null).
- `username`: Your Codewars username (set via CLI command `set_user` if currently null).
- `workspace_folder`: The folder within the root directory where kata files will be stored (default: `codewars_katas`).

## Usage

Run the main script to execute CLI commands:

```bash
python app.py <command> [arguments]
```

### Available Commands

- **set_user `<username>`**  
  Sets your Codewars username in the configuration.

- **set_dir `<path>`**  
  Sets the main working directory for the workspace.

- **fetch_katas**  
  Fetches all completed kata IDs for the configured user and saves them in a JSON file.

- **setup_env**  
  Creates the folder structure for the kata workspace, generating subfolders based on kata difficulty (e.g., "1 kyu", "2 kyu", …, "7 kyu").

- **update_katas**  
  Retrieves detailed information for each kata, and organizes them into the workspace by generating Python files that include metadata such as the kata’s name, difficulty, URL, and description.

- **git_sync**  
  Performs Git operations including initializing the repository (if not already initialized), adding changes, committing with a predefined prefix, and synchronizing (pull/push) with the remote repository.

- **help**  
  Displays a list of available commands along with descriptions and usage examples.

## How It Works

- **Data Retrieval:**  
  The tool uses the [Codewars API](https://www.codewars.com/api) to get data about completed challenges and individual kata details. The `UserKataInfo` and `KataInfo` classes in the `core/kata_data/kata_fetcher.py` module handle these operations.

- **Data Storage:**  
  Fetched data is stored in JSON format using the helper class in `core/kata_data/json_storage.py`.

- **Folder Structure:**  
  The `MainFolder` class in `core/version_control/folder_manager.py` is responsible for creating a directory structure organized by kata difficulty. For each kata, it creates a Python file with a docstring header that documents the kata’s metadata.

- **Git Operations:**  
  The module `core/git_tools/git_manager.py` wraps basic Git commands (init, add, commit, pull, push) to integrate version control into the workflow.

- **CLI Interface:**  
  The custom CLI is defined in `command_interface/command.py`. It handles the registration and execution of commands based on command-line arguments.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request. Make sure to follow the project’s coding guidelines.