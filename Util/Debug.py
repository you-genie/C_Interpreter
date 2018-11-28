class Debug:
    tag = ""
    subtag = ""
    
    def __init__(self, tag):
        self.tag = tag
        
    def __init__(self, tag, subtag):
        self.tag = tag
        self.subtag = subtag
        
    def log(self, data):
        if self.subtag == "":
            print("[" + self.tag + "] " + data)
        else:
            print("[" + self.tag + "] <" + self.subtag + "> " + data)
        
    def log(self, subtag, data):
        print("[" + self.tag + "] <" + subtag + "> " + data)
