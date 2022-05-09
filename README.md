# Ouvidorias-GDF
 
O objetivo desse projeto é criar um pipeline de dados das ouvidorias do GDF que resultrá em um dashboard.

Serão consideradas as 3 etapas de ETL:

- A extração é feita do site do GDF http://www.painel.ouv.df.gov.br/dashboard utilizando o framework Selenium.

- Como a base de dados da ouvidoria é bem organizada, o tratamento de dados é simples.

- O carregamento é feito em um banco local no SQL Server.

O projeto ainda está sendo feito, e essas são minhas próximas ações:

⬜ Alterar o código para baixar a base de forma incremental (A atualmente está baixando a base do ano inteiro sempre que rodo o código<br>
⬜ Criar um dashboard com o Power BI

Ações finalizadas:<br>
✅ Descobrir como usar o selenium com o navegador "invisível" e baixar arquivos<br>
✅ Criar automação para baixar a base de ouvidorias desse ano <br>
✅ Criar banco de dados local com SQL Server <br>
✅ Criar conexão entre o python e o SQL Server


Comecei o dashboard, o mapa no dashboard não ficou legal, vou trabalhar nele mas ja é possível visualiza-lo no link:

https://app.powerbi.com/view?r=eyJrIjoiYjNhZjc2NTEtZmY1Zi00NTczLTg3NmQtOTFiNDYyZjI1YzczIiwidCI6ImVjMzU5YmExLTYzMGItNGQyYi1iODMzLWM4ZTZkNDhmODA1OSJ9
