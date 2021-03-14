sklep = {"jajka":"szt","szynka":"g","ziemniaki":"kg","mleko":"ml","dżem":"szt","chleb":"kg","kajzerki":"szt","jabłka":"kg"}

#odwrocone2 = {value: key for key, value in sklep.items() if value == 'szt'}
sztuki = {key:value for key, value in sklep.items() if value == "szt"}
print(sztuki)