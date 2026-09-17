# Relatório Técnico - Teste Funcional do Programa Identifier

## 1. Objetivo

Implementar e validar o programa `Identifier` por meio do critério funcional de
particionamento em classes de equivalência, complementado pela análise de valor
limite. O programa deve determinar se uma string representa um identificador
válido.

## 2. Especificação adotada

Um identificador válido deve:

1. possuir de 1 a 6 caracteres;
2. começar com uma letra ASCII (`A-Z` ou `a-z`);
3. conter, depois do primeiro caractere, somente letras ou dígitos ASCII
   (`A-Z`, `a-z` ou `0-9`).

Uma entrada nula não pertence ao domínio textual da especificação, mas foi
incluída como teste defensivo e deve ser rejeitada.

## 3. Lista inicial reconstruída

A lista elaborada na aula anterior não foi encontrada nos arquivos fornecidos.
Para permitir a comparação pedida, foi reconstruída uma lista intuitiva, sem a
aplicação formal de uma técnica de teste.

| Caso | Entrada | Tamanho | Resultado esperado | Motivação intuitiva |
|---|---|---:|---|---|
| CT-A1 | string vazia | 0 | Inválido | Imediatamente abaixo do tamanho mínimo |
| CT-A2 | `a` | 1 | Válido | Tamanho mínimo permitido |
| CT-A3 | `abc123` | 6 | Válido | Tamanho máximo permitido |
| CT-A4 | `abcdefg` | 7 | Inválido | Imediatamente acima do tamanho máximo |
| CT-A5 | `1abc` | 4 | Inválido | Começa com dígito |
| CT-A6 | `ab#1` | 4 | Inválido | Possui caractere especial |

Essa lista inicial evidencia os dois lados dos limites de comprimento ao
considerar os tamanhos 0, 1, 6 e 7. Entretanto, por ter sido construída de
forma intuitiva, ela ainda não identifica formalmente as classes de
equivalência exercitadas por cada entrada.

## 4. Passo 1 - Identificação das classes de equivalência

Seguindo a organização dos slides 28 a 31, as variáveis de entrada foram
representadas por `t` (comprimento), `i` (caractere inicial) e `c` (caracteres
contidos). Cada regra origina uma classe válida e uma ou mais classes inválidas.

| Variável de entrada | Classes de equivalência válidas | Classes de equivalência inválidas |
|---|---|---|
| Comprimento (`t`) | **Classe 1:** `1 ≤ t ≤ 6` | **Classe 2:** `t < 1`; **Classe 3:** `t > 6` |
| Iniciar com uma letra (`i`) | **Classe 4:** inicia com letra ASCII | **Classe 5:** não inicia com letra ASCII |
| Conter letras ou dígitos (`c`) | **Classe 6:** contém somente letras ou dígitos ASCII | **Classe 7:** contém algum caractere diferente de letra ou dígito ASCII |

Os testes automatizados utilizam os seguintes representantes:

| Classe | Tipo | Representantes utilizados |
|---:|---|---|
| 1 | Válida | `a`, `abc123`, `Ab12`, `a1B2`, `ab#1`, `1abc`, `_abc` |
| 2 | Inválida | string vazia |
| 3 | Inválida | `abcdefg` |
| 4 | Válida | `a`, `abc123`, `Ab12`, `a1B2`, `ab#1`, `abcdefg` |
| 5 | Inválida | `1abc`, `_abc` |
| 6 | Válida | `a`, `abc123`, `Ab12`, `a1B2`, `1abc`, `abcdefg` |
| 7 | Inválida | `_abc`, `ab#1` |

Uma mesma entrada pode pertencer simultaneamente a classes associadas a
variáveis diferentes. Por exemplo, `1abc` possui comprimento válido (classe 1),
não começa com uma letra (classe 5) e contém apenas letras ou dígitos (classe
6). O resultado final é inválido porque nem todas as regras foram satisfeitas.

## 5. Passo 2 - Derivação dos casos de teste

### 5.1 Casos para o critério de comprimento

Primeiro, foram selecionadas entradas nos limites inferior e superior da faixa
permitida. Essa seleção cobre as classes 1, 2 e 3.

| Caso | Entrada | Tamanho | Classe de `t` | Resultado esperado |
|---|---|---:|---:|---|
| CT-E1 | string vazia | 0 | 2 | Inválido |
| CT-E2 | `a` | 1 | 1 | Válido |
| CT-E3 | `abc123` | 6 | 1 | Válido |
| CT-E4 | `abcdefg` | 7 | 3 | Inválido |

### 5.2 Cobertura dos critérios de início e conteúdo

Depois da seleção por comprimento, os mesmos dados foram avaliados nas três
variáveis. O símbolo `—` indica que o critério não pode ser avaliado por não
existir caractere na entrada.

| Entrada | Comprimento (`t`) | Início (`i`) | Conteúdo (`c`) | Resultado esperado |
|---|---:|---:|---:|---|
| string vazia | 2 | — | — | Inválido |
| `a` | 1 | 4 | 6 | Válido |
| `abc123` | 1 | 4 | 6 | Válido |
| `abcdefg` | 3 | 4 | 6 | Inválido |

Até esse ponto, foram exercitadas as classes 1, 2, 3, 4 e 6. Ainda faltavam
representantes específicos para as classes inválidas 5 e 7.

### 5.3 Classes ainda não contempladas

Foram acrescentadas entradas que não começam com letra e que contêm caracteres
fora do conjunto permitido.

| Entrada | Comprimento (`t`) | Início (`i`) | Conteúdo (`c`) | Resultado esperado |
|---|---:|---:|---:|---|
| `1abc` | 1 | 5 | 6 | Inválido |
| `_abc` | 1 | 5 | 7 | Inválido |
| `ab#1` | 1 | 4 | 7 | Inválido |

Com essas inclusões, todas as classes de equivalência de 1 a 7 passam a ter ao
menos um representante na suíte automatizada.

### 5.4 Suíte consolidada por classes

| Caso | Entrada | Classes exercitadas | Resultado esperado |
|---|---|---|---|
| CT-E1 | `a` | 1, 4 e 6 | Válido |
| CT-E2 | `abc123` | 1, 4 e 6 | Válido |
| CT-E3 | string vazia | 2 | Inválido |
| CT-E4 | `abcdefg` | 3, 4 e 6 | Inválido |
| CT-E5 | `Ab12` | 1, 4 e 6 | Válido |
| CT-E6 | `1abc` | 1, 5 e 6 | Inválido |
| CT-E7 | `_abc` | 1, 5 e 7 | Inválido |
| CT-E8 | `a1B2` | 1, 4 e 6 | Válido |
| CT-E9 | `ab#1` | 1, 4 e 7 | Inválido |
| CT-R1 | `null` | Robustez | Inválido |

A entrada `null` não pertence ao domínio textual das classes 1 a 7. Ela foi
mantida como um teste defensivo de robustez e não é contabilizada na cobertura
do particionamento.

## 6. Análise de valor limite

| Tamanho | Entrada | Posição em relação ao limite | Resultado esperado |
|---:|---|---|---|
| 0 | string vazia | Imediatamente abaixo do mínimo | Inválido |
| 1 | `a` | Mínimo válido | Válido |
| 6 | `abc123` | Máximo válido | Válido |
| 7 | `abcdefg` | Imediatamente acima do máximo | Inválido |

O particionamento poderia usar somente um valor qualquer entre 1 e 6 para a
classe válida. A análise de valor limite complementa o critério ao verificar os
pontos em que erros de comparação, como usar `<` no lugar de `<=`, são mais
prováveis.

## 7. Automação dos testes

<img width="868" height="592" alt="image" src="https://github.com/user-attachments/assets/5d535c65-a874-423c-9e1a-a461613e074c" />

Os testes foram implementados com JUnit 5. Em cada método estão identificadas as
três partes solicitadas:

- **Setup:** criação do validador ou captura da saída padrão;
- **Invocation:** chamada de `validateIdentifier` ou de `IdentifierMain.main`;
- **Assessment:** comparação do resultado com o valor esperado por meio de
  `assertEquals`.

Foram implementadas 14 execuções para o validador, incluindo representantes das
classes, valores-limite e entrada nula, além de 3 execuções para a interface de
linha de comando.

## 8. Resultado da execução

Comando utilizado no Windows:

```powershell
.\mvnw.cmd test
```

Resultado obtido em 15/09/2026:

| Métrica | Resultado |
|---|---:|
| Testes executados | 17 |
| Falhas | 0 |
| Erros | 0 |
| Ignorados | 0 |
| Estado da construção | BUILD SUCCESS |

## 9. Conclusão

Todos os representantes selecionados produziram os resultados esperados. O uso
das classes de equivalência tornou a seleção rastreável em relação à
especificação e garantiu a cobertura das sete classes definidas para
comprimento, caractere inicial e caracteres contidos. Os tamanhos 0, 1, 6 e 7
verificaram precisamente as fronteiras de comprimento. A entrada nula foi
avaliada separadamente como condição de robustez. A aplicação final atende às
regras definidas e sua execução automatizada foi concluída sem falhas.
