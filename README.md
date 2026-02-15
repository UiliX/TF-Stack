# TF-Stack

Tailwindcss + Flask

# Windows Environment Setup

**Using PowerShell**

## Install UV

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1|iex"
```

## Install Node

```powershell
# Download and install Chocolatey:
powershell -c "irm https://community.chocolatey.org/install.ps1|iex"

# Download and install Node.js:
choco install nodejs --version="24.13.1"
```

# Darwin Environment Setup

## Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Install Node

```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"
# Download and install Node.js:
nvm install 24
```

# Linux Environment Setup

## Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Install Node

```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"
# Download and install Node.js:
nvm install 24
```

# Project Setup

Navigate to the project directory and run the following commands:

```bash
uv sync
```

```bash
npm i
```

# Run Menu

This will show all commands available:

```bash
uv run qwe
```