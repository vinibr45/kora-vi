# Resumo Da Cartilha IMENDES - Impactos No Cadastro De Produtos

## Status

rascunho

## Fonte

```text
C:\Users\NOTE-DELL-INTEGRACAO\Downloads\Cartilha Reforma Tributária.pdf
```

Cartilha da IMENDES, edição 2026, conteúdo revisado em agosto de 2026.

## Resumo Executivo

A Reforma Tributária substitui gradualmente cinco tributos sobre o consumo:

- PIS;
- COFINS;
- ICMS;
- ISS;
- IPI.

Por três novos tributos:

- CBS;
- IBS;
- Imposto Seletivo.

Para o cadastro de produtos da WEBER, o ponto mais importante é que cada item da nota passa a depender de classificação correta para IBS/CBS. A cartilha destaca dois novos campos obrigatórios por item:

- `CST-IBS/CBS`;
- `cClassTrib`.

Esses campos trabalham em conjunto. O CST indica a categoria geral de tributação. O cClassTrib detalha qual regra legal se aplica ao item.

## Linha Do Tempo Relevante

```text
2026
Ano de teste.
CBS 0,9% e IBS 0,1% destacados na nota.
Sem recolhimento para quem cumprir as obrigações.
Obrigatório destacar IBS e CBS na NF-e a partir de 03/08/2026.

2027
CBS entra para valer.
PIS e COFINS são extintos.
IBS segue simbólico.
Imposto Seletivo começa a produzir efeitos.

2029 a 2032
ICMS e ISS reduzem gradualmente.
IBS cresce gradualmente.
Benefícios fiscais de ICMS vão sendo extintos na mesma escada.

2033
Sistema pleno.
ICMS e ISS extintos.
Modelo passa a funcionar com CBS, IBS e IS.
```

## O Que Impacta Diretamente No Cadastro De Produtos

### 1. NCM

A cartilha afirma que o caminho de classificação começa pela identificação do item, usando NCM do produto ou natureza do serviço.

Impacto no sistema WEBER:

- o campo `NCM` do cadastro de produto fica ainda mais crítico;
- erro de NCM pode gerar enquadramento errado de CBS/IBS;
- produtos sem NCM revisado devem entrar em lista de validação.

### 2. CST-IBS/CBS

O CST-IBS/CBS indica a categoria geral da tributação:

- tributação integral;
- alíquota reduzida;
- monofásica;
- diferimento;
- isenção;
- imunidade;
- alíquota zero.

Impacto no sistema WEBER:

- corresponde ao campo de CST/descrição CST visto na tela de CBS/IBS;
- deve ser preenchido por item;
- CST incompatível com cClassTrib pode rejeitar nota.

### 3. cClassTrib

O cClassTrib detalha a regra exata da lei aplicável ao item e está ligado a dispositivo legal específico.

Impacto no sistema WEBER:

- corresponde ao campo `Classificação Tributária CBS/IBS` visto na tela;
- deve ser usado sempre junto com o CST;
- define indicadores de campos exigidos no XML;
- pode indicar percentual de redução aplicável;
- deve vir de tabela oficial atualizada.

### 4. Alíquotas CBS, IBS Estadual E IBS Municipal

A cartilha informa que 2026 é ano de teste, com:

- CBS 0,9%;
- IBS 0,1%;
- IBS municipal 0% no exemplo de referência da transição.

Impacto no sistema WEBER:

- a tela `Configurações Fiscais por Produto` possui campos de alíquota CBS, alíquota IBS UF e alíquota IBS Municipal;
- em 2026, esses campos precisam permitir destaque em nota mesmo sem recolhimento;
- valores futuros devem ser tratados como referência/estimativa até definição oficial.

### 5. Reduções E Alíquota Zero

A cartilha descreve tratamentos diferenciados:

- alíquota zero;
- redução de 60%;
- redução de 30%;
- alíquota padrão;
- regimes específicos.

Impacto no sistema WEBER:

- os campos `% Redução Aliq IBS` e `% Redução Aliq CBS` devem refletir o tratamento indicado pelo enquadramento;
- produtos da cesta básica, hortifruti e alimentos exigem atenção especial;
- benefícios não devem ser aplicados sem base legal.

### 6. PIS/COFINS E ICMS Durante A Transição

Os tributos antigos convivem com os novos durante anos.

Impacto no sistema WEBER:

- as abas `ICMs` e `PisCofins` continuam relevantes;
- o botão/tela de `ReformaTributária` complementa o cadastro, não substitui imediatamente as abas atuais;
- o suporte precisa explicar que ICMS/PIS/COFINS e CBS/IBS convivem no período de transição.

## Relação Com Os Prints Do Sistema

### Print `PRODUTOS ICMS.png`

Mostra o cadastro fiscal tradicional de ICMS:

- CST;
- CSON;
- tributação;
- alíquota ICMS;
- PBC;
- FCP;
- MVA;
- IPI;
- benefício fiscal.

Impacto:

- permanece necessário durante a transição;
- benefícios de ICMS podem ser afetados entre 2029 e 2032.

### Print `PRODUTOS PIS COFINS.png`

Mostra configuração de PIS/COFINS de entrada e saída:

- CST de entrada;
- CST de saída;
- alíquota PIS;
- alíquota COFINS;
- natureza da receita.

Impacto:

- permanece necessário em 2026;
- tende a perder centralidade a partir de 2027, quando PIS/COFINS são substituídos pela CBS.

### Print `PRODUTOS IBS CBS.png`

Mostra a nova configuração CBS/IBS:

- classificação tributária CBS/IBS;
- descrição CST;
- alíquota CBS;
- alíquota IBS Municipal;
- alíquota IBS UF;
- reduções CBS/IBS;
- opção de alíquotas personalizadas.

Impacto:

- é a tela mais diretamente ligada à Reforma Tributária;
- deve receber informações de classificação por item;
- precisa estar alinhada às tabelas oficiais e às informações da IMENDES.

## Pontos De Atenção Para A WEBER

- A classificação é por item, não por nota inteira.
- CST e cClassTrib devem ser usados em par.
- Tabelas oficiais podem mudar; o sistema precisa acompanhar versões.
- cClassTrib inexistente ou incompatível rejeita nota.
- Campos exigidos pelo indicador do código precisam ser preenchidos.
- Enquadramento em benefício sem base legal gera risco fiscal.
- 2026 deve ser tratado como ano de teste e preparação cadastral.
- A IMENDES aparece como apoio para automatizar cadastro, classificação, cálculo e conformidade.

## Perguntas Para Validação Interna

- O campo `Classificação Tributária CBS/IBS` na tela WEBER é exatamente o cClassTrib?
- O campo `Descrição CST` é derivado automaticamente da classificação escolhida?
- A IMENDES enviará CST e cClassTrib por produto?
- A IMENDES enviará percentuais de redução para CBS/IBS?
- Quando o usuário deve marcar alíquota personalizada?
- A tela CBS/IBS será usada apenas para venda presencial ao consumidor final ou haverá outras operações?
- O botão `ReformaTributária` abre sempre essa tela?
