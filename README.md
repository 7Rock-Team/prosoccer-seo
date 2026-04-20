# ProSoccer SEO Workforce

Multi-agent AI SEO operations for ProSoccer.com, run by 7 Rock Marketing LLC.

## What This Is

A Claude Code project that coordinates a Master Strategist agent plus six specialist SEO agents to plan, execute, and report on SEO work for a Shopify Plus soccer retail client.

This is Phase 1 of a larger Marketing OS that will eventually cover multiple service lines and multiple clients.

## Structure

- `context/` — everything agents need to know about the client, the industry, and how we write.
- `.claude/agents/` — agent definitions, persistent memory, and briefings.
- `strategy/` — living strategy documents.
- `data/` — raw exports from SEO tools.
- `deliverables/` — artifacts produced by agents.
- `reports/monthly/` — monthly reports for the client.
- `shared-intelligence/` — cross-agent knowledge (algorithm updates, tool changes).
- `work-log/` — human-readable weekly logs.

See `CLAUDE.md` for the project charter.

## Getting Started

1. Fill in the files in `context/`. None of the agents can do useful work until these are populated.
2. Open Claude Code at this directory.
3. Ask the Master Strategist to run its startup protocol and report what it knows.
4. Give it a goal.

## Team

- Mike Hakopyan, 7 Rock Marketing (owner)
- Tony Tatikian, ProSoccer COO (client approval)
- Jorge Cotto, ProSoccer Ops

## Related Repos

- `7Rock-Team/prosoccer` — Shopify theme. SEO agent drafts flow through a `mike-audit` branch in that repo.
