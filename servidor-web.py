#!/usr/bin/env python3
import sys, os, time, math
import string,cgi,time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class http(BaseHTTPRequestHandler): 

    def do_GET(self):
        try:
            """ if self.path.endswith(".html"):
                f = open(DocumentRoot + self.path)
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            if self.path.endswith(".esp"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write("hey, today is the" + str(time.localtime()[7]))
                self.wfile.write(" day in the year " + str(time.localtime()[0]))
                return """
            
            """ if self.path!=".":
                path = "lista.txt"
            else:
                path = self.path
            f = open(DocumentRoot + path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close() """
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            if self.path=="/":
                self.wfile.write(
                    '''<!DOCTYPE html>
                    <html>
                    <body>
                        <h1>Projeto</h1>
                        <form action="/" method="get">
                        <label for="letra">Letra:<input type="text" id="letra" name="letra"></label>
                        <input type="submit" value="ENVIAR">
                        </form>
                    </body>
                    </html>
                    '''
                )
            else:
                self.wfile.write(
                    '''<!DOCTYPE html>
                        <html>
                        <body>
                            <h1>Projeto-Resultado</h1>
                            <p>Resultado:%s</p>
                        </body>
                        </html>
                        ''' % (self.path.split("=")[1])
                )
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    """ def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            self.send_header('Content-type','text/html')
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write(
                '''<!DOCTYPE html>
                    <html>
                    <body>
                        <h1>Projeto-Resultado</h1>
                        <p>Resultado:%s</p>
                    </body>
                    </html>
                    ''' % upfilecontent[0]
            )
        except:
            pass """
       
def main(NameVirtualHost):

    try:
        virtualhost = string.split(NameVirtualHost,":")
        if virtualhost[0] == "*":
            virtualhost[0] = ""
         
        server = HTTPServer((virtualhost[0], int(virtualhost[1])), http)
        print 'Start server HTTP IN %s' % NameVirtualHost
        server.serve_forever()

    except KeyboardInterrupt:
        print 'Shutting down server HTTP'
        server.socket.close()

if __name__ == '__main__':
    DocumentRoot = os.path.realpath(os.path.dirname(__file__))+"/"
    PORT = "8080"
    HOST = "localhost"
    #print HOST,":",PORT,DocumentRoot
    try :
        main(sys.argv[1])
    except :
        main("%s:%s" % (HOST,PORT))
""" from pyDF import*
sys.path.append(os.environ["PYDFHOME"])

def readFile(args):
    filename = args[0]
    f = open(filename, "r")
    vetor = []
    for linha in f:
        vetor.append(linha)
    f.close()
    return nprocs, vetor

def filtraAlbums(args):
    sp1 = args
    sp = sp1[0].split("    ")
    if len(sp) == 2:
        aux = sp[1][:-1]
        if (aux == "A"):
            ret = sp1[0][:-1]
        else:
            ret = ""
    else:
        ret = "not found"
    return ret

def printAlbums(args):
    if args[0] != "":
        print args[0]

nprocs = int(sys.argv[1])
filename = sys.argv[2]
graph = DFGraph()
sched = Scheduler(graph, nprocs, mpi_enabled = False)
fp = open(filename, "r")
src = Source(fp)
graph.add(src)
nd = FilterTagged(filtraAlbums, 1)
graph.add(nd)
ser = Serializer(printAlbums, 1)
graph.add(ser)
src.add_edge(nd, 0)
nd.add_edge(ser, 0)
t0 = time.time()
sched.start()
t1 = time.time()

print "Execution time %.3f" %(t1-t0)
t1 = time.time()

print "Execution time %.3f" %(t1-t0) """
