class Song:
    
    def __init__(self, name):
        self.name = name
        self.next = None
        
    def next_song(self, song):
        self.next = song
        
    def is_repeating_playlist(self):
        if self.next.name == self.name:
            return True
        elif self.next.next.name == self.name:
            return True
        else:
            return None
        

first = Song('barakuda')
lagu = Song('balonku')
lagu2 = Song('cicak')
lagu3 = Song('ulangtahun')
first.next_song(lagu)
lagu.next_song(first)


print(lagu.is_repeating_playlist())

        
        