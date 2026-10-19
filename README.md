# Portfólio — Daniel Castro

Portfólio pessoal desenvolvido em **HTML5 e CSS3**, com layout responsivo e acessível, para apresentar experiência profissional em Tecnologia da Informação, formação e projetos reais de desenvolvimento web, APIs, análise de dados e IoT.

**Site publicado:** https://dhaniels1.github.io/portifolio/  
**Repositório:** https://github.com/Dhaniels1/portifolio

> O nome exibido neste portfólio é **Daniel Castro**, conforme a identidade desejada. O projeto original foi modernizado em outubro de 2026.

## Experiência e formação

O site apresenta **Daniel Castro** como **Auxiliar de Tecnologia da Informação na FAMINAS**, com experiência em suporte técnico, atendimento de chamados e sistemas corporativos, além de sua formação em Gestão da Tecnologia da Informação no IF Sudeste MG — Campus Muriaé. Não inclui dados internos da instituição nem detalhes confidenciais.

## Projetos apresentados

| Projeto | Tecnologias principais | Código | Demonstração |
| --- | --- | --- | --- |
| Biblioteca Digital | Laravel 12, PHP, PostgreSQL, Sanctum | [biblioteca-api](https://github.com/Dhaniels1/biblioteca-api) | [Abrir aplicação](https://biblioteca-api-dhaniels1.onrender.com) |
| Dashboard de Vendas 2020 | Python, Dash, Plotly, Pandas | [dashboard-vendas-2020](https://github.com/Dhaniels1/dashboard-vendas-2020) | [Abrir dashboard](https://dashboard-vendas-2020.onrender.com) |
| Ateliê Lume (projeto Óticas Malta) | React, React Router, Tailwind CSS | [oticas-malta](https://github.com/Dhaniels1/oticas-malta) | [Site fictício no Netlify](https://oticas-malta-demo.netlify.app/) |
| TechStore | HTML5, CSS3, imagens de IA | [TechStore](https://github.com/Dhaniels1/TechStore) | [Vitrine fictícia no GitHub Pages](https://dhaniels1.github.io/TechStore/) |
| Cuidar Muriaé — Projeto de Extensão | JavaScript, HTML5, CSS3 | [Projeto-Extensao](https://github.com/Dhaniels1/Projeto-Extensao) | Protótipo em desenvolvimento; não é serviço oficial de hospitais |
| Carrinho IoT com ESP32 | C++/Arduino, ESP32, Wi-Fi | [carrinho-iot-esp32](https://github.com/Dhaniels1/carrinho-iot-esp32) | Código e demonstração local; funcionalidades novas exigem testes no hardware |

A **TechStore** e o **Ateliê Lume (repositório Óticas Malta)** são sites de empresas fictícias, com imagens criadas por IA, sem serviços comerciais ou produtos reais. O **Cuidar Muriaé** é um protótipo acadêmico independente em planejamento, sem vínculo institucional ou orientações hospitalares oficiais. O **Carrinho IoT** possui recursos testados em montagem anterior e recursos novos ainda pendentes de validação física.

**Privacidade:** o repositório `upando-solo` é privado e não foi incluído no portfólio público. Caso seja publicado no futuro, o acesso e os dados pessoais precisam ser revisados separadamente.

## Páginas e navegação

- `index.html`: página inicial com apresentação, tecnologias e dois projetos publicados.
- `sobre.html`: experiência profissional como Auxiliar de TI na FAMINAS, formação, trajetória técnica e áreas de interesse.
- `projetos.html`: seis projetos públicos com descrições e links.
- `contato.html`: contato por e-mail via `mailto:` e perfil público no GitHub.
- `assets/css/style.css`: estilos e regras responsivas.

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

Há testes de integridade de links locais, navegação, identidade do portfólio e ausência de formulário que simule envio sem backend.

```bash
python -m unittest discover -s tests -v
```

O workflow `.github/workflows/validacao.yml` roda os testes em pushes e pull requests.

## Publicação com GitHub Pages

O site está publicado em **https://dhaniels1.github.io/portifolio/**. A publicação da versão revisada foi confirmada pelo workflow automático **pages build and deployment** do GitHub em 19/10/2026, com etapa de deploy concluída com sucesso.

A configuração utiliza a branch **main**. Como o site é estático e usa caminhos relativos, não necessita backend, banco de dados nem build com Node.js. Novos pushes na branch de publicação podem iniciar uma nova implantação no GitHub Pages.

Para conferir ou alterar a configuração, acesse **Settings → Pages** no repositório.

## Contato e transparência

O e-mail utilizado foi preservado da versão anterior do site. Confirme que ele continua correto antes de divulgar amplamente o portfólio.

A revisão removeu um formulário que exibia confirmação de "mensagem enviada" sem realizar envio real. Agora o site orienta contato pelo cliente de e-mail do visitante ou pelo GitHub, sem alegar que um servidor recebeu mensagens.

## Licença

Os arquivos são disponibilizados neste repositório para fins de apresentação e avaliação. Nenhuma licença de reutilização de terceiros é concedida implicitamente.
