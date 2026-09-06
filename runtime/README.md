# Runtime

This directory stores private/local executable runtime assets for KORA when a tool definition needs an implementation that must not live in a public project repository.

Runtime files may execute local scripts or API clients, but they must not contain credentials, tokens, private account IDs, raw exports, or unnecessary personal/client data.

Each runtime tool should document:

- purpose;
- command entrypoints;
- required private configuration location;
- allowed behavior;
- prohibited behavior;
- approval points;
- related KORA tool/integration definitions.

Do not treat runtime presence as approval for publishing, writing to external systems, spending money, or recurring automation.- `runtime/tools/google-ads-reader/`: read-only Google Ads campaign diagnostics and proposal generation.
