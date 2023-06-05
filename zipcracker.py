import zipfile

from tqdm import tqdm

print("C0d3d by R3bik")

help = input("You need help? [1/2]: ")

if help == 1:

	print("so that the script does not give an error and works correctly, place the script file (required in py format) in the same folder with passwords and zip")

	

wordlist = "passwords.txt"

zip_file = "zipfile.zip"

zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(wordlist, "rb")))

print("Total passwords:", n_words)

with open(wordlist, "rb") as wordlist:

    for word in tqdm(wordlist, total=n_words, unit="word"):

        try:

            zip_file.extractall(pwd=word.strip())

        except:

            continue

        else:

            print("[+] Password cracked:", word.decode().strip())

            exit(0)

print("[-] Password not found.")

#C0d3d by R3bik
