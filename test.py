from G30S import Garuda1945, Garuda45
from base64 import b64decode
from G30S.utils import reverseString

def Garuda45Decoder(enc):
    typeList = ["54ADURAG4".upper(), "54ADURAG4".lower()]
    split = len(enc)
    ori_enc = enc[split-1]
    ori_enc = enc[int(ori_enc):]
    encrypted = ""
    for tipe in typeList:
        if tipe in ori_enc:
            encrypted = ori_enc.replace(tipe, "")
            break
    b64d = b64decode(encrypted)
    print ("original enc: " + enc)
    print ("result: " + reverseString(b64d.decode()))

garuda = Garuda45()
garuda.encrypt("Billal tech")
garuda.show
Garuda45Decoder(garuda.result)
