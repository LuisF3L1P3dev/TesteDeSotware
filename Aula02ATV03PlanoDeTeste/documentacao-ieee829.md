# Documentação de teste baseado na Norma IEEE 829 – estudo de caso: “sistema de apoio a tomada de decisão”

**Autora:** Mariana Zanuzzio Blanco  
**Afiliação:** Departamento de Computação – Universidade Federal de São Carlos (UFSCar)  
**ISSN:** 2316-2872 | T.I.S. São Carlos, v. 1, n. 1, p. 91-97, jul. 2012 © Tecnologias, Infraestrutura e Software  
**Contato:** mzblanco2005@yahoo.com.br  

---

## Resumo
O processo de teste é crucial para obter um software de boa qualidade com a menor quantidade de erros possíveis. Para isso, documentos são desenvolvidos para implementar os testes de unidade, integração e sistema permitindo a organização e a da correção dos erros antes da entrega ao cliente. Esse estudo descreve uma documentação de teste baseada na norma IEEE 829 e a sua aplicabilidade no estudo de caso Sistema de Apoio a Tomada de Decisão (SAD).

**Palavras-chave:** Qualidade de software, testes, documentação de teste.

---

## Abstract
The test process is crucial for a good software quality with the fewest possible errors. Therefore, it is necessary to plan the test integration tests and allowing the organization and the errors corrected prior to customer delivery. This study to describe a test documentation based on the IEEE 829 and its applicability to a case study Support System for decision making.

**Keywords:** Software quality, tests, test documentation.

---

## I. Introdução
Como é notório, a tecnologia avança desde a revolução industrial à velocidade crescente. Novas tecnologias apresentam-se a todo momento. Estar atento a essas transformações e responder às exigências econômicas com custos mais baixos é indispensável.

Entretanto, muitos softwares, apesar de submetidos a um longo desenvolvimento, apresentam erros ao se tornarem operacionais. Para minimizá-los, a atividade de teste é introduzida durante todo o desenvolvimento de software. Normalmente, a implementação do teste ocorre apenas no final do desenvolvimento, gerando uma atividade de teste insatisfatória. Portanto, deve ser feito o planejamento e a geração de casos de teste durante todo o desenvolvimento do sistema.

Este trabalho tem como objetivo descrever um modelo de documentação de teste baseado na norma IEEE 829 visando auxiliar o desenvolvedor de software a organizar e implementar os métodos de testes.

---

## II. Definição de Teste
Segundo Crespo et al. (2004): *"Teste de software é o processo de executar o software de uma maneira controlada com o objetivo de avaliar se o mesmo se comporta conforme o esperado."*

Infelizmente não é possível testar todas as entradas de dados e suas centenas ou milhares de combinações possíveis (Myers, 2004). Além disso, os custos para descobrir e corrigir erros aumentam exponencialmente ao longo das fases do projeto.

Existem basicamente duas técnicas:
- **Caixa-branca (estrutural):** Gera casos de teste baseados na estrutura interna do programa e suas condicionais.
- **Caixa-preta (funcional):** Analisa se todos os requisitos solicitados foram aplicados no software e estão funcionando.

Os testes dividem-se em teste de unidade, teste de integração e teste de sistema.

---

## III. Documentação de Teste (Norma IEEE 829-1998)
A norma IEEE 829-1998 descreve oito documentos para as atividades de teste:
1. Plano de Teste
2. Especificação do Projeto de Teste
3. Especificação dos Casos de Teste
4. Especificação dos Procedimentos de Teste
5. Relatório de Transmissão de Item de Teste
6. Diário de Teste
7. Relatório de Incidente de Teste
8. Relatório-Resumo de Teste

---

## IV. Estudo de Caso: Sistema de Apoio à Tomada de Decisão (SAD)
O SAD foi desenvolvido usando o framework JSF (JavaServer Faces) e JPA no padrão MVC (Model-View-Controller) com banco de dados MySQL e servidor GlassFish V3. O objetivo do sistema é classificar e agrupar os dados da empresa para traçar o perfil exato da carteira de clientes.

---

## V. Aplicação da Norma IEEE 829 no Estudo de Caso

### A. Plano de Teste
Contém: nome do projeto, funcionalidades a testar, cronograma, responsáveis, local e critérios de aceitação.

### B. Casos de Testes (Tabela 2)

| ID | Módulo | Descrição | Roteiro | Resultado Esperado | Resultado do Desenvolvedor | Resultado do Teste |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Usuário | Dados cadastrais dos usuários | 1) Escolher opção Listar Usuário<br>2) Clicar em alterar na lista | Exibir na lista de usuários cadastrados | Usuário2 – 15/02/2010. Executado com sucesso | Usuário1 – 25/02/2010. Mostra um erro ao alterar usuário |
| **2** | Usuário | Validação dos campos | 1) Escolher opção Inserir Usuário<br>2) Deixar campos nome, e-mail e senha em branco | Mostrar a mensagem "Campo obrigatório" | Usuário2 – 15/02/2010. Executado com sucesso | Usuário1 – 25/02/2010. Executado com sucesso |
| **3** | Usuário | Validação dos campos | 1) Escolher opção Inserir Usuário<br>2) Inserir senha < 2 ou > 32 caracteres | Mostrar mensagem de limite de caracteres | Usuário2 – 15/02/2010. Executado com sucesso | Usuário1 – 25/02/2010. O campo senha aceita menos de 6 caracteres |
| **4** | Usuário | Validação dos campos | 1) Escolher opção Inserir Usuário<br>2) Digitar e-mail inválido | Mostrar mensagem "O e-mail informado não é válido" | Usuário2 – 15/02/2010. Executado com sucesso | Usuário1 – 25/02/2010. Executado com sucesso |

### C. Relatório de Incidente de Teste (Tabela 3)

| ID | Status | Responsável pela Correção | Prioridade de Correção | Descrição do Erro | Data e Nome de Quem Corrigiu |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **1** | Pronto para testar novamente | Usuário2 | Alta | Mostra um erro ao alterar usuário | 01/03/2010 – Usuário2 |
| **3** | Pronto para testar novamente | Usuário2 | Alta | O campo senha aceita menos de 6 caracteres | 14/03/2010 – Usuário2 |
| **5** | Pronto para testar novamente | Usuário1 | Baixa | No cabeçalho o nome do relatório está errado | 10/03/2010 – Usuário1 |

### D. Relatório Resumo de Teste (Tabela 4)

- **Nome do Projeto:** Tomada de Decisão (SAD)
- **Período de Execução:** 01/02/2010 a 01/10/2010
- **Pessoas Envolvidas:** Usuário1, Usuário2, Usuário3
- **Métricas dos Testes:**
  - Casos de testes criados antes do teste: 30
  - Casos de testes criados durante o teste: 3
  - Casos de testes executados: 33 (100%)
  - Casos de teste com sucesso: 20 (66,67%)
  - Casos de teste com erro: 13 (43,33%)
  - Taxa de correção pelo desenvolvedor: 100%

---

## VI. Conclusão
A documentação baseada na norma IEEE 829 viabilizou o planejamento, organização e rastreamento de erros no sistema SAD, permitindo correções ágeis antes da entrega final e garantindo maior qualidade ao produto de software.

---

## Referências
- IEEE Computer Society. IEEE Std 829: Standard for Software Test Documentation, 1998.
- PRESSMAN, R. S. Engenharia de Software. 6ª ed. McGraw-Hill, 2006.
- MYERS, G. J. The Art of Software Testing. 2nd ed. Wiley, 2004.
- CRESPO et al. Uma Metodologia de Teste de Software. III Simpósio, 2004.
