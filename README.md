<h1 align="center">Gracjan Szymczak</h1>
<h3 align="center">Full-Stack Engineer - buduję produkty od zera do produkcji</h3>

<p align="center">
  Projektuję i wdrażam kompletne platformy webowe: architektura, backend, frontend, UX,
  SEO/GEO i skalowanie. Biorę pełną odpowiedzialność za projekt od pomysłu, przez wdrożenie, po utrzymanie.
</p>

<p align="center">
  <a href="https://www.pxlmedia.pl">pxlmedia.pl</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/gracjan-szymczak-481308242/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="mailto:gracjan@pxlmedia.pl">gracjan@pxlmedia.pl</a>
</p>

---

### Jak pracuję
- **Zero do produkcji** - samodzielnie prowadzę projekt od architektury po deploy i utrzymanie.
- **Marketplace, agregatory, systemy rezerwacyjne, SaaS** - moja naturalna działka.
- **AI jako wzmocnienie** - wykorzystuję nowoczesne narzędzia (w tym AI), żeby dowozić szybciej i podnosić jakość, nie zastępując nimi inżynierii.
- **Jakość** - czysty kod, wydajność, bezpieczeństwo i dopracowane UX/UI.

### Produkty, które zbudowałem / współtworzyłem

| Produkt | Opis | Live |
|---|---|---|
| **Roadence** | Agregator płatnych niezbędników na wyjazd autem po Europie, z własnym silnikiem liczenia trasy i opłat. | [roadence.com](https://roadence.com) |
| **Matura Ustna AI** | EdTech: ewaluator odpowiedzi ustnych oparty na AI, panel użytkownika, płatności, wersja mobilna. | [matura-ustna.pl](https://matura-ustna.pl) |
| **Creative Wave Workspace** | System operacyjny agencji: projekty, klienci, zadania i rozliczenia w jednym miejscu. | [workspace.cwave.pl](https://workspace.cwave.pl) |
| **Vento Profit** | Platforma rekrutacyjna: lejek konwersji, warstwa anti-bot, tracking server-side i powiadomienia SMS. | [ventoprofit.pl](https://ventoprofit.pl) |
| **Plotuch** | Portal medialny z autorskim systemem publikacji (kategorie, planowanie, zaplecze redakcyjne). | [plotuch.pl](https://plotuch.pl) |
| **PXL Media** | Strona agencji z panelem zarządzania treścią i leadami, na własnej infrastrukturze (VPS). | [pxlmedia.pl](https://www.pxlmedia.pl) |
| **Plusik** | Aplikacja cashback / karty zakupowe (współtworzyłem). | [plusik.com](https://plusik.com) |
| **Indeks** | SaaS dla studentów pierwszego roku, międzynarodowy (auto i18n per kraj). | *wkrótce* |
| **HS All Stars** | Serwis eventowy dużego wydarzenia sportowego: system biletowy z kodami QR, formularze, tracking. | *event* |
| **Tower Rank** | Grywalizacyjne PWA: rankingi, powiadomienia push, pełny tryb offline. | *PWA* |

<sub>Kod produktów komercyjnych jest prywatny. Szczegóły architektury i podejścia pokażę chętnie na rozmowie.</sub>

### Open source - próbki warsztatu

Pięć samodzielnych bibliotek (clean-room, bez kodu produktów) - każda pokazuje inną kompetencję: czysta domena, architektura heksagonalna, testy i zielone CI.

| Projekt | Co pokazuje | Status |
|---|---|---|
| **[route-cost-engine](https://github.com/LuckyTexass/route-cost-engine)** | Agregator / silnik cenowy - liczenie pełnego kosztu podróży (winiety, opłaty, parking). | 18 testów · [![CI](https://github.com/LuckyTexass/route-cost-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/LuckyTexass/route-cost-engine/actions/workflows/ci.yml) |
| **[slot-scheduler](https://github.com/LuckyTexass/slot-scheduler)** | System rezerwacyjny - wyznaczanie wolnych terminów, kolizje, bufory. | 26 testów · [![CI](https://github.com/LuckyTexass/slot-scheduler/actions/workflows/ci.yml/badge.svg)](https://github.com/LuckyTexass/slot-scheduler/actions/workflows/ci.yml) |
| **[feed-forge](https://github.com/LuckyTexass/feed-forge)** | Python - walidacja i normalizacja product feedu e-commerce (mypy strict). | 20 testów · [![CI](https://github.com/LuckyTexass/feed-forge/actions/workflows/ci.yml/badge.svg)](https://github.com/LuckyTexass/feed-forge/actions/workflows/ci.yml) |
| **[conversion-relay](https://github.com/LuckyTexass/conversion-relay)** | Integracje / tracking server-side - idempotencja, retry z backoff. | 24 testy · [![CI](https://github.com/LuckyTexass/conversion-relay/actions/workflows/ci.yml/badge.svg)](https://github.com/LuckyTexass/conversion-relay/actions/workflows/ci.yml) |
| **[llm-answer-grader](https://github.com/LuckyTexass/llm-answer-grader)** | AI w produkcie - ocena odpowiedzi przez LLM za portem, z guardrails i deterministyczną agregacją. | 24 testy · [![CI](https://github.com/LuckyTexass/llm-answer-grader/actions/workflows/ci.yml/badge.svg)](https://github.com/LuckyTexass/llm-answer-grader/actions/workflows/ci.yml) |

### Automatyzacje i integracje

Poza produktami napisałem dziesiątki automatyzacji spinających sklepy, systemy reklamowe, CRM-y i komunikację:

- **Eldar** - feed produktowy zasilający Meta i Google Merchant Center, automatyczny system raportów PDF z IdoSell, migracja i automatyzacja mailingu/SMS, pomiar konwersji offline.
- **Vento Profit** - server-side tracking (Meta CAPI), automatyczny upload konwersji offline do Google Ads, deduplikacja leadów, SMS (Twilio), integracja z Traffit.
- **Plusik** - integracje w aplikacji cashback oraz automatyzacje po stronie danych i komunikacji.
- **Wac Toja** - integracje reklamowo-analityczne i automatyczny reporting kampanii.
- **HS All Stars** - automatyczne redirecty śledzące, generowanie i obsługa biletów QR, mailingi eventowe.

### Stack
**Języki:** `JavaScript` · `TypeScript` · `SQL` · `Python` · `HTML / CSS`
**Frontend:** `React` · `Next.js` · `Tailwind` · `PWA`
**Backend:** `Node.js` · `PostgreSQL / Supabase` · `REST API`
**Infra i integracje:** `Linux / VPS` · `Vercel` · `Stripe` · `Meta CAPI` · `Google Ads API` · `CI/CD` · `Webhooki / cron`

### Kontakt
**gracjan@pxlmedia.pl** · [pxlmedia.pl](https://www.pxlmedia.pl) · [LinkedIn](https://www.linkedin.com/in/gracjan-szymczak-481308242/)

<sub>Szukasz kogoś, kto weźmie projekt od zera i doprowadzi go do produkcji? Pogadajmy.</sub>
