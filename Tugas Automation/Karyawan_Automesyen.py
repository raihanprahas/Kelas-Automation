class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary
        self.karyawan_gaji_naik()

    def increase_salary(self):
        if self.position == "IT":
            self.__salary *= 1.10  # Menaikkan gaji IT sebesar 10%
        elif self.position == "Direktur":
            self.__salary *= 1.20  # Menaikkan gaji Direktur sebesar 20%
        elif self.position == "HR":
            self.__salary *= 1.05  # Menaikkan gaji HR sebesar 5%

    # Getter untuk mendapatkan nilai salary
    def get_salary(self):
        return self.__salary

    def info_karyawan(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print("Salary: Confidential")

    def karyawan_gaji_naik(self):
        if self.position == "IT" or self.position == "HR" or self.position == "Direktur":
            self.increase_salary()
            print("Gaji telah dinaikkan.")
        else:
            print("Gaji tidak naik")

class PT_Automesyen(Employee):
    def info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.get_salary()}")
