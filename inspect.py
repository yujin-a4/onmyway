with open(r'c:\Users\YBM\Desktop\onmyway\prototype.html', 'rb') as f:
    raw = f.read()

# 바이트 63379 부근 확인
chunk = raw[63370:63470]
print('Hex:', chunk.hex())
print('Raw:', chunk)
