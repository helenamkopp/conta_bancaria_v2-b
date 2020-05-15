from main import Employee, Manager, Director

if __name__ == "__main__":
    director = Director("joao", "111.111.111-11", "4000.0")
    print(director.get_bonus())