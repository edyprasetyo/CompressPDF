import subprocess
import os


def compress_pdf(input_path, output_path, quality='ebook'):
    """
    :param quality: The quality of the output PDF file. The value can be one of the following:
        - 'screen': low-resolution output (72 dpi)
        - 'ebook': medium-resolution output (150 dpi)
        - 'printer': high-resolution output (300 dpi)
    """
    gs_command = [
        r'C:\Program Files\gs\gs10.00.0\bin\gswin64.exe',
        '-sDEVICE=pdfwrite', '-dPDFSETTINGS=/ebook',
        '-dCompatibilityLevel=1.4',
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        '-dDetectDuplicateImages=true',
        '-dCompressFonts=true',
        '-dDownsampleColorImages=true',
        '-dColorImageResolution=120',
        '-dMonoImageResolution=120',
        '-sOutputFile=' + os.path.abspath(output_path),
        os.path.abspath(input_path)
    ]
    subprocess.run(gs_command)


compress_pdf(r'D:\MyProject\CompressPDF\tes3.pdf',
             r'D:\MyProject\CompressPDF\output.pdf', quality='ebook')

# print output.pdf size in KB
print(str(int(os.path.getsize(r'D:\MyProject\CompressPDF\tes3.pdf') / 1024)) + ' KB')
print(str(int(os.path.getsize(r'D:\MyProject\CompressPDF\output.pdf') / 1024)) + ' KB')


# open output.pdf
subprocess.Popen(r'D:\MyProject\CompressPDF\output.pdf', shell=True)
