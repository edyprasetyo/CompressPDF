import subprocess
import os
import time


def compress_pdf(input_path, output_path):
    gsExe = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'GhostScript/gswin32c.exe')
    gs_command = [
        gsExe,
        "-sDEVICE=pdfwrite",
        "-dPDFSETTINGS=/ebook",
        "-dCompatibilityLevel=1.4",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        # "-dDetectDuplicateImages=true",
        # "-dCompressFonts=true",
        # "-dDownsampleColorImages=true",
        # "-dColorImageDownsampleThreshold=1",
        # "-dColorImageResolution=120",
        # "-dDownsampleMonoImages=true",
        # "-dMonoImageResolution=120",
        # "-dDownScaleFactor=3",
        # "-dUseFlateCompression=true",
        '-sOutputFile=' + os.path.abspath(output_path),
        os.path.abspath(input_path)
    ]
    subprocess.run(gs_command)


# force delete output folder and create new one
if os.path.exists('output'):
    os.system('rd /s /q output')
os.mkdir('output')

print('Start compressing pdf...')
startTime = time.time()
for filename in os.listdir('input'):
    compress_pdf('input/' + filename, 'output/' +
                 filename.replace(' ', '_').replace('.pdf', '_compressed.pdf'))

print('Done compressing pdf in ' + str(time.time() - startTime) + ' seconds')
