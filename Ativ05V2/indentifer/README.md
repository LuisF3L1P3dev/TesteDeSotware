# Identifier

Implementacao em Java do validador de identificadores proposto na atividade de
teste funcional. Um identificador valido:

- possui de 1 a 6 caracteres;
- comeca com uma letra ASCII;
- contem somente letras ou digitos ASCII.

## Executar os testes

No Windows:

```powershell
.\mvnw.cmd test
```

No Linux ou macOS:

```bash
./mvnw test
```

## Executar o programa

Depois de compilar com `./mvnw package`, execute:

```bash
java -cp target/classes testIdentifier.IdentifierMain abc123
```

O relatorio tecnico final esta em `output/pdf/relatorio-tecnico-identifier.pdf`.
