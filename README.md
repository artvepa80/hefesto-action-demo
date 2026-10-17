# hefesto-action-demo

A minimal public demo of the [HefestoAI GitHub Action](https://github.com/artvepa80/Agents-Hefesto)
used as a pull-request gate.

```yaml
- uses: artvepa80/Agents-Hefesto@v4
  with:
    target: '.'
    fail_on: 'CRITICAL'
```

`@v4` is the floating major tag of the Action; it currently resolves to
[v4.20.1](https://github.com/artvepa80/Agents-Hefesto/releases/tag/v4.20.1).
Pin `@v4.20.1` or a commit SHA if you want an exact version.

## What is in this repo

| Path | Purpose |
| --- | --- |
| `app/greeting.py` | Clean Python sample: reads config from the environment. |
| `settings.example.json` | Clean JSON config with no secrets. |
| `.github/workflows/hefesto.yml` | Runs HefestoAI on every pull request and on `main`, failing on CRITICAL findings and uploading SARIF. |

On `main` the gate is green.

## See it fail on purpose

There is an open pull request that adds a `config.json` with **obviously fake**
credentials (`"password": "not-a-real-secret"`, an `AKIAEXAMPLE-...` placeholder).
HefestoAI's JSON analyzer reports it as rule **J001** (hardcoded secret, CRITICAL),
the job exits with code 1 and the check turns red. That pull request is kept open
and is never merged: it exists only to show the gate blocking a secret.

None of the values in this repository are real credentials.

## Run it locally

```bash
pip install hefesto-ai==4.20.1
hefesto analyze . --fail-on CRITICAL
```

Built by [Narapa LLC](https://hefestoai.narapallc.com).
