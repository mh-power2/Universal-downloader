import os
import subprocess


#check if ffmpeg installed
def ffmpeg_install():
    cwd = os.getcwd()
    if not os.path.exists(os.path.join(cwd, 'Binaries/ffmpeg/ffmpeg.exe')):
        if not os.path.exists(os.path.join(cwd, 'Binaries/ffmpeg/')):
            os.makedirs(os.path.join(cwd, 'Binaries/ffmpeg/'))

        if not os.path.exists(os.path.join(cwd, 'Binaries/ffmpeg/ffmpeg.7z')):
            file_path = os.path.join(cwd, 'Binaries/aria2/aria2c.exe')
            subprocess.run([
                file_path, '-o', 'ffmpeg.7z', '-d',
                os.path.join(cwd, 'Binaries/ffmpeg/'),
                'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z'
            ],
                           shell=True)
        command = [
            os.path.join(cwd, 'Binaries/7z/7za.exe'), 'e',
            os.path.join(cwd, 'Binaries/ffmpeg/ffmpeg.7z'),
            'ffmpeg-*-essentials_build/bin/ffmpeg.exe ffmpeg-*-essentials_build/bin/ffplay.exe ffmpeg-*-essentials_build/bin/ffprobe.exe',
            '-o' + os.path.join(cwd, 'Binaries/ffmpeg/')
        ]
        command = ' '.join(command)
        subprocess.run(command, shell=True)

    os.environ['PATH'] += ';' + os.path.join(cwd, 'Binaries/ffmpeg/')


#check if yt-dlp installed
def yt_dlp_install():
    cwd = os.getcwd()
    if not os.path.exists(os.path.join(cwd, 'Binaries/yt-dlp/yt-dlp.exe')):
        if not os.path.exists(os.path.join(cwd, 'Binaries/yt-dlp/')):
            os.makedirs(os.path.join(cwd, 'Binaries/yt-dlp/'))

        file_path = os.path.join(cwd, 'Binaries/aria2/aria2c.exe')
        subprocess.run([
            file_path, '-o', 'yt-dlp.exe', '-d',
            os.path.join(cwd, 'Binaries/yt-dlp/'),
            'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'
        ],
                       shell=True)
