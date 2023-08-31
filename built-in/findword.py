text = input()
sec_text = "Nabucodonosor"
found = True
start = 0
for ch in text:
    pos = sec_text.find(ch, start)
    if pos < 0:
        found = False
        break
    start = pos+1
if found:
    print("yes")
else:
    print("no")
