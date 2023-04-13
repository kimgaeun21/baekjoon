self_number = []
none_self = []

for i in range(1,10000):
    if i in none_self:
        n = str(i)
        dn = i
        for j in range(len(n)):
            dn = dn + int(n[j])
        none_self.append(dn)
    else:
        self_number.append(i)
        n = str(i)
        dn = i
        for j in range(len(n)):
            dn = dn + int(n[j])
        none_self.append(dn)

for i in range(len(self_number)):
    print(self_number[i])

