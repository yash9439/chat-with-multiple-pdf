from PyPDF2 import PdfMerger
import os

#Create an instance of PdfFileMerger() class
merger = PdfMerger()

#Define the path to the folder with the PDF files
path_to_files = r'src/data/'

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_files):
    #Iterate over the list of the file names
    for file_name in file_names:
        #Append PDF files
        merger.append(path_to_files + file_name)

# Specify the full path for the output file
output_file_path = r'src/data/merged_all_pages.pdf'

# Write out the merged PDF file
merger.write(output_file_path)
merger.close()