import time
import os
from win10toast import ToastNotifier

def read_alert_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except IOError:
        print("An error occurred while reading the file.")
    return ""

def show_toast_notifications(header, message, icon_path, num_notifications):
    my_notifications = ToastNotifier()
    for num in range(num_notifications):
        my_notifications.show_toast(title=header,
                                    msg=message,
                                    icon_path=icon_path,
                                    duration=num_notifications)
    # Wait for threaded notification to finish
    while my_notifications.notification_active():
        time.sleep(0.1)

if __name__ == "__main__":
    file_path = "alert.txt"
    run_while_num = 10

    file_content = read_alert_from_file(file_path)

    header = 'This is an Alert!'
    message = file_content

    script_directory = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_directory, "ndwestern_iv4_7.ico")

    show_toast_notifications(header, message, icon_path, run_while_num)

    print('Done sending notifications')
