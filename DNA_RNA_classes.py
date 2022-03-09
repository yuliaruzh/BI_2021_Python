class DNA:
    def __init__(self, DNA):
        self.DNA = DNA.upper()

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        if self.indx >= len(self.DNA):
            raise StopIteration()
        x = self.DNA[self.indx]
        self.indx += 1

        return x

    def gc_content(self):
        sum_gc = 0
        n = len(self.DNA)
        for nucl in self.DNA:
            if nucl == 'C' or nucl == 'G':
                sum_gc += 1
        return (sum_gc / n) * 100

    def reverse_complement(self):
        compl_dna = ''
        A = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }
        for nucl in self.DNA:
            compl_dna += A[nucl]
        reverse_compl_dna = compl_dna[::-1]
        return DNA(reverse_compl_dna)

    def __eq__(self, other):
        if isinstance(other, DNA):
            return self.DNA == other.DNA

        return False

    def transcribe(self):
        rna = ''
        A = {
            'A': 'U',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }
        for nucl in self.DNA:
            rna += A[nucl]
        return RNA(rna)


class RNA:
    def __init__(self, RNA):
        self.RNA = RNA.upper()

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        if self.indx >= len(self.RNA):
            raise StopIteration()
        x = self.RNA[self.indx]
        self.indx += 1
        return x

    def gc_content(self):
        sum_gc = 0
        n = len(self.RNA)
        for nucl in self.RNA:
            if nucl == 'C' or nucl == 'G':
                sum_gc += 1
        return (sum_gc / n) * 100

    def reverse_complement(self):
        compl_rna = ''
        A = {
            'A': 'U',
            'U': 'A',
            'G': 'C',
            'C': 'G'
        }
        for nucl in self.RNA:
            compl_rna += A[nucl]
        reverse_compl_rna = compl_rna[::-1]
        return RNA(reverse_compl_rna)

    def __eq__(self, other):
        if isinstance(other, RNA):
            return self.RNA == other.RNA

        return False


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