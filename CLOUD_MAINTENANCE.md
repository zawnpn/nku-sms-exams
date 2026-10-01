# Cloud maintenance and manual recovery

This is a materials repository. It has no application build, production server or
standalone website deployment. GitHub, a dev container, or an ordinary terminal
can maintain it without OpenAI dot.

The dev container uses Python 3.12. Validate additions with:

```bash
python3 scripts/check_materials.py
```

The check verifies README links, path boundaries and nonempty files without reading
PDF/ZIP/image contents. The PR workflow uses no secrets and publishes no artifacts.
Review the intended public materials before committing. Mail submissions and
attachments not accepted into Git need a separate backup.

## Publication through Quartz

1. Review and publish the desired exams commit in this repository.
2. Update the `files/nku-sms-exams` gitlink and generated share page in ObsidianVault.
3. Publish the Vault commit, then update Quartz's `content` gitlink.
4. Validate the selected content through a private Quartz preview before an
   authorized production release.

The existing Quartz `update.sh` has commit/push side effects. A checks-only task or
draft PR here does not authorize running it. This repository has no preview port;
do not expose the contents with a public file server for convenience.

## Recovery contract

Keep an independent Git mirror/bundle including required review branches, the
submission inbox/original attachments and the accepted source files. Clone the
chosen commit and run the link check. Recover the Quartz/Vault version references
separately to reproduce the published site. No dependency directory or build
output needs backup. Check Codespaces authorization and billing before creating
a cloud workspace; retain commits before disposing of that workspace.

## Resource limits and manual lifecycle

Create from the reviewed maintenance branch with the smallest machine:

```bash
gh codespace create --repo zawnpn/nku-sms-exams --branch codex/cloud-maintenance --machine basicLinux32gb --idle-timeout 5m
```

GitHub currently allows 5–240 minutes, so the requested 3-minute idle timeout
is unavailable. Use 5 minutes for new maintenance environments. The public REST
update endpoint cannot change an existing environment's idle timeout; stop older
environments explicitly after use instead of treating an ignored update as success.
Keep the account Codespaces budget at $0 with **Stop usage** enabled and check
remaining included compute and storage before creating an environment. Stopped
environments retain storage usage; preserve commits and independent backups
before any later deletion or configured retention expiry.

```bash
gh codespace list
gh codespace stop --codespace <name>
gh api --method POST user/codespaces/<name>/start
gh codespace ssh --codespace <name>
```

The official SSH feature is included in the container. After connecting, change
to `/workspaces/<repository-name>` and run this guide's build and preview commands.
A stopped preview must be restarted; opening its workspace in the browser also
starts the environment. Keep every preview port **Private**. Never copy GitHub
tokens into the workspace to repair a Git credential problem; use the platform's
normal repository credential integration and the Codespaces browser terminal.
