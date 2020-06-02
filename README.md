# icanseeyou

### A simple and light weight port scanner

## Requirment:

### packages 

- socket
- argparse
- sys
- bcolors

### python > 3.x 

## usage: 

portscan.py  -i < Valid ip address > -s1 < start range of port scan > -s2 < end range of port scanning >


OPTIONS: 

```
-h             --help    
             	    < show the available options >
-i             valid Ip address 
  		            < Ip address whose open ports you want to check >
-s1	       Starting port range only ending octate
		< start range of port eg. 100 >  	
-s2	       Ending port range
		< end range of port eg. 110 >
    So it will scan the ports from 100-110
    
```

