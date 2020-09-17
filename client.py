import socket
import time

try:
    file = open("targethosts.txt","r")   #File open read mode
    server_list = file.readlines()          
    server_list_len = len(server_list)       
    file.close()                         
except IOError:                          
    print("File Does Not Exist.Please check file.")
    pause_exit(0, "Press Any Key To Exit...")


file = open("targethosts.txt","r")   

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpClient.settimeout(1.0)

def get_server_ip(file):                   #read server adress from file
    server_list= file.readline()       
    ip_address=str(server_list[0:len(server_list)-1])   
    return ip_address               

def UPD_ping(ip,pings):             
    message=b'ping'  
    message=message.upper()              
    address = (str(ip),12345)       #port and adress
    rtt_start = (time.time() * 1000)    
    
    udpClient.sendto(message, address)   #send massage
    
    print('#'+str(pings + 1)+ '. ->'+' UDP:'+address[0]) 
    print("Send time  :  "+str(rtt_start/10000000000000)+"  seconds.")

    try:
         data, server = udpClient.recvfrom(1024) 
         rtt_end = (time.time() * 1000)         
         elapse = (rtt_end - rtt_start)     
         print('RTT        :  '+str(elapse)+'  ms \n')  #rtt -elapse
         print("Request : %s" % message)        			#Client request
         print("Response: %s" % data+'\n')       		#Server response
    except socket.timeout:                  
         print('timeout!! \n')      
     
for i in range(server_list_len):                      
    ip_address = get_server_ip(file)                        
    print(str(i+1)+".Target Server: "+str(ip_address))     
    for pings in range(5):                          
        UPD_ping(ip_address,pings)                  
    print("\n\n")

input("Press Any Key To Exit...")