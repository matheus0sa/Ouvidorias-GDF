# Ouvidorias-GDF
 
O objetivo desse projeto é criar um pipeline de dados das ouvidorias do GDF que resultrá em um dashboard.

Serão consideradas as 3 etapas de ETL:

- A extração é feita do site do GDF http://www.painel.ouv.df.gov.br/dashboard utilizando o framework Selenium.

- Como a base de dados da ouvidoria é bem organizada, o tratamento de dados é simples.

- O carregamento é feito em um banco local no SQL Server.

O projeto ainda está sendo feito, e essas são minhas próximas ações:

⬜ Descobrir como usar o selenium com o navegador "invisível" e baixar arquivos (por algum motivo, quando ativo "headless" não consigo baixar a base de dados)<br>
⬜ Alterar o código para baixar a base de forma incremental (A atualmente está baixando a base do ano inteiro sempre que rodo o código)<br>
⬜ Criar um conexão ODBC com o Power BI e criar um dashboard
