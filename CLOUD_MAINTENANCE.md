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
