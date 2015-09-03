import zipfile
import optparse
from threading import Thread


def crackfile(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print '[+] Password is :' + password + '\n'
        print '[+] Congratulations...  File extracted !'
        return True
    except:
            pass    
            

def readpassword():
    for line in passwordfile.readlines():
        
        global password
        password = line.strip('\n')
        t = Thread(target=crackfile, args=(zfile, password))
        t.start()
    

        

def main():
        parser = optparse.OptionParser("usage :"+\
			"-f <target zip file> -d <dicctionary list>")
        parser.add_option('-f', dest='zipfilename', type='string',\
                                help='password protected zip file')
	parser.add_option('-d', dest='dictionaryname', type='string',\
                                help='dictionary list(.txt)')
	(options, arg) = parser.parse_args()

        print '\t\t\t ######################################'
        print '\t\t\t ##                                  ##'
        print '\t\t\t ##      Author : Sandeep Saini      ##'
        print '\t\t\t ##        Version : V0.1zPC         ##'
        print '\t\t\t ######################################'

        global passwordfile
	global zfile
	
	if (options.zipfilename == None) | (options.dictionaryname == None):
		print parser.usage
		exit(0)
        else:
                zipfilename = options.zipfilename
                dictionaryname = options.dictionaryname
                zfile = zipfile.ZipFile(zipfilename)
                passwordfile = open(dictionaryname)
        readpassword()
        if not crackfile(zfile, password):
            print '[-] Sorry... Paasword Could not found'
            print '[+] Here is the solution : Try with diffrent dictionary list!'
            
        
main()
