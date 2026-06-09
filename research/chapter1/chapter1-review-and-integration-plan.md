# Chapter 1 Research Review and Integration Plan

## Verdict

Use `deep-research-report.md` as the main base for Chapter 1.

Use `gemini-result.md` only as a secondary source-mining file, not as direct prose for the thesis.

Reason: the Deep Research report is more careful about verification gaps, data discrepancies, source hierarchy, and distinction between official sources and interpretation. The Gemini report is broader, but its language is too editorial for a bachelor thesis and it relies in places on weaker secondary sources such as news articles, law-firm commentary, aggregator pages, and politically loaded wording.

## Main Issues Found

### 1. Citation format is not Word-ready

The Deep Research output uses internal citation markers such as `turn25view0`, which are useful only inside the research tool session. They must be replaced with normal citations:

- Institution / author
- year
- document title
- URL
- page, article, table, or dataset where available
- access date

### 2. Gemini prose is too strong and subjective

Avoid or rewrite expressions such as:

- "aggressive deployment"
- "formidable suite"
- "catastrophic severance"
- "massive, punitive"
- "toxic macroeconomic environment"
- "weaponized"
- "existential security risk"

These can be turned into neutral academic phrasing:

- "expanded use of autonomous trade-defence instruments"
- "targeted reduction of strategic dependencies"
- "definitive countervailing duties"
- "deterioration of the business environment"
- "economic coercion concerns"

### 3. Some Gemini sources should not be used as primary thesis evidence

Avoid using these as final proof unless no better source exists:

- The Guardian
- China Briefing
- White & Case
- Ashurst
- Chambers
- European Sources Online aggregator pages
- Global Times

Prefer replacing them with:

- European Commission
- EUR-Lex
- Council of the European Union / European Council
- European Parliament
- Eurostat
- WTO
- Chinese Ministry of Commerce, when presenting the Chinese official position
- European Union Chamber of Commerce in China, for business survey evidence

### 4. Claims needing direct verification before insertion

These should be rechecked against official primary sources before being included in the Word chapter:

- exact day of diplomatic establishment in 1975
- full text and articles of the 1978 Trade Agreement
- full text and articles of the 1985 Trade and Economic Cooperation Agreement
- final procedural status of WTO DS516
- 2024 trade figures discrepancy between DG Trade and Eurostat
- source behind the 98% rare earths, 93% magnesium, and 97% lithium dependency figures
- exact entry-into-force and expansion details of the EU-China Geographical Indications Agreement
- latest official status of EV price undertakings / countervailing duties
- Chinese dairy tariff data, if used, should come from China's Ministry of Commerce or another official source, not The Guardian

## Recommended Chapter 1 Structure

### Capitolul I: Cadrul general al relatiilor UE-China

### 1.1. Evolutia parteneriatului strategic UE-China (1975-2025)

Use:

- 1975 diplomatic relations
- 1978 first trade agreement
- 1985 Trade and Economic Cooperation Agreement
- 1989 Tiananmen and EU arms embargo
- 2001 China WTO accession
- 2003 comprehensive strategic partnership
- 2013 EU-China 2020 Strategic Agenda
- 2019 Strategic Outlook: partner, competitor, systemic rival
- 2020 GI Agreement and CAI agreement in principle
- 2021 CAI freeze
- 2023-2025 de-risking and 50th anniversary framing

Best sources:

- EEAS / Council / Consilium for official timeline
- EUR-Lex for 1978 and 1985 agreements
- WTO for 2001 accession
- European Commission 2019 Strategic Outlook
- European Parliament for CAI freeze
- recent peer-reviewed interpretation from Men, Krumbein, Maher where accessible

### 1.2. Cadrul institutional si acordurile comerciale bilaterale

Use:

- 1985 agreement as legal backbone
- Joint Committee mechanism
- EU-China summits
- High-Level Economic and Trade Dialogue
- WTO framework and DS516 dispute
- GI Agreement
- CAI non-ratification
- FDI Screening Regulation
- Dual-Use Regulation
- Anti-Coercion Instrument
- Economic Security Strategy

Best sources:

- EUR-Lex
- European Commission DG Trade
- WTO dispute pages
- European Parliament
- Council of the EU
- CEPS only for interpretation of CAI, not for legal fact if primary source exists

### 1.3. Provocari actuale: de-risking vs. de-coupling

Use:

- definition from von der Leyen 2023 speech
- European Council June 2023 conclusions
- Economic Security Strategy risk categories
- "promote, protect, partner" framework
- critical dependencies: rare earths, magnesium, lithium
- BEV anti-subsidy investigation and duties
- rare earth / permanent magnet export control concerns
- European Chamber of Commerce business confidence survey
- distinction between targeted de-risking and broad decoupling

Best sources:

- European Commission President speech, 30 March 2023
- European Council conclusions, 30 June 2023
- European Economic Security Strategy, 2023
- EUR-Lex BEV regulations 2024/1866 and 2024/2754
- European Parliament 2024 study on de-risking vs de-coupling
- European Chamber of Commerce in China 2025 Business Confidence Survey

## Integration Workflow

1. Build a clean source register for Chapter 1 with only primary and high-quality academic sources.
2. Convert all research-tool citation markers into normal APA-style references.
3. Rewrite each subsection in Romanian, using neutral academic tone.
4. Insert only verified numbers into tables.
5. Add footnotes or author-date citations consistently, depending on the thesis style required.
6. Keep uncertain claims in a separate "to verify" list until confirmed.

## Immediate Next Step

Create `chapter1-source-register.md` with:

- source title
- institution / author
- year
- source type
- URL
- exact claim supported
- reliability level
- whether it is ready for Word insertion

