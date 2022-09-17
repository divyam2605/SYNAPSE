modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']

m_family = []
indices = []
characters = []
temp = []
Phew_finally = {}

m_family = list(enumerate(modern_family))

for n in enumerate(modern_family):
    m_family.append(n)

l = len(modern_family)
for n in range(l):
    indices.append(m_family[n][0])
    characters.append(m_family[n][1])

for n in range(l):
    characters[n] = characters[n].lower()
    characters[n] = characters[n].replace("_", "-")

x = lambda phrase: len(phrase)

temp = map(x, characters)
indices2 = list(temp)

# indices = zip(indices, temp)

for n in range(l):
    indices[n] = indices[n] + indices2[n]

indices.sort(reverse=True)

for n in range(l):
    Phew_finally[indices[n]] = characters[n]

print(Phew_finally)