import os
import re
import shlex
import shutil
import subprocess
import webbrowser
import zipfile

from pathlib import Path


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
    rc = process.poll()
    return rc


def sort_files_name(list):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    list.sort(key=alphanum_key)


def init(tryy):
    input_folder_zip_files = Path("./input")
    if not input_folder_zip_files.exists():
        input_folder_zip_files.mkdir()

    if tryy == "t":
        with open("commands.txt", 'r') as commands, open("links.html", 'w') as downloadable_lms_file_links:
            lines = commands.readlines()
            downloadable_lms_file_links.write("<p>Download links:</p>")
            for line in lines:
                command = line.strip().split(">")

                link = command[0][5:].strip()
                file_name = command[1].strip()

                download_link_of_file = "{base_link}/output/{name}.zip?download=zip".format(
                    base_link=link.split("/?")[0],
                    name=file_name
                )
                downloadable_lms_file_links.write(f"""
                    <p>
                        <a href={download_link_of_file}>{file_name}</a>
                    </p>
                """)

        if len(lines) != 0:
            open_html = input(r'The links in the file "link.html" are ready to download. For open it Enter "o" else Enter any.' + "\n")
            if open_html == "o":
                webbrowser.open_new_tab("links.html")

            confirmation = input(
                r'If the files are downloaded, put them in the "input" folder then Enter "s" and for exit Enter any.' + "\n")
            convert_to_mp4(confirmation)
        else:
            init(input('Not exists commands. Try it Enter "t" and for exit Enter any.' + "\n"))


def convert_to_mp4(confirmation):
    if confirmation == "s":
        downloaded_files = os.listdir("./input")
        output_files_name = [name[:-4] for name in downloaded_files if name.endswith(".zip")]
        if len(output_files_name) != 0:
            print("Extracting files...")
            folders_path = []
            for zip_file_name in output_files_name:
                with zipfile.ZipFile(f"./input/{zip_file_name}.zip", 'r') as zip_ref:
                    zip_ref.extractall(f"./output/{zip_file_name}")
                    folders_path.append(f"./output/{zip_file_name}")

            print("Processing files...")
            for folder_path, output_file_name in zip(folders_path, output_files_name):
                with open(f"{folder_path}/inputs.txt", 'w') as flvs:
                    flv_files = os.listdir(f"{folder_path}")
                    flv_files_name = [name for name in flv_files if re.match("cameraVoip(.*)+.flv", name)]

                    sort_files_name(flv_files_name)
                    for flv in flv_files_name:
                        flvs.write(f"file {flv}\n")

                if not Path(f"{folder_path}/output_1.flv").exists():
                    run_command(f"ffmpeg -safe 0 -f concat -i {folder_path}/inputs.txt -c copy {folder_path}/output_1.flv")

                with open(f"{folder_path}/inputs.txt", 'w') as flvs:
                    flv_files = os.listdir(f"{folder_path}")
                    flv_files_name = [name for name in flv_files if re.match("screenshare(.*)+.flv", name)]

                    sort_files_name(flv_files_name)
                    for flv in flv_files_name:
                        flvs.write(f"file {flv}\n")

                if len(flv_files_name) != 0:
                    run_command(f"ffmpeg -safe 0 -f concat -i {folder_path}/inputs.txt -c copy {folder_path}/output_2.flv")
                    run_command(f"ffmpeg -i {folder_path}/output_1.flv -i {folder_path}/output_2.flv -acodec copy -vcodec copy ./output/{output_file_name}.flv")
                else:
                    os.rename(f"{folder_path}/output_1.flv", f"./output/{output_file_name}.flv")
                shutil.rmtree(f"{folder_path}")
                print("Done!")
        else:
            print("Not file found!")
            again_confirmation = input(
                'If you transfer files to a folder "input" make sure Enter "s" and for exit Enter any.' + "\n")
            convert_to_mp4(again_confirmation)


if __name__ == "__main__":
    init("t")
