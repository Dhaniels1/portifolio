# Portfólio — Daniel Castro

Portfólio pessoal desenvolvido em **HTML5 e CSS3**, com layout responsivo e acessível, para apresentar projetos reais de desenvolvimento web, APIs e análise de dados.

**Repositório:** https://github.com/Dhaniels1/portifolio

> O nome exibido neste portfólio é **Daniel Castro**, conforme a identidade desejada. O projeto original foi modernizado em outubro de 2026.

## Projetos apresentados

| Projeto | Tecnologias principais | Código | Demonstração |
| --- | --- | --- | --- |
| Biblioteca Digital | Laravel 12, PHP, PostgreSQL, Sanctum | [biblioteca-api](https://github.com/Dhaniels1/biblioteca-api) | [Abrir aplicação](https://biblioteca-api-dhaniels1.onrender.com) |
| Dashboard de Vendas 2020 | Python, Dash, Plotly, Pandas | [dashboard-vendas-2020](https://github.com/Dhaniels1/dashboard-vendas-2020) | [Abrir dashboard](https://dashboard-vendas-2020.onrender.com) |
| Óticas Malta | React, React Router, Tailwind CSS | [oticas-malta](https://github.com/Dhaniels1/oticas-malta) | Não verificada nesta revisão |
| TechStore | HTML5, CSS3 | [TechStore](https://github.com/Dhaniels1/TechStore) | Código no GitHub |
| TechWave | HTML5, CSS3 | [olamundoweb1](https://github.com/Dhaniels1/olamundoweb1) | Código no GitHub |

Os projetos **TechStore** e **TechWave** são exercícios acadêmicos e não representam serviços comerciais em funcionamento. O projeto Óticas Malta é um site de apresentação; suas informações de atendimento devem ser conferidas antes de uso comercial.

**Privacidade:** o repositório `upando-solo` é privado e não foi incluído no portfólio público. Caso seja publicado no futuro, o acesso e os dados pessoais precisam ser revisados separadamente.

## Páginas e navegação

- `index.html`: página inicial com apresentação, tecnologias e dois projetos publicados.
- `sobre.html`: formação, trajetória técnica e áreas de interesse.
- `projetos.html`: cinco projetos públicos com descrições e links.
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

## Hospedar com GitHub Pages (opcional)

O projeto é compatível com GitHub Pages porque utiliza arquivos HTML/CSS estáticos e caminhos relativos.

1. Acesse **Settings → Pages** do repositório.
2. Em **Build and deployment**, escolha **Deploy from a branch**.
3. Selecione a branch **main** e a pasta **/(root)**, depois salve.
4. Após a publicação, o endereço esperado para esse nome de repositório será `https://dhaniels1.github.io/portifolio/`, **desde que o GitHub Pages esteja habilitado e o deploy tenha funcionado**.

A simples presença do código na branch `main` não garante que o site já esteja publicado via Pages.

## Contato e transparência

O e-mail utilizado foi preservado da versão anterior do site. Confirme que ele continua correto antes de divulgar amplamente o portfólio.

A revisão removeu um formulário que exibia confirmação de "mensagem enviada" sem realizar envio real. Agora o site orienta contato pelo cliente de e-mail do visitante ou pelo GitHub, sem alegar que um servidor recebeu mensagens.

## Licença

Os arquivos são disponibilizados neste repositório para fins de apresentação e avaliação. Nenhuma licença de reutilização de terceiros é concedida implicitamente.
