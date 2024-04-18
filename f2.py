from cryptography.fernet import Fernet

# 解密脚本
# 打开文件，读取内容，并关闭文件
with open('frps.toml.key', 'r') as file:
    content = file.read()
    #print(content)

# 创建加密对象
cipher_suite = Fernet(content)

with open('frps.toml.enc', 'r') as file2:
    content2 = file2.read()
    #print(content2)
# 解密数据
decrypted_data = cipher_suite.decrypt(content2)
#print(f"Decrypted: {decrypted_data}")

with open('frps.toml.dec', 'wb') as enc_file:
    enc_file.write(decrypted_data)
