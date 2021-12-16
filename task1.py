from functools import total_ordering
import argparse

mw_a = 135.13
mw_c = 111.1
mw_t = 126.11
mw_g = 151.13
nucleobase = ["adenine", "cytosine", "tryosine", "guanine", "a", "c", "t", "g"]
dictt = {"A": 135.13, "T": 126.11, "C": 111.1, "G": 151.13}
# @total_ordering
class Nucleobase:
    def __init__(self, name):

        if name.lower() not in nucleobase:
            raise ValueError("not a valid input")

        elif name.lower() == nucleobase[4] or name.lower() == nucleobase[0]:
            self.name = "Adenine"
            self.molecular_weight = mw_a
            self.complimenter = nucleobase[2]
            self.code = "A"

        elif name.lower() == nucleobase[5] or name.lower() == nucleobase[1]:
            self.name = "Cytosine"
            self.molecular_weight = mw_c
            self.complimenter = nucleobase[3]
            self.code = "C"

        elif name.lower() == nucleobase[6] or name.lower() == nucleobase[2]:
            self.name = "Tryosine"
            self.molecular_weight = mw_t
            self.complimenter = nucleobase[0]
            self.code = "T"

        elif name.lower() == nucleobase[7] or name.lower() == nucleobase[3]:
            self.name = "Guanine"
            self.molecular_weight = mw_g
            self.complimenter = nucleobase[1]
            self.code = "G"

    def compliment(self):
        if self.name.lower() not in nucleobase:
            raise ValueError("not a valid input")

        elif self.name.lower() == nucleobase[4] or self.name.lower() == nucleobase[0]:
            name = "Tryosine"

        elif self.name.lower() == nucleobase[5] or self.name.lower() == nucleobase[1]:
            name = "Guanine"

        elif self.name.lower() == nucleobase[6] or self.name.lower() == nucleobase[2]:
            name = "Adenine"

        elif self.name.lower() == nucleobase[7] or self.name.lower() == nucleobase[3]:
            name = "Cytosine"

        return Nucleobase(name)

    def __eq__(self, other):
        return self.molecular_weight == other.molecular_weight

    def __lt__(self, other):
        return self.molecular_weight < other.molecular_weight

    def __gt__(self, other):
        return self.molecular_weight > other.molecular_weight

    def __repr__(self):
        return "name: {}\nmolecular wieght: {}\ncomplementer: {}\ncode: {}".format(
            self.name, self.molecular_weight, self.complimenter, self.code
        )

    def __add__(self, other):
        dna = self.code + other.code
        return DNA(dna)

    def __mul__(self, other):
        if self.name.lower() == other.complimenter:
            return True
        else:
            return False


class DNA(list):
    def __init__(self, nucleobases_many):
        nucleobase_list = []
        for i in nucleobases_many:
            d = Nucleobase(i)
            nucleobase_list.append(d)

        self.nucleobase_list = nucleobase_list
        seq = ""
        for i in range(len(self.nucleobase_list)):
            seq += self.nucleobase_list[i].name[0].upper()
        self.seq = seq

        super().__init__(nucleobase_list)

    def __iter__(self):
        return iter(self.nucleobase_list)

    def molecular_weight(self):
        a = list(self.seq)
        y = 0
        for i in range(len(a)):
            y += dictt[a.pop(0)]

        return "{:.2f}".format(round(y, 2))

    def compliment(self):

        b = list(self.seq)
        for i in range(len(b)):
            if b[i] == "A":
                b[i] = "T"
            elif b[i] == "G":
                b[i] = "C"

            elif b[i] == "C":
                b[i] = "G"

            elif b[i] == "T":
                b[i] = "A"

        dna = "".join(b)
        return dna

    def __str__(self):

        return self.seq

    def __add__(self, other):
        dna_extend = self.seq + other.seq
        return DNA("".join(dna_extend))

    def __mul__(self, other):
        result = []
        if other.seq == self.compliment():
            return True
        else:
            return False


def main():
    # A = Nucleobase("A")
    # B = Nucleobase("C")
    # C = Nucleobase("T")
    # D = Nucleobase("G")
    # E = Nucleobase("aDeNine")
    # F = Nucleobase("GuaNine")
    # G = Nucleobase("cytoSine")
    # H = Nucleobase("Tryosine")
    # print(A, B, C, D, E, F, G, H, sep=" \n")
    # print(
    #    A.molecular_weight,
    #    B.molecular_weight,
    #    C.molecular_weight,
    #    D.molecular_weight,
    #    sep="\n",
    # )
    # Y = A.compliment()
    # print(Y.name, Y.molecular_weight, sep="\n")

    # print(A > B, B > C, D > C, sep="\n")
    # X = DNA("atcga")
    # Z = DNA("tagct")
    # print(X)
    # print(X.molecular_weight())
    # print(X.compliment())
    # for i in X:
    #    print(i)
    #    print(type(i))

    # print(type(A + B))
    # print(X + Z)
    # print(type(X + Z))
    # print(X * Z)
    # print(A * C)
    # print(len(X + Z))

    parser = argparse.ArgumentParser(description="task 1")
    parser.add_argument("-s", "--seq", help="dna sequence", type=str)
    parser.add_argument("-f", "--file", help="dna file", type=str)
    parser.add_argument("-v", "--verbose", help="dna sequence", action="store_true")
    #
    args = parser.parse_args()

    if args.seq and not args.verbose:
        dna = DNA(args.seq)
        print("length of dna is ", len(dna))

    if args.file and not args.verbose:
        file = open(args.file).read()
        dna = DNA(file)
        print("length of dna is ", len(dna))

    if args.seq and args.verbose:
        dna = DNA(args.seq)
        print(
            "length of dna is",
            len(dna),
            "molecular weight",
            dna.molecular_weight(),
            sep="\n",
        )

    if args.file and args.verbose:
        file = open(args.file).read()
        dna = DNA(file)
        print(
            "length of dna is",
            len(dna),
            "molecular weight",
            dna.molecular_weight(),
            sep="\n",
        )


if __name__ == "__main__":
    main()
