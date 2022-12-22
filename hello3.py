def hello(
    to="world",
):  # Equivalente ao function do MATLAB, mas agora atribuindo um valor default para a entrada, caso vazia
    print(f"Hello {to}!")


hello()
# Pede o nome do usuário removendo espaços em excesso e com a primeira letra de cada palavra maiúscula
name = input("What's your name? ").strip().title()
# Diz hello ao usuário
hello(name)
# O slide scope salienta que uma variável de uma função não existe para outra, apenas variáveis globais
