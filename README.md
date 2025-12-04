
# Secret Sharing System

This project is a Python application that allows you to split a secret into multiple shares and to combine those shares to recover the secret. It uses Shamir's Secret Sharing scheme.

The application provides both a Command-Line Interface (CLI) and a Graphical User Interface (GUI).

## Installation

1.  Clone this repository or download the source code.
2.  Open a terminal in the project's root directory.
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can interact with the application through the GUI or the CLI.

### GUI Mode

To launch the graphical interface, run the following command in your terminal:

```bash
python main.py gui
```

The application will open in a new window. The GUI has been redesigned with a clean, modern, and responsive layout, ensuring a user-friendly experience. The interface is organized into two primary sections: "Split Secret" and "Combine Shares." All UI elements, including input fields and text areas, are designed to be clearly visible and will automatically resize with the window, preventing any visual clipping or overlap.

### CLI Mode

The CLI is the default mode. You can use it for splitting and combining secrets directly from your terminal.

#### Splitting a Secret

Use the `split` command to break a secret into a specified number of shares.

**Usage:**

```bash
python main.py split "<your-secret>" -n <num_shares> -k <threshold>
```

-   `<your-secret>`: The secret string you want to split.
-   `<num_shares>`: The total number of shares to generate.
-   `<threshold>`: The minimum number of shares required to reconstruct the secret.

**Example:**

```bash
python main.py split "this is a very secret message" -n 5 -k 3
```

This will output 5 shares.

#### Combining Shares

Use the `combine` command to recover a secret from its shares.

**Usage:**

```bash
python main.py combine <share1> <share2> ...
```

-   `<share1> <share2> ...`: The shares you want to combine. You need to provide at least the threshold number of shares.

**Example:**

```bash
python main.py combine "2-..." "4-..." "5-..."
```

This will output the original secret if the shares are correct and the threshold is met.
