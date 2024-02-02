from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import re
import shutil

# Instantiate a console object
console = Console()

def create_directory(directory_name):
    """ """
    # Create a source directory
    os.makedirs(directory_name, exist_ok=True)
    
def move_user_documents(user_directory, temp_directory):
    """Move all documents and directories from a deleted user's folder to a temporary folder."""
    try:
        # Ensure the temporary directory exists
        os.makedirs(temp_directory, exist_ok=True)
        
        # Iterate over all items in the user's directory
        for item in os.scandir(user_directory):
            source_path = item.path
            target_path = os.path.join(temp_directory, item.name)
            
            # Move the item (file or directory)
            shutil.move(source_path, target_path)
            console.print(f"[bold green]{item.name}[/bold green] has been moved to [bold yellow]{temp_directory}[/bold yellow]")
                
    except FileNotFoundError as e:
        console.print("[bold red]User directory not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    
def move_all_files(source_directory, target_directory):
    """Move all files from the source directory to the target directory."""
    try:
        # Iterate over all entries in the source directory
        for entry in os.scandir(source_directory):
            if entry.is_file():  # Check if the entry is a file
                # Construct full paths for source and destination
                source_path = os.path.join(source_directory, entry.name)
                target_path = os.path.join(target_directory, entry.name)
                
                # Move the file
                shutil.move(source_path, target_path)
                console.print(f"[bold green]{entry.name}[/bold green] has been moved from [bold blue]{source_directory}[/bold blue] to [bold yellow]{target_directory}[/bold yellow]")
    except FileNotFoundError as e:
        console.print("[bold red]Directory not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

        
def main():
    """Main function to run the CLI app."""
    while True:
        console.print("\n1. Create directory\n2. Delete user\n3. Sort documents\n4. Parse a log file for errors and warnings\n5. Count files\n6. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4', '5', '6'], default='6')
        
        if choice == '1':
            directory_name = Prompt.ask("Enter the name of the directory you want to create")
            create_directory(directory_name)
        elif choice == '2':
            directory_name = Prompt.ask("Enter the user to delete (user1 or user2)")
            if directory_name == 'user1':
                source_directory = 'user1'
                move_user_documents(source_directory)
            elif directory_name == 'user2':
                source_directory = 'user2'
                move_user_documents(source_directory)
            else:
                console.print(f"[bold red]Please choose valid user[/bold red]")
                directory_name = Prompt.ask("Enter the user to delete (user1 or user2)")
                
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        else:
            break
    
if __name__ == "__main__":
    main()