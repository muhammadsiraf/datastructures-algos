class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        
        """
        repeat = True
        playlist = False
        this_playlist = self
        while repeat:
            print(self.name)
            if self.next!=None:  
                print(self.next.name)
                if self.next==this_playlist:
                    playlist = True
                    repeat = False
            elif self.next==None:
                repeat = False
            self=self.next
            
        return playlist
    
    def is_loop(self):
        loop = False
        slow_p = self
        fast_p = self.next
        
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("found")
                return True
            
        return False
            
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())
if first.is_loop():
    print("True")
else:
    print("False")
