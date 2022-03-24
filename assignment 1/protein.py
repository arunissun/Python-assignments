from functools import total_ordering
import re

## there are 20 amino acids who make the protein
## sequence
acid_names = [
    "A",
    "G",
    "M",
    "L",
    "H",
    "R",
    "N",
    "D",
    "T",
    "F",
    "W",
    "K",
    "Q",
    "E",
    "S",
    "P",
    "V",
    "C",
    "I",
    "Y",
]


## lets us load the fasta file and read the
## contents


def load_fasta(path):

    fasta = open(path).read()
    # fasta file is a string
    # split the file along >sp
    # fasta = fasta.split(">sp")
    # fasta = fasta[1:]
    fasta = re.split(">sp", fasta)  # using the regex splitting instead of string split
    fasta = fasta[1:]

    protein_list = []
    try:
        for proteins in fasta:
            protein_list.append(Protein(proteins))

        return protein_list
    except:
        raise ValueError("There are no proteins in the proteins.fasta file")


## using total_ordering
@total_ordering
class Protein(list):
    def __init__(self, fasta):
        # first_line = fasta.split("\n")[0]
        first_line = re.split(r"\n", fasta)[0]
        # againg using the split function from regex

        # seq = fasta.split("\n")[1 : len(fasta.split("\n")) - 1]
        seq = re.split(r"\n", fasta)[1 : len(re.split("\n", fasta)) - 1]
        # againg using the split function from regex

        self.sequence = "".join(seq)
        self.size = len(self.sequence)

        # self.id = first_line.split("|")[1]
        self.id = re.split(r"\|", first_line)[1]
        # againg using the split function from regex
        # fls = first_line.split("|")[2]
        fls = re.split(r"\|", first_line)[2]

        # os_ind = fls.find("OS=")
        os_ind = re.search("OS=", fls).start()
        # ox_ind = fls.find("OX=")
        ox_ind = re.search("OX=", fls).start()
        # pe_ind = fls.find("PE=")
        pe_ind = re.search("PE=", fls).start()
        # sv_ind = fls.find("SV=")
        sv_ind = re.search("SV=", fls).start()
        # gn_ind = fls.find("GN=")
        gn_ind = re.search("GN=", fls).start()

        self.name = fls[:os_ind].strip()
        self.os = fls[os_ind + 3 : ox_ind]
        self.gn = fls[gn_ind + 3 : pe_ind].strip()
        self.ox = int(fls[ox_ind + 3 : gn_ind])
        self.pe = int(fls[pe_ind + 3 : sv_ind])
        self.sv = int(fls[sv_ind + 3 :])

        self.aminoacidcounts = {}

        for acids in acid_names:
            self.aminoacidcounts[acids] = self.sequence.count(acids)

        super().__init__(self.sequence)

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "{} id: {}".format(self.name, self.id)


def sort_proteins_pe(proteins):
    return sorted(proteins, key=lambda prot: prot.pe, reverse=True)


def sort_proteins_aa(proteins, acid):
    x = []
    for names in acid_names:
        x += re.findall(acid, names)
        # print(len(x))
    if len(x) == 0:
        raise ValueError("not an aminoacid")

    # if acid not in acid_names:
    #    raise ValueError("not an aminoacid")
    return sorted(proteins, key=lambda prot: prot.aminoacidcounts[acid], reverse=True)


def find_protein_with_motif(proteins, motif):

    protein_by_motif = []
    # x = ""
    # for prot in proteins:
    #    if prot.sequence.find(motif) != -1:
    #        protein_by_motif.append(prot)

    for prot in proteins:
        # print(prot.sequence)
        if re.findall(motif, prot.sequence) != []:
            protein_by_motif.append(prot)

    return protein_by_motif

