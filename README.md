<p align="center">
  <a href="https://github.com/gnaboo/DLogger">
    <img src="https://github.com/gnaboo/DLogger/raw/main/logo.png" alt="Logo" width=72 height=72>
  </a>

  <h3 align="center">DLogger</h3>

  <p align="center">
    A simple project to log Discord Messages easily.
    <br>
    <a href="https://github.com/gnaboo/DLogger/issues/new?template=bug.md">Report bug</a>
    ·
    <a href="https://github.com/gnaboo/DLogger/issues/new?template=feature.md&labels=feature">Request feature</a>
  </p>
</p>


## Table of contents

- [Table of contents](#table-of-contents)
- [Quick start](#quick-start)
- [Requirements](#requirements)
- [What can this project do](#what-can-this-project-do)
- [How it works](#how-it-works)
- [What's included](#whats-included)
  - [Files:](#files)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

---

## Quick start

```shell script
git clone https://github.com/gnaboo/DLogger.git
cd DLogger

python3 interface.py
```

---

## Requirements
  - [python3](https://python.org)


---

## What can this project do

- This project allows you to easily log some conversations. 
- It formats the data in a json file and in an HTML file, allowing people to easily view the log conversation
- You can make your own extension in the ``own_script.py`` file.

## How it works

How can I use this project ?

- This project contains by default a ``interface.py`` file. This file contains a **Tkinter GUI** allowing any user to use this script.

    - When opening it, you will be met with some entries and buttons
    - If you already know your token, you can use it. Otherwise, clicking the ``Extract token`` button. This will automatically gather your token from your computer. **(Safe, you can easily understand how is your token used by looking into the ``_token.py`` file)**
  
    - If more than one tokens are found, you will have to follow the instructions in the terminal.
    - You then need to get the conversation ID. If you don't know how to get it, right click a message from a conversation and click on the button ``Copy the click of the message``. Then paste it into the ``Message URL`` entry of this GUI.
    - To gather all the messages, click on the ``Parse All Messages``. Otherwise, enter the amount to messages in the entry and click the ``Parse Messages``.
    - Once done, it will automatically save it in the ``\ouput`` folder, with a json and html file. The html file will automatically open by default.

- This project also contains a ``own_script.py`` file. This file contains some default code to custom the script.

    - Documentation: **Work In Progress**

---

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

---

## Bugs and feature requests

Have a bug or a feature request? Please first search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/gnaboo/DLogger/issues/new).

## Contributing

Please read through our [contributing guidelines](https://reponame/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, all HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Main author](https://github.com/usernamemainauthor).

Editor preferences are available in the [editor config](https://reponame/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <https://editorconfig.org/>.

---

## Creators

**Founder of the Project**

- <https://github.com/gnaboo>

## Copyright and license

Work On Progress
