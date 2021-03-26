#include <iostream>
#include <sstream>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
 
static void usage();
 
int main(int argc, char *argv[])
{
    if (argc > 1 && *(argv[1]) == '-')
    {
        usage(); exit(1);
    }
 
    // Create socket
    int s0 = socket(AF_INET, SOCK_STREAM, 0);
    if (s0 < 0)
    {
        std::cerr << "Error: " << strerror(errno) << std::endl;
        exit(1);
    }
 
    // Fill in server IP address
    struct sockaddr_in server;
    int serverAddrLen;
    bzero( &server, sizeof( server ) );
 
 
    char* peerHost= "127.0.0.1";
    if (argc > 1)
        peerHost = argv[1];
 
    // Resolve server address (convert from symbolic name to IP number)
    struct hostent *host = gethostbyname(peerHost);
    if (host == NULL)
    {
        std::cerr << "Error: " << strerror(errno) << std::endl;
        exit(1);
    }
 
    server.sin_family = AF_INET;
    short peerPort = 1234;
    if (argc >= 3)
        peerPort = (short) atoi(argv[2]);
    server.sin_port = htons(peerPort);
 	//host->h_addr_list[0]='127.0.0.1';
    // Print a resolved address of server (the first IP of the host)
    std::cout << "server address = " << (host->h_addr_list[0][0] & 0xff) << "." <<
                                        (host->h_addr_list[0][1] & 0xff) << "." <<
                                        (host->h_addr_list[0][2] & 0xff) << "." <<
                                        (host->h_addr_list[0][3] & 0xff) << ", port " <<
                                        static_cast<int>(peerPort) << std::endl;
 
    // Write resolved IP address of a server to the address structure
    memmove(&(server.sin_addr.s_addr), host->h_addr_list[0], 4);
 
    // Connect to the remote server
    int res = connect(s0, (struct sockaddr*) &server, sizeof(server));
    if (res < 0)
    {
        std::cerr << "Error: " << strerror(errno) << std::endl;
        exit(1);
    }
 
    std::cout << "Connected. Reading a server message" << std::endl;
 
    char buffer[1024];
    res = read(s0, buffer, 1024);
    if (res < 0)
    {
        std::cerr << "Error: " << strerror(errno) << std::endl;
        exit(1);
    }
 
    std::cout << "Received:" << "\n" << buffer;
 
    write(s0, "1900000000000\n", 20);
 
    close(s0);
    return 0;
}

static void usage() {
    std::cout << "A simple Internet server application.\n"
              << "It listens to the port written in command line (default 1234),\n"
              << "accepts a connection, and sends the \"Hello!\" message to a client.\n"
              << "Then it receives the answer from a client and terminates.\n\n"
              << "Usage:\n"
              << "     server [port_to_listen]\n"
              << "Default is the port 1234.\n";
}