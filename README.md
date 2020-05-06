# Planejamento de Caminho

## Bibliotecas utilizadas
Para a utilização dos scripts, é necessária a instalação das seguintes bibliotecas:
- Numpy
- Pygame

## Algoritmos utilizados
Foram implementados algoritmos capazes de gerar labirintos de forma aleatória, com apenas uma única resposta, e capazes de buscar a solução.

### Criação dos labirintos
Para a criação dos labirintos, foi utilizado uma versão randômica do algoritmo Depth First Search. Foram implementadas duas versões desse algoritmo, onde uma usava recursividade e a outra não. A criação da versão não recursiva se tornou necessária para criar labirintos de dimensões maiores, em relação a versão recursiva, sem que o limite de recursividade da linguagem seja ultrapassado. 

### Busca de caminho
Para resolver os labirintos propostos, foram implementados dois algoritmos de busca, o Depth First Search e o A*. O algoritmo A* é um algoritmo de busca de menor camminho entre dois pontos e por isso uma saída viável para a resolução do problema, porém como há apenas uma solução para o labirinto, o algoritmo de Depth First Search se mostra funcional para a resolução do problema.

## Restrições
### Dimensões do labirinto
Afim de facilitar a implementação do algoritmo para a geração de labirintos, foi imposto como restrição que as dimensões do labirinto deveriam ser impares, com cada dimensão representando a quantidade de casas do labirinto, seja essa aberta ou preenchida com a parede.


