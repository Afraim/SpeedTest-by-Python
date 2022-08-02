import os
import time
from logging import exception
from traceback import print_tb
from unittest import expectedFailure
import speedtest

def testing():
    test = speedtest.Speedtest()

    try:
        print("Loading Servers...")
        test.get_servers()
    except:
        print("No server found check internet connection")
        os.system("pause")
        exit(1)

    try:
        print("Loading Best Server...")
        best = test.get_best_server()
    except:
        print("Best server not found please retry after some time")
        os.system("pause")
        exit(1)

    try:
        print("Performing Test...")
        download_result = test.download()
    except:
        print("Download Speed not found")
        os.system("pause")
        exit(1)

    try:
        print("Performing Test...")
        upload_result = test.upload()
    except:
        print("Upload speed not found")
        os.system("pause")
        exit(1)
    print("\t..........Afraim's Internet Speed Tester..........")
    print("...Success...")
    time.sleep(0.5)
    os.system("cls")
    download_result = download_result / (1024 * 1024)
    print(f"Download Speed: {download_result:.2f} Mbps")
    upload_result = upload_result / (1024 * 1024)
    print(f"Upload Speed: {upload_result:.2f} Mbps")
    print("Ping: ", test.results.ping," ms\n\n")


    os.system("pause")
    choice = input("1) Check again, 0) Exit\n:")

    if choice=="1":
        os.system("cls")
        main()
    elif choice == "2":
        exit(0)
    



def main():
    print("\t..........Afraim's Internet Speed Tester..........")
    testing()


main()
