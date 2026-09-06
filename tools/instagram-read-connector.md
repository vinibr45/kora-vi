---
name: "instagram-read-connector"
type: tool
scope: hybrid
status: active
owner: "Marcos"
permission_level: read-only
allowed_callers:
  - "marcos-dev/.kora/skills/collect-instagram-post-intelligence.md"
  - "marcos-dev/.kora/agents/instagram-content-analyst.md"
related_agents:
  - "marcos-dev/.kora/agents/instagram-content-analyst.md"
related_skills:
  - "marcos-dev/.kora/skills/collect-instagram-post-intelligence.md"
related_evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Instagram Read Connector

## Purpose

Provide a read-only execution capability for authorized Instagram professional profiles used by Marcos Dev.

The connector supports safe profile/media checks and basic post intelligence without publishing, messaging, comment management, scraping, or profile changes.

## Scope

Hybrid.

The tool pattern is reusable for authorized Instagram professional profiles, but each profile requires isolated local configuration and explicit owner authorization.


## Runtime Implementation

Current private runtime path:

```text
C:\KORA\runtime\tools\instagram-connector\
```

Current private environment path:

```text
C:\KORA\.env
```

The runtime was verified on 2026-09-05 with `health_check.py --profile marcos-dev` and `read_media.py --profile marcos-dev --limit 3`.
## Inputs

- profile key, such as `marcos-dev`;
- limit for media reads, normally 1 to 50;
- local environment values stored outside public repositories;
- selected Meta/Instagram API version, defaulting to the currently verified version in the implementation.

## Outputs

Health check output:

```json
{"profile":"marcos-dev","authorized":true,"scope":"leitura_minima_de_perfil"}
```

Media read output should be sanitized and limited to operational fields such as:

- media type;
- media product/format;
- publication timestamp;
- caption excerpt and truncation flag;
- permalink;
- public like count;
- public comment count.

## Allowed Callers

- Marcos Dev local skill: `collect-instagram-post-intelligence`.
- Marcos Dev local agent: `instagram-content-analyst`, through the collection skill.
- Future KORA workflows explicitly approved for read-only Instagram analysis.

## Required Permissions

Read-only authorization for an Instagram professional account controlled or explicitly authorized by the owner.

For Marcos Dev, the current known use is basic profile/media read access through the Instagram Platform API.

Broader Insights access requires current official Meta documentation review, appropriate permissions, and explicit approval before implementation.

## Safety Constraints

- Do not print, persist, commit, or summarize access tokens, account IDs, raw API responses, or private account data.
- Do not use Marcos Dev credentials to analyze third-party profiles.
- Do not publish posts, send messages, reply to comments, delete content, download media files, scrape pages, or create recurring sync.
- Read only the minimum amount of data needed for the task.
- Treat API/platform behavior as update-sensitive and verify official documentation before expanding fields, endpoints, permissions, or automation.

## Failure Modes

- local environment missing or incomplete;
- token expired or revoked;
- Meta API rejects the request;
- network or timeout failure;
- API version changed or endpoint behavior changed;
- requested profile lacks required account type or permission.

When a failure occurs, return a sanitized reason and do not attempt to recover secrets, scrape Instagram, or reuse another profile's token.

## Approval Points

Explicit human approval is required before:

- connecting or renewing account authorization;
- changing permission scope;
- adding Insights access;
- changing storage/retention behavior;
- creating recurring automation;
- writing to Instagram or any external system;
- moving secrets to a new store.

## Related

- Integration: `integrations/meta-instagram-platform.md`
- Local Marcos Dev tool reference: `C:\marcbmrs.github.io\.kora\tools\instagram-connector.md`
- Local Marcos Dev skill: `C:\marcbmrs.github.io\.kora\skills\collect-instagram-post-intelligence.md`
- Local Marcos Dev agent: `C:\marcbmrs.github.io\.kora\agents\instagram-content-analyst.md`