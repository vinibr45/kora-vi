# DR-0007: KORA diferencia modos de execucao

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

Algumas tarefas podem ser resolvidas manualmente, enquanto outras justificam skills, agentes, ferramentas, integracoes ou automacoes.

Exemplo: gerar um calendario semanal de postagens pode ser feito manualmente no inicio, mas depois pode envolver agentes de conteudo, skills de calendario, geracao de imagens, integracoes com ferramentas externas e automacoes recorrentes.

## Decision

KORA deve diferenciar modos de execucao antes de criar complexidade.

Modos iniciais:

- Manual;
- Assisted;
- Tool-Supported;
- Integrated;
- Automated.

Quando houver mais de um caminho razoavel, KORA deve apresentar opcoes e perguntar sobre contas, assinaturas, permissoes e nivel desejado de automacao.

## Reasoning

Isso evita criar integracoes ou automacoes prematuras, mas preserva a capacidade de evoluir quando a tarefa se repetir ou gerar ganho operacional claro.

## Consequences

- Capability Management deve fazer discovery das capacidades existentes antes de executar.
- Integracoes externas devem exigir clareza de permissao, acesso e beneficio.
- Automacoes recorrentes devem ser propostas e aprovadas antes de serem criadas.
- KORA deve preferir o menor nivel de complexidade que resolva bem a tarefa atual.
