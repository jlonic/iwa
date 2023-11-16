import socket


def connect_to_server(ip, port):
    s=socket.socket()
    s.connect((ip, port))    
    return s

def get_source(s, ip, page):

    get='GET /'+page+' HTTP/1.1'+'\r\n'+'Host: '+ip+'\r\n\r\n'
    #print(get)
    s.send(get.encode('utf-8'))
    response=s.recv(10000000000).decode('latin-1')
    #print(response)
    return response


def get_all_links(response, links):
    beg=0
    while True:
        beg_str=response.find('href=', beg)

        if beg_str==-1:
            return links

        end_str=response.find('"', beg_str+6)
        link=response[beg_str+6:end_str]

        if link not in links:
            links.append(link)
        beg=end_str+1

    return links


ip='www.optimazadar.hr'
port=80
links=[]

s=connect_to_server(ip, port)

page='1280/djelatnost1280.html'
#linkovi=['1280/djelatnost1280.html', '1280/galerija1280.html', '1280/reference1280.html', '1280/kontakt1280.html']
#for page in linkovi:
response=get_source(s, ip, page)
links=get_all_links(response, links)


# for i in range(len(links)):
#      response=get_source(s, ip, links[i])
#      get_all_links(response, links)


print(links)
print('\nu listi ima ' +  str(len(links)) + ' linkova')