---
name: "meta-instagram-platform"
external_system: "Meta Instagram Platform API"
scope: hybrid
status: active
owner: "Marcos"
permission_level: read-only
related_tools:
  - "tools/instagram-read-connector.md"
related_agents:
  - "marcos-dev/.kora/agents/instagram-content-analyst.md"
related_skills:
  - "marcos-dev/.kora/skills/collect-instagram-post-intelligence.md"
related_evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Meta Instagram Platform

## Purpose

Connect KORA-managed workflows to authorized Instagram professional account data for Marcos Dev social media analysis.

The integration exists to support evidence-based content review, post intelligence, and future Insights import/analysis without giving KORA blanket permission to publish, message, scrape, or modify Instagram.

## External System

Meta Instagram Platform API.

Current Marcos Dev use: read authorized professional profile/media data.

## Scope

Hybrid.

The integration pattern is reusable, but each business/profile must have isolated authorization, local configuration, owner approval, and data boundaries.

## Runtime Status

The Marcos Dev read-only runtime is active on this machine at `C:\KORA\runtime\tools\instagram-connector\` as of 2026-09-05.

## Access Requirements

- Instagram professional account, Business or Creator as supported by the active Meta API path.
- Owner-controlled Meta app or approved official authorization flow.
- Access token and account identifier stored in `C:\KORA\.env`, outside public repositories and ignored by Git.
- Current official Meta documentation review before expanding permissions, fields, endpoints, or automation.

## Data Behavior

Current read-only behavior may fetch:

- profile authorization status;
- owned media list;
- media type and format;
- publication timestamp;
- caption excerpt;
- permalink;
- public like count;
- public comment count.

Current behavior does not fetch or store Directs, private follower/customer data, downloaded media files, full raw API dumps, or unpublished account information.

## Permissions

Permission level: read-only.

Basic profile/media access is the approved current scope for Marcos Dev. Insights expansion is not included unless separately approved and implemented after documentation review.

## Platform Constraints

Instagram/Meta APIs, permissions, account requirements, API versions, rate limits, and Insights availability are update-sensitive.

Before real implementation changes, verify current official Meta documentation and record the verification date in the relevant KORA/local project file.

## Fallback Mode

If API access is unavailable, use one of these safer fallbacks:

- official Meta Business Suite or Instagram Insights export supplied by Marcos;
- user-provided screenshots of public or owned account surfaces;
- manual list of post links, dates, captions, and observed metrics.

Do not replace unavailable API access with scraping or browser automation unless a separate policy explicitly approves it and the platform rules allow it.

## Security And Privacy

Secrets must stay outside public repositories and chat logs.

Do not store access tokens, account IDs, raw API responses, Directs, customer/follower private data, or unnecessary personal data in KORA project records.

Persist only summaries, decisions, learning, capability gaps, and safe operational metadata.

## Approval Points

Explicit approval is required before:

- initial account connection or token renewal;
- changing scopes or requesting Insights permissions;
- moving secrets to a new private store;
- creating recurring collection;
- storing raw exports or post archives;
- publishing, messaging, comment management, or any write operation.

## Related

- Tool: `tools/instagram-read-connector.md`
- Marcos Dev local decision: `C:\marcbmrs.github.io\.kora\decisions\DR-0005-kora-independence-from-marcosos.md`
- Marcos Dev local tool reference: `C:\marcbmrs.github.io\.kora\tools\instagram-connector.md`