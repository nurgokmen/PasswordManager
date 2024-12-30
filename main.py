from cryptography.fernet import Fernet
#symmetric cryptography method

class PasswordManager:

    def __init__(self):
        self.key = None
        self.psw_file = None
        self.psw_dict = {}

    def createKey(self, path):
        self.key = Fernet.generate_key()
        #print(self.key)
        with open(path, 'wb') as f: #writing mode bytes
            #to store the keys in another file
            f.write(self.key)

    def loadKey(self, path):
        with open(path, 'rb') as f: #reading bytes mode
            self.key = f.read()

    def createPswFile(self, path, initials=None):#initials helps to reach outside the dict
        self.psw_file = path

        if initials is not None:
            for key, value in initials.items():
                self.addPsw(key, value)

    def loadPswFile(self, path):
        self.psw_file = path

        """with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.psw_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()"""
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()  # Remove any extra whitespace or newline characters
                if ":" not in line:
                    print(f"Skipping invalid line: {line}")
                    continue
                try:
                    site, encrypted = line.split(":", 1)  # Split into two parts only
                    decrypted_password = Fernet(self.key).decrypt(encrypted.encode()).decode()
                    self.psw_dict[site] = decrypted_password
                except Exception as e:
                    print(f"Error decrypting password for {site}: {e}")


    def addPsw(self, site, password):
        self.psw_dict[site] = password

        if self.psw_file is not None:
            with open(self.psw_file, 'a+') as f: #a to avoid overwriting
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")


    def getPsw(self, site):
        return self.psw_dict[site]



def main():
    password = {
        "email" : "123456",
        "facebook":"hellopswd",
        "youtube":"favpswdisthis"
    }

    pm = PasswordManager()

    print("""What do you want to do:
    (1) Create a new key
    (2) Load an existing key
    (3) Create new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit 
    """)

    done = False
    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.createKey(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.loadKey(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.createPswFile(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.loadPswFile(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.addPsw(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.getPsw(site)}")
        elif choice == "q":
            done = True
            print("Goodbye")
        else:
            print("Invalid choice for Password Manager!")


if __name__ == "__main__":
    main()