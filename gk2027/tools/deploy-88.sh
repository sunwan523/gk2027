#!/bin/sh
# gk2027 部署到 88：docker load + tag + 重建容器（绕开 ghcr 认证问题）
set -e
echo "== 1/4 docker load =="
docker load -i /root/gk2027-arm64.tar | tail -1
NEWID=$(docker images --no-trunc --format '{{.ID}} {{.Repository}}:{{.Tag}}' | grep '<none>:<none>' | head -1 | awk '{print $1}')
if [ -z "$NEWID" ]; then
  echo "!! 未找到新加载的 <none> 镜像，退出"; exit 1
fi
echo "== 2/4 新镜像: $NEWID =="
docker tag "$NEWID" ghcr.io/sunwan523/gk2027-mobile:latest
echo "== 3/4 重建容器 =="
docker rm -f gk2027-mobile
docker run -d --name gk2027-mobile --restart always \
  -p 8577:8577 -p 8443:8443 \
  -v /root/gk2027-data:/app/data \
  ghcr.io/sunwan523/gk2027-mobile:latest
echo "== 4/4 验证 =="
sleep 6
docker ps --format '{{.Names}} {{.Status}}' | grep gk2027 || true
echo "ai_config 出现次数: $(docker exec gk2027-mobile grep -c ai_config /app/config.py 2>/dev/null || echo FAIL)"
echo "模型: $(docker exec gk2027-mobile grep -o 'agnes-2.5-flash' /app/config.py 2>/dev/null | head -1 || echo FAIL)"
