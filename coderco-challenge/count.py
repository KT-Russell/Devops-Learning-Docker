import os
import random
from flask import Flask, render_template_string, jsonify
import redis

app = Flask(__name__)

# ---- Config ----
APP_NAME   = os.getenv('APP_NAME', 'BlueWave Tracker') 
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

# Return str (not bytes) from Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

QUOTES = [
    "Build, break, fix, learn, repeat.",
    "Small commits, big progress.",
    "Shipping beats perfect.",
    "If it hurts, automate it.",
    "Curiosity scales better than certainty.",
]

# ---- Shared gradient + styles (navy → light blue) ----
BASE_START = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>__TITLE__</title>
<style>
  /* Page-wide gradient & typography */
  body{
    margin:0;min-height:100vh;color:#eaf2ff;
    background:
      radial-gradient(1200px 600px at 80% -10%, rgba(173,216,255,.18), transparent 60%),
      radial-gradient(800px 400px at 10% 110%, rgba(128,200,255,.22), transparent 55%),
      linear-gradient(160deg,#0a1a33 0%,#102a5c 55%,#1c4b8f 100%);
    font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial,sans-serif;
    display:grid;place-items:center;
  }
  .wrap{width:100%;max-width:960px;padding:32px 20px 60px}

  /* Hero */
  .hero{
    text-align:center;padding:72px 20px 56px;
    display:flex;flex-direction:column;align-items:center;justify-content:center;
  }
  .hero h1{
    margin:0 0 10px;font-weight:800;letter-spacing:.3px;
    font-size:clamp(28px,4.6vw,44px);color:#eef5ff;text-shadow:0 4px 24px rgba(0,0,0,.35)
  }
  .hero p.sub{
    margin:0 0 24px;color:#c9dbff;font-size:clamp(14px,2.2vw,18px)
  }
  .btns{display:inline-flex;gap:12px;flex-wrap:wrap;justify-content:center}

  /* Buttons */
  .btn{
    appearance:none;border:0;cursor:pointer;padding:12px 18px;border-radius:12px;
    color:#0a1a33;background:#eaf2ff;font-weight:700;text-decoration:none;display:inline-block;
    transition:transform .08s ease,filter .2s ease,box-shadow .2s ease;
    box-shadow:0 6px 18px rgba(10,26,51,.25)
  }
  .btn:hover{filter:brightness(1.02);transform:translateY(-1px)}
  .btn.secondary{background:transparent;color:#eaf2ff;border:1px solid rgba(234,242,255,.5)}

  /* Cards & text */
  .card{
    background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.18);
    border-radius:16px;padding:18px 18px;backdrop-filter:blur(6px);
    box-shadow:0 8px 28px rgba(0,0,0,.28);margin-top:20px
  }
  .title-sm{margin:0 0 8px;font-size:18px;color:#f0f6ff}
  .stat{font-size:28px;font-weight:800;color:#fff}
  .quote{margin-top:10px;font-style:italic;color:#d4e5ff;border-left:3px solid rgba(255,255,255,.45);padding-left:10px}
  .muted{color:#c9dbff}
  .kvs{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;color:#c7dafc;margin-top:6px}
  .list{margin:8px 0 0 18px}
</style>
</head><body><div class="wrap">
"""
BASE_END = "</div></body></html>"

# ---- Routes ----

@app.route('/')
def home():
    body = f"""
    <section class="hero">
      <h1>Welcome to {APP_NAME}</h1>
      <p class="sub">Easy tracking of visits to this site shown below</p>
      <div class="btns">
        <a class="btn" href="/count">View Live Count</a>
        <a class="btn secondary" href="/about">About</a>
      </div>
    </section>

    <section class="card">
      <h3 class="title-sm">What is this?</h3>
      <p class="muted">A tiny Flask app that increments a counter in Redis. Containerised with Docker, optionally scaled behind NGINX.</p>
    
    </section>
    """
    html = BASE_START.replace("__TITLE__", f"{APP_NAME} · Home") + body + BASE_END
    return html

@app.route('/count')
def count():
    current = r.incr('visits')
    quote = random.choice(QUOTES)
    body = f"""
    <section class="card">
      <h3 class="title-sm">Live Counter</h3>
      <div class="stat">This page has been visited {current} times.</div>
      <div class="quote">“{quote}”</div>
      <div style="margin-top:14px;">
        <a class="btn" href="/count">Refresh</a>
        <a class="btn secondary" href="/">Home</a>
      </div>
    </section>
    """
    html = BASE_START.replace("__TITLE__", f"{APP_NAME} · Count") + body + BASE_END
    return html

@app.route('/about')
def about():
    body = f"""
    <section class="card">
      <h3 class="title-sm">About This Project</h3>
      <p class="muted">
        {APP_NAME} was built as part of my DevOps learning journey — showcasing how to design
        and run a <strong>multi-container application</strong> using modern tools.
      </p>

      <p class="muted">This application is powered by:</p>
      <ul class="list muted">
        <li><strong>Flask</strong> — lightweight Python web framework</li>
        <li><strong>Redis</strong> — in-memory data store for the visitor counter</li>
        <li><strong>NGINX</strong> — reverse proxy & load balancer when scaled</li>
        <li><strong>Docker & Compose</strong> — containerisation & service orchestration</li>
      </ul>

      <p class="muted" style="margin-top:10px">
        This project showcases my growing DevOps skills — learning how to design, containerise,
        and scale applications using Docker, Redis, Flask, and NGINX.
      </p>

      <div style="margin-top:20px; text-align:center;">
        <a href="https://github.com/KT-Russell" target="_blank">
         <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" 
              alt="GitHub" style="width:36px; margin:0 10px;">
        </a>
        <a href="https://www.linkedin.com/in/kamran-russell" target="_blank">
          <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" 
               alt="LinkedIn" style="width:36px; margin:0 10px;">
  </a>
</div>


      <div style="margin-top:14px;">
        <a class="btn" href="/">Home</a>
        <a class="btn secondary" href="/count">View Live Count</a>
      </div>
    </section>
    """
    html = BASE_START.replace("__TITLE__", f"{APP_NAME} · About") + body + BASE_END
    return html

@app.route('/health')
def health():
    try:
        r.ping()
        return jsonify({"status": "ok", "redis": "up"}), 200
    except redis.exceptions.ConnectionError:
        return jsonify({"status": "degraded", "redis": "down"}), 503

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
