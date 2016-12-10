import eyed3

song_link = "/home/narenuday/Music/songs/Zariya.mp3"

audiofile = eyed3.load(song_link)

print audiofile
print audiofile.tag.artist
print audiofile.tag.album_artist
print audiofile.tag.album
print audiofile.tag.title
print audiofile.tag.track_num