from pwn import *
import requests, signal, argparse, time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def def_handler(sig, frame):
    print("\n\n[!]Bye\n\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

def banner():
    print("""
    ███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
    █████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
    ██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                 
    \t\t\t\t\t\t\tBy: h4ckndr3s
    """)

def load_progress():

    p1 = log.progress("Web Fuzzing")
    loading = p1.status = "Fuzzing..."
    return  loading


def verify_url(url):

    if url[0:7] == "http://" or url[0:8] == "https://":
        return True
    else:
        print("\nYou have to specify the protocol")
        print(f'\n{bcolors.BOLD}Example http:// or https://')
        return False

def validate_root_directory(url):
    if url[-1] == "/":
        return True
    else:
        return False

def enumerate_directory(url, word, progress):
    full_url = url + word
    request = requests.get(full_url)
    status = f'URL: {full_url}\t\t\t\tStatus: {request.status_code}'
    
    progress.status(status)
    if request.status_code == 200:
        print(f'{bcolors.OKGREEN}{status}')
    elif request.status_code != 404:
        print(f'{bcolors.OKCYAN}{status}')

def enumerate_subdomain(url, word, progress):
    if url[0:7] == "http://":
        full_url = url[0:7] + word + "." + url[7:]                    
    elif url[0:8] == "https://":
        full_url = url[0:8] + word + "." + url[8:]

    try:
        request = requests.get(full_url)
        status = f'URL: {full_url}\t\t\t\tStatus: {request.status_code}'
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        request = 0
        status = f'URL: {full_url}\t\t\t\tStatus: This website cannot be accessed'    
    progress.status(status)

    if type(request) is requests.models.Response:
        if request.status_code == 200:
            print(f'{bcolors.OKGREEN}{status}')
        elif request.status_code != 404:
            print(f'{bcolors.OKCYAN}{status}')


def enumerate(url, dictionary, option, time_op):
    load_progress()
    progress = log.progress("Progress")
    signal.signal(signal.SIGINT, def_handler)

    if verify_url(url) == True:

        if validate_root_directory(url) == False:
            url = url + "/"
        else:
            pass

        try:
            dictionary = open(dictionary, "r")
        except:
            print(f"{dictionary} doesn't exist")
            pass

        for word in dictionary:
            word = word.rstrip()

            match option:
                case 1:
                    enumerate_directory(url, word, progress)
                case 2:
                    enumerate_subdomain(url, word, progress) 
            if time_op != None: 
                time.sleep(time_op)
            elif option ==2:
                time.sleep(0.4)
    else:
        pass

if __name__ == "__main__":
    
    banner()

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--mode", "-m", help="Please add the mode. Example: directory or subdomain", required=True)
    parser.add_argument("--url", "-u", help="Please give a URL. Example: https://google.com", required=True)
    parser.add_argument("--dictionary", "-d", help="Please add a dictionary. Example: /usr/share/dirb/wordlists/common.txt", required=True)
    parser.add_argument("--time", "-t", help="Time between requests (in seconds). Examples --time 2", type=int, required=False)

    args = parser.parse_args()

    if args.mode == "directory":
        enumerate(args.url, args.dictionary, 1, args.time)
    elif args.mode == "subdomain":
        enumerate(args.url, args.dictionary, 2, args.time)
    else:
        pass
