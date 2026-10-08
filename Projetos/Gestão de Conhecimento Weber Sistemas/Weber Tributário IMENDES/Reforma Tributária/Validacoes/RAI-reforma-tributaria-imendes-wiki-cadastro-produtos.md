**Título: Weber Tributário IMENDES - Análise da Reforma Tributária e criação de artigo de Wiki para cadastro de produtos**

### Objetivo

Registrar a atividade interna realizada para analisar a cartilha de Reforma Tributária enviada pela IMENDES e transformar as informações principais em material de apoio para a gestão de conhecimento da WEBER Sistemas.

O objetivo foi resumir os pontos mais relevantes da cartilha, relacionar essas informações com os prints do cadastro fiscal de produtos e criar um artigo em HTML compatível com o padrão colável da Wiki WEBER.

### Ambiente e procedimento

A análise foi realizada com base nos materiais disponíveis na pasta de gestão de conhecimento da WEBER e no PDF enviado pela IMENDES.

Foram utilizados como fonte:

- cartilha `Cartilha Reforma Tributária.pdf`, enviada pela IMENDES;
- print `PRODUTOS ICMS.png`;
- print `PRODUTOS PIS COFINS.png`;
- print `PRODUTOS IBS CBS.png`;
- contexto local da KORA para Gestão de Conhecimento Weber Sistemas;
- padrão de criação de artigos da Wiki WEBER.

O procedimento executado foi:

1. leitura e extração do conteúdo da cartilha da IMENDES;
2. identificação dos capítulos mais relevantes para cadastro de produtos;
3. análise dos prints das telas fiscais do produto;
4. cruzamento entre os conceitos da cartilha e os campos vistos no sistema WEBER;
5. criação de um resumo interno em Markdown;
6. criação de um HTML inicial para visualização;
7. correção do HTML para o formato colável usado na Wiki WEBER;
8. inclusão de índice no início do artigo, conforme padrão exigido para artigos estruturados.

### Comportamento observado

A cartilha da IMENDES apresenta a Reforma Tributária como uma transição gradual que substitui tributos atuais sobre consumo por novos tributos, principalmente CBS, IBS e Imposto Seletivo.

Durante a análise, foi identificado que o maior impacto operacional para a WEBER está no cadastro de produtos, pois a cartilha destaca a necessidade de classificação correta por item, especialmente com:

- NCM do produto;
- CST-IBS/CBS;
- cClassTrib;
- alíquotas de CBS;
- alíquotas de IBS;
- reduções de alíquota;
- regras de alíquota zero, redução e tributação integral.

Nos prints do sistema, foi observado que o cadastro de produtos mantém as configurações fiscais tradicionais nas abas de ICMS e PIS/COFINS, e também apresenta uma nova tela de configurações fiscais CBS/IBS relacionada à Reforma Tributária.

O artigo inicial foi ajustado porque o primeiro HTML gerado era uma página completa, com estrutura própria de navegador. Em seguida, foi criada uma versão compatível com o padrão da Wiki WEBER, usando apenas o corpo do artigo em HTML simples.

### Comportamento esperado

O conteúdo produzido deve servir como base interna para orientar suporte, implantação, documentação e gestão de conhecimento sobre os impactos da Reforma Tributária no cadastro de produtos.

O artigo deve estar em formato adequado para ser colado na Wiki WEBER, com:

- título;
- índice;
- explicação objetiva do que mudou;
- pontos afetados;
- relação com as telas do sistema;
- orientação para suporte;
- resumo final;
- rastreabilidade técnica interna.

### Resultado e encaminhamento

Foi criado um resumo interno da cartilha da IMENDES relacionando os conceitos da Reforma Tributária aos campos do cadastro de produtos da WEBER.

Também foi criado um artigo HTML colável para Wiki, seguindo o padrão usado nos materiais da WEBER. O artigo explica, de forma resumida e operacional, como as informações da Reforma Tributária podem impactar o cadastro de produtos, principalmente nas configurações de CBS/IBS, NCM, CST-IBS/CBS e cClassTrib.

Durante a revisão, foi identificada a necessidade de sempre incluir índice nos artigos estruturados da Wiki WEBER. A skill local de criação de artigos da WEBER foi atualizada para reforçar essa regra.

### Evidência

Foram utilizados os seguintes arquivos como evidência e fonte da atividade:

- `C:\Users\NOTE-DELL-INTEGRACAO\Downloads\Cartilha Reforma Tributária.pdf`;
- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Prints\PRODUTOS ICMS.png`;
- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Prints\PRODUTOS PIS COFINS.png`;
- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Prints\PRODUTOS IBS CBS.png`;
- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Validacoes\resumo-cartilha-imendes-impactos-cadastro-produtos.md`;
- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Artigos\wiki-reforma-tributaria-imendes-impactos-cadastro-produtos-colavel.html`.

### Descrição da Solução

Foi realizada a análise da cartilha de Reforma Tributária enviada pela IMENDES, com foco nos pontos que afetam o cadastro de produtos no sistema WEBER.

As informações principais foram resumidas e relacionadas com as telas fiscais do cadastro de produtos, incluindo ICMS, PIS/COFINS e a nova configuração de CBS/IBS.

Como resultado, foi criado um artigo em HTML simples, compatível com o padrão colável da Wiki WEBER, contendo índice, explicação do impacto da Reforma Tributária, pontos afetados, orientação para suporte e resumo final.

Também foi ajustada a orientação interna da skill local para reforçar que todo artigo estruturado da Wiki WEBER deve conter índice no início.

### Evidência

Arquivos gerados como resultado da atividade:

- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Validacoes\resumo-cartilha-imendes-impactos-cadastro-produtos.md`;
- `C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Artigos\wiki-reforma-tributaria-imendes-impactos-cadastro-produtos-colavel.html`;
- `C:\Kora\kora-vi\Projetos\Principais Alterações de Usabilidade de Nova Versão - Weber\.kora\skills\create-weber-knowledge-article.md`.
