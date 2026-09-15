package testIdentifier;

/**
 * Ponto de entrada de linha de comando do programa Identifier.
 */
public final class IdentifierMain {

    private IdentifierMain() {
        // Classe utilitaria.
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Uso: IdentifierMain <string>");
            return;
        }

        Identifier identifier = new Identifier();
        System.out.println(identifier.validateIdentifier(args[0]) ? "Valido" : "Invalido");
    }
}
