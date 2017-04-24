from lantern.modules import simplesubstitution
from lantern.score_functions import ngram

ciphertext = """Tmlk fqp oaiazpa, qda kluai oabafuar kazo tkfuaopzi zbbizfj. Ziqdltcd Rfbhakp' blkqajmlozox Qdljzp Bzoixia oasaooar ql fq rfpmzozcfkcix zp qdzq "Mfm klkpakpa," da kauaoqdaiapp oazbqar ql azbd soapd fkpqzijakq vfqd "olzop ls iztcdqao."Izqao, Caloca Eaokzor Pdzv mozfpar qda kluai, zp "Zii ls lka mfaba zkr blkpfpqakqix qotqdsti." Rtofkc qda paofzi mteifbzqflk, Rfbhakp vzp miazpar vfqd mteifb oapmlkpa ql Coazq Awmabqzqflkp zkr fqp pziap; vdak qda milq sfopq slojar fk dfp jfkr, da bziiar fq "z uaox sfka, kav zkr colqapnta fraz."""

decryptions = simplesubstitution.crack(ciphertext, [ngram.quadgram()])
top_decryption = decryptions[0]
print(top_decryption.plaintext)
