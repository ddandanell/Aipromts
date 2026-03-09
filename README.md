# Aipromts

AI-prompts og agent-opsætninger behandlet som softwarekomponenter — med versionering, modulopdeling, klare inputs/outputs, testcases og dokumentation.

---

## Struktur

```
Aipromts/
│
├── README.md
├── agents/
│   ├── research-agent/
│   │   ├── system_prompt.md
│   │   ├── user_template.md
│   │   ├── config.yaml
│   │   └── examples/
│   │       ├── input.json
│   │       └── output.md
│   │
│   ├── seo-agent/
│   │   ├── system_prompt.md
│   │   ├── user_template.md
│   │   ├── config.yaml
│   │   └── examples/
│   │       ├── input.json
│   │       └── output.md
│   │
│   └── analysis-agent/
│       ├── system_prompt.md
│       ├── user_template.md
│       ├── config.yaml
│       └── examples/
│           ├── input.json
│           └── output.md
│
├── prompt-library/
│   ├── frameworks/
│   │   ├── problem-solution.md
│   │   ├── market-analysis.md
│   │   └── research-template.md
│   │
│   └── tools/
│       ├── web-search.md
│       ├── summarizer.md
│       └── data-extractor.md
│
├── schemas/
│   ├── output_schema.json
│   └── task_schema.json
│
└── tests/
    ├── test_research_agent.py
    └── prompt_validation.py
```

---

## Formål

| Mappe | Beskrivelse |
|---|---|
| `agents/` | Én mappe per AI agent med system prompt, user template og config |
| `prompt-library/` | Genbrugelige prompt frameworks og tool-beskrivelser |
| `schemas/` | Faste JSON output-strukturer til agent chaining og automatisering |
| `tests/` | Sikrer at prompts og agent-konfigurationer stadig virker efter ændringer |

---

## Standard agent-struktur

Hver agent indeholder:

- **`system_prompt.md`** — Agentens identitet, mål og regler
- **`user_template.md`** — Skabelon til opgaver med `{{placeholder}}`-variabler
- **`config.yaml`** — Teknisk setup (model, temperature, tools, memory)
- **`examples/input.json`** — Eksempel-input til test og demonstration
- **`examples/output.md`** — Forventet output til validering

---

## Kørsel af tests

```bash
pip install pytest pyyaml
python -m pytest tests/ -v
```

---

## Best practices

1. **Modular prompts** — én agent = én mappe
2. **Structured outputs** — JSON schemas muliggør agent chaining
3. **Agent configs** — tekniske parametre adskilt fra prompts
4. **Versioning** — brug Git commits til at spore prompt-versioner
5. **Testing** — valider altid structure og placeholders efter ændringer
