class Analyze_DNA:

    def __init__(self):
        self.size = None
        self.gc_content = None
        self.start_codons = None
        self.stop_codons = None

    def size_of(self, sequence):
        sequence = sequence.upper()
        self.size = len(sequence)
        return self.size

    def gc_content_of(self, sequence):
        sequence = sequence.upper()
        self.gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        return self.gc_content

    def find_start_codons(self, sequence):
        sequence = sequence.upper()
        self.start_codons = []
        start_codons = ['ATG', 'GTG', 'TTG']
        for i in range(len(sequence) - 2):
            codon = sequence[i:i+3]
            if codon in start_codons:
                self.start_codons.append(i)
        return self.start_codons

    def find_stop_codons(self, sequence):
        sequence = sequence.upper()
        self.stop_codons = []
        stop_codons = ['TAA', 'TAG', 'TGA']
        for i in range(len(sequence) - 2):
            codon = sequence[i:i+3]
            if codon in stop_codons:
                self.stop_codons.append(i)
        return self.stop_codons

    def analyze_all(self, sequence):
        self.size_of(sequence)
        self.gc_content_of(sequence)
        self.find_start_codons(sequence)
        self.find_stop_codons(sequence)
        return {
            "Size": self.size,
            "GC_Content": self.gc_content,
            "Start_Codons": self.start_codons,
            "Stop_Codons": self.stop_codons
        }
