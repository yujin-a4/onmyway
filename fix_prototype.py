# encoding: utf-8
with open(r'c:\Users\YBM\Desktop\onmyway\prototype.html', 'rb') as f:
    raw = f.read()

# parse5 also flags U+0080~U+009F which are encoded in UTF-8 as C2 80 ~ C2 9F
# Find all such 2-byte sequences
issues = []
i = 0
while i < len(raw) - 1:
    if raw[i] == 0xC2 and 0x80 <= raw[i+1] <= 0x9F:
        line_num = raw[:i].count(b'\n') + 1
        col = i - raw[:i].rfind(b'\n') - 1
        ctx = raw[max(0,i-40):i+40]
        issues.append((i, line_num, col, raw[i+1], ctx))
        i += 2
        continue
    i += 1

print(f'Found {len(issues)} C1 control characters (U+0080~U+009F in UTF-8):')
for pos, line, col, byte, ctx in issues[:20]:
    codepoint = 0x80 + (byte - 0x80)
    print(f'  U+00{codepoint:02X} at file offset {pos}, line {line}, col {col}')
    print(f'  Context (hex): {ctx.hex()}')
    print(f'  Context: {ctx}')
    print()

if not issues:
    print('None found! Checking for other HTML-illegal chars...')
    # Check for U+FFFE, U+FFFF etc.
    # Also check for null bytes
    for i, b in enumerate(raw):
        if b == 0x00:
            line_num = raw[:i].count(b'\n') + 1
            print(f'  Null byte at line {line_num}')
