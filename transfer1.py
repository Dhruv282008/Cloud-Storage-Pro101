import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "07lqo7Oq8IYAAAAAAAAAAcx-f-KD8RvHHC6TdQE5hpsSEc4HSeNYzQbQpXIY_QXz"
    transferData = TransferData(access_token)

    file_from = 'file.txt'
    file_to = '/UPLOADING FILES_CLOUDSTORAGE/file.txt'

    transferData.uploadFile(file_from, file_to)

    print("File Moved SUCCESSFULLY")
    print(input("Do you like this application(Rate out of 5): "))
    print("Thank You for Your Review")

if __name__ == '__main__':
    main()

    



