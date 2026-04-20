# 07 - Operational Context

_Read by: all agents. This is the "how we actually get things done" file. Tools, access, workflows, handoffs._

## Tech Stack

- **Storefront:** Shopify Plus
- **Theme repo:** `github.com/7Rock-Team/prosoccer` (separate repo, not this one)
- **Analytics:** Google Analytics 4
- **Search data:** Google Search Console
- **Tag management:** _Google Tag Manager?_ confirm
- **Email:** _Klaviyo? Mailchimp?_ confirm
- **Reviews:** _Yotpo? Judge.me?_ confirm
- **Site search:** Shopify native or _third party?_ confirm

## Data Access

_Which tools the agents can pull from, and how the exports get into this repo._

- **Google Search Console:** Mike pulls exports manually into `data/gsc-exports/` as CSV.
- **Google Analytics 4:** Mike pulls reports into `data/ga4-exports/`.
- **Ahrefs:** Mike exports keyword and backlink data into `data/ahrefs/`.
- **Screaming Frog:** Mike runs crawls and exports to `data/screaming-frog/`.

Until an MCP server is connected to these tools, Mike is the bridge. Agents read what is in `data/`.

## MCP Servers Configured

_Update this as MCPs are connected._

- Tavily - live web research
- Memory - persistent agent memory
- Google Drive - exports and client reports

_Planned:_

- GSC MCP (when available)
- Shopify MCP (read-only product and collection data)

## Theme Change Workflow

1. SEO agent drafts a change (Liquid snippet, schema JSON, meta template, Shopify metafield update) into `deliverables/technical-fixes/`.
2. Mike reviews the draft.
3. Mike opens the theme repo, creates or updates a branch called `mike-audit`, pastes the change, tests locally on a dev theme.
4. Mike opens a PR from `mike-audit` to the theme repo's main branch.
5. Misha reviews and merges.
6. SEO agent notes the deployment in `work-log/` and updates any tracking in this repo.

Agents in this repo never commit to the theme repo. Ever.

## Content Workflow

1. Keyword Research or Master Strategist identifies a target topic.
2. Master Strategist writes a brief in `deliverables/content-drafts/in-progress/<slug>-brief.md`.
3. Content Writer agent writes a draft in the same folder.
4. Human writer (TBD) polishes or approves.
5. Mike reviews.
6. Mike or Jorge publishes on the Shopify blog.
7. URL goes into `deliverables/content-drafts/article-archive/_INDEX.md`.
8. Article gets monitored in next monthly report.

## Approval and Communication

- **Internal approvals:** Mike approves agent actions in-session.
- **Client approvals:** Mike sends the artifact to Tony via email. No direct agent-to-client contact.
- **Status updates:** weekly, in `work-log/`.
- **Bugs or blockers:** documented inline in the relevant deliverable and surfaced in the next weekly log.

## Security and Privacy

- No customer PII in this repo.
- No order data in this repo. Aggregates only.
- Secrets stay out of the repo (see `.gitignore`).
- Claude Code sessions run on Mike's Windows machine. No shared machine use for now.
