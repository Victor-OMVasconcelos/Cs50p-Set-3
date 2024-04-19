total = []
while True:
    try:
        item = input().upper()
        total.append(item)
    except EOFError:
        break





unique = list(set(total))
unique.sort()
for item in unique:
   times = total.count(item)
   print(times, item)