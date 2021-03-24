
num_country_stamps = int(input().strip())
stamps = set()
for _ in range(num_country_stamps):
    stamp = input().strip()
    stamps.add(stamp)

print(len(stamps))

