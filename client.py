import socket
from win10toast import ToastNotifier


def receive_file_and_notification():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Replace 'server_ip' with the IP address of the server
    server_address = ('server_ip', 12345)

    try:
        client_socket.connect(server_address)

        # Receive the text file content from the server
        file_content = client_socket.recv(4096).decode()

        # Show the notification
        header = 'This is an Alert!'
        message = file_content
        icon_path = "path_to_icon.ico"  # Replace with the path to the icon file
        num_notifications = 10

        my_notifications = ToastNotifier()
        for num in range(num_notifications):
            my_notifications.show_toast(title=header,
                                        msg=message,
                                        icon_path=icon_path,
                                        duration=num_notifications)

        # Wait for threaded notification to finish
        while my_notifications.notification_active():
            time.sleep(0.1)

    except ConnectionRefusedError:
        print("Connection to the server was refused. Please check the server IP and port.")
    except ConnectionError:
        print("An error occurred while connecting to the server.")
    finally:
        client_socket.close()


if __name__ == "__main__":
    receive_file_and_notification()
