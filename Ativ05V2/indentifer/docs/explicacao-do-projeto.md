# Explicação do projeto Identifier

O projeto implementa e testa um validador de identificadores em Java. A
atividade utiliza particionamento em classes de equivalência e análise de valor
limite para selecionar os casos de teste.

## Classe `Identifier`

Arquivo: [`Identifier.java`](../src/main/java/testIdentifier/Identifier.java)

O método principal é:

```java
validateIdentifier(String identifier)
```

Ele valida a entrada na seguinte ordem:

1. rejeita valores `null`;
2. rejeita textos com menos de 1 ou mais de 6 caracteres;
3. verifica se o primeiro caractere é uma letra ASCII;
4. percorre os caracteres restantes, aceitando somente letras ou dígitos ASCII;
5. retorna `true` quando todas as regras são atendidas.

As constantes `MIN_LENGTH` e `MAX_LENGTH` centralizam os limites permitidos.
Os métodos privados `isAsciiLetter` e `isAsciiLetterOrDigit` fazem a verificação
explícita dos intervalos ASCII. Dessa forma, caracteres acentuados, símbolos e
outros caracteres Unicode não são aceitos automaticamente.

## Classe `IdentifierMain`

Arquivo: [`IdentifierMain.java`](../src/main/java/testIdentifier/IdentifierMain.java)

Essa classe fornece a interface de linha de comando:

- sem argumentos, exibe a mensagem de uso;
- com um argumento, cria um `Identifier` e valida o texto;
- imprime `Valido` ou `Invalido` de acordo com o resultado.

Exemplo:

```powershell
java -cp target/classes testIdentifier.IdentifierMain abc123
```

A classe é `final` e possui construtor privado porque funciona somente como
ponto de entrada estático da aplicação.

## Testes do validador

Arquivo: [`IdentifierTest.java`](../src/test/java/testIdentifier/IdentifierTest.java)

Os testes usam JUnit 5 e verificam:

- comprimentos válidos e inválidos;
- limites de tamanho 0, 1, 6 e 7;
- inicial com letra;
- inicial com dígito ou símbolo;
- conteúdo formado por letras e números;
- caracteres especiais;
- entrada `null`.

Os testes parametrizados (`@ParameterizedTest`) permitem executar o mesmo
comportamento para vários valores. Cada teste segue a estrutura solicitada na
atividade:

- **Setup:** preparação do objeto ou do ambiente;
- **Invocation:** chamada do método sob teste;
- **Assessment:** comparação do resultado com `assertEquals`.

## Testes da interface de linha de comando

Arquivo: [`IdentifierMainTest.java`](../src/test/java/testIdentifier/IdentifierMainTest.java)

Essa classe captura a saída padrão para verificar:

- a mensagem exibida quando não há argumento;
- a saída `Valido` para uma entrada aceita;
- a saída `Invalido` para uma entrada rejeitada.

Ao todo, a suíte contém 17 execuções: 14 relacionadas ao validador e 3 à
interface de linha de comando.

## Configuração Maven

Arquivo: [`pom.xml`](../pom.xml)

O Maven configura:

- Java 21;
- JUnit 5.11.4;
- Maven Compiler Plugin;
- Maven Surefire Plugin para execução dos testes.

O comando principal é:

```powershell
.\mvnw.cmd test
```

## Scripts Python

Os scripts da pasta [`tools`](../tools/) apoiam a documentação da atividade:

- `generate_report.py` gera o relatório técnico em PDF usando ReportLab;
- `verify_report.py` verifica quantidade de páginas, conteúdo obrigatório,
  metadados e renderização do PDF.

## Fluxo geral

```text
Entrada do usuário
        |
        v
IdentifierMain
        |
        v
Identifier.validateIdentifier
        |
        +--> regras de tamanho
        +--> primeiro caractere: letra ASCII
        +--> demais caracteres: letras ou dígitos ASCII
        |
        v
Resultado: Valido ou Invalido
```

A lógica de validação está concentrada em `Identifier`. As outras partes do
projeto fornecem a execução pela linha de comando, a cobertura automatizada e a
geração do relatório técnico.
