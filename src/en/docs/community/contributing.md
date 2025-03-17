# Contributing

Thank you for considering contributing to this project. Your support is essential to improving and expanding it. We appreciate your interest and value your contributions.

We're always looking to expand and improve Cheatsheets! If you have a cheat sheet to share or see something that could be improved, feel free to submit a pull request. Let's build a valuable resource for developers together.

## How to Contribute

There are several ways you can contribute to this project:

- Reporting a bug
- Suggesting a feature
- Improving documentation
- Sharing your knowledge
- Giving feedback
- Contributing to translations
- and more...

## Contribution Requirements

To get started with development, please follow these steps:

**1.** Fork the repository.

**2.** Clone your forked repository.

**3.** Install the project dependencies.

```bash
pip install -r requirements.txt
```

**4.** Start the development server.

```bash
mkdocs serve -f src/en/mkdocs.yml
```

Once running, visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to preview your changes.

## Adding a New Cheat Sheet

Each cheat sheet should be placed inside either the `quick-ref` or `clean-code` directory. If you're adding a new cheat sheet for Python, for example, create a `python` folder inside `quick-ref`:

```console
├── quick-ref
    ├── python
        ├── .toc.md
        ├── index.md 
        ├── getting-started.md
        ├── ...
```

The `index.md` file is the landing page for the cheatsheet. It should contain a table of contents for the cheatsheet.

```yaml title="index.md"
---
title: Python
icon: appicons/python # (1)!
description: A concise and practical ...

tags:
  - script
  - interpret
categories:
  - programming
---
```

1. The `icon` field should be the name of the icon file in the `material/overrides/.icons/appicons` directory. For example, if the icon file is `python.svg`, the `icon` field should be `appicons/python`.

!!! info "Required Fields"
    Only the `title`, `icon`, and `description` are required. The `tags`, `cover`, and `categories` fields are optional.

The `.toc.md` file is used to generate the navigation menu for the cheat sheet.

```yaml
- [Python](index.md) # (1)!
- [Getting Started](getting-started.md) # (2)!
...
```

1. The `[Python](index.md)` link should point to the `index.md` file in the `python` directory.
2. The `[Getting Started](getting-started.md)` link should point to the `getting-started.md` file in the `python` directory.

The `getting-started.md` file is the first page of the cheat sheet. It should contain a brief introduction to the topic and a table of contents for the rest of the cheat sheet.

Additional Markdowns files (`getting-started.md`, etc.) containing the content of the cheat sheet.

## Contributing to Translations

We welcome contributions to the documentation in other languages. If you'd like to contribute to translations, please follow these steps:

**1.** Duplicate the `src/en/` folder and rename it using a [supported language code](https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/#site-language). Each language directory contains the following files:

```console
├── docs
    ├── quick-ref
        ├── index.md
        ├── python
            ├── index.md
            ├── getting-started.md
├── mkdocs.yml
```

**2.** Edit the `mkdocs.yml` file in the language directory to set the `language` field.

For example, if you want to translate the cheat sheet to Portuguese Brazil, you should set the `language` field to `pt-BR`.

```yaml title="src/pt-BR/mkdocs.yml"
INHERIT: ../../mkdocs.yml

# Project information
site_dir: ../../site/pt-BR  # (4)!
site_description: Share quick ... # (1)!
edit_uri: edit/master/src/en/docs/ # (2)!

# Configuration
theme:
  name: material
  language: en  # (3)!
```

1. Translate the `site_description` field to your language.
2. Edit the `edit_uri` field to point to the correct language (e.g., `edit/master/src/pt-BR/docs/`).
3. Set the `language` field (e.g., `language: pt-BR`).
4. Set the `site_dir` field (e.g., `site_dir: ../../site/pt-BR`).

**3.** Add the new language to the `languages` field in the main `mkdocs.yml` file that is located in the root directory.

```yaml title="mkdocs.yml"
extra:
  alternate:
    - name: English
      link: https://ivansaul.github.io/cheatsheets
      lang: en
    - name: Portuguese (BR) # (1)!
      link: https://ivansaul.github.io/cheatsheets/pt-BR/ # (2)!
      lang: pt-BR # (3)!
```

1. This field will be used to display the language name in the language selector.
2. This field will be used to redirect users to the correct language version of the cheat sheet.
3. This field will be used to set the `language` field in the `mkdocs.yml` file in the language directory.

**4.** Start the development server.

```bash
mkdocs serve -f src/pt-BR/mkdocs.yml
```

**5.**  Add new jobs to the `deploy.yml` workflow file to build the documentation for the new language.

```yaml title=".github/workflows/deploy.yml"
- name: Build English Documentation
    run: mkdocs build -f src/en/mkdocs.yml

- name: Build Portuguese (BR) Documentation
    run: mkdocs build -f src/pt-BR/mkdocs.yml
```

!!! danger "Build and Deploy Workflow"
    The new jobs should be added after the `Build English Documentation` job.

**6.** Once your translation is complete, commit your changes and submit a pull request.
