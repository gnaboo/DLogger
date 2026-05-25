<p align="center">
  <a href="https://github.com/gnaboo/DLogger">
    <img src="https://github.com/gnaboo/DLogger/raw/main/Markdown/logo.png" alt="Logo" width=72 height=72>
  </a>

  <h3 align="center">DLogger</h3>

  <p align="center">
    A simple discord logging tool

    THIS PROJECT HAS NOW BEEN ARCHIVED ; BECAUSE OF CHANGES IN DISCORD'S API, IT NO LONGER WORKS NOR WILL BE UPDATED.
    IT NOW SERVES AS A EXAMPLE OF FORMER PROJECTS I HAVE WORKED ON.
    <br>
    <a href="https://github.com/gnaboo/DLogger/issues/new?template=bug.md">Report bug</a>
    ·
    <a href="https://github.com/gnaboo/DLogger/issues/new?template=feature.md&labels=feature">Request feature</a>
  </p>
</p>


<h1 align="center"><a href="https://github.com/gnaboo/DLogger/markdown/ARCHIVE.md">Ce projet a été archivé. Veuillez consulter ARCHIVE.md </a></h1>


## Table of contents

- [Table of contents](#table-of-contents)
- [Archive of this project](#archive-of-this-project)
- [Quick start](#quick-start)
- [How it works](#how-it-works)
- [What's included](#whats-included)
  - [Files:](#files)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)


## Archive of this project

This project may be used in gnaboo's portfolio. For this purpose, please read ARCHIVE.md

## Quick start

DLogger is a logging tool for Discord chats. It formats the data in the JSON and HTML format, allowing easy access

## How it works

- This app contains by default a ``interface.py`` file. This file contains a **Tkinter GUI** allowing any user to use this script.

    - When opening it, you will be met with some entries and buttons
    - If you already know your token, you can use it. Otherwise, clicking the ``Extract token`` button. This will automatically gather your token from your computer. **(This is a safe feature, you can easily understand and check how your token is being used by looking into the ``_token.py`` file)**
  
    - If more than one tokens are found, you will have to follow the instructions in the terminal.
    - You then need to get the conversation ID. If you don't know how to get it, right click a message from a conversation and click on the button ``Copy the click of the message``. Then paste it into the ``Message URL`` entry of this apps GUI.
    - To gather all the messages, click on the ``Parse All Messages`` button. Otherwise, enter the amount to messages in the entry and click the ``Parse Messages``.
    - Once done, it will automatically save it in the ``\ouput`` folder, with a json and html file. The html file will automatically open by default.

## What's included

### Files:

```text
Dlogger/
└── interface.py
    own_script.py
    _parser.py
    _requests.py
    _save.py
    _token.py
    .gitignore
    logo.png
    README.md
    _̶_̶p̶y̶c̶a̶c̶h̶e̶__/
    ├── _parser.cpython-39.pyc_/
    │   ├── *
    └── requests.cpython-39.pyc/
        ├── *
```

## Bugs and feature requests

Have a bug or a feature request? Please first search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/gnaboo/DLogger/issues/new).

## Contributing

Please read through our [contributing guidelines](https://reponame/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, all HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Main author](https://github.com/usernamemainauthor).

Editor preferences are available in the [editor config](https://reponame/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <https://editorconfig.org/>.

## Creators

**Founder of the Project**

- <https://github.com/gnaboo>

## Copyright and license

Code and documentation copyright 2011-2018 the authors. Code released under the [MIT License](https://reponame/blob/master/LICENSE).

---