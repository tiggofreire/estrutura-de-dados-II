# ConectaUDF - trabalho em grupo (35 vertices)

Projeto de grafos nao direcionados com base no *Caderno do Estudante ConectaUDF* e na apresentacao da professora. **Projeto preparado para entrega e revisão final dos integrantes.**

## Integrantes
- Aloisio Veleda
- Giovanna Nascimento
- Guilherme Brito
- Isabela Cristina
- Julia Barreira
- Pedro Paulo
- Tiago Freire

## Interpretacao da orientacao oral

A professora orientou **7 integrantes x 5 vertices = 35 vertices no total**. Para respeitar esse total e manter a rede do enunciado, cada conjunto de cinco inclui um integrante real; seis conjuntos incluem um dos seis usuarios originais (Ana a Felipe). Os outros 22 vertices sao ficticios. Assim: **7 integrantes + 6 originais + 22 ficticios = 35**.

Essa divisao e uma proposta de modelagem, e NAO representa atribuicao de autoria, nem diz que os colegas aceitaram suas conexoes.

A apresentacao escrita da professora pede apenas 4 usuarios ficticios e 5 amizades novas para o grupo; esta versao segue o requisito **mais amplo, informado em sala**.

## Estrutura dos nucleos

| Nucleo | 5 vertices |
|---|---|
| 1 | Aloisio Veleda, Ana, Bia, Caio, Duda |
| 2 | Giovanna Nascimento, Bruno, Eva, Fred, Gabi |
| 3 | Guilherme Brito, Carla, Hugo, Iris, Joao |
| 4 | Isabela Cristina, Diego, Katia, Leo, Mila |
| 5 | Julia Barreira, Elisa, Nina, Otavio, Pietra |
| 6 | Pedro Paulo, Felipe, Rafa, Sara, Tomas |
| 7 | Tiago Freire, Ursula, Vitor, Wesley, Yara |


## Resultados calculados (sem valores inseridos manualmente no programa)

| Indicador | Rede original | Rede ampliada |
|---|---:|---:|
| Vertices | 6 | 35 |
| Arestas | 8 | 37 |
| Novas arestas | - | 29 |
| Soma dos graus | 16 | 74 |
| Densidade | 53,33% | 6.22% |

- Grafo simples, nao direcionado e conectado; sem lacos ou arestas duplicadas.
- Cada grupo tem quatro amizades em formato de estrela, totalizando 28, e o grupo Tiago se conecta adicionalmente a Ana (1 amizade). Somando as 8 originais: 37 amizades.
- Os 6 usuarios e as 8 amizades originais permanecem.
- O codigo oferece graus, BFS (menor caminho), densidade e sugestoes por amigos em comum.

## Arquivos

- `conecta_udf.py`: codigo executavel Python 3.9+, sem bibliotecas externas.
- `test_conecta_udf.py`: 11 testes automatizados.
- `grafo_original.png` e `grafo_ampliado.png`: desenhos da rede.
- `tabela_graus.csv`: tabela de vertices, graus e amizades.
- `Relatorio_ConectaUDF_Grupo.docx`: relatório editável para entrega.
- `Relatorio_ConectaUDF_Grupo.pdf`: versão de leitura do relatório.

## Como executar

```powershell
python conecta_udf.py
python -m unittest -v test_conecta_udf.py
```

## Nota sobre os desenhos

O arquivo `grafo_ampliado.png` usa o **primeiro nome** como rotulo para os sete alunos, para evitar sobreposicoes. O README e o relatorio identificam os nomes completos; todos os 35 vertices estao representados uma vez.

## Fontes e limites

- Material da professora: `Grafo/apresentacao_conectaUDF_grafos-2_16out.pdf`, caderno `Grafo/caderno_estudante_conectaUDF.md`.
- O minimo de 35 vertices segue o relato da orientacao oral. A divisao em sete nucleos e as arestas novas foram propostas nesta versao para revisao e podem ser alteradas pelo grupo.
- Nao usamos amizades reais dos integrantes; as conexoes sao ficticias para demonstrar o conceito de grafo.
