# Prompt - Oriente o cliente: Weber Tributário

```text
Crie uma seção para adicionar à Wiki de Versão Weber Sistemas.

Título da seção:
Oriente o cliente da seguinte forma

Contexto da wiki:
O artigo explica alterações no Cadastro de Produtos quando o produto está com a flag "Habilita Weber Tributário" ativada.

O que mudou:
Quando o Weber Tributário está habilitado no produto, alguns campos ficam bloqueados para edição manual e destacados em verde.

Campos afetados:
- Descrição do produto
- NCM
- CEST
- Aba ICMS
- Aba PIS/COFINS

Objetivo da seção:
Criar uma orientação prática para o técnico explicar ao cliente o que esse bloqueio significa, quando faz sentido desabilitar a flag e quais cuidados devem ser tomados.

Regras:
- Seguir o padrão da wiki base.
- Escrever em HTML.
- Usar linguagem simples e operacional.
- Não repetir o passo a passo da wiki.
- Não repetir toda a explicação sobre iMendes.
- Não usar linguagem de marketing.
- Usar poucos emojis, apenas se necessário.
- Usar ⚠️ somente para alerta importante.
- Não citar DLL, ZIP, executável, beta ou dados técnicos internos.
- A seção deve funcionar como uma fala orientativa para o técnico usar com o cliente.

Pontos que devem aparecer:
- O bloqueio dos campos não é erro do sistema.
- O bloqueio existe para preservar os dados vinculados ao Weber Tributário.
- Se o cliente precisar alterar manualmente descrição ou informações fiscais, deve desabilitar a flag "Habilita Weber Tributário".
- Ao desabilitar a flag, o produto deixa de receber saneamento fiscal automático.
- A descrição do produto deve ser clara e completa.
- Evitar descrições genéricas, abreviações e apelidos internos.
- Quando não houver código de barras/EAN, a descrição se torna ainda mais importante.
- Antes de alterar manualmente um produto já sincronizado, o cliente deve avaliar o impacto fiscal.

Estrutura obrigatória:

<h2>Oriente o cliente da seguinte forma</h2>

<p>Explicar de forma simples o que o técnico deve dizer ao cliente.</p>

<p>Explicar que o bloqueio não é erro.</p>

<p>Explicar quando desabilitar a flag.</p>

<p>Incluir um alerta com ⚠️ sobre o produto deixar de receber saneamento fiscal automático.</p>

<p>Explicar a importância da descrição clara do produto.</p>

<ul>
  <li>Incluir exemplos ou cuidados com descrição.</li>
</ul>

<p>Finalizar orientando que alterações manuais devem ser avaliadas com cuidado por causa do impacto fiscal.</p>

Saída esperada:
Entregar um arquivo HTML contendo apenas a seção pronta para ser adicionada à wiki, sem explicações fora do HTML.
```

