""""
@08/02/24
script to process and prepare parallel data for training.
we use the translated siswati bible text, therefore the model might be
bias to a religious context, but since this is for educational purposes
it should be sufficient.

Add more data here and twerk the PyTorch configs in order to improve the model.
"""

import sqlite3 as sq


###: this is where we will save our data for traininig and testing
###: we use parallel data, in english and siswati
EN_FILE = 'jw300.en-ss.en'
SS_FILE = 'jw300.en-ss.ss'


# 1. PROCESS BIBLE DATA

con = sq.connect("bible.db")

cur = con.cursor()

with open('bible.en-ss.en', 'w', encoding='utf-8') as f_en, open('bible.en-ss.ss', 'w', encoding='utf-8') as f_ss:
    cur.execute("SELECT NIV_VERSE, SISWATI_VERSE FROM VERSES;")
    for row in cur.fetchall():
        niv_verse, siswati_verse = row

        if not len(niv_verse) or not len(siswati_verse):
            continue

        # save each verse in the correct file
        f_en.write(niv_verse + "\n")
        f_ss.write(siswati_verse + "\n")

    cur.execute("SELECT distinct NIV_BOOK, SISWATI_BOOK FROM VERSES;")
    for row in cur.fetchall():
        niv_book, siswati_book = row
        
        f_en.write(niv_book + "\n")
        f_ss.write(siswati_book + "\n")


cur.close()
con.close()


with open('bible.en-ss.en', encoding='utf-8') as bible_en, \
        open('bible.en-ss.ss', encoding='utf-8') as bible_ss, \
        open("NLLB.en-ss.en", encoding='utf-8') as nllb_en, \
        open("NLLB.en-ss.ss", encoding='utf-8') as nllb_ss, \
        open("wikimedia.en-ss.en", encoding='utf-8') as wiki_en, \
        open("wikimedia.en-ss.ss", encoding='utf-8') as wiki_ss, \
        open("XLEnt.en-ss.en", encoding='utf-8') as xlent_en, \
        open("XLEnt.en-ss.ss", encoding='utf-8') as xlent_ss, \
        open(EN_FILE, 'w', encoding='utf-8') as f_en, \
        open(SS_FILE, 'w', encoding='utf-8') as f_ss:
    
            # 2. ADD BIBLE DATA
            for line in bible_en.readlines():
                f_en.write(line)
            for line in bible_ss.readlines():
                f_ss.write(line)
            
            # 3. ADD DATA FROM `NLLB`
            for line in nllb_en.readlines():
                f_en.write(line)
            for line in nllb_ss.readlines():
                f_ss.write(line)
            
            # 4. ADD DATA FROM `WIKIMEDIA`
            for line in wiki_en.readlines():
                f_en.write(line)
            for line in wiki_ss.readlines():
                f_ss.write(line)
            
            # 5. ADD DATA FROM `XLENT`
            for line in xlent_en.readlines():
                f_en.write(line)
            for line in xlent_ss.readlines():
                f_ss.write(line)


with open(EN_FILE, encoding='utf-8') as f_en, open(SS_FILE, encoding='utf-8') as f_ss:
    # VERIFY THAT THE OUTPUT ROWS MATCH
    en_len = len(f_en.readlines())
    ss_len = len(f_ss.readlines())

    print("EN DATASET LENGHT: ", en_len)
    print("SS DATASET LENGHT: ", ss_len)


    #: if en_len != ss_len, raise an exception
    assert en_len == ss_len
    
