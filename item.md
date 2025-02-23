#1 - [User Story] Implementar Login com Redes Sociais

**Descrição**:
Como usuário do sistema, quero poder realizar login usando minhas contas de redes sociais (Google, Facebook), 
para não precisar criar novas credenciais e agilizar meu acesso ao aplicativo.

**Critérios de Aceite**:
- Ao clicar no botão "Login com Google", deve abrir a tela de login da Google.
- Ao retornar com sucesso, o usuário deve ser logado na aplicação com seu perfil.
- Deve haver tratamento de erro caso a autenticação falhe.
- Deve haver logs de erros e acertos.
  
**Protótipo / UI Design**:
- [Link para o Figma ou outra ferramenta]  

**Requisitos**:
- Uso da biblioteca X de autenticação OAuth2.
- Tempo de resposta abaixo de 2s para a autenticação.

**Responsável Principal**:
- Fulano de Tal

**Subtarefas**:
1. **Front-End**  
   - Ajustar tela de login para incluir botão “Login com Google” e “Login com Facebook”.
   - Responsável: Ciclano  
   - GitHub/PR: [link para PR]

2. **Back-End**  
   - Implementar endpoint de autenticação OAuth2 e salvar dados do usuário.
   - Responsável: Beltrano  
   - GitHub/PR: [link para PR]

3. **Integração com SQL Server**  
   - Definir tabela de usuários e campos necessários para armazenar tokens de sessão (se aplicável).
   - Responsável: Fulano  
   - GitHub/PR: [link para PR ou script de banco]

4. **Casos de Teste / Teste de Aceite**  
   - Responsável QA: Maria  
   - Testar fluxo de login com Google e Facebook, cenários de sucesso e falha.

**Estimativa**:
- 5 story points

**Prioridade**:
- Alta

**Status**:
- Planejado

**Referências e Anexos**:
- Documento de requisitos detalhados: [link]
- Protótipo de alta fidelidade: [link]