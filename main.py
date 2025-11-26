
import sys
from cli.main import main as cli_main
from gui.main import main as gui_main

def start():
    """
    Determines whether to launch the GUI or the CLI based on command-line arguments.
    """
    # To prevent issues with how PyInstaller packages scripts, we check for the 'gui' argument.
    # If 'gui' is passed as the first argument, launch the GUI.
    # Otherwise, default to the CLI.
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'gui':
        # Remove 'gui' from argv so that the GUI application doesn't try to process it
        sys.argv.pop(1)
        print("Launching GUI...")
        gui_main()
    else:
        # If 'cli' is the first argument, remove it to avoid confusing the CLI parser.
        if len(sys.argv) > 1 and sys.argv[1].lower() == 'cli':
            sys.argv.pop(1)
        print("Launching CLI... (use 'gui' argument to launch the graphical interface)")
        cli_main()

if __name__ == "__main__":
    start()
