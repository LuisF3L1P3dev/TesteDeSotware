Especificação do Programa Identifier

Nome
	Identifier - Determina se um identificador é válido.

Uso
	IdentifierMain <string>

Descrição
	O programa Identifier determina se um identificador é válido. Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter no mínimo um caractere e no máximo seis caracteres de comprimento.

Exemplos
	Verificando um identificador válido (respeita as restrições impostas na descrição):
Identifier “string”		- Output: Válido

	Verificando um identificador inválido (supera o número máximo de caracteres aceitos):
Identifier “stringmuitogrande”		 - Output: Inválido
