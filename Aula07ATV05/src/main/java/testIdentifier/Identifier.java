package testIdentifier;

/**
 * Valida identificadores de acordo com a especificação da atividade.
 */
public class Identifier {

    public static final int MIN_LENGTH = 1;
    public static final int MAX_LENGTH = 6;

    /**
     * Um identificador válido possui de 1 a 6 caracteres, começa com uma letra
     * ASCII e contém somente letras ASCII ou dígitos ASCII.
     *
     * @param identifier texto a validar
     * @return {@code true} apenas quando todas as regras forem satisfeitas
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
