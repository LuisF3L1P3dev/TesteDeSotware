# Identifier

Projeto acadêmico desenvolvido em Java para implementar e testar um validador
de identificadores. A atividade aplica as técnicas de **particionamento em
classes de equivalência** e **análise de valor limite**, com testes automatizados
em JUnit 5.

## Regras de validação

Um identificador é considerado válido quando:

- possui entre 1 e 6 caracteres;
- começa com uma letra ASCII (`A-Z` ou `a-z`);
- contém somente letras e dígitos ASCII (`A-Z`, `a-z` ou `0-9`).

Entradas nulas, vazias, maiores que seis caracteres ou que contenham símbolos,
espaços e outros caracteres são rejeitadas.

| Entrada | Resultado |
|---|---|
| `a` | Válido |
| `abc123` | Válido |
| `1abc` | Inválido |
| `ab#1` | Inválido |
| `abcdefg` | Inválido |

## Tecnologias

- Java 21
- Maven Wrapper
- JUnit 5.11.4

## Estrutura do projeto

```text
.
├── docs/                  # Enunciado e relatório técnico em Markdown
├── output/pdf/            # Relatório técnico final em PDF
├── src/main/java/         # Implementação e aplicação de linha de comando
├── src/test/java/         # Testes automatizados
├── tools/                 # Geração e verificação do relatório em PDF
├── pom.xml                # Configuração do Maven
└── requirements-report.txt
```

## Pré-requisitos

- JDK 21 instalado e disponível na variável `PATH`;
- conexão com a internet na primeira execução do Maven Wrapper, caso as
  dependências ainda não estejam no cache local.

Não é necessário instalar o Maven separadamente.

## Executar os testes

No Windows, a partir desta pasta:

```powershell
.\mvnw.cmd test
```

No Linux ou macOS:

```bash
sh ./mvnw test
```

A suíte contém 17 execuções de teste que cobrem as classes válidas e inválidas,
os limites de comprimento `0`, `1`, `6` e `7`, a entrada nula e a interface de
linha de comando.

## Executar o programa

Compile o projeto:

```powershell
.\mvnw.cmd package
```

Execute a aplicação informando o identificador como argumento:

```powershell
java -cp target/classes testIdentifier.IdentifierMain abc123
```

Saída esperada:

```text
Valido
```

Para uma entrada rejeitada, a aplicação imprime `Invalido`. Quando nenhum
argumento é fornecido, ela exibe a instrução de uso.

## Relatório técnico

- [Relatório em Markdown](docs/relatorio-tecnico-identifier.md)
- [Relatório final em PDF](output/pdf/relatorio-tecnico-identifier.pdf)
- [Enunciado da atividade](<docs/Teste Funcional e Implementação do Programa _Identifier_.md>)

Para regenerar o PDF, crie um ambiente virtual Python e instale as dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-report.txt
.\.venv\Scripts\python.exe tools\generate_report.py
.\.venv\Scripts\python.exe tools\verify_report.py
```

Os arquivos temporários de compilação, ambientes virtuais e configurações de
IDE são ignorados pelo Git.
