import sys
import os
import PyPDF2

# list of PDF inputs (including necessary filepath if not in the same cwd)
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    '''
    pdf_list = list of file inputs

    function will check if combined file has been created before
    initializing the merge command
    '''
    dir_list = os.listdir(os.getcwd())
    try:
        if 'combined.pdf' not in dir_list:
            merger = PyPDF2.PdfFileMerger()
            for pdf in pdf_list:
                head, tail = os.path.split(pdf)
                print(f'PDF File: {tail} has been merged')
                merger.append(pdf)
            merger.write('combined.pdf')
            print('Combined File created')
        else:
            print('Combined File has already been created')
    except:
        print('there is an error!')


# output combined file
pdf_combiner(inputs)
