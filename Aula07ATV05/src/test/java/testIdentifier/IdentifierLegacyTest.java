package testIdentifier;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

@DisplayName("Lista histórica de casos de teste")
class IdentifierLegacyTest {

    private Identifier identifier;

    @BeforeEach
    void setUp() {
        // Setup: inicializa o sistema sob teste antes de cada caso.
        identifier = new Identifier();
    }

    @ParameterizedTest(name = "{0} - {1}")
    @MethodSource("legacyCases")
    void shouldMatchLegacyCase(
            String id, String description, String input, boolean expected) {
        // Invocation: executa o programa com a entrada do caso.
        boolean actual = identifier.validateIdentifier(input);

        // Assessment: compara o resultado obtido com o esperado.
        assertEquals(expected, actual, id + " - " + description);
    }

    private static Stream<Arguments> legacyCases() {
        return Stream.of(
                Arguments.of("H01", "comprimento mínimo", "A", true),
                Arguments.of("H02", "comprimento máximo", "a1b2c3", true),
                Arguments.of("H03", "letra seguida de letra", "Ab", true),
                Arguments.of("H04", "somente letras", "acbde", true),
                Arguments.of("H05", "letras e dígitos", "x12", true),
                Arguments.of("H06", "um espaço em branco", " ", false),
                Arguments.of("H07", "sete caracteres", "abcdefg", false),
                Arguments.of("H08", "identificador muito grande", "stringmuitogrande", false),
                Arguments.of("H09", "primeiro caractere dígito", "1abc", false),
                Arguments.of("H10", "primeiro caractere especial", "_abc", false),
                Arguments.of("H11", "primeiro caractere em branco", " a", false),
                Arguments.of("H12", "caractere especial interno", "a#b", false),
                Arguments.of("H13", "espaço interno", "a b", false),
                Arguments.of("H14", "pontuação interna", "a.b", false));
    }
}
