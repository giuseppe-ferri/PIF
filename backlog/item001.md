# Item#001 - Tela de Cadastro

## **Descrição:**  
*A recepcionista cadastra os dados do aluno em um formulário. Ao finalizar o preenchimento, o sistema gera automaticamente um RA (login) e uma senha provisória, que são enviados para o e-mail do aluno. ***Em seguida, o aluno deve utilizar esses dados para acessar o sistema pela primeira vez e definir uma nova senha***.*

## **Requisitos:**
Formulário contendo os dados pessoais do usuário (aluno), como listado abaixo:
- Identificação do paciente: Nome completo, data de nascimento, sexo/gênero, CPF, RG.
- Endereço e Contato: Endereço completo (rua, número, bairro, cidade, CEP, complemento), telefone, e-mail.
- Autorização para o uso de dados: Termo de consentimento informando sobre o uso dos dados pessoais, assinatura ou aceite digital, respeitando a Lei Geral de Proteção de Dados (LGPD) no Brasil (ou legislação equivalente).

## **Critérios de aceitação:**
    1. O sistema deve identificar automaticamente se a entrada fornecida pelo usuário é um CPF ou um endereço de e-mail e, a partir disso, aplicar regras de validação e tratamento específicas para cada tipo de dado.
	2. Regras para o CPF.
		2.1. Deve conter 11 dígitos, todos numéricos.
		2.2. Gerar cálculo para validar a autenticidade do CPF.
	3. Regras para o e-mail.		
		3.1. Seguir o padrão 'usuario@dominio' contendo pelo menos um @ e um domínio válido.
		3.2. Pode incluir checagem de TLD (top-level domain), por exemplo, .com, .br, .net e etc...
		3.3. Garantir que haja apenas números, pontos, sublinhados e alguns caracteres especiais antes do @.
	4. Regras para a senha
		4.1. O tamanho mínimo será de 8 caracteres.
		4.2. Deverá conter letras minúsculas e pelo menos uma letra maiúscula, número e caractere especial (!@#$&'"%-).
		4.3. Impedir o uso de dados pessoais óbvios (nome, data de nascimento, CPF, etc.) dentro da senha, para dificultar adivinhações baseadas em informações públicas.
		4.4. Ao receber a senha, armazená-la usando algoritmos de hash seguros (bcrypt, argon2, scrypt) e não em texto puro.
		4.5. Política de ciclos de troca, a senha deverá ser alterada obrigatoriamente a cada 90 dias.
		4.6. Confirmar senha, a senha confirmada deve ser idêntica com a senha fornecida inicialmente.
	5. Validar CEP.
		5.1. Garantir que o CEP utilizado é válido.
	6. Permitir a criação da conta somente se o usuário concordar com os termos de uso do aplicativo.
	7. Após concluir o cadastro, será atribuído a cada usuário um ID único. Esse ID será um número inteiro que começa em 1 e será incrementado automaticamente em 1 a cada novo usuário registrado.
	8. Deve haver logs de erros e acertos.  
	9.  Ao finalizar o formulário, o sistema gera automaticamente um RA (login) e uma senha provisória, que são enviados para o e-mail do aluno cadastrado.
      	9.1. Ao logar pela primeira vez, o sistema deverá solicitar o login (RA e senha), digitar nova senha e confirmar nova senha, o sistema deve realizar a autenticação das senhas.

## **Protótipo / UI Design**:
    Responsável: Thyago Yoshida / Pedro Rocha da Silva Guedes
    
**Link para o protótipo:** [Figma](https://url.com.br/)

- Implementar todos os ***requisitos*** na tela de cadastro.

## **Subtarefas**:
### 1. **Front-End**
    Responsável: João Vitor da Costa
    
**Link para o código:** [GitHub](https://url.com.br/)

- Desenvolver a tela seguindo o ***protótipo no Figma***.

### 2. **Back-End**
    Responsável: Wesley Henrique Dias de Melo

**Link para o código:** [GitHub](https://url.com.br/)

- Integrar com o Front-End.
- Implementar todos os ***Critérios de aceitação***.

### 3. **Integração com SQL Server**  
    Responsável: Giuseppe Ferri

**Link para o código:** [GitHub](https://url.com.br/)

- Criar a tabela ***TABELA***.
- Integrar com o Back-End e gravar os dados essenciais dos ***Requisitos*** na tabela

### 4. **Casos de Teste**
    Responsável: Lucas Miguel Bonini da Silva

- Validar todos os ***Requisitos***.
- Validar todos os ***critérios de aceitação***, cenários de sucesso e falha.

## **Estimativa**:
- 1 / 2 / 3 / 4 / 5 story points

## **Prioridade**:
- Baixa / Muito baixa / Normal / Alta / Muito Alta

## **Status**:
- Planejado / Não Planejado

## **Referências e Anexos**:
