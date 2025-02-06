names = ["Nuka", "Nika", "Irakli", "Nini"]
for name in names:
    print(name)

for name in names:
    print(f"Hello, {name}! You are invited to my party!")
    
telescopes = ["Celestron", "Meade", "Orion", "Sky-Watcher"]
print(f"I really would like to have {telescopes[2]} telescope.")

scientists = ["Albert Einstein", "Nicola tesla", "Charles darwin"]
for scientist in scientists:
    print(f"Hello {scientist}, I know that you died for a long time ago but I'd love just one dinner with you.")
print(f"Oh, {scientists[-1]} can't come to dinner. ")

scientists[-1] = "Neil deGrasse Tyson"
for scientist in scientists:
    print(f"Hello {scientist}, I know that you died for a long time ago but I'd love just one dinner with you.")

print("I found a bigger table, so I can invite more people.")
scientists.insert(0, "Stephen Hawking")
scientists.insert(2, "Carl Sagan")
scientists.append("Merry Curie")
for scientist in scientists:
    print(f"Hello {scientist}, I know that you died for a long time ago but I'd love just one dinner with you.")

print("Guys, I'm sorry but I can invite only two people.")
for i in range(len(scientists)-2):
    popped_scientist = scientists.pop()
    print(f"I am so sorry, {popped_scientist}, I can't invite you.")
    
print(scientists)
for scientist in scientists:
    print(f"Dear, {scientist}, I am happy I still can invite you to my dinner.")
    
print(scientists)
del scientists[:]
print(scientists)

places = ["Sweden", "Japan", "Antarctica", "Sydney", "New York"]
for place in places:
    print(place)

print(sorted(places))

print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)