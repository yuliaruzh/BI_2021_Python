class NuclAcid:
    def __init__(self, seq, compl_nucl, clas):
        self.seq = seq.upper()
        self.compl_nucl = compl_nucl
        self.clas = clas

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        if self.indx >= len(self.seq):
            raise StopIteration()
        x = self.seq[self.indx]
        self.indx += 1

        return x

    def __repr__(self):
        return self.seq

    def gc_content(self):
        sum_gc = 0
        n = len(self.seq)
        for nucl in self.seq:
            if nucl == 'C' or nucl == 'G':
                sum_gc += 1
        return (sum_gc / n) * 100

    def reverse_complement(self):
        compl_dna = ''

        for nucl in self.seq:
            compl_dna += self.compl_nucl[nucl]
        reverse_compl_dna = compl_dna[::-1]
        return self.clas(reverse_compl_dna)

    def __eq__(self, other):
        if isinstance(other, self.clas):
            return self.seq == other.seq

        return False


class DNA(NuclAcid):
    def __init__(self, seq):
        super().__init__(seq, {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }, DNA)

    def transcribe(self):
        rna = ''
        A = {
            'A': 'U',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }
        for nucl in self.seq:
            rna += A[nucl]
        return RNA(rna)


class RNA(NuclAcid):
    def __init__(self, seq):
        super().__init__(seq, {
            'A': 'U',
            'U': 'A',
            'G': 'C',
            'C': 'G'
        }, RNA)


assert DNA('gcgcgc').gc_content() == 100
assert DNA('gcgcatat').gc_content() == 50
assert DNA('aaatat').gc_content() == 0
assert DNA('gcatat').reverse_complement() == DNA('ATATGC')
assert list(iter(DNA('atgcgc'))) == list(iter("ATGCGC"))
assert RNA('gcgcgc').gc_content() == 100
assert RNA('gcgcauau').gc_content() == 50
assert RNA('aaauau').gc_content() == 0
assert RNA('gcauau').reverse_complement() == RNA('AUAUGC')
assert list(iter(RNA('augcgc'))) == list(iter("AUGCGC"))
assert DNA('agctag').transcribe() == RNA('ucgauc')
