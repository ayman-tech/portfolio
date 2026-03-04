# 🚀 Ayman AI Portfolio

A modern, responsive personal portfolio website built with **NiceGUI** and **Tailwind CSS**, showcasing my experience, projects, and skills as an AI/ML Engineer.

🌐 **Live:** [aymanai.com](https://aymanai.com)

---

## ✨ Features

- 🌙 **Dark mode by default** with manual light/dark toggle
- 📱 **Fully responsive** design using Tailwind CSS
- ⚡ **Single-page layout** with smooth navigation
- 🧠 **AI/ML focused** — highlights experience, projects, and technical skills
- 🔗 **Social links** — GitHub, LinkedIn, email, and more
- 🐍 **Pure Python** — no HTML/JS templates needed

---

## 🛠️ Tech Stack

| Layer        | Technology                    |
| ------------ | ----------------------------- |
| 🖥️ Frontend | NiceGUI, Tailwind CSS, Quasar |
| 🐍 Backend   | Python 3.12+                  |
| 📦 Packages  | `uv`                          |
| 🚀 Hosting   | GCP Compute Engine + Nginx    |
| 🔒 SSL       | Let's Encrypt (Certbot)       |

---

## 📸 Preview

![Portfolio Screenshot](https://img.shields.io/badge/status-live-brightgreen?style=for-the-badge)


---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/portfolio.git
cd portfolio

# Install dependencies & create venv automatically
uv sync
```

### ▶️ Run Locally

```bash
uv run python main.py
```

Visit 👉 [http://localhost:8080](http://localhost:8080)

---

## 🐳 Docker

### Build & Run

```bash
docker build -t portfolio .
docker run -p 8080:8080 portfolio
```

---

## ☁️ Deployment (GCP Compute Engine)


### 1. Clone & install

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone https://github.com/YOUR_USERNAME/portfolio.git
cd portfolio
uv sync
```


### 2. Configure Nginx reverse proxy

```bash
sudo nano /etc/nginx/sites-available/aymanai.com
```

```nginx
server {
    listen 80;
    server_name aymanai.com www.aymanai.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/aymanai.com /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

### 3. Enable HTTPS 🔒

```bash
sudo certbot --nginx -d aymanai.com -d www.aymanai.com
```

### 6️⃣ DNS Configuration

Point your domain to the instance's external IP in domain settings

---

## 🧰 Useful Commands

| Action           | Command                                                          |
| ---------------- | ---------------------------------------------------------------- |
| 📋 View logs     | `sudo journalctl -u portfolio -f`                                |
| 🔄 Restart app   | `sudo systemctl restart portfolio`                               |
| 🔄 Restart nginx | `sudo systemctl restart nginx`                                   |
| 📊 Check status  | `sudo systemctl status portfolio`                                |
| ⬆️ Pull updates  | `cd ~/portfolio && git pull && sudo systemctl restart portfolio` |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contact

- 🌐 Website: [aymanai.com](https://aymanai.com)
- 💼 LinkedIn: [Ayman's LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
- 🐙 GitHub: [Ayman's GitHub](https://github.com/YOUR_USERNAME)
- 📧 Email: hello@aymanai.com

---

<p align="center">
  Made with 🐍 Python & ❤️ by Ayman. Copyright © Ayman Sayed.
</p>
