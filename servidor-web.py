#!/usr/bin/env python3
import sys, os, time, math
import string,cgi,time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from pyDF import*
sys.path.append(os.environ["PYDFHOME"])
def Chamada(workers, file):
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

	nprocs = int(workers)
	filename = file
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
	return "Execution time %.3f" %(t1-t0) 


class http(BaseHTTPRequestHandler): 
    def do_GET(self):
        try:
            
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            if self.path=="/":
                self.wfile.write(
                    ''' <!DOCTYPE html>
			<html>
				<body>
					<form action="/action_page.php">
					  <label for="fname">Quantidade de workers:</label><br>
					  <input type="text" id="fname" name="fname"><br>
					  <input type="submit" value="Submit">
					</form>
				</body>
			</html>

                    '''
                )
            else:
                self.wfile.write(
                    ''''<!DOCTYPE html>
                        <html>
                        <body>
                            <h1>Projeto-Resultado</h1>
                            <p>Resultado:%s</p>
                        </body>
                        </html>
                        ''' % Chamada(self.path.split("=")[1], "lista.txt")
                )

            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

       
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

