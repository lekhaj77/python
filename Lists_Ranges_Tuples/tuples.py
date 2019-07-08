# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)

title, artist, year = imelda
print(title)
print(artist)
print(year)

#### Tuples Examples #######

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))
