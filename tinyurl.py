class Codec:
    alphnumeric=string.ascii_letters+string.digits
    def __init__(self):
        self.url2code={}
        self.code2url={}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        while longUrl not in self.url2code:
            code=''
            for i in range(6):
                code+=random.choice(Codec.alphnumeric)
            if code not in self.code2url:
                self.url2code[longUrl]=code
                self.code2url[code]=longUrl
        #url_list=longUrl.split('/')
        #print url_list[0]+'/'+url_list[1]+'/'+url_list[2]+'/'+code
        #return url_list[0]+'/'+url_list[1]+'/'+url_list[2]+'/'+code
        return "http://tinyurl.com/"+code
            
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        code=shortUrl[-6:]
        return self.code2url[code]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode(url))