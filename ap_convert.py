import argparse
import zipfile
import os
from dix2text import dix2text
parser = argparse.ArgumentParser(description='Convert Apertium .dix database')
parser.add_argument('output',
    type=str,
    help='Output path where to store results')
args = parser.parse_args()


dicts = {
    'en_it': "https://raw.githubusercontent.com/apertium/apertium-eng-ita/master/apertium-eng-ita.eng-ita.dix",
    'en_pt': "https://raw.githubusercontent.com/apertium/apertium-en-pt/5805be78132bbce6de528346aa9b72134a02be03/apertium-en-pt.en-pt.dix",
    'en_ca': "https://github.com/apertium/apertium-eng-cat/raw/master/apertium-eng-cat.eng-cat.dix",
    'fi_en': "https://github.com/apertium/apertium-fin-eng/raw/master/apertium-fin-eng.fin-eng.dix",
    'ja_en': "https://github.com/apertium/apertium-jpn-eng/raw/master/apertium-jpn-eng.jpn-eng.dix",
    'en_de': "https://github.com/apertium/apertium-eng-deu/raw/master/apertium-eng-deu.eng-deu.dix",
    'th_en': "https://github.com/apertium/apertium-tha-eng/raw/master/apertium-tha-eng.tha-eng.dix",
    'nb_en': "https://github.com/apertium/apertium-nor-eng/raw/master/apertium-nor-eng.nor-eng.dix",
    'en_es': "https://github.com/apertium/apertium-eng-spa/raw/master/apertium-eng-spa.eng-spa.dix",
    'eo_en': "https://github.com/apertium/apertium-eo-en/raw/main/apertium-eo-en.eo-en.dix",
    'sv_en': "https://github.com/apertium/apertium-swe-eng/raw/master/apertium-swe-eng.swe-eng.dix",
    'id_en': "https://github.com/apertium/apertium-ind-eng/raw/master/apertium-ind-eng.ind-eng.dix",
    'ga_en': "https://github.com/apertium/apertium-gle-eng/raw/master/apertium-gle-eng.gle-eng.dix",
    'en_fa': "https://github.com/apertium/apertium-eng-pes/raw/master/apertium-eng-pes.eng-pes.dix",
    'en_lv': "https://github.com/apertium/apertium-eng-lvs/raw/master/apertium-eng-lvs.eng-lvs.dix",
    'el_en': "https://github.com/apertium/apertium-ell-eng/raw/master/apertium-ell-eng.ell-eng.dix",
    'fr_en': "https://github.com/apertium/apertium-fra-eng/raw/master/apertium-fra-eng.fra-eng.dix",
    'en_hi': "https://github.com/apertium/apertium-eng-hin/raw/master/apertium-eng-hin.eng-hin.dix",
    'fa_en': "https://github.com/apertium/apertium-pes-eng/raw/master/apertium-pes-eng.pes-eng.dix",
    'en_pl': "https://github.com/apertium/apertium-eng-pol/raw/master/apertium-eng-pol.eng-pol.dix",
    'en_ga': "https://github.com/apertium/apertium-eng-gle/raw/master/apertium-eng-gle.eng-gle.dix",
    'bg_en': "https://github.com/apertium/apertium-bg-en/raw/master/apertium-bg-en.bg-en.dix",
    'en_nl': "https://github.com/apertium/apertium-en-nl/raw/master/apertium-en-nl.en-nl.dix",
    'tr_en': "https://github.com/apertium/apertium-tur-eng/raw/master/apertium-tur-eng.tur-eng.dix",
    'hu_en': "https://github.com/apertium/apertium-hun-eng/raw/master/apertium-hun-eng.hun-eng.dix",
    'en_sq': "https://github.com/apertium/apertium-en-sq/raw/master/apertium-en-sq.en-sq.dix",
    'ru_en': "https://github.com/apertium/apertium-rus-eng/raw/master/apertium-ru-en.ru-en.dix",
}

for lang in dicts:
    outfile = os.path.join(args.output, lang + ".zip")
    if os.path.isfile(outfile):
        print(f"S\t{outfile}")
        continue
    try:
        dix2text(dicts[lang], "source.txt", "target.txt")
        with zipfile.ZipFile(outfile, 'w') as zipf:
            zipf.write("source.txt")
            zipf.write("target.txt")
            print(f"W\t{outfile}")
    except Exception as e:
        print(lang, str(e))