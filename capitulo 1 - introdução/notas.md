# Introdução a algoritmos
## Pesquisa Binária
Entrada - lista de elementos ordenada e Saida - posição (se estiver na lista) ou null (se nao estiver).
Exemplo do número de 1 a 100 - chutar sempre no meio.
De maneira geral para uma lista de n números, a pesquisa binária precisa de $\log_2 n$ etapas para achar.

### Exercícios
1.1 - $\log_2 128 = 7$
1.2 - $\log_2 256 = 8$

## Tempo de Execução
Queremos otimizar nosso algoritmo - menor tempo e espaço.
Na pesquisa binária é executada com tempo logaritmico.

### Notação Big O
Notação especial que diz o quão rápido é um algoritmo.

#### Tempo de execução de cada algoritmo cresce em taxas diferentes
O tempo de execução da pesquisa simples ou binária cresce em totalmente diferentes, exemplo: para uma lista de 100 elementos que demora 1 ms para checar cada elemento, a pesquisa simples demoraria 100 ms e a binária 7 ms, já para 1 bilhão de elementos a simples demoraria 11 dias, já a binária 32 ms.
