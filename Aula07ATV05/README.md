# Programa Identifier

Implementação em Java 21 do programa que valida identificadores e suíte de testes
funcionais com JUnit 5.

## Regras

Um identificador válido:

- possui entre 1 e 6 caracteres;
- começa com uma letra ASCII (`A-Z` ou `a-z`);
- contém somente letras ASCII ou dígitos (`0-9`).

## Executar os testes

No PowerShell, a partir desta pasta:

```powershell
.\mvnw.cmd clean test
```

O Maven Wrapper baixa automaticamente a versão configurada do Maven na primeira
execução. Os relatórios XML dos testes são gravados em `target/surefire-reports`.

## Executar o programa

```powershell
.\mvnw.cmd package
java -cp target/classes testIdentifier.IdentifierMain string
```

Saída esperada: `Válido`.

## Relatório técnico

- Fonte editável: `relatorio-tecnico-identifier.md`.
- PDF final: `../output/pdf/relatorio-tecnico-identifier.pdf`.

Para regenerar o PDF depois de instalar as dependências de
`requirements-report.txt`:

```powershell
python tools/generate_report.py
```
