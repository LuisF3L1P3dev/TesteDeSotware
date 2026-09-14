# Documentação de Teste de Software (IEEE 829)
## Projeto: Programa Identifier

Esta documentação foi elaborada em conformidade com as diretrizes da **Norma IEEE 829**, adaptando ao contexto do **Programa Identifier**.

1. **Plano de Teste** (Planejamento e Estratégia)
2. **Casos de Teste** (Especificação e Resultados)
3. **Relatório de Incidente** (Rastreamento de Falhas)
4. **Relatório de Resumo de Teste** (Métricas e Avaliação de Qualidade)

---

## 1. Plano de Teste

### **Tabela 1.1 - Planejamento Geral do Teste**

| **Item do Plano de Teste** | **Detalhamento / Especificação Técnica** |
| :--- | :--- |
| **Nome do Projeto** | Programa Identifier |
| **Pessoas Envolvidas & Responsabilidades** | • **Usuário1 (Analista de Testes):** Responsável pelo planejamento, elaboração, execução dos testes e relato de incidentes.<br>• **Usuário2 (Desenvolvedor):** Responsável pelo desenvolvimento do programa, execução de testes de unidade e correção de bugs. |
| **Módulos / Funcionalidades do Escopo** | • **Módulo de Validação:** Verificação das strings de entrada para determinar se representam identificadores alfanuméricos válidos.<br>• **Módulo de Console:** Captura de argumentos de linha de comando e exibição da saída ("Válido" ou "Inválido"). |
| **Cenário Geral do Sistema (O que será testado)** | Validação de string enviada por parâmetro via linha de comando (`IdentifierMain <string>`) sob três regras cumulativas:<br>1. **Início obrigatório:** Deve começar obrigatoriamente por uma letra (maiúscula ou minúscula).<br>2. **Composição de caracteres:** Deve conter exclusivamente letras (a-z, A-Z) ou dígitos (0-9). Não são permitidos caracteres especiais, pontuação ou espaços.<br>3. **Comprimento permitido:** Deve conter no mínimo 1 caractere e no máximo 6 caracteres. |
| **Estratégias de Teste (Como será testado)** | • **Abordagem:** Teste Funcional de Caixa-Preta.<br>• **Técnicas de Projeto de Teste:** Particionamento por Classes de Equivalência (dados válidos e inválidos) e Análise de Valores Limite nas fronteiras de tamanho (tamanhos de 0, 1, 2, 5, 6 e 7 caracteres). |
| **Cronograma de Atividades** | • **08/09/2026:** Inicio do projeto <br>• **09/09/2026:** Inicio do teste<br>• **10/09/2026:** Execução dos testes e abertura de Incidentes<br>• **11/09/2026:** Fim dos testes<br>• **12/09/2026:** Encerramento do projeto|
| **Local dos Testes e Recursos** | Execução descentralizada executada diretamente nas máquinas locais dos analistas de teste e desenvolvedores envolvidos (locais aleatórios). |
| **Critério para Considerar o Teste Finalizado** | O ciclo de testes será finalizado quando todos os casos de teste planejados forem executados com êxito, obtendo resultado correspondente ao esperado e tendo a coluna "Resultado do Teste" marcada como "Executado com sucesso". Quaisquer incidentes impeditivos devem ser devidamente corrigidos pelo desenvolvedor e retestados com sucesso. |
| **Observações e Comunicação** | O relatório de incidente atualizado será distribuído para todos os desenvolvedores por e-mail institucional assim que alguma falha for cadastrada ou alterada. |

### **Tabela 1.2 - Definição das Classes de Equivalência de Entrada**

| **Atributo de Entrada** | **Classe de Equivalência Válida** | **Classes de Equivalência Inválidas** |
| :--- | :--- | :--- |
| **Primeiro caractere** | Letra (a-z, A-Z) | • Dígito (0-9)<br>• Caractere especial (ex: `#`, `_`, `@`, etc.)<br>• Espaço em branco |
| **Demais caracteres** | Apenas letras ou dígitos | • Contém caractere especial/pontuação subsequente<br>• Contém espaço em branco subsequente |
| **Comprimento (L)** | 1 <= L <= 6 | • L = 0 (String vazia)<br>• L > 6 (Ultrapassa limite de 6 caracteres) |
| **Parâmetros no Console** | Um único argumento string | • Nenhum argumento passado<br>• Múltiplos argumentos separados por espaço |

---

## 2. Casos de Teste

### **Tabela 2.1 - Matriz Geral de Casos de Teste**

| **ID** | **Módulo** | **Descrição** | **Classe de Equivalência / Entrada** | **Resultado Esperado** | **Resultado do Desenvolvedor** | **Resultado do Teste** |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Validação | Validar comprimento mínimo (limite inferior) | Classe Válida (L=1). Entrada: `"A"` | Output: \"Válido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **2** | Validação | Validar comprimento máximo (limite superior) | Classe Válida (L=6). Entrada: `"a1b2c3"` | Output: \"Válido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **3** | Validação | Validar comprimento curto (letra + letra) | Classe Válida (L=2). Entrada: `"Ab"` | Output: \"Válido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **4** | Validação | Validar comprimento médio (só letras) | Classe Válida (L=5). Entrada: `"acbde"` | Output: \"Válido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **5** | Validação | Validar caracteres mistos típicos | Classe Válida (L=3). Entrada: `"x12"` | Output: \"Válido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **6** | Validação | Erro: Identificador vazio (limite inferior - 1) | Classe Inválida (L=0). Entrada: `" "` | Output: \"Inválido\" | Executado com sucesso | **Erro de Execução (Crash):** Sistema travou no console. (10/09) |
| **7** | Validação | Erro: Comprimento maior que máximo (limite superior + 1) | Classe Inválida (L=7). Entrada: `"abcdefg"` | Output: \"Inválido\" | Executado com sucesso | **Erro de Aceitação:** Retornou \"Válido\" indevidamente. (10/09) |
| **8** | Validação | Erro: Identificador extremamente grande | Classe Inválida (L=17). Entrada: `"stringmuitogrande"` | Output: \"Inválido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **9** | Validação | Erro: Iniciar com dígito | Classe Inválida (Primeiro dígito). Entrada: `"1abc"` | Output: \"Inválido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **10** | Validação | Erro: Iniciar com caractere especial | Classe Inválida (Primeiro especial). Entrada: `"_abc"` | Output: \"Inválido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **11** | Validação | Erro: Iniciar com espaço em branco | Classe Inválida (Primeiro espaço). Entrada: `" a"` | Output: \"Inválido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **12** | Validação | Erro: Contém caractere especial subsequente | Classe Inválida (Especial interno). Entrada: `"a#b"` | Output: \"Inválido\" | Executado com sucesso | **Erro de Aceitação:** Retornou \"Válido\" indevidamente. (10/09) |
| **13** | Validação | Erro: Contém espaço em branco subsequente | Classe Inválida (Espaço interno). Entrada: `"a b"` | Output: \"Inválido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **14** | Validação | Erro: Contém caractere de pontuação subsequente | Classe Inválida (Ponto interno). Entrada: `"a.b"` | Output: \"Inválido\" | Executado com sucesso | Executado com sucesso (10/09) |
| **15** | Console | Erro: Chamar programa sem parâmetros | Classe Inválida (Parâmetro ausente). Entrada: (Nulo) | Output: Mensagem de Uso do Programa | Executado com sucesso | Executado com sucesso (10/09) |
| **16** | Console | Erro: Chamar programa com múltiplos parâmetros | Classe Inválida (Multi-parâmetros). Entrada: `"arg1"` `"arg2"` | Output: Erro de Entrada ou ignora extra | Executado com sucesso | Executado com sucesso (10/09) |

---

## 3. Relatório de Incidente

O relatório de incidentes compila todos os eventos em que os resultados observados divergiram do esperado, registrando o fluxo de correção técnica conduzido pelas pessoas envolvidas.

**Nome do Projeto:** Programa Identifier  
**Responsável por Enviar Atualizações:** Usuário1 (por e-mail institucional)

### **Tabela 3.1 - Registro de Incidentes de Teste**

| **ID do Caso** | **Status** | **Responsável pela Correção** | **Prioridade de Correção** | **Descrição do Erro** | **Data e Nome de Quem Corrigiu** |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **6** | **Aberto** | Usuário2 | **Baixa** | **Erro de Execução (Crash):** Quando o programa é executado passando uma string vazia `" "` como parâmetro, ele sofre uma quebra técnica de ponteiro/memória (Crash) no console em vez de retornar "Inválido". | *(Aguardando correção pelo desenvolvedor)* |
| **7** | **Pronto para testar novamente** | Usuário2 | **Alta** | **Falha de Valor Limite Máximo:** O programa processou a entrada `"abcdefg"` (7 caracteres) e emitiu o output "Válido". O comportamento correto é emitir "Inválido" por ultrapassar o limite máximo de 6 caracteres. | 11/09/2026 – Usuário2 |
| **12** | **Aberto** | Usuário2 | **Alta** | **Falha de Caractere Inválido Aceito:** O programa emitiu o output "Válido" para a entrada `"a#b"`. O correto é "Inválido", pois o caractere especial `#` viola a regra de conter exclusivamente letras ou dígitos. | *(Aguardando correção pelo desenvolvedor)* |

---

## 4. Relatório de Resumo de Teste

Este relatório apresenta o panorama consolidado dos resultados obtidos durante o ciclo de testes concluído em primeira rodada, gerando transparência quanto à qualidade atual do produto.

### **Tabela 4.1 - Informações Básicas de Controle**

| **Métrica / Atributo** | **Detalhamento do Ciclo de Teste** |
| :--- | :--- |
| **Nome do Projeto** | Programa Identifier |
| **Data Início Teste** | 09/09/2026 |
| **Data Fim Teste** | 11/09/2026 |
| **Descrição Geral** | A elaboração prévia dos casos de teste facilitou a detecção e a correção rápida dos erros. O relatório de incidente de teste demonstrou de forma clara a correção do programador e o momento correto para o retorno à equipe de teste para reteste. |
| **Pessoas Envolvidas** | Usuário1 (Analista de Testes) e Usuário2 (Desenvolvedor) |

### **Tabela 4.2 - Métricas de Execução e Qualidade**

| **Métrica do Teste** | **Valor Quantitativo** | **Percentual (%)** |
| :--- | :---: | :---: |
| **Casos de Testes Criados Antes do Teste** | 16 | - |
| **Casos de Testes Criados Durante o Teste** | 0 | - |
| **Casos de Testes Executados** | 16 | **100,00%** |
| **Casos de Testes Executados com Sucesso (Pass Rate)** | 13 | **81,25%** |
| **Casos de Testes com Erros Detectados (Defect Rate)** | 3 | **18,75%** |
| **Casos de Testes Enviados para Correção** | 3 | **100,00%** |
| **Casos de Testes Corrigidos pelo Desenvolvedor** | 1 | **33,33%** |