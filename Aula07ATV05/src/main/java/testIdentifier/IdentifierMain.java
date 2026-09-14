package testIdentifier;

/**
 * Interface de linha de comando do programa Identifier.
 */
public final class IdentifierMain {

    private static final String USAGE = "Uso: IdentifierMain <string>";

    private IdentifierMain() {
        // Impede instanciação de uma classe utilitária.
    }

    public static void main(String[] args) {
        if (args == null || args.length != 1) {
            System.out.println(USAGE);
            return;
        }

        Identifier identifier = new Identifier();
        String output = identifier.validateIdentifier(args[0]) ? "Válido" : "Inválido";
        System.out.println(output);
    }
}
