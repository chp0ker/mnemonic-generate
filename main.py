import threading
import uuid

from bip_utils import Bip39WordsNum, Bip39MnemonicGenerator, Bip39Languages


def mnemonic_gen():
    while True:
        with open(f"{name_file}.txt", "a+") as file:
            mnemonic = Bip39MnemonicGenerator(Bip39Languages.ENGLISH).FromWordsNumber(Bip39WordsNum.WORDS_NUM_15)
            print(f"Mnemonic: {mnemonic}")
            file.write(f"{mnemonic}\n")


if __name__ == '__main__':
    name_file = str(uuid.uuid4())
    for _ in range(1000):
        threading.Thread(target=mnemonic_gen).start()
