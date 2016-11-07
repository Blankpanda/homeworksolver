import csv
import os


class DataCsv(object):
    
    def __init__(self, csv_file, delimiter, quotechar):
        if not os.path.exists(csv_file):
            open(csv_file, 'w').close()
        
        self.csv_file = csv_file
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.classifiers = list()

    def open_csv_io(self, modif):
        if modif.startswith("r"):
            f = open(self.csv_file, modif)
            return csv.reader(f, delimiter=self.delimiter, quotechar=self.quotechar), f
        elif modif.startswith("w"):
            f = open(self.csv_file,modif)
            return csv.writer(f, delmiter=self.delimiter, quotechar=self.quotechar), f
        elif modif.startswith("a"):
            f = open(self.csv_file,modif)
            return None, f
        else:
            return None
            
    def get_rows(self):
        csv_reader, file = self.open_csv_io("r")
        l = list()
        for row in csv_reader:
            # we don't want any empty row entries
            # TODO: we dont need to split anything if its already split, especially if were creating the csv
            if len(row) >= 1:
                l.append(row[0].split(','))
        file.close()
        return l
    
    def write_new_row(self, row):
        csv_writer, file = self.open_csv_io("a")
        row_string = self.create_csv_row_string(row)
        print(row_string)
        file.write(row_string)            
        file.close()

    # assuming the last column are the classifiers
    def set_classifiers(self):
        classifiers = [row[-1] for row in self.get_rows()]
        used = list()
        count = 0
        for classifier in classifiers:
            if classifier not in used:
                used.append(classifier)
                self.classifiers.append(dict([(str(count),classifier)]))
                count += 1
        print(classifiers)
        
    def add_new_classifier(self,classifier):                   
        number_class = len(self.classifiers) + 1
        self.classifier.append(dict([str(number_class),classifier]))                    
        
    # TODO: consider quotechar
    def create_csv_row_string(self,row):
        return self.delimiter.join(row).strip() + '\n'
        
