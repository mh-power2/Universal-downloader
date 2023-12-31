from FFMPEG import ffmpeg_install
import os
import subprocess

ffmpeg_install()

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Video_Output/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def convert_video(path, extension):
    input_file = path
    output_file = os.path.join(download_directory,
                               f"{os.path.basename(path)}.{extension}")
    ffmpeg_cmd = ['ffmpeg', '-i', input_file, output_file]
    subprocess.run(ffmpeg_cmd)


def compress_video(input_file, crf):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    output_file = os.path.join(download_directory,
                               f"{base_name}_compressed{ext}.mkv")
    ffmpeg_cmd = [
        'ffmpeg', '-v', 'error', '-stats', '-i', input_file, '-c:v', 'libx265',
        '-preset:v', 'slow', '-crf',
        str(crf), '-c:a', 'copy', output_file
    ]
    subprocess.run(ffmpeg_cmd)


def compress_video_GPU(input_file, crf):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    output_file = os.path.join(download_directory,
                               f"{base_name}_compressed{ext}.mkv")
    ffmpeg_cmd = [
        'ffmpeg', '-v', 'error', '-stats', '-hwaccel_output_format', 'cuda',
        '-i', input_file, '-c:v', 'hevc_nvenc', '-preset:v', 'slow', '-rc',
        'vbr', '-cq',
        str(crf), '-qmin',
        str(crf), '-qmax', '34', '-b:v', '0', '-profile:v', 'main10',
        '-init_qpP', '23', '-init_qpB', '25', '-init_qpI', '21', '-c:a',
        'copy', output_file
    ]
    subprocess.run(ffmpeg_cmd)


import os
import subprocess


def is_video_file(path):
    cwd = os.getcwd()
    ffprobe_path = os.path.join(cwd, 'Binaries/ffmpeg/ffprobe.exe')

    try:
        subprocess.run([
            ffprobe_path, '-hide_banner', '-loglevel', 'quiet',
            '-show_streams', path
        ],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.STDOUT,
                       check=True)
        os.system("cls")
        return True
    except subprocess.CalledProcessError:
        os.system("cls")
        return False
