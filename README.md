# Installation

```
# clone the repo
$ git clone https://github.com/h4ckndr3s/Fuzzer.git

# change the working directory to Fuzzer
$ cd Fuzzer

# install the requirements
$ python3 -m pip install -r requirements.txt

```

# Usage

```bash
$ python3 fuzzer.py --help


    ███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
    █████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
    ██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                 
                                By: h4ckndr3s
    
usage: fuzzer.py [-h] --mode MODE --url URL --dictionary DICTIONARY [--time TIME]

options:
  -h, --help            show this help message and exit
  --mode MODE, -m MODE  Please add the mode. Example: directory or subdomain
  --url URL, -u URL     Please give a URL. Example: https://google.com
  --dictionary DICTIONARY, -d DICTIONARY
                        Please add a dictionary. Example: /usr/share/dirb/wordlists/common.txt
  --time TIME, -t TIME  Time between requests (in seconds). Examples --time 2

```

To enumerate directories:

```bash
$ python3 fuzzer.py --mode directory --url <URL> -d <WORDLIST>
```

To enumerate subdomains:

```bash
$ python3 fuzzer.py --mode subdomain --url <URL> -d <WORDLIST>
```