# Programa de Pesquisa de Opinião - TudoWeb
# Desenvolvido para coletar e analisar o grau de satisfação dos clientes

# Inicialização de contadores
qtd_excelente = 0
qtd_ruim = 0

# Definição do número de entrevistados 
# (Altere para 50 para a execução oficial ou mantenha 10 para os testes solicitados)
TOTAL_ENTREVISTADOS = 10 

print(f"=== INICIANDO PESQUISA DE SATISFAÇÃO TUDOWEB ({TOTAL_ENTREVISTADOS} ENTREVISTADOS) ===\n")

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    # Coleta de dados básicos
    nome = input("Digite o nome do entrevistado: ")
    
    # Validação simples da idade para garantir entrada numérica
    while True:
        try:
            idade = int(input("Digite a idade do entrevistado: "))
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")

    # Coleta e validação da opinião
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    while True:
        try:
            opiniao = int(input("Digite o código da sua opinião (1, 2 ou 3): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Digite apenas 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro correspondente à opção.")

    # Estrutura de decisão para contabilizar as respostas
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    # Nota: A opção 2 (BOM) é coletada, mas não exige contagem específica segundo os itens 4.a e 4.b.

    print("\n") # Linha em branco para separar os cadastros

# Exibição dos resultados finais
print("=" * 40)
print("       RESULTADO FINAL DA PESQUISA")
print("=" * 40)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("=" * 40)
print("Pesquisa finalizada com sucesso!")
