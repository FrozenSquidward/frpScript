from cryptography.fernet import Fernet

# 加密脚本
# 读取 frps.toml 文件内容
with open('frps.toml', 'r') as file:
    config = file.read()
 
# 生成密钥
key = Fernet.generate_key()
 
# 创建加密对象
cipher_suite = Fernet(key)
 
# 加密配置内容
encrypted_config = cipher_suite.encrypt(config.encode('utf-8'))
 
# 保存密钥和加密内容到文件
with open('frps.toml.key', 'wb') as key_file:
    key_file.write(key)
with open('frps.toml.enc', 'wb') as enc_file:
    enc_file.write(encrypted_config)
