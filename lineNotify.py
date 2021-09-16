import requests


class LineNotify:

    API_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, lineNotifyToken):
        self.__headers = {
            'Authorization': f'Bearer {lineNotifyToken}',
        }

    def setPayload(self, notificationMessage):
        self.__payload = {
            'message': f'message: {notificationMessage}'
        }
        return self.__payload

    def sendRequest(self):
        requests.post(LineNotify.API_URL, headers=self.__headers, data=self.__payload)
