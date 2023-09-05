def favorite_song(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
print(favorite_song(input("What is your favorite song?\n"), input("Who is the artist?\n")))