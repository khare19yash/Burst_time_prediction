import sys

def print_log(logfilename):
    fin = open(logfilename,'r');

    while 1:
            lines = fin.readlines(10000000) # 10M buffer
            if not lines: break
            #-- process lines
            for line in lines:
                print(line)

    fin.close()

def main(argv):
    if (len(argv) > 0):
        logfilename = argv[0]
        print_log(logfilename)
    else:
        print("Usage: load_gwf.py <logfile>")
        exit()

if __name__ == "__main__":
    main(sys.argv[1:])
    
