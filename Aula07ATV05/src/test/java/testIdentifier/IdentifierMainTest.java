package testIdentifier;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Interface de linha de comando")
class IdentifierMainTest {

    private PrintStream originalOutput;
    private ByteArrayOutputStream capturedOutput;

    @BeforeEach
    void setUp() {
        // Setup: redireciona a saída do console para uma área verificável.
        originalOutput = System.out;
        capturedOutput = new ByteArrayOutputStream();
        System.setOut(new PrintStream(capturedOutput, true, StandardCharsets.UTF_8));
    }

    @AfterEach
    void tearDown() {
        System.setOut(originalOutput);
    }

    @Test
    @DisplayName("CLI01 - imprime Válido para uma entrada válida")
    void shouldPrintValid() {
        // Invocation
        IdentifierMain.main(new String[] {"string"});

        // Assessment
        assertEquals("Válido", consoleOutput());
    }

    @Test
    @DisplayName("CLI02 - imprime Inválido para uma entrada inválida")
    void shouldPrintInvalid() {
        // Invocation
        IdentifierMain.main(new String[] {"stringmuitogrande"});

        // Assessment
        assertEquals("Inválido", consoleOutput());
    }

    @Test
    @DisplayName("H15 - exibe uso quando não há argumentos")
    void shouldPrintUsageWithoutArguments() {
        // Invocation
        IdentifierMain.main(new String[0]);

        // Assessment
        assertEquals("Uso: IdentifierMain <string>", consoleOutput());
    }

    @Test
    @DisplayName("H16 - exibe uso quando há múltiplos argumentos")
    void shouldPrintUsageWithMultipleArguments() {
        // Invocation
        IdentifierMain.main(new String[] {"arg1", "arg2"});

        // Assessment
        assertEquals("Uso: IdentifierMain <string>", consoleOutput());
    }

    private String consoleOutput() {
        return capturedOutput.toString(StandardCharsets.UTF_8).trim();
    }
}
