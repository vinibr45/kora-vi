# Demanda: Weber Patches

## Titulo

Criar Weber Patches para comunicacao padronizada das atualizacoes por data de release

## Problema

Hoje a Weber nao possui um versionamento formal para organizar as entregas do sistema, como `v1.2.0`, `v1.3.0` ou equivalente.

Na pratica, as "versoes" sao identificadas pela **data de release**. Isso dificulta a comunicacao clara do que mudou em cada atualizacao, principalmente quando suporte, desenvolvimento, clientes ou gestao precisam entender:

- quais recursos foram alterados;
- quais correcoes foram entregues;
- quais problemas conhecidos foram tratados;
- quais modulos foram impactados;
- quais mudancas podem explicar novos comportamentos apos uma atualizacao.

Sem um registro padronizado, o conhecimento sobre cada release fica disperso em chamados, conversas, testes, memoria da equipe ou anotacoes isoladas.

## Situacao identificada

A Weber ja possui uma referencia temporal para separar entregas: a data de release.

Essa data pode ser usada como identificador principal de cada "patch", criando uma camada de documentacao semelhante aos patch notes usados em jogos online e softwares SaaS, mas sem exigir que a empresa adote imediatamente um modelo formal de versionamento.

## Proposta

Criar o recurso/processo **Weber Patches**, composto por registros padronizados de atualizacao.

Cada Weber Patch representa uma release publicada em uma data especifica e deve reunir, em linguagem clara, as principais alteracoes entregues naquela atualizacao.

Exemplo de identificacao:

```text
Weber Patch - Release 2026-09-15
```

ou:

```text
Weber Patch - 15/09/2026
```

## Objetivo

Permitir que cada release da Weber tenha um historico simples, consultavel e organizado, mesmo sem versionamento formal.

O Weber Patches deve ajudar a equipe a responder rapidamente:

- o que mudou nessa release;
- qual modulo foi afetado;
- se houve correcao, melhoria, novo recurso ou ajuste tecnico;
- se existe impacto operacional para clientes ou suporte;
- quais evidencias ou chamados deram origem a determinada alteracao;
- quais problemas podem ter surgido apos uma release especifica.

## Comportamento atual

As atualizacoes sao separadas por data de release, mas nao existe um padrao centralizado para registrar e comunicar o conteudo de cada entrega.

Com isso:

- a rastreabilidade das mudancas fica limitada;
- a equipe de suporte pode ter dificuldade para relacionar problemas a releases especificas;
- a gestao nao tem uma visao simples do valor entregue em cada atualizacao;
- clientes e usuarios podem nao entender o que foi corrigido ou alterado;
- investigacoes de causa raiz perdem contexto historico.

## Comportamento esperado

Ao publicar ou registrar uma release, deve ser possivel criar um Weber Patch contendo:

- data da release;
- resumo executivo;
- modulos impactados;
- novidades;
- melhorias;
- correcoes;
- alteracoes tecnicas;
- problemas conhecidos;
- orientacoes para suporte;
- evidencias, chamados ou demandas relacionadas;
- responsaveis e status de validacao, quando aplicavel.

O registro deve ser claro o suficiente para ser entendido por suporte, desenvolvimento, gestao e, quando necessario, adaptado para comunicacao externa.

## Estrutura sugerida do Weber Patch

```text
Weber Patch - Release AAAA-MM-DD

1. Resumo da release
2. Modulos impactados
3. Novidades
4. Melhorias
5. Correcoes
6. Alteracoes tecnicas
7. Impactos para suporte
8. Impactos para clientes/usuarios
9. Problemas conhecidos
10. Demandas, chamados ou RAAs relacionadas
11. Evidencias
12. Validacao
13. Observacoes finais
```

## Regras sugeridas

- A data de release deve ser o identificador obrigatorio do patch.
- O patch nao precisa substituir um versionamento formal.
- Cada item registrado deve indicar modulo ou area afetada sempre que possivel.
- Correcoes devem mencionar o comportamento anterior e o comportamento esperado apos a release.
- Mudancas com impacto operacional devem trazer orientacao para o suporte.
- Problemas conhecidos devem ser registrados mesmo quando ainda nao houver correcao definitiva.
- Quando houver origem em chamado, RAA ou demanda interna, a referencia deve ser informada.

## Beneficios esperados

- Melhor rastreabilidade entre releases e problemas reportados.
- Mais clareza para suporte entender o que mudou.
- Menos dependencia de memoria individual da equipe.
- Melhor comunicacao entre suporte, desenvolvimento e gestao.
- Base historica para investigar problemas apos atualizacao.
- Possibilidade futura de evoluir para versionamento formal.
- Apoio a documentacao interna, base de conhecimento e analise de causa raiz.

## Criterios de aceitacao

- Deve existir um modelo padrao para registrar uma release como Weber Patch.
- O modelo deve usar data de release como identificador principal.
- O modelo deve separar novidades, melhorias, correcoes e alteracoes tecnicas.
- O modelo deve permitir registrar modulos impactados.
- O modelo deve permitir associar chamados, RAAs ou demandas relacionadas.
- O modelo deve conter espaco para impactos ao suporte e aos usuarios.
- O modelo deve permitir registrar problemas conhecidos da release.
- A estrutura deve ser simples o suficiente para uso recorrente pela equipe.

## Fora do escopo inicial

- Criar um novo sistema completo de versionamento.
- Definir numeracao semantica oficial para a Weber.
- Automatizar publicacao de releases.
- Criar comunicacao externa para clientes sem revisao previa.
- Substituir chamados, RAAs ou demandas tecnicas existentes.

## Evolucoes futuras

- Criar uma tela no IOS ou ferramenta interna para consultar Weber Patches.
- Permitir filtro por data de release, modulo, tipo de mudanca ou problema conhecido.
- Relacionar patches a RAAs, chamados, demandas e evidencias.
- Gerar resumo tecnico para suporte e resumo simplificado para clientes.
- Criar indicadores de problemas por release.
- Evoluir de data de release para versionamento formal, se a Weber decidir adotar esse processo.

## Observacoes

O Weber Patches deve nascer como organizacao pratica das releases atuais, nao como mudanca obrigatoria de processo de desenvolvimento.

A primeira versao pode ser manual e baseada em documento. Depois que o formato estiver validado pela equipe, pode evoluir para recurso dentro de sistema, wiki interna, IOS ou automacao.

