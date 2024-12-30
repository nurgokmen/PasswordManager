
# Password Manager

This project is a simple and secure password manager implemented in Python using the Fernet encryption from the cryptography library. The program enables users to store, retrieve, and manage passwords for different sites in an encrypted format.

# Features

- Create a new encryption key to secure your passwords.

- Load an existing encryption key to decrypt stored passwords.

- Create a new password file or load an existing one.

- Add passwords for various sites.

- Retrieve passwords for saved sites.

# Requirements

Python 3.8 or above.

**cryptography** library (install using **pip install cryptography**).

# Usage

# 1. Clone the Repository
```
# Clone the repository from GitHub
$ git clone https://github.com/yourusername/password-manager.git
$ cd password-manager
```
# 2. Install Dependencies
```
# Install the required library
$ pip install cryptography
```
# 3. Run the Application
```
# Run the main Python script
$ python main.py
```
# 4. Program Menu

The program provides the following menu options:
```
What do you want to do:
(1) Create a new key
(2) Load an existing key
(3) Create new password file
(4) Load existing password file
(5) Add a new password
(6) Get a password
(q) Quit
```
# File Structure

**main.py**: The main script containing the password manager logic.

**requirements.txt**: List of required Python libraries.

**.gitignore**: Excludes sensitive or unnecessary files from being pushed to the repository.

# Example Workflow

**Create a new key**:
```
Enter your choice: 1
Enter path: mykey.key
```
**Load an existing key**:
```
Enter your choice: 2
Enter path: mykey.key
```
**Create or load a password file**:
```
Enter your choice: 3
Enter path: mypasswords.pass
```
**Add a password**:
```
Enter your choice: 5
Enter the site: facebook
Enter the password: myfbpassword
```
**Retrieve a password**:
```
Enter your choice: 6
What site do you want: facebook
Password for facebook is myfbpassword
```
License

This project is licensed under the MIT License. See the LICENSE file for more information.

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

