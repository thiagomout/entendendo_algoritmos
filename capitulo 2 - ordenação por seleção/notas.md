# Ordenação por seleção

## Entendendo a memória

Cada vez que quer armazenar um item na memoria você pede para o computador um espaço e ele te retorna um endereço. Para armazenar multiplos elementos, podemos usar listas ou arrays.

## Arrays e listas encadeadas

Exemplo do aplicativo para gerenciar afazeres $\rightarrow$ usando um array todas suas tarefas são armazenadas contiguamente na memória, se você quisesse adicionar uma nova tarefa, e esse espaço na memória já estivesse em uso, teríamos que mover todas as outras tarefas na memória, para um lugar que haja espaço. E se adicionasse mais um, novamente o mesmo processo, então adicionar itens a um array é um processo lento, a não ser que você reserve o espaço antes. Isso tem problemas, pois pode ser que não usemos o espaço alocado com a antecedência, ou que precisamos de mais espaço que o antecipado.

## Listas encadeadas

Nas listas encadeadas seus intens podem estar em qualquer lugar na memória, e esses espaços são ligados entre si, não necessariamente em espaços subsequentes. Funciona da seguinte maneira: cada espaço da memória tem o endereço do próximo. Isso evita o problema anterior do espaço na memória, logo, listas encadeadas são bem melhores para inserções.

## Arrays

A principal vantagem de um array é, já que suas posições são subsequentes, sabemos onde na memória está cada item, e podemos acessá-lo diretamente, já numa lista encadeada, teremos que passar elemento por elemento até chegar no item desejado.
