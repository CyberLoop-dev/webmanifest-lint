<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#60a5fa&height=180&section=header&text=Webmanifest%20Lint&fontSize=42&fontColor=ffffff" alt="Webmanifest Lint banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=60A5FA&center=true&vCenter=true&width=650&lines=Catch%20PWA%20manifest%20issues%20before%20shipping." alt="Animated project tagline"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/webmanifest-lint?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/webmanifest-lint?style=for-the-badge" alt="Top language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/webmanifest-lint?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/webmanifest-lint?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="Webmanifest Lint illustration"/></p>

## 🚀 Overview

Webmanifest Lint checks a local web app manifest and reports missing or inconsistent fields that can affect installability. It validates common names, display modes, icon declarations, and start URL scope relationships without uploading the file.

## ✨ Features

- 📱 Validate common PWA manifest fields
- 🖼️ Check icon declarations and size formats
- 🧭 Detect start_url paths outside the declared scope
- 📤 Emit readable findings or JSON for CI

## 🎬 Demo

~~~bash
python main.py public/manifest.webmanifest --json
~~~

The report is generated locally; no account or hosted service is needed.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/webmanifest-lint.git
cd webmanifest-lint
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
webmanifest-lint/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#60a5fa,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
