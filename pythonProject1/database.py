class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, firstname, lastname = line.strip().split("|")
            self.users[email] = (password, firstname, lastname)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1
# negative 1 means the key was not found which is the email#

    def add_user(self, email, password, firstname, lastname):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), firstname.strip(), lastname.strip())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + "|" + self.users[user][0] + "|" + self.users[user][1] + "|" + self.users[user][2] + "\n")


"""class SizeDataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.usersize = {}

        for line in self.file:
            shoesize, shoestyle = line.strip().split("|")
            self.usersize[shoesize] = (shoestyle)

        self.file.close()

    def add_usersize(self, shoesize, shoestyle):
        if shoesize.strip() not in self.usersize:
            self.usersize[shoesize.strip()] = (shoestyle.strip())
            self.save()
            return 1
        else:
            print("Shoe Size already inputted!")
            return -1

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.usersize:
                f.write(user + "|" + self.users[user][0] + "|" + self.users[user][1] + "|" + self.users[user][2] + "\n")"""