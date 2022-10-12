import socket

# read and parse command Line arguments
userInput = input("Enter host, port, and file name in comma separated format: ").split(', ')
host = userInput[0]
port = int(userInput[1])
file = open(userInput[2], "a")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    try:
        s.connect((host, port))
    except Exception as e:
        print("error connecting to server: " + str(e))
        file.write("error connecting to server: " + str(e))

    # send a string to server
    try:
        message = "network"
        s.send(message.encode('utf-8'))

        data = s.recv(1024)  # data received back and decoded
        data.decode('utf-8')
        file.write("\nMessage receiver: " + str(data))
        print(f"Received {data!r}")
    except Exception as e:
        print("error sending message to server: " + str(e))
        file.write("error sending message to server: " + str(e))

    # close connection to server
    try:
        s.close()
    except Exception as e:
        print("error closing connection to server: " + str(e))
        file.write("error closing connection to server: " + str(e))
