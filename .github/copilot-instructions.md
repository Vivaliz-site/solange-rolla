# GitHub Copilot / coding agents

Antes de qualquer trabalho, leia e cumpra `AGENTS.md` e `AI-TO-CLI-PROTOCOL.md`. A secao `Continuidade obrigatoria diante de falha de ferramenta ou comando` e vinculante: uma falha de CLI/API/tool nao encerra a tarefa; diagnostique, use fallback seguro, persista checkpoint e continue ate CONCLUIDO ou bloqueio externo real.

<!-- MARINA_MCP_AS_USER_20261112 -->
> **MCP Marina: executar como `ubuntu` e root do backend (2026-11-12):** `marina_admin_shell` aceita o argumento opcional `as_user="ubuntu"` (sudo -n -u ubuntu, auditado por hash; exclusivo com `as_root`; qualquer outro usuario e recusado). Ativo na Marina desde a release `eb81e37c` (grant PR #3918 do `site-shopvivaliz`). No backend, o usuario `root` tambem tem os MCPs `shopvivaliz-marina-admin` e `shopvivaliz-remote-control` e a credencial do Marina MCP ja provisionada. Fonte de verdade e procedimento: `Vivaliz-site/site-shopvivaliz` em `docs/knowledge/marina-mcp-admin-agent-access.md`. Credenciais continuam so em arquivos protegidos (0600), sem expor valores.
