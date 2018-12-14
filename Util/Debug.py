"""This is Debug class
@authorized by Gennne Chung
@description: for log
"""

class Debug:
    tag = ""
    subtag = ""
    
    def __init__(self, tag):
        self.tag = tag
        
    def log(self, data):
        if self.subtag == "":
            print("[" + str(self.tag) + "] " + str(data))
        else:
            print("[" + str(self.tag) + "] <" + str(self.subtag) + "> " + str(data))
        
    def log_t(self, subtag, data):
        print("[" + str(self.tag) + "] <" + str(subtag) + "> " + str(data))
