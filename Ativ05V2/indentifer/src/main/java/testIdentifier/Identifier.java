package testIdentifier;

/**
 * Valida identificadores de acordo com a especificacao da atividade.
 *
 * <p>Um identificador valido possui de um a seis caracteres, comeca com uma
 * letra ASCII e contem somente letras ou digitos ASCII.</p>
 */
public class Identifier {

    private static final int MIN_LENGTH = 1;
    private static final int MAX_LENGTH = 6;

    /**
     * Informa se o texto recebido representa um identificador valido.
     *
     * @param identifier texto a validar
     * @return {@code true} quando todas as regras sao atendidas; caso
     *         contrario, {@code false}
     */
    public boolean validateIdentifier(String identifier) {
        if (identifier == null
                || identifier.length() < MIN_LENGTH
                || identifier.length() > MAX_LENGTH) {
            return false;
        }

        if (!isAsciiLetter(identifier.charAt(0))) {
            return false;
        }

        for (int index = 1; index < identifier.length(); index++) {
            if (!isAsciiLetterOrDigit(identifier.charAt(index))) {
                return false;
            }
        }

        return true;
    }

    private boolean isAsciiLetter(char character) {
        return (character >= 'A' && character <= 'Z')
                || (character >= 'a' && character <= 'z');
    }

    private boolean isAsciiLetterOrDigit(char character) {
        return isAsciiLetter(character)
                || (character >= '0' && character <= '9');
    }
}
