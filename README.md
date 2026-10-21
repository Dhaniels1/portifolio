# Portfólio — Daniel Castro

Portfólio pessoal desenvolvido em **HTML5 e CSS3**, com layout responsivo e acessível, para apresentar experiência profissional em Tecnologia da Informação, formação e projetos reais de desenvolvimento web, APIs, análise de dados e IoT.

**Site principal:** https://daniel-castro-portfolio.pages.dev/
**Espelho no GitHub Pages:** https://dhaniels1.github.io/portifolio/  
**Repositório:** https://github.com/Dhaniels1/portifolio

> O nome exibido neste portfólio é **Daniel Castro**, conforme a identidade desejada. O projeto original foi modernizado em outubro de 2026.

## Experiência e formação

O site apresenta **Daniel Castro** como **Auxiliar de Tecnologia da Informação na FAMINAS**, com experiência em suporte técnico, atendimento de chamados e sistemas corporativos, além de sua formação em Gestão da Tecnologia da Informação no IF Sudeste MG — Campus Muriaé. Não inclui dados internos da instituição nem detalhes confidenciais.

## Projetos apresentados

| Projeto | Tecnologias principais | Código | Demonstração |
| --- | --- | --- | --- |
| Biblioteca Digital | Laravel 12, PHP, MySQL, Sanctum | [biblioteca-api](https://github.com/Dhaniels1/biblioteca-api) | [Abrir aplicação](https://biblioteca-api-dhaniels1.onrender.com) |
| Dashboard de Vendas 2020 | Python, Dash, Plotly, Pandas | [dashboard-vendas-2020](https://github.com/Dhaniels1/dashboard-vendas-2020) | [Abrir dashboard](https://dashboard-vendas-2020.onrender.com) |
| Ateliê Lume (projeto Óticas Malta) | React, React Router, Tailwind CSS | [oticas-malta](https://github.com/Dhaniels1/oticas-malta) | [Demonstração no GitHub Pages](https://dhaniels1.github.io/oticas-malta/) |
| TechStore | HTML5, CSS3, imagens de IA | [TechStore](https://github.com/Dhaniels1/TechStore) | [Vitrine fictícia no GitHub Pages](https://dhaniels1.github.io/TechStore/) |
| Cuidar Muriaé — Projeto de Extensão | JavaScript, HTML5, CSS3 | [Projeto-Extensao](https://github.com/Dhaniels1/Projeto-Extensao) | [Abrir simulação 0.2](https://cuidar-muriae-demo.pages.dev/) |
| Carrinho IoT com ESP32 | C++/Arduino, ESP32, Wi-Fi | [carrinho-iot-esp32](https://github.com/Dhaniels1/carrinho-iot-esp32) | Código e demonstração local; funcionalidades novas exigem testes no hardware |

A **TechStore** e o **Ateliê Lume (repositório Óticas Malta)** são sites de empresas fictícias, com imagens criadas por IA, sem serviços comerciais ou produtos reais. O **Cuidar Muriaé** é um protótipo acadêmico independente em planejamento, sem vínculo institucional: a versão 0.2 utiliza apenas unidades e informações fictícias, não orientações de hospitais reais. O **Carrinho IoT** possui recursos testados em montagem anterior e recursos novos ainda pendentes de validação física.

**Privacidade:** o repositório `upando-solo` é privado e não foi incluído no portfólio público. Caso seja publicado no futuro, o acesso e os dados pessoais precisam ser revisados separadamente.

## Páginas e navegação

- `index.html`: página inicial com apresentação, tecnologias, destaques e links para estudos de caso.
- `sobre.html`: experiência profissional como Auxiliar de TI na FAMINAS, formação, trajetória técnica e áreas de interesse.
- `projetos.html`: seis projetos públicos com descrições, demonstrações e estudos de caso.
- `contato.html`: contato por e-mail via `mailto:` e perfil público no GitHub.
- `estudo-cuidar.html`: evolução de protótipo acadêmico, cenário sintético e governança.
- `estudo-biblioteca.html`: arquitetura, autenticação, regras e testes de API REST.
- `estudo-dashboard.html`: preparação de dados, visualizações, filtros e limitações.
- `assets/css/style.css`: estilos e regras responsivas.
- `robots.txt` e `sitemap.xml`: indexação e descoberta das páginas na Cloudflare.

O portfólio é **estático** e não possui backend, formulário de envio, APIs próprias nem banco de dados. As aplicações citadas são projetos independentes e podem ter indisponibilidades temporárias associadas aos planos gratuitos de hospedagem.

## Executar localmente

Clone e abra `index.html` diretamente no navegador:

```bash
git clone https://github.com/Dhaniels1/portifolio.git
cd portifolio
```

Para testar também com um servidor local:

```bash
python -m http.server 8000
```

Acesse `http://localhost:8000`. Nenhum `npm install` é necessário.

## Validação

Há testes de integridade de links locais, navegação, identidade do portfólio, integração de estudos de caso, metadados, sitemap e ausência de formulário que simule envio sem backend.

```bash
python -m unittest discover -s tests -v
```

O workflow `.github/workflows/validacao.yml` roda os testes em pushes e pull requests.

## Publicação com Cloudflare Pages e GitHub Pages

A publicação principal está em **https://daniel-castro-portfolio.pages.dev/**, conectada ao GitHub pela Cloudflare Pages.

Há também uma versão no **https://dhaniels1.github.io/portifolio/**. A publicação da versão revisada foi confirmada pelo workflow automático **pages build and deployment** do GitHub em 19/10/2026, com etapa de deploy concluída com sucesso.

A configuração utiliza a branch **main**. Como o site é estático e usa caminhos relativos, não necessita backend, banco de dados nem build com Node.js. Novos pushes na branch `main` podem disparar um deploy na Cloudflare e na configuração de espelho do GitHub Pages.

Para conferir o espelho, acesse **Settings → Pages** no repositório. Para a publicação principal, consulte Cloudflare Pages.

## Estudos de caso

- [Cuidar Muriaé 0.2](https://daniel-castro-portfolio.pages.dev/estudo-cuidar.html): demo 100% sintética, sem parceria institucional.
- [Biblioteca API](https://daniel-castro-portfolio.pages.dev/estudo-biblioteca.html): API REST em Laravel com CRUD e autenticação.
- [Dashboard de Vendas](https://daniel-castro-portfolio.pages.dev/estudo-dashboard.html): Python, Dash, Plotly e análise de dados de 2020.

Os conteúdos descrevem funcionalidades documentadas nos respectivos repositórios, sem afirmar métricas de impacto ou disponibilidade permanente dos serviços.

## Contato e transparência

O e-mail utilizado foi preservado da versão anterior do site. Confirme que ele continua correto antes de divulgar amplamente o portfólio.

A revisão removeu um formulário que exibia confirmação de "mensagem enviada" sem realizar envio real. Agora o site orienta contato pelo cliente de e-mail do visitante ou pelo GitHub, sem alegar que um servidor recebeu mensagens.

## Licença

Os arquivos são disponibilizados neste repositório para fins de apresentação e avaliação. Nenhuma licença de reutilização de terceiros é concedida implicitamente.
