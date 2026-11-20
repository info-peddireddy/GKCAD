# KCAD

KCAD is a read-only engineering copilot for mechanical design teams.

The repository is in Phase 0. The prototype folder `kcad-agent/` is not present.
Phase 0 records the company defaults, architecture decisions, and scope.

## Phase 0 gate

Review these files:

- `config/company.yaml`
- `KCAD_QUESTIONS.md`
- `docs/adr/`
- `docs/prototype-assessment.md`
- `docs/severity.md`

## Constraints

- KCAD does not replace FEA, CAM, or PLM.
- KCAD does not write G-code or send programs to machines.
- KCAD uses Released data by default.
- KCAD uses numbers only from tools.
- Agent output must pass `ste_check`.