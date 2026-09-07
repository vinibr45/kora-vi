# Maturidade Da KORA

Este mapa mostra o estado atual de maturidade da KORA Core.

## Niveis

```text
0 - Ideia
1 - Documento inicial
2 - Procedimento definido
3 - Uso assistido por agente
4 - Avaliado por health check ou eval
5 - Automatizacao proposta
6 - Automatizacao ativa aprovada
```

## Estado Atual

```text
Arquitetura Core -> 3
Conhecimento reutilizavel -> 2
Projetos e bindings -> 3
Agentes Core -> 2
Skills Core -> 3
Ferramentas -> 2
Integracoes -> 2
Automacoes -> 5 para manutencao/design; demais ainda propostas
Evals manuais -> 3
Experimentos e aprendizado -> 2
Entrada de uso humano -> 3
Instrucao para agente -> 3
Manutencao organica -> 3
Health check -> 3
Versionamento organico -> 3
Governanca e aprovacao -> 3
Loop diario -> 3
Captura de ideias soltas -> 3
Deteccao de lacunas de capacidade -> 3
Uso da KORA instalada em outros repositorios -> 3
Checagem de instalacao local da KORA -> 3
Registro central de instalacoes KORA -> 3
Geracao de imagem revisada -> 5
Integracoes de canais de marketing -> 5
```

## Leitura Rapida

A KORA ja possui uma base operacional assistida por agente.

Ela ainda nao e um sistema autonomo com watchers, schedulers, dashboards ou execucao persistente. O modelo atual e Markdown-first, com automacoes definidas como contratos e execucao assistida durante conversas ou manutencoes manuais.

## Proximos Saltos De Maturidade

```text
Nivel 3 -> Nivel 4
Criar e rodar evals recorrentes para health check, roteamento, manutencao e versionamento.
Rodar o eval da esteira de imagem revisada com projetos reais antes de ativar loops menos assistidos.

Nivel 4 -> Nivel 5
Definir automacoes propostas para loops comprovadamente recorrentes.

Nivel 5 -> Nivel 6
Ativar automacoes somente depois de aprovacao, logs, stop conditions e testes.
```

## Como Atualizar Este Mapa

Atualize este arquivo quando:

```text
uma capacidade sair de documento para uso assistido
uma capacidade ganhar eval
uma automacao for proposta
uma automacao for aprovada e ativada
um fluxo deixar de ser usado
uma regra de governanca mudar
```

Use:

```text
skills/maintain-kora-indexes.md
skills/check-kora-health.md
skills/assess-kora-version-impact.md
```
