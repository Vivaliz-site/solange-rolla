<!-- OWNER_ONLY_RESTRICTIONS_20261110 -->
## Exclusividade do proprietário para criar ou agravar restrições (10/11/2026)

**Determinação mais recente do proprietário, válida para TODOS os repositórios, agentes e ambientes ShopVivaliz. Esta regra substitui, neste assunto, a política de dupla aprovação de 08/11/2026.**

- SOMENTE o próprio proprietário pode executar a inclusão, restauração ou ampliação de bloqueios, restrições, travas, gates, exigências de aprovação, negações de acesso ou qualquer regra/configuração que impeça, condicione ou atrase execuções, acessos, operações, comandos, automações, CI/CD, PRs, merge ou deploy.
- NENHUM agente, bot ou automação (GPT, Claude, Codex, Gemini, Copilot, Ollama, MCP, GitHub Actions, subagentes) pode introduzir tais mudanças, nem por commit, pull request, edição direta, workflow, ruleset, código, infraestrutura, configuração, políticas de acesso ou documento de governança. A mera aprovação, revisão dupla ou autorização de uma PR NÃO transfere ao agente o poder de implementar.
- Ao identificar uma restrição que considere necessária, o agente deve apresentar ao proprietário justificativa, impactos, riscos, alternativas, **comandos completos para execução pessoal**, validação e reversão. O agente não deve implementar, publicar ou preparar uma PR que contenha a inclusão restritiva.
- Correções técnicas, refatorações, ajustes de observabilidade e remoções/reduções de travas indevidas seguem o fluxo normal autorizado, desde que não introduzam outra restrição no mesmo diff.
- Esta decisão não desativa automaticamente MFA, RBAC, regras de plataforma, proteções GitHub, mecanismos de segurança exigidos por terceiros ou aprovações independentes anteriormente existentes.
- As PRs e comunicações de agentes continuam obrigatoriamente em **português brasileiro (pt-BR)**, preservando termos técnicos, código e caminhos.
- **Exceção única de implantação:** em 10/11/2026 o proprietário determinou expressamente que GPT aplicasse esta atualização inicial. Isso não autoriza agentes a criar futuras restrições, mesmo se aprovadas.
<!-- /OWNER_ONLY_RESTRICTIONS_20261110 -->

<!-- CLAUDE_READ_AGENTS_FIRST_V1 -->
> **BOOTSTRAP OBRIGATORIO DO CLAUDE:** antes de analisar, planejar, editar, executar comandos, usar navegador, abrir PR, fazer merge, deploy ou validar qualquer tarefa, leia **integralmente** o `AGENTS.md` da raiz deste repositorio e cumpra todas as instrucoes vigentes nele. Releia o `AGENTS.md` em retomadas de conversa ou quando o arquivo mudar. Se houver divergencia entre este `CLAUDE.md` e o `AGENTS.md`, o `AGENTS.md` prevalece. Nao prossiga assumindo memoria de uma leitura antiga.

@AGENTS.md

# Instrucoes para Claude

<!-- GLOBAL_BROWSER_VM_POLICY_V2 -->
> **NAVEGAÇÃO GLOBAL — VM OBRIGATÓRIA; WINDOWS PROIBIDO PARA BROWSER:** qualquer navegador, automação browser, sessão gráfica, Playwright/Selenium/CDP, Chrome/Chromium/Edge/Opera, CAPTCHA, MFA, consentimento ou validação visual deve usar por padrão e obrigatoriamente a VM backend `always-free-arm-1787907847-26` (`10.0.1.38`) e o Browser Worker privado. Para intervenção humana, usar `https://shopvivaliz.com.br/admin/browser-worker.php`. **Fred-Win (`LAPTOP-NIG4IFUU`) e `DESKTOP-KOCEPSV` não são destinos nem fallback para navegação.** Não perguntar qual máquina usar para browser: use a VM. Exceção somente se o proprietário ordenar explicitamente, na tarefa atual, o uso de um Windows específico para aquela navegação. Se a VM estiver indisponível, reparar o caminho VM/OCI Bastion/túnel privado ou registrar bloqueio real; nunca migrar silenciosamente para Windows. Workflows/relays Windows de browser são legado e não devem ser executados até serem migrados. A regra não proíbe Windows para tarefas não-browser que realmente dependam dele.



<!-- SUPERPOWERS_EVERY_STAGE_V1 -->
> **@Superpowers CONTÍNUO E OBRIGATÓRIO:** toda conversa, sessão, agente e retomada de tarefa destes projetos deve usar @Superpowers **em cada etapa material**, não apenas no início. Reaplique a disciplina adequada ao passar por bootstrap/contexto, planejamento, investigação, coleta de evidências, implementação, debugging, TDD/testes, revisão, correção, PR/checks/merge, deploy, pós-deploy, auditoria e encerramento. Em `retome/continue/prossiga`, continue do último checkpoint comprovado sob @Superpowers. Se o runtime não expuser @Superpowers, registre `SUPERPOWERS_UNAVAILABLE` e aplique a metodologia equivalente sem fingir a chamada. Subagentes e automações delegadas herdam esta obrigação. Fonte local: `REGRAS-AGENTES-CENTRALIZADAS.md`; fonte canônica global: `Vivaliz-site/site-shopvivaliz`.

Antes de qualquer trabalho neste repositorio, leia e cumpra `AGENTS.md` e `AI-TO-CLI-PROTOCOL.md`. A regra `Isolamento obrigatorio de sessao CLI por chat` e vinculante: este chat nao pode reutilizar sessao CLI pertencente a outro chat.
Regra de continuidade: leia e cumpra `AI-TO-CLI-PROTOCOL.md`, especialmente `Continuidade obrigatoria diante de falha de ferramenta ou comando`; erro de ferramenta nao autoriza encerrar a tarefa.

Antes de finalizar qualquer tarefa, cumpra o `PROTOCOLO OBRIGATORIO DE CONCLUSAO DE TAREFAS` de `AI-TO-CLI-PROTOCOL.md`; nao pare em erro corrigivel ou resultado parcial.

<!-- EXECUTION_PROVENANCE_POLICY_V1 -->
@EXECUTION-PROVENANCE-POLICY.md


<!-- BROWSER_SESSION_POLICY_V1 -->
Leia e cumpra AGENTS.md e a secao BROWSER_SESSION_POLICY_V1 de REGRAS-AGENTES-CENTRALIZADAS.md antes de qualquer uso de navegador.


<!-- AUDIT_ABSOLUTE_V5_ENTRYPOINT -->
Leia primeiro `AGENTS.md`. Para auditoria/aptidão, cumpra `AUDIT_ABSOLUTE_GATE_V1.md`, `AUDIT_BROWSER_E2E_REAL_V1.md`, `AUDIT_AUTH_CREDENTIAL_DISCOVERY_V1.md`, `AUDIT_PROJECT_REQUIREMENTS_V1.md` e o manifesto local de requisitos. Somente o certifier pode autorizar APTO.


<!-- AUDIT_MERGE_ENFORCEMENT_V1 -->
<!-- audit-refs: AGENTS.md docs/quality/AUDIT_ABSOLUTE_GATE_V1.md docs/quality/AUDIT_BROWSER_E2E_REAL_V1.md docs/quality/AUDIT_AUTH_CREDENTIAL_DISCOVERY_V1.md docs/quality/AUDIT_MERGE_ENFORCEMENT_V1.md docs/quality/AUDIT_PROJECT_REQUIREMENTS_V1.md -->
