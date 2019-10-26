require 'socket'

server = TCPServer.open(2000)

loop{
    client = server.accept
    client.puts(Time.now.ctime)
    client.puts "Closing connection on client"
    client.close
}