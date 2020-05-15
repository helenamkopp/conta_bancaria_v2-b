from main import Employee, Manager, Director

if __name__ == "__main__":
    director = Director("joao", "111.111.111-11", "4000.0")
    print(director.get_bonus())


    # Esse teste vai dar erro! É uma classe abstrata.. Não conseguimos instanciar a classe Employee MAS podemos
    # instanciar as classes filhas que são objetos que realmente existem no sistema.

    # Abstract class (é como se ela não existisse no nosso programa) - Tipo conta / conta corrente e conta poupança.

    employee = Employee("maria", "222.222.222-22", "5000.0")
    print(employee.get_bonus())

