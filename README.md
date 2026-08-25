# SKYCOIN4444 System Architecture Docs

A version-controlled architecture-reference package for the SKYCOIN4444 engineering portfolio. This repository documents integration principles, trust boundaries, operational evidence expectations, and architecture-decision practices; it is not a runtime service.

## Contents

- [`docs/architecture.md`](docs/architecture.md) — reference system context, zones, design principles, integration checklist, and explicit non-claims.
- [`docs/adr-template.md`](docs/adr-template.md) — reusable architecture decision record template.
- [`scripts/validate_docs.py`](scripts/validate_docs.py) — dependency-free structural/local-link validator used by CI.

## Validation

```bash
python scripts/validate_docs.py
python -m py_compile scripts/validate_docs.py
```

The CI gate also checks the Markdown set for several obvious secret/private-key patterns. That lightweight check is not a substitute for a dedicated secret scanner or security review.

## Documentation policy

Architecture statements should separate implemented/verified facts from intended design. Repository names, infrastructure configuration, diagrams, or roadmap language alone do not prove a production deployment, security certification, capacity target, availability objective, backup/restore result, or external-provider integration.

When documenting an integrated component, record its repository and exact version, contract, dependency and trust assumptions, persistence model, resource limits, failure behavior, observability, security-sensitive data, test/release evidence, and upgrade/rollback approach.

## Product status

Engineering-beta documentation package. It provides reusable design/reference material and CI validation only. It does not centrally enforce architecture policy, deploy services, provision infrastructure, introspect live systems, generate compliance evidence, or certify the wider portfolio as production-ready.
