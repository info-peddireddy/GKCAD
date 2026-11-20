# ADR-0001: Architecture platform

## Status

Accepted for Phase 0.

## Context

The prompt requires Python 3.12, the Claude Agent SDK, MCP tools, FastAPI,
PostgreSQL with pgvector, TimescaleDB for sensor data, object storage,
Streamlit for the MVP, Docker Compose, and an unapproved future cloud target.

## Decision

Use the prompt choices.
Use Docker Compose for local development.
Use PostgreSQL with pgvector for documents, parts, defects, and standards.
Use TimescaleDB for sensor data in the sensor phase.
Use MinIO for local object storage.
Use FastAPI for the API.
Use Streamlit for the MVP.

## Consequence

Later phases can add the required components without a platform change.
