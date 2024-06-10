# Password Compiler

**Author:** alfanowski

## Description

The "Password Compiler" program is a Python application that generates possible passwords based on a person's name, surname, and date of birth.

## How it Works

The program prompts the user to input their name, surname, and date of birth. It utilizes this information to create a password by intelligently combining different components, and then adds numbers and special characters to enhance the password's security.

## Dependencies Installation
Before running the program, make sure you have installed the `tqdm` library. You can easily install it via pip by executing the following command:

```bash
pip install tqdm
```

**Note**: Even if the `tqdm` library is not installed, the program will attempt to install it automatically on first launch; automatic installation will be performed to ensure the proper functioning of the program.

## Installation on Linux

1. **Clone the repository:**

    ```bash
    git clone https://github.com/alfanoandrea/password-compiler.git
    cd password-compiler
    ```

2. **Install Python:**

    Ensure you have Python 3.x installed on your Linux system. If not, you can install it using your package manager.

    ```bash
    sudo apt update
    sudo apt install python3
    ```

3. **Run the program:**

    ```bash
    python3 compiler.py
    ```

   Follow the on-screen instructions to generate passwords based on your name, surname, and date of birth.
