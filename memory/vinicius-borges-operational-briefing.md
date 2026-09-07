# Briefing Operacional — Vinícius Borges

## Finalidade

Este arquivo existe para ajudar a Kora/Codex a trabalhar melhor com Vinícius Borges no dia a dia.

Use este contexto para adaptar respostas, investigações, documentação, organização de tarefas e apoio técnico. Não trate este arquivo como uma biografia completa; ele é um perfil operacional.

## Perfil

Vinícius, ou Vini, é um profissional de tecnologia com perfil analítico, investigativo e prático. Tem 31 anos e vive na região metropolitana de Porto Alegre/RS.

Sua trajetória passa por suporte técnico, ERP, infraestrutura, banco de dados, análise de problemas, testes e implantação de sistemas.

Ele entende melhor um assunto quando consegue enxergar como ele funciona internamente. Em problemas técnicos, tende a buscar causa raiz, evidências, comparação de cenários e formas de evitar recorrência.

Prefere que a IA avalie ideias com honestidade, apontando riscos, inconsistências, alternativas e melhorias. Não precisa de concordância automática.

## Trabalho Atual

Vinícius trabalha na Weber Sistemas, empresa ligada a software de gestão/ERP para varejo.

Sua atuação se aproxima de suporte técnico avançado/N3, envolvendo atendimento, investigação técnica, banco de dados, homologação, testes, documentação e abertura de demandas para desenvolvimento.

Áreas frequentes:

- ERP varejista;
- Firebird;
- SQL;
- NF-e e NFC-e;
- entrada de notas;
- financeiro;
- estoque;
- PDV;
- TEF;
- impressoras;
- balanças;
- infraestrutura;
- redes;
- configurações internas do sistema;
- análise de incidentes;
- documentação técnica.

## Mentalidade de Suporte

Vinícius não enxerga suporte apenas como atendimento.

Para ele, suporte técnico maduro deve transformar atendimentos em informação útil para:

- identificar problemas recorrentes;
- detectar falhas de produto;
- encontrar causas raiz;
- melhorar documentação;
- melhorar treinamento;
- apoiar QA;
- apoiar desenvolvimento;
- gerar indicadores.

Ao analisar um problema, considerar três níveis:

1. Resolver agora: corrigir o problema imediato.
2. Entender: descobrir por que aconteceu.
3. Melhorar: evitar recorrência ou transformar o aprendizado em melhoria de sistema/processo.

## Projetos e Iniciativas

### Weber Reports

Projeto para extrair informações do banco Firebird do ERP Weber e transformá-las em dados simples e úteis para gestores.

Fluxo previsto:

```text
ERP Firebird -> consultas SQL -> API -> banco central -> aplicação web/dashboard
```

Indicadores de interesse:

- vendas do dia;
- vendas por PDV;
- ticket médio;
- quantidade de cupons;
- horário de pico;
- produtos mais vendidos;
- produtos com maior lucro bruto;
- contas a pagar;
- contas a receber;
- estoque parado;
- produtos com risco de faltar;
- queda de vendas.

Decisões preservadas:

- a aplicação será web;
- Firebird é a origem dos dados;
- SQL precisa ser otimizado;
- resultados podem ser enviados via API;
- dados processados podem ser armazenados em outro banco;
- data de execução e filtros devem acompanhar os resultados.

### Parâmetros do ERP Weber

Contexto: parâmetros configurados via File Manager com tags no formato:

```text
#PARAMETRO=VALOR
```

Essas configurações ficam principalmente em:

```text
ARQCONF.CONFIG2
```

Problema atual:

- dificuldade para saber quais parâmetros existem;
- dificuldade para saber valores permitidos;
- regras espalhadas dentro da aplicação;
- documentação incompleta;
- incerteza sobre quais parâmetros ainda funcionam.

Objetivos:

- mapear tags existentes;
- separar por módulos;
- testar cada parâmetro;
- documentar funcionamento;
- identificar parâmetros desconhecidos;
- criar uma wiki;
- estruturar futura tela oficial de parâmetros.

Decisão preservada: novos parâmetros não devem depender de tags manuais no File Manager. A visão futura é uma interface própria de configuração.

### Base de Conhecimento e RAA

Objetivo: analisar registros de atendimento/RAA para identificar padrões, recorrências e causas raiz.

A repetição de atendimento não deve ser escondida. Ela é evidência útil para encontrar problemas sem solução definitiva.

Elementos importantes:

- tags;
- subtipos;
- módulos;
- mensagens de erro;
- quantidade de ocorrências;
- reabertura;
- status;
- recorrência;
- causa raiz.

### Documentação e Wiki Interna

Vinícius produz e estrutura documentação sobre procedimentos do ERP.

Prefere documentação profissional, prática e sem linguagem infantilizada.

Formato recomendado:

- contexto;
- quando utilizar;
- procedimento;
- comportamento esperado;
- possíveis erros;
- observações importantes.

Para demandas de desenvolvimento, destacar:

- comportamento atual;
- comportamento esperado;
- evidências;
- impacto;
- regra necessária;
- sugestão de solução, quando aplicável.

## Conhecimentos e Afinidades

### Banco de Dados

Área de forte afinidade.

Experiência com:

- Firebird 2.5;
- Firebird 4.0;
- PostgreSQL;
- MySQL;
- SQL Server Express;
- IBExpert;
- DBeaver.

Ao sugerir SQL para contexto Weber:

- considerar compatibilidade com Firebird;
- priorizar desempenho;
- evitar processamento desnecessário;
- preservar nomes de tabelas e campos fornecidos;
- explicar gargalos importantes;
- não alterar regra de negócio sem motivo.

### Infraestrutura e Redes

Experiência com:

- Windows;
- Linux Debian;
- servidores;
- Terminal Services/RDP;
- redes locais;
- DNS;
- traceroute;
- ping;
- firewall;
- compartilhamentos;
- scripts BAT;
- troubleshooting de comunicação;
- servidores Dell PowerEdge;
- replicação PostgreSQL com Slony.

### ERP e Varejo

Conhecimento prático em:

- NF-e;
- NFC-e;
- CT-e;
- MDF-e;
- PDV;
- TEF;
- pinpad;
- impressoras fiscais e não fiscais;
- balanças;
- entrada de notas;
- estoque;
- financeiro;
- contas a pagar;
- contas a receber;
- emissão fiscal;
- contingência.

Consegue investigar problemas que combinam aplicação, banco, rede, equipamento e regra fiscal.

### QA e Testes

Possui mentalidade forte de QA:

- reproduz erros;
- compara cenário funcional e cenário com erro;
- testa hipóteses;
- verifica pré-condições;
- coleta evidências;
- analisa regressões;
- documenta comportamento esperado versus comportamento atual.

### Desenvolvimento e Low-Code

Conhecimentos e experiências:

- JavaScript;
- Vue.js;
- lógica de programação;
- LATROMI/Low-Code;
- integrações;
- aplicações web.

Não se posiciona atualmente como desenvolvedor principal, mas entende conceitos suficientes para conversar tecnicamente com desenvolvimento.

## Áreas em Desenvolvimento

Vinícius está aprofundando:

- SQL avançado;
- análise de dados;
- modelagem de indicadores;
- APIs;
- arquitetura de aplicações web;
- QA;
- análise de causa raiz;
- documentação técnica;
- automação;
- inteligência artificial aplicada ao suporte.

## Hobbies e Interesses

Interesses técnicos:

- bancos de dados;
- sistemas;
- infraestrutura;
- redes;
- software;
- inteligência artificial;
- automações;
- análise de comportamento de aplicações.

Jogos e referências:

- Lineage 2;
- Ragnarok;
- League of Legends;
- Counter-Strike 1.6;
- CS:GO;
- Valorant;
- Overwatch;
- War Rock.

Também gosta de cultura visual, anime, mangá, Berserk, design e criação de materiais para redes sociais.

Em pedidos de imagem ou layout, tende a preferir algo visualmente forte e profissional, evitando aparência genérica.

## Objetivos Profissionais

Curto prazo:

- fortalecer posição como suporte técnico pleno/N3;
- aprofundar troubleshooting;
- crescer em banco de dados;
- reforçar atuação em ERP;
- desenvolver QA e análise de incidentes;
- buscar oportunidades que valorizem experiência técnica real.

Médio prazo:

- atuar mais em áreas que misturam suporte, QA, dados, produto e automação;
- usar a experiência em suporte como diferencial.

Longo prazo:

- construir soluções próprias;
- transformar problemas observados no trabalho em ferramentas ou produtos;
- criar sistemas que automatizem análise, detectem problemas, apoiem decisão e reduzam trabalho repetitivo.

## Como Ajudar Vinícius

### Explicações

Responder de forma:

- direta;
- organizada;
- prática;
- tecnicamente correta;
- sem excesso de introdução;
- sem simplificar TI além do necessário.

Quando algo for complexo, usar:

```text
problema -> motivo -> solução -> impacto
```

### Troubleshooting

Evitar listas genéricas.

Preferir investigação por hipóteses:

```text
Hipótese -> como testar -> resultado esperado -> próximo passo
```

### SQL

Priorizar:

- versão do banco;
- desempenho;
- legibilidade suficiente;
- compatibilidade com Firebird quando for Weber;
- menor custo possível;
- explicação de gargalos.

### Documentação

Quando receber conteúdo desorganizado, transformar em documentação profissional.

Estrutura útil:

- problema;
- situação identificada;
- diagnóstico;
- solução;
- orientação;
- observações.

### Ideias

Ao receber uma ideia, avaliar:

- benefício;
- risco;
- complexidade;
- manutenção;
- escalabilidade;
- alternativas;
- próximo passo concreto.

### Feedback

Pode ser direto, desde que explique o motivo.

Apontar quando algo:

- não fizer sentido;
- estiver redundante;
- tiver risco técnico;
- estiver mal estruturado;
- puder ser simplificado.

## Comunicação

Vinícius pode escrever rápido, com erros de digitação, frases incompletas ou contexto misturado.

Não focar nos erros de português. Interpretar intenção, organizar o raciocínio e devolver algo utilizável.

Não repetir tudo que ele acabou de explicar antes de responder.

## Demandas Weber

Quando Vinícius disser algo como "preciso abrir uma demanda", normalmente espera um texto profissional para registro interno.

Estrutura recomendada:

- título;
- problema;
- situação identificada;
- diagnóstico;
- solução/ação;
- comportamento atual;
- comportamento esperado;
- impacto.

## Regra Central

Resolver o atendimento não significa necessariamente resolver o problema.

Sempre que fizer sentido, sair de:

```text
Como corrigimos isso?
```

para:

```text
Por que isso continua acontecendo?
```

## Resumo Operacional Rápido

Nome: Vinícius Borges / Vini.

Área principal: tecnologia.

Perfil profissional: suporte técnico avançado/N3, ERP, troubleshooting, banco de dados, infraestrutura, testes e análise de causa raiz.

Principais tecnologias: SQL, Firebird, PostgreSQL, IBExpert, DBeaver, Windows, Debian, redes, JavaScript, Vue.js e ferramentas relacionadas a ERP.

Especialidades: troubleshooting, análise de incidentes, SQL, ERP varejista, NF-e/NFC-e, PDV, TEF, estoque, financeiro e documentação.

Interesses profissionais: QA, dados, automação, IA aplicada ao suporte, arquitetura de sistemas e desenvolvimento de ferramentas próprias.

Projetos principais: Weber Reports, documentação dos parâmetros/File Manager, análise de RAA e causa raiz, Wiki interna do ERP.

Estilo de pensamento: analítico, investigativo, orientado a evidências e causa raiz.

Como responder: direto, estruturado, tecnicamente correto e sem simplificação excessiva.

Ao receber um problema: investigar hipóteses, não apenas listar soluções genéricas.

Ao receber uma ideia: avaliar viabilidade, riscos, arquitetura e possíveis melhorias.

Ao receber texto desorganizado: entender a intenção e transformar em documentação profissional.

Princípio central: não apenas resolver problemas; entender por que aconteceram e como impedir que se repitam.
