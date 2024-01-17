import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Convert Apertium .dix dictionary files to text')
parser.add_argument('input',
    type=str,
    help='Input .dix file path or URL')
parser.add_argument('source',
    type=str,
    default="source.txt",
    help='Source output file. Default: %(default)s')
parser.add_argument('target',
    type=str,
    default="target.txt",
    help='Target output file. Default: %(default)s')
args = parser.parse_args()

if args.input.startswith("http"):
    import urllib.request

    with urllib.request.urlopen(args.input) as response:
        # Read the content of the file
        content = response.read().decode('utf-8')
        root = ET.fromstring(content)
else:
    tree = ET.parse(args.input)
    root = tree.getroot()

if root.tag != "dictionary":
    raise IOError("Invalid .dix file (root key is not <dictionary>)")

def extract_text(el):
    text = " ".join(el.itertext())
    return text.strip()

i = 0
added = {}
duplicates = 0
with open(args.source, "w", encoding="utf-8") as src, \
     open(args.target, "w", encoding="utf-8") as tgt:
    for c in root:
        if c.tag == 'section':
            section = c
            for ch in section:
                if ch.tag == 'e':
                    p = ch[0]
                    if p.tag != 'p':
                        continue
                    l = extract_text(p[0])
                    r = extract_text(p[1])
                    if not l in added:
                        src.write(l + "\n")
                        tgt.write(r + "\n")
                        i += 1
                        added[l] = True
                    else:
                        duplicates += 1
print(f"{i} entries (skipped {duplicates} duplicates)")
print(f"W\t{args.source}")
print(f"W\t{args.target}")

