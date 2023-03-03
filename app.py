import subprocess
import os


def compress_pdf(input_path, output_path):
    gsExe = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'GhostScript/gswin64c.exe')
    gs_command = [
        gsExe,
        "-sDEVICE=pdfwrite",
        "-dPDFSETTINGS=/ebook",
        "-dCompatibilityLevel=1.4",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-dDetectDuplicateImages=true",
        "-dCompressFonts=true",
        "-dDownsampleColorImages=true",
        "-dColorImageResolution=120",
        "-dMonoImageResolution=120",
        '-sOutputFile=' + os.path.abspath(output_path),
        os.path.abspath(input_path)
    ]
    subprocess.run(gs_command)


# force delete output folder and create new one
if os.path.exists('output'):
    os.system('rd /s /q output')
os.mkdir('output')


# loop all pdf inside input folder
for filename in os.listdir('input'):
    # compress pdf to output folder and name _compressed replace all space with _
    compress_pdf('input/' + filename, 'output/' +
                 filename.replace(' ', '_').replace('.pdf', '_compressed.pdf'))
