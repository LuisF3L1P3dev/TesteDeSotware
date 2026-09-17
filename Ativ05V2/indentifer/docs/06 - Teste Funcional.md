# Técnicas de Teste: Teste Funcional

**Disciplina:** Teste de Software  
**Professor:** Raphael Muniz  
**Contato:** raphael.muniz@ifrn.edu.br

## Slide 1 — Técnicas de Teste: Teste Funcional

Apresentação da disciplina **Teste de Software** sobre técnicas de teste, com foco em **teste funcional**.

## Slide 2 — Teste funcional: a analogia da construção de uma casa

- Um lote ou terreno é adquirido para a construção de uma casa.
- Uma equipe é contratada para construir a casa.

> **Nota do apresentador:** Você comprou um lote ou terreno e quer construir a casa dos seus sonhos, considerando suas demandas e necessidades. Para isso, contrata uma equipe com pedreiros e engenheiro, que construirá a casa seguindo suas vontades e necessidades.

## Slide 3 — Vistorias externas durante a construção

Ao longo do desenvolvimento, são realizadas visitas periódicas para verificar questões externas.

> **Nota do apresentador:** A tinta ficou adequada? Há rachaduras? A construção está ficando como esperado?

## Slide 4 — Da construção de casas ao desenvolvimento de software

| Desenvolvimento de casas | Desenvolvimento de software |
| --- | --- |
| O proprietário realiza vistorias externas durante a construção. | O responsável verifica externamente se o software atende ao que foi especificado. |

Essa analogia ajuda a compreender a técnica chamada **teste funcional**.

> **Nota do apresentador:** A tinta ficou adequada? Há rachaduras? A construção está ficando como esperado?

## Slide 5 — Funcionamento do teste funcional

O teste funcional equivale ao proprietário que realiza visitas de vistoria externa em sua futura casa.

A partir da **especificação de requisitos do software**, são identificadas as funções que o sistema deverá realizar, por exemplo:

- incluir pessoa física;
- consultar CPF;
- emitir relatório de clientes.

Em seguida, são projetados casos de teste formados por pares de **entrada** e **saída esperada**:

1. Uma entrada é fornecida ao programa.
2. O programa produz uma saída.
3. A saída obtida é comparada com a saída esperada.
4. Verifica-se se as duas saídas são iguais.

## Slide 6 — Perguntas respondidas pelo teste funcional

O teste funcional tende a responder perguntas como:

- O usuário consegue fazer isso?
- Essa funcionalidade funciona?

Como resultado, podem ser reveladas inconformidades com os objetivos especificados, tais como:

- funções incorretas ou ausentes;
- erros na interface;
- erros em estruturas de dados;
- erros de acesso a softwares externos;
- erros de inicialização e término.

## Slide 7 — Características do teste funcional

Como os critérios de teste funcional se baseiam na especificação do produto testado, essa técnica:

- requer uma boa especificação dos requisitos;
- pode ser aplicada em todas as fases de teste, incluindo unidade, integração e sistema;
- permite a atuação de equipes independentes;
- pode ser realizada de forma manual e/ou automática;
- pode ser aplicada a produtos criados em diversos paradigmas.

## Slide 8 — Visão geral

1. Identificar as funções que o software deve realizar.
2. Projetar casos de teste capazes de verificar se essas funções estão sendo realizadas pelo software.
3. Executar os casos de teste.
4. Comparar os resultados computados com os resultados previamente identificados.

## Slide 9 — Critérios de teste funcional

O domínio de entrada pode ser infinito ou muito grande. Por isso, critérios podem ser utilizados para identificar casos de teste mais adequados e com maior cobertura do software.

Entre esses critérios estão:

- particionamento em classes de equivalência;
- análise do valor limite;
- teste funcional sistemático;
- grafo de causa e efeito;
- outros critérios.

## Slide 10 — Síntese do teste funcional

- Requer a especificação do produto para derivar os casos de teste.
- Utiliza critérios baseados na especificação do produto testado.
- Pode ser aplicado em todas as fases de teste, como unidade, integração e sistema.
- Reflete a ótica do usuário ou *stakeholder* ao utilizar o programa.
- Pode ser aplicado a qualquer programa.
- Cada critério explora tipos de defeitos utilizando valores específicos do domínio de entrada.

> **Nota do apresentador:** É importante identificar pesquisas recentes, pois essas técnicas continuam evoluindo e novos critérios e técnicas têm sido criados.

## Slide 11 — Critério: particionamento em classes de equivalência

**Professor:** Raphael Muniz  
**Contato:** raphael.muniz@ifrn.edu.br

## Slide 12 — Alguns critérios de teste funcional

- Particionamento em classes de equivalência;
- análise de valor limite;
- grafo de causa e efeito;
- *error guessing*;
- teste funcional sistemático;
- entre outros.

Todos os critérios se baseiam na especificação do produto testado.

## Slide 13 — Exemplo: programa Identifier

> O programa deve determinar se um identificador é válido ou não. Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter o mínimo de um caractere e o máximo de seis caracteres de comprimento.

## Slide 14 — Teste

**TEST**

## Slide 15 — Atividade 03: ClassRoom

Tente listar pares de casos de teste — entrada e saída esperada — que cubram toda a especificação descrita.

## Slide 16 — Conceito de classes de equivalência

O critério de particionamento em classes de equivalência divide o **domínio de entradas** em **classes de equivalência**, isto é, subconjuntos que, de acordo com a especificação do programa, podem ser tratados da mesma maneira.

Qualquer elemento ou dado de teste selecionado deve representar o subconjunto do qual faz parte.

## Slide 17 — Como aplicar o particionamento em classes de equivalência

### Passo 1: identificar as classes de equivalência

- Partir da especificação do software.
- Procurar termos como **intervalo**, **conjunto** ou palavras similares.
- Verificar as diretrizes para definir as classes.
- Se elementos de uma mesma classe forem tratados de forma diferente, dividir essa classe em classes menores.
- Definir classes válidas e inválidas.

### Passo 2: gerar os casos de teste

- Selecionar um elemento de cada classe.
- Depois de identificar as classes, escolher arbitrariamente os elementos de cada uma.
- Definir casos de teste para as classes válidas e inválidas.

## Slide 18 — Diretrizes para definir classes

- Se a condição de entrada especifica um **intervalo**, define-se uma classe válida e duas inválidas.
- Se a condição de entrada especifica uma **quantidade**, define-se uma classe válida e duas inválidas.
- Se a condição especifica **conjuntos determinados de valores**, define-se uma classe válida para cada conjunto e uma classe inválida com outro valor qualquer. Exemplo: tabela de imposto de renda.
- Se a condição de entrada é **específica** — “deve ser assim” —, define-se uma classe válida e uma inválida. Exemplo: o identificador deve iniciar com uma letra.

## Slide 19 — Identifier: classes de equivalência e conjunto de teste

### Especificação

> O programa deve determinar se um identificador é válido ou não. Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter o mínimo de um caractere e o máximo de seis caracteres de comprimento.

### Passo 1: identificação das classes de equivalência

| Variável de entrada | Classes de equivalência válidas | Classes de equivalência inválidas |
| --- | --- | --- |
| Comprimento (`t`) | `1 ≤ t ≤ 6` — classe 1 | `t < 1` — classe 2; `t > 6` — classe 3 |
| Iniciar com uma letra (`i`) | Sim, inicia com letra — classe 4 | Não inicia com letra — classe 5 |
| Conter letras ou dígitos (`c`) | Contém apenas letras ou dígitos — classe 6 | Contém caracteres diferentes de letras e dígitos — classe 7 |

### Passo 2: definição do conjunto de teste

\[
T_0 = \{(\text{a5}, \text{Válido}), (\text{""}, \text{Inválido}), (\text{665432197}, \text{Inválido}), (\text{B*ss1}, \text{Inválido})\}
\]

Cobertura das classes:

- `a5`: classes 1, 4 e 6;
- `""`: classe 2;
- `665432197`: classes 3 e 5;
- `B*ss1`: classe 7.

## Slide 20 — Critério: análise do valor limite

**Professor:** Raphael Muniz  
**Contato:** raphael.muniz@ifrn.edu.br

## Slide 21 — Relação com as classes de equivalência

Alguns critérios de teste funcional são:

- particionamento em classes de equivalência;
- análise de valor limite;
- grafo de causa e efeito;
- *error guessing*;
- teste funcional sistemático;
- entre outros.

Todos se baseiam na especificação do produto testado. A **análise do valor limite complementa** os resultados do **particionamento em classes de equivalência**.

## Slide 22 — Conceito de análise do valor limite

A análise do valor limite:

- é uma extensão do particionamento em classes de equivalência;
- considera como valores limites os valores mínimos e máximos de uma classe;
- geralmente é utilizada para testar requisitos que exigem intervalos de números;
- é utilizada quando a classe é ordenada, consistindo em dados numéricos ou sequenciais.

## Slide 23 — Seleção dos dados de teste nos limites

Em vez de selecionar os dados de teste aleatoriamente, eles devem ser escolhidos considerando os valores limitantes inferior e superior de cada classe de equivalência.

## Slide 24 — Exemplo: faixa etária de 20 a 30 anos

Um sistema premiará aniversariantes. A regra determina que somente pessoas com idade entre 20 e 30 anos poderão concorrer.

### Classes de equivalência

| Classe | Valores | Resultado |
| --- | --- | --- |
| Inferior | 0, 1, 2, …, 19 | Inválido |
| Central | 20, 21, 22, …, 30 | Válido |
| Superior | 31, 32, 33, … | Inválido |

Considerando a análise do valor limite, devem ser usados os dados imediatamente antes e nos extremos do intervalo válido:

**Resposta:** 19, 20, 30 e 31.

## Slide 25 — Suíte de teste para a faixa etária

| Dado de teste | Saída esperada |
| ---: | --- |
| 19 | Inválido |
| 20 | Válido |
| 30 | Válido |
| 31 | Inválido |

## Slide 26 — Recomendações gerais para análise do valor limite

| Condição de entrada | Exemplo | Dados de teste recomendados |
| --- | --- | --- |
| (1) Especifica um intervalo de valores | Um valor no intervalo entre −1 e +1 | Os limites do intervalo e os valores imediatamente subsequentes que explorem classes inválidas vizinhas: `−1,001`, `−1`, `+1` e `+1,001`. |
| (2) Especifica uma quantidade de valores | Um valor com tamanho entre 1 e 255 caracteres | Nenhum valor de entrada; 1 valor; 255 valores; e 256 valores de entrada. |

Recomendações adicionais:

- usar a recomendação 1 para as condições de saída;
- usar a recomendação 2 para as condições de saída;
- se a entrada ou saída for um conjunto ordenado, considerar o primeiro e o último elemento.

## Slide 27 — Identifier: retomada do exemplo

> O programa deve determinar se um identificador é válido ou não. Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter o mínimo de um caractere e o máximo de seis caracteres de comprimento.

## Slide 28 — Identifier: classes identificadas

### Passo 1: identificar as classes de equivalência

| Variável de entrada | Classes de equivalência válidas | Classes de equivalência inválidas |
| --- | --- | --- |
| Comprimento (`t`) | `1 ≤ t ≤ 6` — classe 1 | `t < 1` — classe 2; `t > 6` — classe 3 |
| Iniciar com uma letra (`i`) | Sim, inicia com letra — classe 4 | Não inicia com letra — classe 5 |
| Conter letras ou dígitos (`c`) | Contém apenas letras ou dígitos — classe 6 | Contém caracteres diferentes de letras e dígitos — classe 7 |

Conjunto de teste inicial:

\[
T_0 = \{(\text{a5}, \text{Válido}), (\text{""}, \text{Inválido}), (\text{665432197}, \text{Inválido}), (\text{B*ss1}, \text{Inválido})\}
\]

Cobertura: `(1, 4, 6)`, `(2)`, `(3, 5)` e `(7)`.

## Slide 29 — Identifier: casos para o critério de comprimento

### Passo 2: definir os casos considerando os limites

Para o critério de comprimento (`t`), as classes são:

- `1 ≤ t ≤ 6` — classe 1;
- `t < 1` — classe 2;
- `t > 6` — classe 3.

| Entrada para `t` | Classe | Saída esperada |
| --- | ---: | --- |
| `""` | 2 | Inválido |
| `a` | 1 | Válido |
| `a12345` | 1 | Válido |
| `a123456` | 3 | Inválido |

## Slide 30 — Identifier: cobertura dos critérios de início e conteúdo

É necessário verificar se os dados definidos também atendem às classes dos critérios `i` e `c`:

- `i`: inicia com letra — classe 4; não inicia com letra — classe 5;
- `c`: contém apenas letras ou dígitos — classe 6; contém outros caracteres — classe 7.

| Entrada | Comprimento (`t`) | Início (`i`) | Conteúdo (`c`) | Saída esperada |
| --- | ---: | ---: | ---: | --- |
| `""` | 2 | 5 | — | Inválido |
| `a` | 1 | 4 | 6 | Válido |
| `a12345` | 1 | 4 | 6 | Válido |
| `a123456` | 3 | — | — | Inválido |

## Slide 31 — Identifier: classes ainda não contempladas

As classes que ainda precisam ser contempladas são:

- não inicia com letra — classe 5;
- contém caracteres diferentes de letras e dígitos — classe 7.

| Entrada | Comprimento (`t`) | Início (`i`) | Conteúdo (`c`) | Saída esperada |
| --- | ---: | ---: | ---: | --- |
| `""` | 2 | 5 | — | Inválido |
| `a` | 1 | 4 | 6 | Válido |
| `a12345` | 1 | 4 | 6 | Válido |
| `a123456` | 3 | — | — | Inválido |
| `2` | — | 5 | — | Inválido |
| `A#$12` | — | — | 7 | Inválido |

## Slide 32 — Teste

**TEST**

## Slide 33 — Exercício: escolha da técnica de teste

O uso de uma técnica não exclui o uso de outra. É possível empregar várias técnicas para gerar casos de teste.

A escolha da técnica depende de fatores como:

- tipo do sistema;
- clientes;
- requisitos contratuais;
- nível e tipo de riscos;
- objetivos do teste;
- documentação disponível;
- conhecimento dos testadores;
- tempo e dinheiro;
- ciclo de desenvolvimento adotado, como cascata ou iterativo/incremental;
- modelo de caso de uso;
- experiência prévia com os tipos de defeitos encontrados;
- outras questões relevantes.

### Cenário

Você e sua equipe receberam a tarefa de implantar o **ScriptLattes**, um *script* GNU-GPL desenvolvido para a extração e compilação automática de:

- produções bibliográficas;
- produções técnicas;
- produções artísticas;
- orientações;
- projetos de pesquisa;
- prêmios e títulos;
- grafo de colaborações;
- mapa de geolocalização de um conjunto de pesquisadores cadastrados na Plataforma Lattes.

A equipe possui informações sobre a especificação do ScriptLattes — manual, funcionalidades, atores etc. —, mas não possui a documentação necessária sobre o código nem conhece sua estrutura interna, que foi criada por terceiros.

**Pergunta:** nesse cenário, qual técnica de teste é mais apropriada para derivar os casos de teste?

- Teste funcional;
- teste de mutação;
- teste estrutural.

## Slide 34 — Encerramento

**Teste de Software**  
**Técnicas de Teste: Teste Funcional**

**Professor:** Raphael Muniz  
**Contato:** raphael.muniz@ifrn.edu.br
