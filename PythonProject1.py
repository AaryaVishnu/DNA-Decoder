Response = input("Would you like to input a DNA sequence through the console or a file? Input: C for console or F for file:   ")

#FILE:
if Response == 'F' or Response == 'f':
    def SequenceStatsFILE(inputName, outputName):
            #Variables

        inputfile = open(inputName, "r")
        outputfile = open(outputName, 'w')
        RNASequence = ''
        countA = 0
        countT = 0
        countC = 0
        countG = 0
        DNASequence = ''

            #Processing 
        for line in inputfile:
            for i in range(len(line)):
                DNASequence += line[i]
                if line[i] == 'A'or line[i] == 'a':
                    countA += 1
                    RNASequence += 'U'
                elif line[i] == 'T'or line[i] == 't':
                    countT += 1
                    RNASequence += 'A'
                elif line[i] == 'C'or line[i] == 'c':
                    countC += 1
                    RNASequence += 'G'
                elif line[i] == 'G'or line[i] == 'g':
                    countG += 1
                    RNASequence += 'C'

        TotalCount = countA + countT + countC + countG

        outputfile.write("DNA Section!" + "\n")
        outputfile.write("\n" + "DNA Nucleotide Counts:" + "\n" + "Adenine Count: " + str(countA) + "\n" +"Thymine Count: " + str(countT) + "\n" + "Cytosine Count: " + str(countC) + "\n" + "Guanine Count: " + str(countG) + "\n" + "\n")
        outputfile.write("\n" + "RNA Section!" + "\n")
        outputfile.write("\n" + "Transcribed RNA Nucleotide Counts:" + "\n" + "Adenine Count: " + str(countT) + "\n" + "Uracil Count: " + str(countA) + "\n" + "Cytosine Count: " + str(countG) + "\n" + "Guanine Count: " + str(countC) + "\n")
        outputfile.write("\n" + "\n" + "The TOTAL Nucleotide Count is: " + str(TotalCount) + " Bases") 
        outputfile.write("\n" + "The Transcribed RNA Sequence is: " + RNASequence + "\n")
        

        #Close Files and Return to Console


        outputfile.close()
        inputfile.close()
        return "Succesful!"


        #Get File Names / Path
    inputName = input("Pathname of Input File:  ")
    outputName = input("Name of Output File:  ")
    print(SequenceStatsFILE(inputName, outputName))




#CONSOLE: 
elif Response == 'C' or Response == 'c':
    def SequenceStatsCONSOLE(DNASequence):
        
            #Variables
        
        RNASequence = ''
        countA = 0
        countT = 0
        countC = 0
        countG = 0

            #Variable Processing
        for i in range(len(DNASequence)):
            if DNASequence[i] == 'A' or DNASequence[i] == 'a':
                countA += 1
                RNASequence += 'U'
            elif DNASequence[i] == 'T'or DNASequence[i] == 't':
                countT += 1
                RNASequence += 'A'
            elif DNASequence[i] == 'C'or DNASequence[i] == 'c':
                countC += 1
                RNASequence += 'G' 
            elif DNASequence[i] == 'G'or DNASequence[i] == 'g':
                countG += 1
                RNASequence += 'C'
        
        TotalCount = countA + countT + countC + countG
       

            #Output:
        print ("\n" + "DNA Nucleotide Counts" + "\n" + "Adenine Count: " + str(countA) + "\n" +"Thymine Count: " + str(countT) + "\n" + "Cytosine Count: " + str(countC) + "\n" + "Guanine Count: " + str(countG) + "\n")

        print("The Transcribed RNA Sequence is: " + RNASequence)
        
        print("Transcribed RNA Nucleotide Counts" + "\n" + "Adenine Count: " + str(countT) + "\n" + "Uracil Count: " + str(countA) + "\n" + "Cytosine Count: " + str(countG) + "\n" + "Guanine Count: " + str(countC))

        return "\n" + "\n" + "The TOTAL Nucleotide Count is: " + str(TotalCount) + " Bases"

    DNASequence = input("Print the sequence of the DNA:  ")
    print(SequenceStatsCONSOLE(DNASequence))


#IMPROPER INPUT:
else:
    print("Improper input, please use only F or C")

