<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg" />
  <img alt="The Earl of Lemongrab presents Mark Jayson Farol, quantitative economist." src="assets/hero-light.svg" width="100%" />
</picture>

</div>

I build **research-grade data systems** for messy administrative datasets and use them to study **higher-education finance, student aid, college pricing, and macroeconomic questions.**

M.A. in Quantitative Business Economics and B.S.B.A. in Economics with a theatre minor, University of Nevada, Las Vegas. The work sits across economics, data engineering, empirical research, and technical communication: I write the pipeline, run the regression, and ship the platform.

Open to **Economist, Research Analyst, Data Analyst, and Financial Analyst** roles. Remote, hybrid, or relocation.

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/stats-light.svg" />
  <img alt="By the numbers. 2004 to 2024 IPEDS file: 147,782 by 2,676. Labeled release full-panel-labels-v1: 141,711 by 2,721. A 39-check acceptance audit. 25-plus years of Title IV volume. 200-plus students a term. 10 researchers mentored." src="assets/stats-light.svg" width="100%" />
</picture>

</div>

The **2004–2024** consolidated IPEDS analysis file is **147,782 rows × 2,676 columns**. Labeled release `full-panel-labels-v1` is **141,711 rows × 2,721 columns**. Builds run a **39-check acceptance audit**.

<div align="center">
  <img src="assets/divider.svg" alt="" width="100%" />
</div>

## Act I — The economist

<details>
<summary><b>Open the curtain — program notes</b></summary>

I immigrated to the United States from the Philippines at 14.

Founder and sole employee of **Mark Jayson Nation LLC** (Las Vegas, formed October 2026). The house ships [Macro by Mark](https://macrobymark.com), an economics learning and U.S. macro research platform; [getriff](https://get-riff.com), an iOS workout app in TestFlight; and a Macro by Mark island-tycoon game now in development.

I edit UNLV's Undergraduate Economics Working Paper Series, which I helped build.

**Research focus:** higher-education pricing, financial-aid packaging, federal cost-of-attendance policy, panel econometrics, causal inference, dynamic specifications, and large-scale data validation.

</details>

### On the research bill

- Published **"Revisiting Bennett's Hypothesis"** in *Spectra Undergraduate Research Journal* (2025)
- Presented at **WEAI's 100th Annual Conference**
- Authored **4 working papers** on higher-ed pricing, financial aid packaging, and federal cost-of-attendance policy
- Helped build, and now edit, the **UNLV Undergraduate Economics Working Paper Series**

### Teaching and mentorship

At UNLV I supported instruction in economics, statistics, econometrics, and senior capstone research: lectures and review sessions for **200+ students a semester**, course materials, high-volume office hours, and **10 undergraduate researchers** mentored through end-to-end empirical projects.

## Act II — The work

### Now playing

<a href="https://macrobymark.com">
  <img src="assets/posters/macro.svg" alt="Macro by Mark, economics learning and U.S. macro research" width="100%" />
</a>

Indicators, release calendars, dashboards, forecasting, and reference workflows. Integrates **FRED, BEA, BLS, Census, and World Bank**, with **Marco**, an AI macro assistant, and a status page built to **fail loud, never lie green.**

<a href="https://get-riff.com">
  <img src="assets/posters/riff.svg" alt="getriff, an iOS workout app in TestFlight" width="100%" />
</a>

iOS workout app, in TestFlight.

A Macro by Mark island-tycoon game is in development.

### The data season

<a href="https://github.com/markjayson13/IPEDSDB_Panel">
  <img src="assets/posters/ipedsdb.svg" alt="IPEDSDB_Panel. 2004 to 2024 consolidated file, 147,782 by 2,676. Labeled release full-panel-labels-v1, 141,711 by 2,721." width="100%" />
</a>

Reproducible Python and SQL pipeline from NCES/IPEDS Access databases to unbalanced UNITID-by-year panels. The **2004–2024** consolidated analysis file is **147,782 × 2,676**. Labeled release `full-panel-labels-v1` is **141,711 × 2,721**.

<a href="https://github.com/markjayson13/FSAVolumeReports_Panel">
  <img src="assets/posters/fsa.svg" alt="FSAVolumeReports_Panel, 25-plus years of Title IV volume reports" width="100%" />
</a>

Downloads, harmonizes, panelizes, QA-checks, and exports **25+ years** of Federal Student Aid Title IV volume reports into institution-by-award-year panels for grants, campus-based aid, and loans.

<a href="https://github.com/markjayson13/IPEDS-FSA_Panel">
  <img src="assets/posters/ipeds-fsa.svg" alt="IPEDS-FSA_Panel, Federal Student Aid reports linked to IPEDS" width="100%" />
</a>

Links those FSA volume reports to IPEDS institutions, aligns aid periods, and exports combined research panels.

<a href="https://github.com/markjayson13/IPEDS_Paneling">
  <img src="assets/posters/paneling.svg" alt="IPEDS_Paneling, a DuckDB pipeline for NCES IPEDS" width="100%" />
</a>

Python and DuckDB pipeline that downloads, harmonizes, QC-validates, and panelizes NCES IPEDS into research-ready institution-year datasets.

<a href="https://github.com/markjayson13/COA_FINAID_SUBS">
  <img src="assets/posters/coa.svg" alt="COA_FINAID_SUBS, replication code for cost-of-attendance research" width="100%" />
</a>

Public replication code for research on cost-of-attendance headroom and institutional grant aid, built from the IPEDS panel. Baseline sample: four-year Title IV public and private nonprofit institutions, 2009–2023.

### Scenery

<a href="https://github.com/markjayson13/markjaysonwebsite-v2">
  <img src="assets/posters/site.svg" alt="markjaysonwebsite-v2, personal site built with Astro" width="100%" />
</a>

Personal site, Astro on Cloudflare Pages. Live at [markjayson.com](https://markjayson.com).

<a href="https://github.com/markjayson13/creative-markjayson">
  <img src="assets/posters/creative.svg" alt="creative-markjayson, creative portfolio on Cloudflare Pages" width="100%" />
</a>

Creative portfolio, Astro on Cloudflare Pages. Live at [creative.markjayson.com](https://creative.markjayson.com).

<details>
<summary><b>Open the curtain — how a panel gets made</b></summary>

**IPEDSDB_Panel** extracts annual IPEDS Access databases with `mdb-tools`, harmonizes them in DuckDB, and writes a research-ready UNITID-by-year panel. The extended **2004–2024** consolidated analysis file is 147,782 rows × 2,676 columns. The labeled release `full-panel-labels-v1` is 141,711 rows × 2,721 columns. A **39-check acceptance audit** gates the build.

**FSAVolumeReports_Panel** keeps the Federal Student Aid side at the OPEID-by-award-year grain: acquisition, identity normalization, program harmonization, and suppression handling for grants, campus-based aid, and loans, across 25+ years of Title IV volume.

**IPEDS-FSA_Panel** consumes both outputs, resolves annual UNITID links, and exports the combined research panels. It does not rebuild either upstream panelizer.

**IPEDS_Paneling** is the separate Python and DuckDB lane for downloading, harmonizing, and QC-validating NCES IPEDS into institution-year datasets.

**COA_FINAID_SUBS** is the public replication layer for cost-of-attendance headroom and institutional grant aid. It starts from the clean IPEDS panel, builds the 2009–2023 four-year public and private nonprofit sample, and estimates institution-level fixed effects. Those estimates are associations, not student-level packaging results.

</details>

<details>
<summary><b>Open the curtain — house lights</b></summary>

Macro by Mark's status page probes the app's own endpoints and folds in vendor health. Strict-mode checks return a real failure when configuration is broken, instead of a cheerful 200. A sentinel validates the chat config without calling the model. Vendor probes time out, cache, and degrade to "unknown," so a third-party outage cannot take the page down. The monitoring vendor is an environment variable (`betterstack`, `instatus`, `statuspage`, or `none`), and indicator groups roll up worst-of-fold.

</details>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pipeline-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/pipeline-light.svg" />
  <img alt="From the archive to the stage: NCES IPEDS, student aid, and FRED, BEA, BLS, Census, and World Bank move through mdb-tools, DuckDB, and a QA gate into year panels, Macro by Mark, working papers, and replication code." src="assets/pipeline-light.svg" width="100%" />
</picture>

</div>

## Intermission — Instruments

| Area | Tools |
| --- | --- |
| **Data engineering** | Python · pandas · DuckDB · SQL · PyArrow · mdb-tools |
| **Econometrics** | Stata · R · Excel |
| **Front end** | Next.js · TypeScript · React · Tailwind · Zustand |
| **Infra / services** | Supabase · Vercel · Trigger.dev · Upstash · Stripe |
| **Data sources** | NCES/IPEDS · Federal Student Aid · FRED · BEA · BLS · Census · World Bank |

Portfolio sites are Astro on Cloudflare Pages.

## This season

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/quest-log-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/quest-log-light.svg" />
  <img alt="Pixel grid of public GitHub contributions over the past year. The count is redrawn from GitHub by a scheduled Action." src="assets/quest-log-light.svg" width="100%" />
</picture>

</div>

The grid is redrawn from the public contribution calendar by a [scheduled Action](.github/workflows/quest-log.yml). The count in the card is GitHub's, and it updates when the calendar does.

## Curtain call

<div align="center">

<a href="https://markjayson.com"><img src="assets/links/website.svg" alt="markjayson.com" height="48" /></a>
&nbsp;
<a href="https://www.linkedin.com/in/markjaysonfarol/"><img src="assets/links/linkedin.svg" alt="LinkedIn" height="48" /></a>
&nbsp;
<a href="mailto:markjayson@markjayson.com"><img src="assets/links/email.svg" alt="Email markjayson@markjayson.com" height="48" /></a>
&nbsp;
<a href="https://letterboxd.com/markjayson13/"><img src="assets/links/letterboxd.svg" alt="Letterboxd" height="48" /></a>

</div>

Open to **Economist, Research Analyst, Data Analyst, and Financial Analyst** roles. Remote, hybrid, or relocation.

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/footer-light.svg" />
  <img alt="Mark Jayson Farol, Las Vegas. Two pixel Lemongrab figures stand on a candy hill." src="assets/footer-light.svg" width="100%" />
</picture>

</div>
