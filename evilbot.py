import webbrowser
import os
import sys
import random
from random import randint
import time
import schedule


def ran_time():
    sec = randint(20, 200)
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")


def open_page():
    link = ["https://techforhack.com/84-woocommerce-extensions-updates/",
            "https://techforhack.com/56-woocommerce-extensions-updates/",
            "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
            "https://techforhack.com/elementor_pro_3-0-4_nulled/",
            "https://techforhack.com/adobe-cc-2020-universal-crack-for-adobe-cc-2020-full-version/",
            "https://techforhack.com/wireshark-termux/",
            "https://techforhack.com/windows-10-kali-linux-subsystem-full-tutorial/",
            "https://techforhack.com/tool-x/",
            "https://techforhack.com/routersploit/",
            "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
            "https://techforhack.com/networkingfundamentals/",
            "https://techforhack.com/networkdevices/",
            "https://techforhack.com/portable_hacking_device/",
            "https://techforhack.com/tbomber/",
            "https://techforhack.com/metasploit-termux/",
            "https://techforhack.com/lazy_script/",
            "https://techforhack.com/nethunter-on-android/",
            "https://techforhack.com/install-hidden-eye-advanced-phishing-tool-full-guide/",
            "https://techforhack.com/instagram-tools-hack-insta-from-termux/",
            "https://techforhack.com/black_hydra/",
            "https://techforhack.com/nmap/",
            "https://techforhack.com/hackpro/",
            "https://techforhack.com/fix-any-android-game-lag-in-few-minutes/",
            "https://techforhack.com/elementor_pro_3-0-4_nulled/",
            "https://techforhack.com/ddos-termux/",
            "https://techforhack.com/databasetechnology/",
            "https://techforhack.com/database-models-all-you-need-to-know/",
            "https://techforhack.com/metasploit-payload-termux/"
            ]

    url_link_1 = random.choice(link)
    url_link_2 = random.choice(link)
    url_link_3 = random.choice(link)

    print("Opening URL")
    print(url_link_1, "||", url_link_2, "||", url_link_3)

    webbrowser.open_new_tab(url_link_1)
    time.sleep(60)
    webbrowser.open(url_link_2)
    time.sleep(60)
    webbrowser.open(url_link_3)
    time.sleep(60)


def loop():
    global completed_views
    print("##################################################################################")
    print("Generate free traffic")

    i = randint(300, 1000)

    print(i, "Generated")

    try:
        completed_views = 0
        while i > 0:
            print(i, " views remaining")
            open_page()
            ran_time()
            i -= 3
            completed_views += 3
            print("Closing Browser")
            os.system("./exi.sh")
    except Exception as e:
        print(e)
        print("you got", completed_views, "visitors")

    print("you got", completed_views, "visitors")


if __name__ == '__main__':
    print("prg start")
    # schedule.every(10).seconds.do(loop)
    # schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(loop)
    # schedule.every(5).to(10).minutes.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)