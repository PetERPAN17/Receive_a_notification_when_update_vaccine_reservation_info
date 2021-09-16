import filecmp

class FileControl:

    def __init__(self, filePath):
        self.__filePath = filePath

    def getFileContext(self):
        file = open(self.__filePath, 'r')
        context = file.read()
        file.close()
        return context

    def saveContextToFile(self, context):
        file = open(self.__filePath, 'w+')
        file.write(context)
        file.close()

    def isSameFile(filePath1, filePath2):
        return filecmp.cmp(filePath1, filePath2)
        