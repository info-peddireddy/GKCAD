# ADR-0003: Units and read-only access

## Status

Accepted for Phase 0.

## Context

The platform must avoid unit defects and must not write to external systems.

## Decision

Use Python 3.12 and a shared Pint registry.
Use US customary units as the Phase 0 default.
Use read-only database users and allow-listed SQL views.
Do not provide write connectors for PLM, ERP, machines, or databases.
Write ECR output only as a document.

## Consequence

Unit and access rules are the basis for later schema and integration work.
