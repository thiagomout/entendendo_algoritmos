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

Notação especial que diz o quão rápido é um algoritmo. Essa notação não leva em consideração o tempo, mas sim o número de operações, ela informa o quão rapidamente um algoritmo cresce. para pesquisa binária na notação Big O, escrevemos $O(\log n)$. É importante ressaltar que a notação Big O leva em conta a pior hipótese, pode ser que na pesquisa simples encontremos o item na primeira tentativa, do mesmo jeito a notação é $O(n)$.

#### Exercícios

1.3 - Pela lista estar ordenada $O(log n)$
1.4 - $O(n)$
1.5 - $O(n)$
1.6 - São 26 letras no alfabeto, já que queremos percorrer apenas 1 delas, $O(n/26)$

#### Caixeiro Viajante

No exemplo do caixeiro viajante vemos que para decidir o melhor itinerário entra n cidades temos que testar todas as combinações entre elas, resultando em $O(n!)$, muitas pessoas já tentaram resolver esse problema, mas parece ser um problema impossível.
