#!/bin/sh
# gk2027-mobile 容器入口：确保自签证书 → 起 8443(HTTPS) + 8577(HTTP)
set -e

CERT_DIR=/app/data/certs
if [ ! -f "$CERT_DIR/cert.pem" ] || [ ! -f "$CERT_DIR/key.pem" ]; then
  mkdir -p "$CERT_DIR"
  openssl req -x509 -newkey rsa:2048 \
    -keyout "$CERT_DIR/key.pem" -out "$CERT_DIR/cert.pem" \
    -days 3650 -nodes -subj "/CN=192.168.100.88" \
    -addext "subjectAltName=IP:192.168.100.88,IP:127.0.0.1,DNS:p.mhtc.top,DNS:localhost" 2>/dev/null
  echo "[entrypoint] 自签证书已生成 -> $CERT_DIR"
else
  echo "[entrypoint] 使用已有证书 $CERT_DIR"
fi

# HTTPS 实例：https://IP:8443 或 https://p.mhtc.top:8443（放行证书后防锁屏生效）
python -m uvicorn server:app --host 0.0.0.0 --port 8443 \
  --ssl-certfile "$CERT_DIR/cert.pem" --ssl-keyfile "$CERT_DIR/key.pem" \
  > /app/logs/https.log 2>&1 &

# HTTP 主实例（兼容旧入口 8577）
exec python -m uvicorn server:app --host 0.0.0.0 --port 8577
