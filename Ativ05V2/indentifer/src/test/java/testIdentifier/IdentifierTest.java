package testIdentifier;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.NullSource;
import org.junit.jupiter.params.provider.ValueSource;

class IdentifierTest {

    private Identifier identifier;

    @BeforeEach
    void setup() {
        // Setup: cria uma instancia limpa do validador antes de cada teste.
        identifier = new Identifier();
    }

    @ParameterizedTest(name = "comprimento valido: [{0}]")
    @ValueSource(strings = {"a", "abc123"})
    void deveAceitarComprimentoValido(String entrada) {
        // Invocation: executa o software com o representante selecionado.
        boolean resultado = identifier.validateIdentifier(entrada);

        // Assessment: compara o resultado obtido com o resultado esperado.
        assertEquals(true, resultado);
    }

    @ParameterizedTest(name = "comprimento invalido: [{0}]")
    @ValueSource(strings = {"", "abcdefg"})
    void deveRejeitarComprimentoInvalido(String entrada) {
        // Invocation
        boolean resultado = identifier.validateIdentifier(entrada);

        // Assessment
        assertEquals(false, resultado);
    }

    @Test
    void deveAceitarLetraComoCaractereInicial() {
        // Invocation
        boolean resultado = identifier.validateIdentifier("Ab12");

        // Assessment
        assertEquals(true, resultado);
    }

    @ParameterizedTest(name = "caractere inicial invalido: [{0}]")
    @ValueSource(strings = {"1abc", "_abc"})
    void deveRejeitarCaractereInicialInvalido(String entrada) {
        // Invocation
        boolean resultado = identifier.validateIdentifier(entrada);

        // Assessment
        assertEquals(false, resultado);
    }

    @Test
    void deveAceitarSomenteLetrasEDigitosNoConteudo() {
        // Invocation
        boolean resultado = identifier.validateIdentifier("a1B2");

        // Assessment
        assertEquals(true, resultado);
    }

    @Test
    void deveRejeitarCaractereEspecialNoConteudo() {
        // Invocation
        boolean resultado = identifier.validateIdentifier("ab#1");

        // Assessment
        assertEquals(false, resultado);
    }

    @ParameterizedTest(name = "valor-limite [{0}] deve resultar em {1}")
    @CsvSource(delimiter = '|', value = {
            "''      | false",
            "a       | true",
            "abc123  | true",
            "abcdefg | false"
    })
    void deveValidarValoresLimite(String entrada, boolean esperado) {
        // Invocation
        boolean resultado = identifier.validateIdentifier(entrada);

        // Assessment
        assertEquals(esperado, resultado);
    }

    @ParameterizedTest
    @NullSource
    void deveRejeitarEntradaNula(String entrada) {
        // Invocation
        boolean resultado = identifier.validateIdentifier(entrada);

        // Assessment
        assertEquals(false, resultado);
    }
}
