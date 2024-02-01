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



#### How to use your library (where applicable)

- N/A

#### Tests

- N/A
