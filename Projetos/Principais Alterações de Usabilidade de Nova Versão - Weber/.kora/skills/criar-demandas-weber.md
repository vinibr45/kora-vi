---
name: "criar-demandas-weber"
type: execution
scope: local
status: active
version: "0.10"
owner: "WEBER Sistemas"
domains:
  - support
  - erp
  - customer-service
  - knowledge-management
related_agents: []
related_skills:
  - create-weber-knowledge-article
required_knowledge:
  - .kora/binding.md
  - .kora/context/weber-knowledge-management-context.md
required_tools: []
evals: []
created_at: 2026-09-30
updated_at: 2026-09-30
---

# Criar Demandas Weber

## Purpose

Criar registros de atendimento (RAA), demandas internas (RAI) e Registros de Necessidade (RN) para suporte ao ERP Weber a partir de relatos informais.

Transforme relatos informais em registros profissionais, claros e prontos para uso. Preserve a diferença entre o que o cliente relatou, o que foi observado, o que foi testado, o que foi feito e o que ainda está pendente.

## When To Use

- Quando o usuário pedir uma demanda, chamado, registro, teste interno, encerramento, RAA, RAI ou RN.
- Quando uma ligação ou atendimento precisar virar registro profissional.
- Quando um teste interno, homologação, treinamento ou repasse precisar virar RAI.
- Quando uma necessidade de correção, melhoria, novo recurso, relatório ou análise pelo desenvolvimento precisar virar RN.

## When Not To Use

- Quando o usuário pedir um artigo de wiki, tutorial, roteiro ou material de treinamento da WEBER; nesses casos, use `create-weber-knowledge-article.md`.
- Quando o relato ainda não trouxer informação mínima para separar problema, observação, ação e pendência.
- Quando a demanda exigir acesso, publicação, abertura real de chamado em sistema externo ou consulta a dados sensíveis sem aprovação.

## Inputs

- Relato do usuário.
- Tipo desejado, se informado: RAA, RAI ou RN.
- Módulo, rotina, tela, função, versão, parâmetro, mensagem de erro e contexto operacional, quando informados.
- Testes realizados, resultados observados, ações tomadas, contornos, pendências e responsáveis, quando informados.
- Evidências fornecidas: print, vídeo, log, XML, mensagem literal ou anexo.

## Escolha Do Tipo

- **RAA — Registro de Atendimento:** atendimento ao cliente, diagnóstico, orientação, ajuste, contorno ou encerramento.
- **RAI — Registro de Atendimento Interno:** teste, homologação, treinamento, análise ou encaminhamento para outra equipe.
- **RN — Registro de Necessidade:** pedido de correção, melhoria, novo recurso, relatório ou análise pelo desenvolvimento.

Se uma ligação gerar um atendimento e uma necessidade de desenvolvimento, crie uma RAA e uma RN separadas quando o usuário pedir ambas.

## Regras Para Todas As Demandas

1. Escreva em português claro e profissional. Use títulos que identifiquem o módulo e o problema.
2. Preserve nomes de telas, mensagens de erro, parâmetros e versões exatamente como informados.
3. Não invente causa raiz, teste, solução, autorização fiscal ou resultado.
4. Se o erro não foi reproduzido, diga isso. Se o cliente ainda vai testar, mantenha o status pendente.
5. Identifique contornos como temporários e registre o que ainda precisa ser resolvido.
6. Não exponha senhas, tokens, dados pessoais ou dados fiscais completos sem necessidade.
7. Não use consultas SQL como evidência operacional de atendimento.
8. **Toda demanda completa deve terminar com `### Evidência`. Nenhuma seção pode aparecer depois dela.**
9. Se não houver evidência fornecida, escreva: `Não foram fornecidos prints, logs, XMLs ou outros anexos.`
10. Se o usuário pedir apenas um trecho, como o resumo de encerramento, entregue somente esse trecho.
11. Sempre que houver print, transcreva abaixo do contexto da demanda o que o print demonstra, em linguagem objetiva e conectada ao problema. Identifique tela, rotina, campos, valores, mensagem ou comportamento visível sem inventar resultado que não aparece na imagem.
12. A transcrição do print deve explicar do que se trata a evidência antes de listar o arquivo ou anexo na seção `### Evidência`.
13. Toda RAA e toda RAI devem incluir `### Descrição da Solução`, com um resumo do que foi feito e o desfecho do atendimento ou da atividade interna.
14. Em RAA e RAI, mantenha uma seção `### Evidência` antes de `### Descrição da Solução` e outra seção `### Evidência` ao final, vinculada à descrição da solução. Quando não houver anexos, use a mesma indicação de ausência de evidências nas duas seções.
15. Entregue a demanda sempre como conteúdo único e pronto para copiar, sem comentários antes ou depois do texto quando o usuário pedir a demanda final.
16. Preserve títulos em negrito quando o padrão exigir, especialmente no formato `**Título: ...**`.
17. Jamais use a KORA, o assistente ou qualquer outra IA como fonte, evidência ou origem do conteúdo. Registre somente arquivos, telas, prints, logs, XMLs, documentos, sistemas, testes ou ações humanas efetivamente informadas.
18. Quando uma imagem fizer parte da demanda, mas não puder ser anexada ou incorporada diretamente no texto da evidência, use um marcador objetivo como `[imagem referente ao conteúdo]`.
19. Para RAI, o usuário deve informar o título antes. Caso o título não seja informado, pergunte pelo título antes de montar a demanda.
20. Quando a RAI for de Gestão de Conhecimento, use somente as seções `### Objetivo`, `### Ambiente e Procedimento` e `### Fonte Técnica`. Não inclua `### Comportamento observado`, `### Comportamento esperado`, `### Resultado e encaminhamento`, `### Descrição da Solução` nem `### Evidência`.
21. Em RAI de Gestão de Conhecimento, o desfecho deve ficar dentro de `### Fonte Técnica`, como um resumo do que foi feito com as fontes técnicas utilizadas.
22. Evite conteúdo duplicado ou repetitivo. Cada seção deve ter uma função própria: contexto apresenta o cenário, problema descreve a dificuldade, necessidade registra o pedido, situação atual informa o status e evidência lista somente fonte, anexo, link ou ausência de anexo.
23. Se a mesma informação aparecer em mais de uma seção, reescreva de forma resumida ou remova a repetição, preservando apenas o detalhe necessário para a seção.
24. Formate os tópicos de seção em negrito no Markdown final, por exemplo `### **Contexto**`, `### **Problema**`, `### **Necessidade**` e `### **Evidência**`.
25. Não inclua 5W2H em RAA por padrão. Use 5W2H somente se o usuário pedir explicitamente.

## Estrutura Da RAA

Use o padrão Problema, Situação identificada e Solução. Se ainda não houver solução, substitua o título dessa seção por `Encaminhamento` ou `Solução temporária`.

```markdown
**Título: [problema principal e contexto]**

### **Problema**

[O que o cliente informou e qual foi o impacto.]

### **Situação identificada**

[O que foi verificado, testado ou observado. Separe relato de constatação.]

### **Solução**

[O que foi feito, qual resultado foi confirmado e o que ficou pendente.]

### **Resumo de encerramento**

[Achado, ação e status em duas ou três frases.]

### **Evidência**

[Mensagem de erro, comportamento observado, print, vídeo, log ou anexo disponível.]

### **Descrição da Solução**

[Resumo do que foi feito e qual foi o desfecho do atendimento.]

### **Evidência**

[Mensagem de erro, comportamento observado, print, vídeo, log ou anexo disponível.]
```

Se o usuário pedir 5W2H explicitamente, cada descrição deve ter pelo menos **20 caracteres**, inclusive a resposta de "Quanto?". Não invente dados apenas para alcançar esse tamanho.

## Estrutura Da RAI

Use para documentar trabalho interno. Em testes, destaque cenário, procedimento e resultado. Em repasses ao CX ou desenvolvimento, destaque a solicitação e a pendência. Adapte os títulos quando se tratar de treinamento.

Quando a RAI for de Gestão de Conhecimento, use a estrutura reduzida:

```markdown
**Título: [título informado pelo usuário]**

### **Objetivo**

[O que a atividade de gestão de conhecimento precisava analisar, organizar ou produzir.]

### **Ambiente e Procedimento**

[Materiais, documentos, telas, arquivos e procedimento realmente utilizado.]

### **Fonte Técnica**

[Fontes técnicas utilizadas e desfecho resumindo o que foi feito a partir delas.]
```

Para RAI de teste, homologação, treinamento, análise técnica ou encaminhamento operacional que não seja Gestão de Conhecimento, use a estrutura completa:

```markdown
**Título: [módulo] Teste ou encaminhamento - contexto**

### **Objetivo**

[O que precisava ser testado, analisado ou encaminhado.]

### **Ambiente e procedimento**

[Ambiente, versão e passos realmente utilizados, quando informados.]

### **Comportamento observado**

[Resultado de cada cenário testado. Informe quando o erro não foi reproduzido.]

### **Comportamento esperado**

[O que deveria ocorrer. Para treinamento, use "Conteúdo abordado".]

### **Resultado e encaminhamento**

[Conclusão sustentada pelo teste, responsável pela próxima análise e status.]

### **Evidência**

[Print, vídeo, mensagem, XML, log ou indicação de ausência de anexos.]

### **Descrição da Solução**

[Resumo do que foi feito e qual foi o desfecho da atividade interna.]

### **Evidência**

[Print, vídeo, mensagem, XML, log ou indicação de ausência de anexos.]
```

Exemplo de cuidado: se a quantidade decimal digitada manualmente não causou erro, mas a leitura de uma etiqueta de balança causou, registre os **dois resultados**. Não diga que um parâmetro foi a causa antes de confirmar sua atuação na rotina.

## Estrutura Da RN

Descreva o problema e o resultado necessário de forma que a equipe responsável consiga analisar a demanda. Quando a causa for desconhecida, peça investigação sem apresentar uma hipótese como solução definitiva.

**Não inclua "Critérios de aceite" por padrão.** Acrescente essa seção somente se o usuário solicitar.

```markdown
# RN — [necessidade específica]

**Módulo:** [módulo]
**Rotina/Tela:** [rotina confirmada ou "não informado"]
**Função:** [função afetada]

### **Contexto**

[Motivação e cenário, se necessários.]

### **Problema**

[Comportamento atual, passos conhecidos e impacto.]

### **Necessidade**

[O que precisa ser analisado, corrigido, criado ou disponibilizado.]

### **Comportamento esperado**

[Resultado verificável. Em pedidos de investigação, use "Resultado esperado".]

### **Situação atual**

[Contorno ou atendimento aguardando retorno, se houver.]

### **Evidência**

[Resultados dos testes, mensagem literal e anexos realmente disponíveis.]
```

Omita seções opcionais vazias, mas **nunca omita `### Evidência`**.

## Exemplos De Aplicação

- **RAA:** cliente relata TEF indisponível; suporte encontra o Destaxa fechado, abre o aplicativo e confirma a operação. Registre o ajuste e a orientação ao cliente.
- **RAI:** teste do Entrada de Notas Recebe Fácil com estoque antigo, comparando Robô XML, importação e entrada manual. Registre separadamente o resultado de cada fluxo.
- **RN:** associação de produtos apresenta divergência apesar de GTIN e descrição iguais no XML e no cadastro. Peça revisão da validação e identificação do campo divergente; não invente quais outros campos o sistema compara.

## Outputs

- RAA, RAI ou RN pronta para uso.
- Trecho específico solicitado pelo usuário, quando ele pedir apenas resumo, encerramento ou outra parte.
- Conteúdo final limpo, contínuo e pronto para copiar.

## Evals

Antes de entregar, confirme:

- O tipo de demanda corresponde ao pedido.
- Relatos, testes, hipóteses, ações e pendências não foram misturados.
- Nenhum resultado foi presumido.
- RAA não inclui 5W2H, exceto quando o usuário pedir explicitamente.
- As descrições do 5W2H, quando solicitado, têm pelo menos 20 caracteres.
- RAA e RAI incluem `### Descrição da Solução` e uma evidência final vinculada a esse bloco.
- Prints anexados foram transcritos em relação ao contexto da demanda.
- `### Evidência` é a última seção.
- A resposta final contém somente a demanda, sem explicações externas, quando o usuário quiser copiar o conteúdo.
- Nenhuma IA foi citada como fonte, evidência ou origem do conteúdo.
- RAI de Gestão de Conhecimento usa apenas `Objetivo`, `Ambiente e Procedimento` e `Fonte Técnica`.
- RAI só foi criada depois de o título estar informado.
- O texto não repete o mesmo conteúdo em várias seções sem necessidade.
- Os tópicos de seção estão em negrito.

## Approval Points

Peça aprovação humana antes de:

- publicar, abrir ou alterar registros em sistemas externos;
- usar dados fiscais, pessoais ou de produção que não sejam necessários;
- promover esta skill local para KORA Core.

## Boundaries

Esta skill cria o texto do registro. Ela não abre chamados em sistemas externos, não consulta banco de dados, não acessa ERP, não valida autorização fiscal e não confirma causa raiz sem evidência.

Não armazene senhas, tokens, dados pessoais ou dados fiscais completos. Não use consultas SQL como evidência operacional de atendimento.

## Related

```text
.kora/binding.md
.kora/skills/create-weber-knowledge-article.md
skills/classify-scope.md
skills/create-skill.md
```
