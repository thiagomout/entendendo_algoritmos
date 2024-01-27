# Ordenação por seleção

## Entendendo a memória

Cada vez que quer armazenar um item na memoria você pede para o computador um espaço e ele te retorna um endereço. Para armazenar multiplos elementos, podemos usar listas ou arrays

## Arrays e listas encadeadas

Exemplo do aplicativo para gerenciar afazeres $\rightarrow$ usando um array todas suas tarefas são armazenadas contiguamente na memória, se você quisesse adicionar uma nova tarefa, e esse espaço na memória já estivesse em uso, teríamos que mover todas as outras tarefas na memória, para um lugar que haja espaço. E se adicionasse mais um, novamente o mesmo processo, então adicionar itens a um array é um processo lento, a não ser que você reserve o espaço antes.