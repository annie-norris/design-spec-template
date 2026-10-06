# Contributing

This repo holds the shared template and process only. **Never put client specs here.** They belong in your own private copy, made with **Use this template**.

## Ways to contribute

- **Give advice or ask a question** about the template or process: start a thread in **Discussions**.
- **Report a problem**, like a section that doesn't fit a kind of project or a checker bug: open an **Issue**.
- **Suggest a specific change** to the README, checker, or example spec: open a **Pull Request**.

## Opening a pull request

1. Fork this repo (it holds no client work, so a fork is safe), or ask for write access and create a branch.
2. Make your change. If you change a section, table, or field in the README's `## Template`, update `specs/_example/` to match.
3. Run the check: `python3 scripts/check_specs.py`. It must pass.
4. Open the pull request and say what problem the change solves, ideally with an anonymized example from real work.

Every pull request is reviewed before it's merged. Merged changes are listed in [CHANGELOG.md](CHANGELOG.md).

## Getting template updates into your own copy

Copies made with **Use this template** don't update automatically. When the changelog shows something you want, either:

- **Copy it by hand:** open the changed file here and paste the relevant section into your copy.
- **Pull it with git** (from your copy, the first line is one-time setup; repeat the last two for each update):
  ```
  git remote add template https://github.com/annie-norris/design-spec-template.git
  git fetch template
  git merge template/main --allow-unrelated-histories
  ```
  If you've customized your README, expect merge conflicts there and keep the parts you want.
