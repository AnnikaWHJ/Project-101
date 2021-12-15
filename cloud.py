import dropbpx

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

        def upload_file(self, file_from, file_to)
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files.upload(f.read()),

def main():
    access_token = 'riFu6Ybhc9AAAAAAAAAAHWkfE9AiGyD6n4254tOxesw7ShRjGjFhrjhRVa3NX3mx'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : - ")
    file_to = input("enter the full path to upload to dropbox:- ")


    transferData.upload_file(file_from, file_to)
    print("file has been moved !!! ")