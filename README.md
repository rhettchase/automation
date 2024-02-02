# LAB - Class 19

## Project: Automation

## Project Description

Console application that includes the below features:

- Automate the creation of a folder
- Handle a deleted user
- Sorts documents into appropriate folder
  - Move log files into a `logs` folder. If a `logs` folder doesn’t exist, the app creates one
  - Move email files into a `mail` folder. If a `mail` folder doesn’t exist, the app creates one
- Parses a log file for errors and warnings and creates two separate log files in a target directory:
  - `errors.log`: Contains all error messages
  - `warnings.log`: Contains all warning messages
- Menu-driven application
  - Gives the user a list of automation tasks (1-4) and lets them choose one to execute

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT

### Setup

- `pip install -r requirements.txt`

Alternatively:

- `pip install rich`
- `pip install pytest`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

- Initialize app in console: `python3 app.py`
- Select from menu of from `1-6` on what you would like to execute

1. Create directory: enter the path of the directory you want to create the new directory (e.g., `user-docs/new_directory_name`)

2. Delete user
  - enter the user to delete (e.g., `user1`)
  - enter the directory where user directories are located (`user-docs`)

3. Sort documents in given directory:
  - enter the path of the directory you want sorted (e.g., `user-docs/user1`)

4. Parse log files for errors and warnings
  - enter the path of the `logs` directory where the file(s) to be parsed reside

5. Count files of specific type in a given directory
  - enter the path of the directory you want to count files
  - enter the regular expression pattern you'd like to search for (e.g., `txt`)

6. Type `6` + `Enter` to Exit

#### How to use your library (where applicable)

- N/A

#### Tests

- N/A
