from .kamus import kamus

class Alay:
  def __init__(self):
    self.teks = ""

  def besarkecil(self):
    teks = self.teks
    hasil = ""
    for i in range(len(teks)):
      if i % 2 == 0:
        hasil = hasil + teks[i].upper()
      else:
        hasil = hasil + teks[i].lower()
    return hasil

  def gabunganangka(self):
    teks = self.teks
    hasil = ""
    kamus = ['4', '3', '6', '!', '7', '0', '5', '2']
    for i in range(len(teks)):
      if teks[i] == 'a':
        hasil = hasil + kamus[0]    
      elif teks[i] == 'e':
        hasil = hasil + kamus[1]  
      elif teks[i] == 'g':
        hasil = hasil + kamus[2]  
      elif teks[i] == 'i':
        hasil = hasil + kamus[3]  
      elif teks[i] == 'j':
        hasil = hasil + kamus[4]  
      elif teks[i] == 'o':
        hasil = hasil + kamus[5]  
      elif teks[i] == 's':
        hasil = hasil + kamus[6]  
      elif teks[i] == 'z':
        hasil = hasil + kamus[7]
      else:
        hasil = hasil + teks[i]
    return hasil

  def vokal(self):
    teks = self.teks
    kamus = ['a', 'i', 'u', 'e', 'o']
    for e in teks:
      if e in kamus:
        teks = teks.replace(e, 'i')
    return teks

  def konversi_kata(self):
    kata = self.teks.split()

    kamus_key = kamus.keys()
    kamus_key = list(kamus_key)

    for i in range(len(kata)):
      if kata[i] in kamus_key:
        kata[i] = kamus[kata[i]]
    
    hasil = ' '.join(kata)
    return hasil