# -*- coding: utf-8 -*-

import os
import subprocess

path = r'C:\Users\HSANG3\Desktop\Raplyzer\lyricsGenerator'

def IPA(dir=path, artist=None, album=None, print_stats=False, language='en-us', lookback=15):

    if artist is not None:
        artists = [artist]
    else:
        artists = os.listdir(dir)
    for artist in artists:
        lyrics_dir = dir+'\\'+artist
        print ("Analyzing artist: %s" % artist)
        songs = os.listdir(lyrics_dir)
            # Only the .txt files
        songs = [song for song in songs if len(song)>=4 and song[-4:]=='.txt']
        os.chdir(lyrics_dir)
        for song in songs:
            # create .ipa file
            cmd = u"espeak -xqf %s --phonout= %s.ipa" %(song, song)
            subprocess.run(cmd, stdout=subprocess.PIPE)
            
def main():
    IPA(dir=path, language='en-us', lookback=15)

if __name__ == '__main__':
    main()

