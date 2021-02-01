# EMPLOYEE RESOURCE PLANNING SYSTEM
# BLL
class employee: # PARENT CLASS
    def __init__(self):
        self.ID=0
        self.name=0
        self.age=0
        self.mob=0
class manager(employee): #MANAGER CLASS
    emplistm = [] #LIST WHICH CONTAINS DETAILS OF MANAGER LEVEL EMPLOYEE
    def __init__(self):
        self.area=0
        super().__init__()
    def addemployee(self): #FUNCTION FOR ADDING AN EMPLOYEE TO THE LIST
        manager.emplistm.append(self)
    @staticmethod
    def searchemployee (ID): #FUNCTION FOR SEARCHING AN EMPLOYEE TO THE LIST
        for e in range(len(manager.emplistm)):
            if (manager.emplistm[e].ID==ID):
                return manager.emplistm[e]
    @staticmethod
    def deleteemployee(ID): #FUNCTION FOR DELETING AN EMPLOYEE TO THE LIST
        for i in manager.emplistm:
            if(i.ID==ID):
                manager.emplistm.remove(i)
                break
    def modifyemployee(self): #FUNCTION FOR MODIFYING AN EMPLOYEE TO THE LIST
        for e in manager.emplistm:
            if(e.ID==self.ID):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.area=e.area
                return

class trainer(employee):
    emplistt = []
    def __init__(self):
        self.course=0
        super().__init__()
    def addemployee(self):
        trainer.emplistt.append(self)
    @staticmethod
    def searchemployee (ID):
        for e in range(len(trainer.emplistt)):
            if (trainer.emplistt[e].ID==ID):
                return trainer.emplistt[e]
            else:
                return "Not found"
    @staticmethod
    def deleteemployee(ID):
        for e in trainer.emplistt:
            if (e.ID==ID):
                trainer.emplistt.remove(e)
                return
    def modifyemployee(self):
        for e in trainer.emplistt:
            if(e.ID==self.ID):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.course=e.course
                return

class director(employee):
    emplistd = []
    def __init__(self):
        self.share=0
        super().__init__()
    def addemployee(self):
        director.emplistd.append(self)
    @staticmethod
    def searchemployee (ID):
        for e in range(len(director.emplistd)):
            if (director.emplistd[e].ID==ID):
                return director.emplistd[e]
            else:
                return "Not found"
    @staticmethod
    def deleteemployee(ID):
        for e in director.emplistd:
            if (e.ID==ID):
                director.emplistd.remove(e)
                return
    def modifyemployee(self):
        for e in director.emplistd:
            if(e.ID==self.ID):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.share=e.share
                return

# PLL
print("Welcome to Employee Resource Planning 2021")
while(1):
    print("Enter the Category of employee\n1: MANAGER\n2: TRAINER\n3: DIRECTOR\n4: EXIT ")
    category=input("enter category:")
    category=category.lower()
    while(1):
        if(category=="manager"):
            print(" 1: Add a new Employee \n 2: Search a Employee \n 3: Delete a Employee \n 4: Modify a Employee \n 5: Exit")
            choice = int(input("Enter a choice:"))
            if (choice==1):
                man = manager()
                man.ID=input("Enter the ID")
                man.name = input("enter the name")
                man.age=input("Enter the age")
                man.mob=input("enter the Mob")
                man.area=input(("enter the area of expertise"))
                man.addemployee()
                print("employee added successfully")
                for e in manager.emplistm:
                    print("EMPID\tEMPName\tEMPAge\tEMPMob\tEMPArea")
                    print("\t",e.ID,"\t",e.name,"\t",e.age,"\t",e.mob,"\t",e.area)
            elif (choice == 2):
                man=manager()
                man.ID=int(input("enter the ID you want to search"))
                emp=manager.searchemployee(man.ID)
                print("EMP ID",emp.ID,"\nEMP Name",emp.name,"\nEMP Age",emp.age,"\n EMP Mob",emp.mob,"\nEMP Area",emp.area)
            elif (choice == 3):
                man=manager()
                ID=input("enter the ID")
                man.deleteemployee(ID)
                print("employee Deleted successfully")
                for e in manager.emplistm:
                    print("EMPID", e.ID, "\nEMP Name", e.name, "\nEMP Age", e.age, "\n EMP Mob", e.mob,
                          "\nEMP Area", e.area)
            elif (choice == 4):
                man = manager()
                man.ID=input("Enter the ID")
                man.name = input("enter the name")
                man.age=input("Enter the age")
                man.mob=int(input("enter the Mob"))
                man.area=input("enter the area of expertise")
                man.modifyemployee()
                print("employee modified successfully")
                print("EMP ID", man.ID, "\nEMP Name", man.name, "\nEMP Age", man.age, "\n EMP Mob", man.mob,
                      "\nEMP Area", man.area)
            elif (choice == 5):
                exit()
            else:
                print("wrong choice")
        elif(category=="trainer"):
            print(" 1: Add a new Employee \n 2: Search a Employee \n 3: Delete a Employee \n 4: Modify a Employee \n 5: Exit")
            choice = int(input("Enter a choice:"))
            if (choice==1):
                tra = trainer()
                tra.ID=input("Enter the ID")
                tra.name = input("enter the name")
                tra.age=input("Enter the age")
                tra.mob=int(input("enter the Mob"))
                tra.course=input(("enter the course"))
                tra.addemployee()
                print("employee added successfully")
            elif (choice == 2):
                tra=trainer()
                tra.ID=input("enter the ID you want to search")
                emp=trainer.searchemployee(tra.ID)
                print("EMP ID",emp.ID,"\nEMP Name",emp.name,"\nEMP Age",emp.age,"\n EMP Mob",emp.mob,"\nEMP Area",emp.area)
            elif (choice == 3):
                DeleteID=input("enter the ID")
                trainer.deleteemployee(DeleteID)
                print("employee Deleted successfully")
            elif (choice == 4):
                tra = trainer()
                tra.ID=input("Enter the ID")
                tra.name = input("enter the name")
                tra.age=input("Enter the age")
                tra.mob=int(input("enter the Mob"))
                tra.course=input(("enter the course"))
                tra.modifyemployee()
                print("employee modified successfully")
            elif (choice == 5):
                exit()
            else:
                print("wrong choice")
        elif(category=="director"):
            def showemployee(director):
                print("EmpID", director.ID, "EmpName", director.name, "EmpAge", director.age, "Empmob", director.mob)
            print(" 1: Add a new Employee \n 2: Search a Employee \n 3: Delete a Employee \n 4: Modify a Employee \n 5: Exit")
            choice = int(input("Enter a choice:"))
            if (choice==1):
                dire = director()
                dire.ID=input("Enter the ID")
                dire.name = input("enter the name")
                dire.age=input("Enter the age")
                dire.mob=int(input("enter the Mob"))
                dire.share=input(("enter the shares of company"))
                dire.addemployee()
                print("employee added successfully")
            elif (choice == 2):
                dire=director()
                dire.ID=int(input("enter the ID you want to search"))
                emp=director.searchemployee(dire.ID)
                print("EMP ID",emp.ID,"\nEMP Name",emp.name,"\nEMP Age",emp.age,"\n EMP Mob",emp.mob,"\nEMP Area",emp.area)
            elif (choice == 3):
                DeleteID=input("enter the ID")
                director.deleteemployee(DeleteID)
                print("employee Deleted successfully")
            elif (choice == 4):
                dire = director()
                dire.ID=input("Enter the ID")
                dire.name = input("enter the name")
                dire.age=input("Enter the age")
                dire.mob=int(input("enter the Mob"))
                dire.course=input(("enter the course"))
                dire.modifyemployee()
                print("employee modified successfully")
                showemployee(dire)
            elif (choice == 5):
                exit()
            else:
                print("wrong choice")
        elif(category=="exit"):
            exit()
        else:
            print("Please input the given choices properly")
