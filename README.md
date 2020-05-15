# conta_bancaria_v2-b

Pequeno projeto Orientado a Objetos, construido utilizando o PyCharm com o objetivo de aprendizado de conceitos de classes abstratas. 
Continuação do projeto conta_bancaria_v2-a

Todo projeto é muito semelhante a v2-a e aqui, foco apenas nas mudanças principais:

# Arquivo mais.py:
 importamos o pacote abc para poder tornar nossa class Employee abstrata;
 tornamos o método get_bonus abstrato;
 
 Observamos aqui que é como se a class Employee não "existisse" mais, apenas os seus atributos, que poderão ser utilizados pelas duas classes
 filhas / sub classes, como é o caso de class Manager e class Director (criada nessa versão) 
 
 # Arquivo test_main.py:
 contém dois pequenos testes onde um não funciona de propósito para mostrar o que foi descrito acima. 
