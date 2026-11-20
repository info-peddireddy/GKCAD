# ADR-0002: Agent and tool platform

## Status

Accepted for Phase 0.

## Context

The platform needs one chat interface, deterministic tools, specialist subagents,
and auditable results.

## Decision

Use Claude through the Anthropic API.
Use claude-opus-5-5 for orchestration and review.
Use claude-haiku-5-5 for high-volume classification and extraction.
Use the Claude Agent SDK for specialist subagents.
Use one MCP server for each tool.
Each tool result uses the shared envelope in Section 6.

## Consequence

A specialist agent uses tools as the source of numbers and findings.
