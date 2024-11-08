import pprint
from csv_diff import load_csv, compare
from diff_pdf_visually import pdf_similar


'''
Utilizes csv-diff python library 

Instructions: https://pypi.org/project/csv-diff/
pip install csv-diff 
'''
def compare_csv(file1, file2, parse_key):
    diff_csv = compare(
        load_csv(open(file1), key=parse_key),
        load_csv(open(file2), key=parse_key)
    )

    csv_diff_fail = 0
    csv_diff = []

    for i in diff_csv:
        if(diff_csv[i] != []):
            csv_diff_fail += 1
            csv_diff.append(diff_csv[i])
            
    if (csv_diff_fail > 0):
        print("FAIL: Differences found\n")
        return pprint.pp(csv_diff)
    else:
        return print("PASS: No differences found in CSV")

'''
Utilizes diff-pdf-visually python library

Instructions: https://pypi.org/project/diff-pdf-visually/

For Mac 
brew install poppler imagemagick
pip3 install --user diff-pdf-visually

For Windows PC 
Install diff-pdf-visually via Pip.
Install ImageMagick, e.g. via https://imagemagick.org/script/download.php
Download pdftocairo/Poppler


To see visual differences in PDF use diff-pdf: 
https://vslavik.github.io/diff-pdf/

mac os  
brew install diff-pdf

diff-pdf prod.pdf staging.pdf --output-diff=diff.pdf 
'''
def compare_pdf(file1, file2):
    pdf_diff = pdf_similar(file1, file2)

    if(pdf_diff == "True"):
        return print("\nPASS: No differences found in PDF")
    else:
        return print("\nFAIL: Differences found in PDF")


'''
MAIN
'''
prodCSV = 'prod/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.csv'
stagingCSV = 'staging/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.csv'
prodPDF = 'prod/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.pdf'
stagingPDF = 'staging/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.pdf'

print("------------------------------------------------------------------------------")
print(f"""Test 1: Comparing CSV using key 'Article Number'
        {prodCSV} 
        {stagingCSV} \n""")
compare_csv(prodCSV, stagingCSV, 'Article Number')

print("\n\n\n------------------------------------------------------------------------------")
print(f"""Test 2: Comparing PDF Files
        {prodPDF} 
        {stagingPDF}\n """)
compare_pdf(prodPDF, stagingPDF)