from PyPDF2 import PdfFileMerger
import optparse

def banner():
    print("           .___ _____                                            ")
    print("______   __| _// ____\   _____   ___________  ____   ___________ ")
    print("\____ \ / __ |\   __\   /     \_/ __ \_  __ \/ ___\_/ __ \_  __ \ ")
    print("|  |_> > /_/ | |  |    |  Y Y  \  ___/|  | \/ /_/  >  ___/|  | \/")
    print("|   __/\____ | |__|    |__|_|  /\___  >__|  \___  / \___  >__|   ")
    print("|__|        \/               \/     \/     /_____/      \/       ")

    print("\n" + "*"*66)
    print("\t\t  Author  : Furkan BEKAR\n\t\t  Version : 1.0\n\t\t  GitHub  : https://github.com/FurkanBekar")
    print("*"*66)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-f","--final",dest="final",help="Enter the final file name. Enter the name of the file that will occur when you merge it.")
    parse_object.add_option("-l","--list",dest="list",help="Merges your files according to the list in the file you given.")
    parse_object.add_option("-m","--merge",dest="merge",help="Enter the file locations you want to merge",nargs="*")

    return parse_object.parse_args()


def merge(pdfs=None):
    if pdfs == None:
        file_name = input("Lütfen birleştirmek istediğiniz pdf dosyalarının adını sırasıyla giriniz :")

        pdfs = []

        while (file_name != "q"):
            pdfs.append(file_name + ".pdf")
            file_name = input("Birleştirmek istediğiniz dosyalar bittiğinde lütfen q ya basın : ")

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    final_name = input("Lütfen nihai dosya adını giriniz : ")

    merger.write(final_name)
    merger.close()

banner()

(user_input,arguments) = get_user_input()
print(user_input)
merge()






