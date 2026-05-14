with open(r'c:\Users\YBM\Desktop\onmyway\prototype.html', 'rb') as f:
    raw = f.read()

# Find workspace in buildPushMessage — get surrounding bytes
idx = raw.find(b"workspace'))")
print(f'workspace at: {idx}')
if idx >= 0:
    chunk = raw[idx:idx+200]
    print(f'Hex: {chunk.hex()}')
    print(f'Raw: {chunk}')
