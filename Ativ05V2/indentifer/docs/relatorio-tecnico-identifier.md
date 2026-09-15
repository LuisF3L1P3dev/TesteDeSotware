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

| Caso | Entrada | Resultado esperado | Motivação intuitiva |
|---|---|---|---|
| CT-A1 | `abc` | Válido | Exemplo comum |
| CT-A2 | `1abc` | Inválido | Começa com dígito |
| CT-A3 | `ab#1` | Inválido | Possui caractere especial |
| CT-A4 | `abcdefg` | Inválido | Excede o tamanho máximo |
| CT-A5 | string vazia | Inválido | Não possui caracteres |

Essa lista cobre regras importantes, porém não evidencia sistematicamente todas
as classes nem os dois lados dos limites de comprimento.

## 4. Passo 1 - Identificação das classes de equivalência

| ID | Condição | Classe | Dados pertencentes à classe | Representante |
|---|---|---|---|---|
| CE-C1 | Comprimento | Válida | 1 a 6 caracteres | `abc123` |
| CE-C2 | Comprimento | Inválida | 0 caracteres | string vazia |
| CE-C3 | Comprimento | Inválida | 7 ou mais caracteres | `abcdefg` |
| CE-I1 | Caractere inicial | Válida | Letra ASCII | `Ab12` |
| CE-I2 | Caractere inicial | Inválida | Dígito ASCII | `1abc` |
| CE-I3 | Caractere inicial | Inválida | Símbolo, espaço ou outro caractere | `_abc` |
| CE-F1 | Demais caracteres | Válida | Letras e dígitos ASCII | `a1B2` |
| CE-F2 | Demais caracteres | Inválida | Símbolo, espaço ou outro caractere | `ab#1` |

Cada classe inválida representa uma maneira diferente de violar a
especificação. Assim, selecionar pelo menos um representante de cada classe
reduz redundância sem perder a cobertura das regras.

## 5. Passo 2 - Casos derivados das classes

| Caso | Entrada | Classes exercitadas | Resultado esperado |
|---|---|---|---|
| CT-E1 | `a` | CE-C1, CE-I1 | Válido |
| CT-E2 | `abc123` | CE-C1, CE-I1, CE-F1 | Válido |
| CT-E3 | string vazia | CE-C2 | Inválido |
| CT-E4 | `abcdefg` | CE-C3 | Inválido |
| CT-E5 | `Ab12` | CE-I1, CE-F1 | Válido |
| CT-E6 | `1abc` | CE-I2 | Inválido |
| CT-E7 | `_abc` | CE-I3 | Inválido |
| CT-E8 | `a1B2` | CE-F1 | Válido |
| CT-E9 | `ab#1` | CE-F2 | Inválido |
| CT-E10 | `null` | Robustez | Inválido |

Comparada à lista intuitiva, a nova lista demonstra explicitamente a origem de
cada caso e diferencia inicial inválida por dígito de inicial inválida por
símbolo.

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
especificação, enquanto os tamanhos 0, 1, 6 e 7 verificaram precisamente as
fronteiras de comprimento. A aplicação final atende às regras definidas e sua
execução automatizada foi concluída sem falhas.
