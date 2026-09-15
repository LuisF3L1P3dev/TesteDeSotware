package testIdentifier;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class IdentifierMainTest {

    private PrintStream standardOutput;
    private ByteArrayOutputStream capturedOutput;

    @BeforeEach
    void setup() {
        // Setup: redireciona a saida padrao para permitir a avaliacao.
        standardOutput = System.out;
        capturedOutput = new ByteArrayOutputStream();
        System.setOut(new PrintStream(capturedOutput, true, StandardCharsets.UTF_8));
    }

    @AfterEach
    void restoreStandardOutput() {
        System.setOut(standardOutput);
    }

    @Test
    void deveExibirInstrucaoQuandoNaoHaArgumento() {
        // Invocation
        IdentifierMain.main(new String[0]);

        // Assessment
        assertEquals("Uso: IdentifierMain <string>" + System.lineSeparator(), output());
    }

    @Test
    void deveExibirValidoParaIdentificadorAceito() {
        // Invocation
        IdentifierMain.main(new String[] {"abc123"});

        // Assessment
        assertEquals("Valido" + System.lineSeparator(), output());
    }

    @Test
    void deveExibirInvalidoParaIdentificadorRejeitado() {
        // Invocation
        IdentifierMain.main(new String[] {"1abc"});

        // Assessment
        assertEquals("Invalido" + System.lineSeparator(), output());
    }

    private String output() {
        return capturedOutput.toString(StandardCharsets.UTF_8);
    }
}
