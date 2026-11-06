# ==============================================================================
# TÓPICO 8: Desafio Prático — Gestão de Estoque
# Lista de produtos com processamento de métricas e busca de extremos
# ==============================================================================

# Requisito 1 & 2: Cadastro de pelo menos 5 produtos usando lista de dicionários
estoque = [
    {"nome": "Notebook Pro", "preco": 4500.00, "quantidade": 8},
    {"nome": "Mouse Sem Fio", "preco": 120.00, "quantidade": 45},
    {"nome": "Teclado Mecânico", "preco": 350.00, "quantidade": 25},
    {"nome": "Monitor 27 Ultra", "preco": 1800.00, "quantidade": 12},
    {"nome": "Cadeira Ergonômica", "preco": 1200.00, "quantidade": 15}
]

# Inicialização de variáveis acumuladoras e de referência para os extremos
valor_total_estoque = 0.0
produto_mais_caro = estoque[0]
produto_maior_volume = estoque[0]

print("=== RELATÓRIO DETALHADO DO ESTOQUE CADASTRADO ===\n")

# Processamento dos itens do estoque
for produto in estoque:
    # Cálculo do valor financeiro total do item (Preço * Quantidade)
    subtotal_item = produto["preco"] * produto["quantidade"]

    # Acumula o valor total do estoque
    valor_total_estoque += subtotal_item

    # Impressão formatada dos dados de cada produto
    print(f"Produto: {produto['nome']:<20} | "
          f"Preço Un.: R$ {produto['preco']:8.2f} | "
          f"Qtd: {produto['quantidade']:3d} | "
          f"Subtotal: R$ {subtotal_item:9.2f}")

    # Verificação 1: Produto de maior preço unitário
    if produto["preco"] > produto_mais_caro["preco"]:
        produto_mais_caro = produto

    # Verificação 2: Produto com maior quantidade armazenada
    if produto["quantidade"] > produto_maior_volume["quantidade"]:
        produto_maior_volume = produto

print("\n" + "="*65)
print("=== MÉTRICAS E RESULTADOS DO DESAFIO DE ESTOQUE ===")
print("="*65)
print(f"1. Valor Total Financeiro em Estoque: R$ {valor_total_estoque:,.2f}")
print(f"2. Produto Mais Caro (Preço Un.):    {produto_mais_caro['nome']} (R$ {produto_mais_caro['preco']:.2f})")
print(f"3. Maior Volume de Estoque (Qtd):    {produto_maior_volume['nome']} ({produto_maior_volume['quantidade']} unidades)")