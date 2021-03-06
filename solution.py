from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n This is My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    mailServer = (mailserver,port)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailServer)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':
       print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFromCommand = "MAIL FROM: <mailfrom@email.com> \r\n"
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024)
    print(recv2)
    if recv2[:3] != '250':
       print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcptToCommand = "RCPT TO: <rcptto@email.com> \r\n"
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024)
    print(recv3)
    if recv3[:3] != '250':
       print('250 reply not received from server.')

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = "DATA \r\n"
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024)
    if recv4[:3] != '250':
       print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    clientSocket.send("\r\n This is My message".encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send("\r\n.\r\n".encode())
    recv5 = clientSocket.recv(1024)
    if recv5[:3] != '250':
       print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = "QUIT \r\n"
    clientSocket.send(quitCommand)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')