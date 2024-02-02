from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import re
import shutil

# Instantiate a console object
console = Console()

def create_directory(directory_name):
    """
    Creates a directory at the specified path if it doesn't already exist.

    Parameters:
    - directory_name: The path where the directory will be created.
    """
    # Create a source directory
    os.makedirs(directory_name, exist_ok=True)
    
def move_user_documents(user_directory, temp_directory):
    """
    Moves all files and directories from a user's folder to a specified temporary folder.

    Parameters:
    - user_directory: The source directory from which files and folders are to be moved.
    - temp_directory: The target directory where files and folders will be moved to.
    """
        
    try:
        # Ensure the temporary directory exists
        os.makedirs(temp_directory, exist_ok=True)
        
        # Iterate over all items in the user's directory
        for item in os.scandir(user_directory):
            source_path = item.path
            target_path = os.path.join(temp_directory, item.name)
            
            # Move the item (file or directory)
            shutil.move(source_path, target_path)
            console.print(f"[bold green]{item.name}[/bold green] has been moved to [bold yellow]{temp_directory} and {user_directory} has been removed.[/bold yellow]")
            shutil.rmtree(user_directory)  # Remove the user_directory after moving its contents
                
    except FileNotFoundError as e:
        console.print("[bold red]User directory not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        
def sort_documents(folder_path):
    """
    Sorts documents into 'logs' and 'mail' folders based on their file type within the given directory.

    Parameters:
    - folder_path: The directory whose documents are to be sorted.
    """
    # Define the target folders for each file type
    log_folder = os.path.join(folder_path, 'logs')
    mail_folder = os.path.join(folder_path, 'mail')

    # Ensure the target folders exist
    os.makedirs(log_folder, exist_ok=True)
    os.makedirs(mail_folder, exist_ok=True)

    # Compile regex patterns for matching file types
    log_pattern = re.compile(r'\.log(\.txt)?$', re.IGNORECASE)  # Matches .log and .log.txt
    mail_pattern = re.compile(r'\.(mail|email)$', re.IGNORECASE)  # Matches .mail and .email

    # Go through the given folder
    for item in os.scandir(folder_path):
        if item.is_file():  # Ensure we're dealing with a file
            file_name = item.name
            
            # Determine the target folder based on the file type
            if log_pattern.search(file_name):
                target_folder = log_folder
            elif mail_pattern.search(file_name):
                target_folder = mail_folder
            else:
                continue  # Skip files that don't match the criteria

            # Construct the target path and move the file
            target_path = os.path.join(target_folder, file_name)
            shutil.move(item.path, target_path)
            console.print(f"[bold green]{file_name}[/bold green] has been moved to [bold yellow]{target_folder}[/bold yellow]")

def parse_logs(source_directory):
    """
    Parses log files in the given directory for errors and warnings, creating separate files for each in a 'warnings_errors' directory.

    Parameters:
    - source_directory: The directory containing log files to be parsed.
    """
    try:
        # Calculate the path for the 'warnings_errors' directory alongside 'logs'
        warnings_errors_dir = os.path.join(source_directory, 'warnings_errors')

        # Ensure the 'warnings_errors' directory exists
        os.makedirs(warnings_errors_dir, exist_ok=True)
        
        errors_log_path = os.path.join(warnings_errors_dir, 'errors.log')
        warnings_log_path = os.path.join(warnings_errors_dir, 'warnings.log')

        # Initialize or clear the files
        with open(errors_log_path, 'w') as _, open(warnings_log_path, 'w') as _:
            pass  # Just to create/clear the file

        # Iterate through each log file in the source directory
        for log_file_name in os.listdir(source_directory):
            log_file_path = os.path.join(source_directory, log_file_name)
            if log_file_name.endswith('.log') or log_file_name.endswith('.txt'):  # Adjust based on your log files' extensions
                with open(log_file_path) as log_file:
                    for line in log_file:
                        if 'ERROR' in line:
                            with open(errors_log_path, 'a') as errors_file:
                                errors_file.write(line)
                        elif 'WARNING' in line:
                            with open(warnings_log_path, 'a') as warnings_file:
                                warnings_file.write(line)

    except FileNotFoundError:
        console.print("[bold red]The specified directory does not exist.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
        
def search_and_count_files(directory, pattern):
    """
    Searches for and counts the number of files matching a given regex pattern in the specified directory.

    Parameters:
    - directory: The directory to search within.
    - pattern: The regex pattern to match file names against.

    Returns:
    - The count of files matching the pattern.
    """
    try:
        files = os.listdir(directory)
        matches = [file for file in files if re.search(pattern, file)]
        
        # Count the matches
        count = len(matches)
        
        # Display the results in a table, with the count included in the title
        table = Table(title=f"Files in [bold green]{directory}[/bold green] matching [bold blue]{pattern}[/bold blue]: [bold yellow]{count} matches found[/bold yellow]")
        table.add_column("Matching File Name", style="dim")
        
        for match in matches:
            table.add_row(match)
        
        console.print(table)
        
        return count
        
    except FileNotFoundError:
        console.print("[bold red]Directory not found.[/bold red]")
        return 0  # Return 0 if the directory is not found
        
        
def main():
    """Main function to run the CLI app."""
    base_directory = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    
    while True:
        console.print("\n1. Create directory\n2. Delete user\n3. Sort documents in given directory\n4. Parse log files for errors and warnings\n5. Count files of specific type in a given directory\n6. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4', '5', '6'], default='6')
        
        if choice == '1':
            # Ask for the relative or absolute path where the directory should be created
            directory_path = Prompt.ask("Enter the path of the directory you want to create (relative to the current working directory or absolute)")
            # Resolve the path to an absolute path
            absolute_directory_path = os.path.abspath(directory_path)
            create_directory(absolute_directory_path)
            console.print(f"Directory created at: {absolute_directory_path}")
        
        elif choice == '2':
            user_name = Prompt.ask("Enter the user to delete (e.g., user1)")
            # Ask for the relative or absolute base directory where user directories are located
            relative_base_dir = Prompt.ask("Enter the base directory where user directories are located (relative to the script or absolute)")
            base_dir = os.path.abspath(os.path.join(base_directory, relative_base_dir))
            source_directory = os.path.join(base_dir, user_name)
            temp_directory_path = os.path.join(base_dir, f"{user_name}_temp")
            create_directory(temp_directory_path)
            move_user_documents(source_directory, temp_directory_path)
                
        elif choice == '3':
            # Ask for the relative or absolute path of the directory you want to sort
            relative_directory_path = Prompt.ask("Enter the path of the directory you want to sort (relative to the script or absolute)")
            directory_path = os.path.abspath(os.path.join(base_directory, relative_directory_path))
            
            sort_documents(directory_path)

            
        elif choice == '4':
            # Ask for the path directly to the "logs" directory
            relative_logs_path = Prompt.ask("Enter the relative or absolute path of the logs directory you want to parse")
            logs_directory_path = os.path.abspath(relative_logs_path)

            # Now, directly call parse_logs with the user-provided path
            parse_logs(logs_directory_path)
            
        elif choice == '5':
            # Ask for the relative or absolute path of the directory you want to count
            relative_directory_path = Prompt.ask("Enter the path of the directory you want to count file types (relative to the script or absolute)")
            directory_path = os.path.abspath(os.path.join(base_directory, relative_directory_path))
            pattern = Prompt.ask("Enter the regex pattern to search for")
            search_and_count_files(directory_path, pattern)
    
        else:
            break
    
if __name__ == "__main__":
    main()