package testIdentifier;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

import java.util.stream.Stream;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.api.Test;

@DisplayName("Particionamento em classes de equivalência e valores limite")
class IdentifierEquivalenceTest {

    private Identifier identifier;

    @BeforeEach
    void setUp() {
        // Setup: inicializa o sistema sob teste antes de cada caso.
        identifier = new Identifier();
    }

    @ParameterizedTest(name = "{0} - {1}")
    @MethodSource("equivalenceAndBoundaryCases")
    void shouldMatchEquivalenceClass(
            String id, String equivalenceClass, String input, boolean expected) {
        // Invocation: executa o programa com um representante da classe.
        boolean actual = identifier.validateIdentifier(input);

        // Assessment: compara o resultado obtido com o esperado.
        assertEquals(expected, actual, id + " - " + equivalenceClass);
    }

    @Test
    @DisplayName("ROB01 - entrada nula é rejeitada sem lançar exceção")
    void shouldRejectNull() {
        // Setup: a instância é criada em setUp e a entrada é nula.
        String input = null;

        // Invocation: executa o programa com a entrada técnica.
        boolean actual = identifier.validateIdentifier(input);

        // Assessment: uma entrada nula deve ser inválida.
        assertFalse(actual);
    }

    private static Stream<Arguments> equivalenceAndBoundaryCases() {
        return Stream.of(
                Arguments.of("CE01", "todas as classes válidas", "abc", true),
                Arguments.of("CE02", "comprimento igual a zero", "", false),
                Arguments.of("CE03", "comprimento maior que seis", "abcdefg", false),
                Arguments.of("CE04", "primeiro caractere é dígito", "1abc", false),
                Arguments.of("CE05", "primeiro caractere é especial", "_abc", false),
                Arguments.of("CE06", "primeiro caractere é espaço", " abc", false),
                Arguments.of("CE07", "caractere especial interno", "a#b", false),
                Arguments.of("CE08", "espaço interno", "a b", false),
                Arguments.of("AVL01", "limite válido inferior: comprimento 1", "A", true),
                Arguments.of("AVL02", "limite válido superior: comprimento 6", "a1b2c3", true));
    }
}
