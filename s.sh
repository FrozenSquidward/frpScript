#!/bin/bash

# 启动脚本
# 读取密钥
KEY=$(cat frps.toml.key)
echo "秘钥 $KEY"

# 解密配置文件
python3.9 fs2.py

# 启动 frp 服务
./frps -c frps.toml.dec

#sleep 2
#rm -rf frps.toml.dec
