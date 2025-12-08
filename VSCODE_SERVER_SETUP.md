# VS Code Server Setup for Hospital Management System

## What is VS Code Server?

VS Code Server is a service that runs on a remote development machine (your local computer). It allows you to securely connect using VS Code from anywhere without SSH. It enables seamless development with all your local code, runtimes, and extensions.

Ref: https://code.visualstudio.com/docs/remote/vscode-server

---

## Why Use VS Code Server?

- Work on your project from any browser
- Access your local machine securely from anywhere
- No SSH setup required
- Use VS Code features in the browser
- Develop on iPad, Chromebook, or tablet
- Single-user secure tunnel connection

---

## Installation & Setup (5 minutes)

### Step 1: Install VS Code Server CLI

Download and install VS Code from https://code.visualstudio.com

The `code` CLI is included with VS Code installation.

### Step 2: Start VS Code Server

Open terminal/command prompt and run:

```bash
code tunnel
```

On first run, you'll be prompted to:
1. Accept the license terms
2. Sign in with GitHub account
3. Name your machine

### Step 3: Connect to Your Machine

After setup, VS Code Server will display a link:

```
* Connected to VS Code Server at: https://vscode.dev/tunnel/your-machine-name
```

Open this link in any browser to access VS Code.

---

## Using VS Code Server with Hospital App

### Step 1: Open Project Folder

1. In VS Code (browser or desktop), open the hospital project
2. File > Open Folder
3. Navigate to your hospital- directory
4. Click Open

### Step 2: Open Integrated Terminal

Press: `Ctrl + ` (backtick)

Or: Terminal > New Terminal

### Step 3: Run Setup Script

```bash
bash setup-local.sh
```

This will:
- Create virtual environment
- Install dependencies
- Configure .env file
- Run migrations
- Create superuser (admin/admin123)

### Step 4: Start Development Server

```bash
source venv/bin/activate
python manage.py runserver
```

You'll see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 5: Access Your App

1. Click the port notification in VS Code
2. Or open: http://127.0.0.1:8000/admin/
3. Login: admin / admin123

---

## VS Code Server Commands

### Start tunnel
```bash
code tunnel
```

### Stop tunnel
```bash
Ctrl+C
```

### View other commands
```bash
code tunnel --help
```

### Disable telemetry
```bash
code tunnel --disable-telemetry
```

---

## Useful VS Code Extensions

For Django/Python development, install these extensions:

1. **Python** - Microsoft
   - Intellisense, debugging, linting

2. **Pylance** - Microsoft
   - Fast, feature-rich language support

3. **Django** - Baptiste Darthenay
   - Django-specific syntax highlighting

4. **Thunder Client** - Ranga Vadhineni
   - API testing without leaving editor

5. **REST Client** - Huachao Mao
   - Make HTTP requests directly in editor

6. **SQLite** - alexcvzz
   - Browse SQLite databases

7. **Git Graph** - mhutchie
   - Visualize repository branches

---

## Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
```

### Virtual Environment Not Activating

Windows:
```bash
venv\\Scripts\\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### VS Code Server Connection Issues

1. Ensure VS Code is installed
2. Open new terminal/command prompt
3. Run `code tunnel` again
4. Check firewall settings allow VS Code

### Keyring/Secrets Error

This is normal on some Linux systems. Settings Sync will use in-memory storage and reset when server restarts.

Ignore safely or refer to: https://github.com/microsoft/vscode-remote-release/issues/8628

---

## Advanced: Running on Different Port

```bash
code tunnel --port 8080
```

## Advanced: Run Without Browser

Use VS Code Desktop and connect:
1. Install VS Code Desktop
2. Install "Remote - Tunnels" extension
3. Click Remote icon (bottom left)
4. Select "Connect to Tunnel"
5. Choose your machine

---

## Key Points

- VS Code Server runs locally on your machine
- Access from browser via secure tunnel
- Single-user only (per license)
- Not designed as hosted service
- Updates available via VS Code notifications
- No SSH required
- All code stays on your machine

---

## Quick Reference

| Task | Command |
|------|----------|
| Start tunnel | `code tunnel` |
| Run app | `python manage.py runserver` |
| Access admin | http://127.0.0.1:8000/admin/ |
| Activate venv | `source venv/bin/activate` |
| Install deps | `pip install -r requirements.txt` |
| Run migrations | `python manage.py migrate` |
| Create user | `python manage.py createsuperuser` |

---

**Now you can develop your hospital management system from anywhere using VS Code Server!**
