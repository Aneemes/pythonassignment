class branchinfo:
    def __init__(self,branchname,password):
        self.branchname=branchname
        self.password=password

    def set_branchname(self,branchname):
        self.branchname=branchname

    def get_branchname(self):
        return self.branchname

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password
