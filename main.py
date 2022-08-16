import os
import time
# from logging import exception
# from traceback import print_tb
# from unittest import expectedFailure
import speedtest
def tryAgain(C):
    if C=="1":
        main()
    else :
        exit(0)
    


def testing():
    try:
        test = speedtest.Speedtest()
    except:
        print("Timeout! can not connect")
        tryAgain(input("Press 1 to try agian and any key to exit: "))

    try:
        print("Loading Servers...")
        test.get_servers()
    except:
        print("No server found check internet connection")
        tryAgain(input("Press 1 to try agian and any key to exit: "))

    try:
        print("Loading Best Server...")
        best = test.get_best_server()
    except:
        print("Best server not found please retry after some time")
        tryAgain(input("Press 1 to try agian and any key to exit: "))

    try:
        print("Performing Test...")
        download_result = test.download()
    except:
        print("Download Speed not found")
        tryAgain(input("Press 1 to try agian and any key to exit: "))

    try:
        print("Performing Test...")
        upload_result = test.upload()
    except:
        print("Upload speed not found")
        tryAgain(input("Press 1 to try agian and any key to exit: "))
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
    
    tryAgain(input("Press 1 to try agian and any key to exit: "))
    



def main():
    os.system("cls")
    print("\t..........Afraim's Internet Speed Tester..........")
    testing()


main()
