"""Verificações leves do portfólio estático, sem dependências externas."""
from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
NAV_PAGES = ("index.html", "sobre.html", "projetos.html", "contato.html")
PAGES = NAV_PAGES + (
    "estudo-cuidar.html", "estudo-biblioteca.html", "estudo-dashboard.html",
)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.scripts = []
        self.forms = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag in {"a", "link", "img", "script", "source"}:
            target = a.get("href") if tag in {"a", "link"} else a.get("src")
            if target:
                self.links.append((tag, target, a))
        if tag == "form":
            self.forms.append(a)


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


class PortfolioTest(unittest.TestCase):
    def test_paginas_e_css_existem(self):
        for page in PAGES:
            with self.subTest(page=page):
                self.assertTrue((ROOT / page).is_file())
        self.assertTrue((ROOT / "assets/css/style.css").is_file())

    def test_identidade_e_navegacao(self):
        for page in PAGES:
            with self.subTest(page=page):
                body = (ROOT / page).read_text(encoding="utf-8")
                self.assertIn("Daniel Castro", body)
                self.assertIn('lang="pt-BR"', body)
                parser = parse_page(ROOT / page)
                self.assertIn("conteudo", parser.ids)
                links = {url for tag, url, _ in parser.links if tag == "a"}
                self.assertTrue(set(NAV_PAGES).issubset(links))

    def test_links_locais_e_ancoras(self):
        for page in PAGES:
            parser = parse_page(ROOT / page)
            for tag, href, attrs in parser.links:
                with self.subTest(page=page, link=href):
                    parsed = urlsplit(href)
                    if parsed.scheme in {"http", "https", "mailto", "tel", "data"} or href.startswith("//"):
                        if tag == "a" and attrs.get("target") == "_blank":
                            rel = (attrs.get("rel") or "").split()
                            self.assertIn("noopener", rel)
                            self.assertIn("noreferrer", rel)
                        continue
                    if parsed.scheme:
                        self.fail(f"Protocolo inesperado: {href}")
                    relative = unquote(parsed.path)
                    target = (ROOT / page).parent / relative if relative else ROOT / page
                    self.assertTrue(target.is_file(), f"Arquivo não encontrado: {href} em {page}")
                    if parsed.fragment:
                        target_parser = parser if target.resolve() == (ROOT / page).resolve() else parse_page(target)
                        self.assertIn(unquote(parsed.fragment), target_parser.ids, f"Âncora ausente: {href}")

    def test_portfolio_mostra_projetos_reais(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        projects = (ROOT / "projetos.html").read_text(encoding="utf-8")
        for repo in ("biblioteca-api", "dashboard-vendas-2020", "oticas-malta", "TechStore", "Projeto-Extensao", "carrinho-iot-esp32"):
            self.assertIn("https://github.com/Dhaniels1/" + repo, projects)
        for live in ("biblioteca-api-dhaniels1.onrender.com", "dashboard-vendas-2020.onrender.com"):
            self.assertIn(live, index)
            self.assertIn(live, projects)
        self.assertNotIn("olamundoweb1", projects)
        self.assertNotIn("TechWave", projects)
        self.assertIn("FAMINAS", index)
        self.assertIn("FAMINAS", (ROOT / "sobre.html").read_text(encoding="utf-8"))
        self.assertIn("projeto acadêmico independente", projects.lower())
        self.assertIn("pendentes de validação", projects)
        self.assertEqual(projects.count('<article class="project-card">'), 6)
        self.assertNotIn("upando-solo", index.lower())
        self.assertNotIn("upando-solo", projects.lower())
        self.assertNotIn("Café Aconchego", projects)
        self.assertNotIn("TaskFlow", projects)


    def test_estudos_de_caso_e_integracao(self):
        projects = (ROOT / "projetos.html").read_text(encoding="utf-8")
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        expected = {
            "estudo-cuidar.html": ("Projeto-Extensao", "cuidar-muriae-demo.pages.dev"),
            "estudo-biblioteca.html": ("biblioteca-api", "biblioteca-api-dhaniels1.onrender.com"),
            "estudo-dashboard.html": ("dashboard-vendas-2020", "dashboard-vendas-2020.onrender.com"),
        }
        for page, (repo, demo) in expected.items():
            with self.subTest(page=page):
                body = (ROOT / page).read_text(encoding="utf-8")
                self.assertIn(repo, body)
                self.assertIn(demo, body)
                self.assertIn(page, projects)
                self.assertIn(page, home)

    def test_canonicos_metadados_e_sitemap(self):
        from xml.etree import ElementTree as ET

        base = "https://daniel-castro-portfolio.pages.dev/"
        urls = {base + ("" if page == "index.html" else page) for page in PAGES}
        for page in PAGES:
            with self.subTest(page=page):
                body = (ROOT / page).read_text(encoding="utf-8")
                canonical = base + ("" if page == "index.html" else page)
                self.assertIn('rel="canonical" href="' + canonical + '"', body)
                for prop in ('og:title', 'og:description', 'og:url'):
                    self.assertIn('property="' + prop + '"', body)
                self.assertIn('name="twitter:card"', body)
        root = ET.fromstring((ROOT / "sitemap.xml").read_text(encoding="utf-8"))
        namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        listed = {el.text for el in root.iter(namespace + "loc")}
        self.assertEqual(listed, urls)
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn(base + "sitemap.xml", robots)

    def test_contato_nao_finge_envio(self):
        page = (ROOT / "contato.html").read_text(encoding="utf-8")
        self.assertIn("mailto:", page)
        self.assertNotIn('<form', page.lower())
        self.assertNotIn("Mensagem enviada com sucesso", page)
        self.assertFalse((ROOT / "assets/js/script.js").exists())


if __name__ == "__main__":
    unittest.main()
