from pathlib import Path
from dotenv import load_dotenv
from os import environ
from lineNotify import LineNotify
from scraping import Scraping
from fileControl import FileControl


def main():

    DOT_ENV_PATH = Path('.env')
    load_dotenv(DOT_ENV_PATH)

    LINE_NOTIFY_TOKEN = environ.get("LINE_NOTIFY_TOKEN")
    NOTIFICATION_OLD_PATH = Path('notification/old.html')
    NOTIFICATION_OLD_NEW = Path('notification/new.html')

    scraping = Scraping()
    scraping.getHtml(targetUrl='https://[domain]]/')
    notificationHtml = str(scraping.getHtmlOfSpecifyClass(
        targetClass='.c_block.p_top_news_block')[0])

    file = FileControl(NOTIFICATION_OLD_NEW)
    file.saveContextToFile(context=notificationHtml)

    if (FileControl.isSameFile(filePath1=NOTIFICATION_OLD_PATH, filePath2=NOTIFICATION_OLD_NEW) != True):
        lineNotifyToken = LINE_NOTIFY_TOKEN
        lineNotify = LineNotify(lineNotifyToken=lineNotifyToken)

        notificationMessage = "백신접종예약에 관한 정보가 갱신되었음!!!!!\nワクチン接種予約情報が更新されました！！！！\n(https://[domain]/)"
        lineNotify.setPayload(notificationMessage=notificationMessage)

        lineNotify.sendRequest()

        file = FileControl(NOTIFICATION_OLD_PATH)
        file.saveContextToFile(context=notificationHtml)


if __name__ == "__main__":
    main()
