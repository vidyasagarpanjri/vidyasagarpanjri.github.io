---
layout: post
title: Creating filter template for apimonitor
---



### Tools used
  
  * API Monitor v2 (Alpha-r13) - x86 32-bit     [Download as per your OS](http://www.rohitab.com/downloads)
  * peframe   [DOwnload and install from here](https://github.com/guelfoweb/peframe)
  
### Problem statement  

During the Dynamic analysis of any file in window we often(we = me) use apimoitor from rohitab. It is a very handy tool, we can monitor the apicalls and argumets passed. 
 But problem I face is to quicly find out what APIs to monitor how quckly we can check/select those APIs.
 
 As I wrote this script specily for malware analysis, I used peframe by [@guelfoweb](https://twitter.com/guelfoweb) to get possible APIs.
### peframe result
[![asciicast](https://asciinema.org/a/pRG8MROJMfcptYBrbXjWmLwOX.svg)](https://asciinema.org/a/pRG8MROJMfcptYBrbXjWmLwOX)

 I have modified the the peframe little bit to get APIs along with their libraries names, something like "KERNEL32.TerminateProcess".
    update "peframe/peframe/modules/apialert.py" file
      replace line '''alerts.append(imp.name.decode('ascii'))''' with '''alerts.append(str(lib.dll)[2:-5]+"."+imp.name.decode('ascii'))'''
### update peframe apialert.py module
[![asciicast](https://asciinema.org/a/X9ccxQXWcXxVKMjxNo76vMrci.svg)](https://asciinema.org/a/X9ccxQXWcXxVKMjxNo76vMrci)

now using the script we can create the filter xml for apimonitr.
### demo
file [create_apimonitortab.py](https://github.com/vidyasagarpanjri/vidyasagarpanjri.github.io/blob/master/_posts/data/2021-05-21/create_apimonitortab.py)
[![asciicast](https://asciinema.org/a/415543.svg)](https://asciinema.org/a/415543)
now just load xml file in the apimonitor  see the magic.
