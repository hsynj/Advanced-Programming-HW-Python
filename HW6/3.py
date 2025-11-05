def to_bin(ip):
    parts = ip.split('.')
    binary = [format(int(part), '08b') for part in parts]
    res = ''.join(binary)
    return res


def prfx(bins):
    if not bins:
        return ''
    prefix = ''
    for i in range(32):
        bit = bins[0][i]
        if all(bina[i] == bit for bina in bins):
            prefix += bit
        else:
            break
    return prefix


def unbin(prfx):
    return '.'.join(str(int(prfx[i:i + 8], 2)) for i in range(0, len(prfx), 8))

ips = ["192.168.1.1", "192.168.1.5", "192.168.1.9"]
bins = [to_bin(ip) for ip in ips]
prefix = prfx(bins)
print("Longest common prefix:", prefix)
print(unbin(prefix))