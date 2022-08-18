class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("university")
    Name = TreeNode(" Name_of_univerity")
    root.add_child(Name)

    ADDRESSUNIVER = TreeNode("Address")
    ADDRESSUNIVER.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSUNIVER.add_child(TreeNode("Motibagh"))
    ADDRESSUNIVER.add_child(TreeNode("DELHI"))
    ADDRESSUNIVER.add_child(TreeNode("New_DELHI"))
    ADDRESSUNIVER.add_child(TreeNode("India"))

    root.add_child(ADDRESSUNIVER)









    ViceChancellor = TreeNode("ViceChancellor")
    ViceChancellor.add_child(TreeNode("Name"))
    ViceChancellor.add_child(TreeNode("ContactNumber"))
    ViceChancellor.add_child(TreeNode("EmailID"))
    root.add_child(ViceChancellor)

    ADDRESSVC = TreeNode("Address")
    ADDRESSVC.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSVC.add_child(TreeNode("Motibagh"))
    ADDRESSVC.add_child(TreeNode("DELHI"))
    ADDRESSVC.add_child(TreeNode("New_DELHI"))
    ADDRESSVC.add_child(TreeNode("India"))
    ViceChancellor.add_child(ADDRESSVC)


    Dean1 = TreeNode("Dean1")
    Dean1.add_child(TreeNode("NameOfFaculty"))
    Dean1.add_child(TreeNode("Name"))
    Dean1.add_child(TreeNode("ContactNumber"))
    Dean1.add_child(TreeNode("EmailID"))
    Dean1.add_child(TreeNode("EmployeeID"))


    ADDRESSDean1 = TreeNode("Address")
    ADDRESSDean1.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDean1.add_child(TreeNode("Motibagh"))
    ADDRESSDean1.add_child(TreeNode("DELHI"))
    ADDRESSDean1.add_child(TreeNode("New_DELHI"))
    ADDRESSDean1.add_child(TreeNode("India"))


    Dean1.add_child(ADDRESSDean1)
    ViceChancellor.add_child(Dean1)
    Departments = TreeNode("Departments")
    DepartmentsDetails_1=TreeNode("DepartmentsDetails_1")
    DepartmentsDetails_1.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_1.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_1.add_child(TreeNode("Name"))
    DepartmentsDetails_1.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_1.add_child(TreeNode("EmailID"))
    Departments.add_child(DepartmentsDetails_1)



    Dean1.add_child(Departments)
    Members = TreeNode("Members")
    Members.add_child(TreeNode("Name_of_Professor1"))
    Members.add_child(TreeNode("Name_of_Professor2"))
    Members.add_child(TreeNode("Name_of_Professor3"))
    DepartmentsDetails_1.add_child(Members)

    ADDRESSDEP1 = TreeNode("Address")
    ADDRESSDEP1.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDEP1.add_child(TreeNode("Motibagh"))
    ADDRESSDEP1.add_child(TreeNode("DELHI"))
    ADDRESSDEP1.add_child(TreeNode("New_DELHI"))
    ADDRESSDEP1.add_child(TreeNode("India"))
    DepartmentsDetails_1.add_child(ADDRESSDEP1)


    DepartmentsDetails_2=TreeNode("DepartmentsDetails_2")
    DepartmentsDetails_2.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_2.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_2.add_child(TreeNode("Name"))
    DepartmentsDetails_2.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_2.add_child(TreeNode("EmailID"))
    Departments.add_child(DepartmentsDetails_2)



    # Dean1.add_child(Departments)
    MembersDEP2 = TreeNode("Members")
    MembersDEP2.add_child(TreeNode("Name_of_Professor1"))
    MembersDEP2.add_child(TreeNode("Name_of_Professor2"))
    MembersDEP2.add_child(TreeNode("Name_of_Professor3"))
    DepartmentsDetails_2.add_child(MembersDEP2)

    ADDRESSDEP2 = TreeNode("Address")
    ADDRESSDEP2.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDEP2.add_child(TreeNode("Motibagh"))
    ADDRESSDEP2.add_child(TreeNode("DELHI"))
    ADDRESSDEP2.add_child(TreeNode("New_DELHI"))
    ADDRESSDEP2.add_child(TreeNode("India"))
    DepartmentsDetails_2.add_child(ADDRESSDEP2)

    DepartmentsDetails_3 = TreeNode("DepartmentsDetails_3")
    DepartmentsDetails_3.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_3.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_3.add_child(TreeNode("Name"))
    DepartmentsDetails_3.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_3.add_child(TreeNode("EmailID"))
    Departments.add_child(DepartmentsDetails_3)




 ###################################################
    ########DEAN2###########################

    Dean12 = TreeNode("Dean2")
    Dean12.add_child(TreeNode("NameOfFaculty"))
    Dean12.add_child(TreeNode("Name"))
    Dean12.add_child(TreeNode("ContactNumber"))
    Dean12.add_child(TreeNode("EmailID"))
    Dean12.add_child(TreeNode("EmployeeID"))

    ADDRESSDean12 = TreeNode("Address")
    ADDRESSDean12.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDean12.add_child(TreeNode("Motibagh"))
    ADDRESSDean12.add_child(TreeNode("DELHI"))
    ADDRESSDean12.add_child(TreeNode("New_DELHI"))
    ADDRESSDean12.add_child(TreeNode("India"))

    Dean12.add_child(ADDRESSDean12)
    ViceChancellor.add_child(Dean12)
    Departmentsdea2 = TreeNode("Departments")
    DepartmentsDetails_12 = TreeNode("DepartmentsDetails_1")
    DepartmentsDetails_12.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_12.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_12.add_child(TreeNode("Name"))
    DepartmentsDetails_12.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_12.add_child(TreeNode("EmailID"))
    Departmentsdea2.add_child(DepartmentsDetails_12)

    Dean12.add_child(Departmentsdea2)
    Membersdea2 = TreeNode("Members")
    Membersdea2.add_child(TreeNode("Name_of_Professor1"))
    Membersdea2.add_child(TreeNode("Name_of_Professor2"))
    Membersdea2.add_child(TreeNode("Name_of_Professor3"))
    DepartmentsDetails_12.add_child(Membersdea2)

    ADDRESSDEP1dea2 = TreeNode("Address")
    ADDRESSDEP1dea2.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDEP1dea2.add_child(TreeNode("Motibagh"))
    ADDRESSDEP1dea2.add_child(TreeNode("DELHI"))
    ADDRESSDEP1dea2.add_child(TreeNode("New_DELHI"))
    ADDRESSDEP1dea2.add_child(TreeNode("India"))
    DepartmentsDetails_12.add_child(ADDRESSDEP1dea2)

    DepartmentsDetails_22 = TreeNode("DepartmentsDetails_2")
    DepartmentsDetails_22.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_22.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_22.add_child(TreeNode("Name"))
    DepartmentsDetails_22.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_22.add_child(TreeNode("EmailID"))
    Departmentsdea2.add_child(DepartmentsDetails_22)

    # Dean1.add_child(Departments)
    MembersDEP2dea2 = TreeNode("Members")
    MembersDEP2dea2.add_child(TreeNode("Name_of_Professor1"))
    MembersDEP2dea2.add_child(TreeNode("Name_of_Professor2"))
    MembersDEP2dea2.add_child(TreeNode("Name_of_Professor3"))
    DepartmentsDetails_22.add_child(MembersDEP2dea2)

    ADDRESSDEP2dea2 = TreeNode("Address")
    ADDRESSDEP2dea2.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDEP2dea2.add_child(TreeNode("Motibagh"))
    ADDRESSDEP2dea2.add_child(TreeNode("DELHI"))
    ADDRESSDEP2dea2.add_child(TreeNode("New_DELHI"))
    ADDRESSDEP2dea2.add_child(TreeNode("India"))
    DepartmentsDetails_22.add_child(ADDRESSDEP2dea2)

    ###################################################
    ########DEAN3###########################

    Dean123 = TreeNode("Dean3")
    Dean123.add_child(TreeNode("NameOfFaculty"))
    Dean123.add_child(TreeNode("Name"))
    Dean123.add_child(TreeNode("ContactNumber"))
    Dean123.add_child(TreeNode("EmailID"))
    Dean123.add_child(TreeNode("EmployeeID"))

    ADDRESSDean123 = TreeNode("Address")
    ADDRESSDean123.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDean123.add_child(TreeNode("Motibagh"))
    ADDRESSDean123.add_child(TreeNode("DELHI"))
    ADDRESSDean123.add_child(TreeNode("New_DELHI"))
    ADDRESSDean123.add_child(TreeNode("India"))

    Dean123.add_child(ADDRESSDean123)
    ViceChancellor.add_child(Dean123)
    Departmentsdea3 = TreeNode("Departments")
    DepartmentsDetails_123 = TreeNode("DepartmentsDetails_1")
    DepartmentsDetails_123.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_123.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_123.add_child(TreeNode("Name"))
    DepartmentsDetails_123.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_123.add_child(TreeNode("EmailID"))
    Departmentsdea3.add_child(DepartmentsDetails_123)

    Dean123.add_child(Departmentsdea3)
    Membersdea3 = TreeNode("Members")
    Membersdea3.add_child(TreeNode("Name_of_Professor1"))
    Membersdea3.add_child(TreeNode("Name_of_Professor2"))
    Membersdea3.add_child(TreeNode("Name_of_Professor3"))
    DepartmentsDetails_123.add_child(Membersdea3)

    ADDRESSDEP1dea3 = TreeNode("Address")
    ADDRESSDEP1dea3.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDEP1dea3.add_child(TreeNode("Motibagh"))
    ADDRESSDEP1dea3.add_child(TreeNode("DELHI"))
    ADDRESSDEP1dea3.add_child(TreeNode("New_DELHI"))
    ADDRESSDEP1dea3.add_child(TreeNode("India"))
    DepartmentsDetails_123.add_child(ADDRESSDEP1dea3)

    DepartmentsDetails_223 = TreeNode("DepartmentsDetails_2")
    DepartmentsDetails_223.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_223.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_223.add_child(TreeNode("Name"))
    DepartmentsDetails_223.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_223.add_child(TreeNode("EmailID"))
    Departmentsdea3.add_child(DepartmentsDetails_223)

    # Dean1.add_child(Departments)
    MembersDEP2dea3 = TreeNode("Members")
    MembersDEP2dea3.add_child(TreeNode("Name_of_Professor1"))
    MembersDEP2dea3.add_child(TreeNode("Name_of_Professor2"))
    MembersDEP2dea3.add_child(TreeNode("Name_of_Professor3"))
    DepartmentsDetails_223.add_child(MembersDEP2dea3)

    ADDRESSDEP2dea3 = TreeNode("Address")
    ADDRESSDEP2dea3.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDEP2dea3.add_child(TreeNode("Motibagh"))
    ADDRESSDEP2dea3.add_child(TreeNode("DELHI"))
    ADDRESSDEP2dea3.add_child(TreeNode("New_DELHI"))
    ADDRESSDEP2dea3.add_child(TreeNode("India"))
    DepartmentsDetails_223.add_child(ADDRESSDEP2dea3)


    root.print_tree()

if __name__ == '__main__':
    build_product_tree()





