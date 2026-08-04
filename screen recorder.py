import subprocess
import os
import signal
def record_screen(fps=15):

    script_folder = os.path.dirname(os.path.abspath(__file__))
    print("Notice: once the file is named the program will start automatically")
    print("in case you miss it the recording ends when you press Ctrl+C")
    print("once the recording ends the program will save the file and end")
    filename = input("Enter recording name: ").strip()
    if not filename:
        filename = "screen_recording"

    invalid = '<>:"/\\|?*'
    for c in invalid:
        filename = filename.replace(c, "_")

    output = os.path.join(script_folder, filename + ".mp4")
    audio_device = "audio=Stereo Mix (Realtek Audio)"
    command = [
        "C:\\ffmpeg-8.1.2-essentials_build\\bin\\ffmpeg.exe",
        "-y",
        "-f", "gdigrab",
        "-framerate", str(fps),
        "-i", "desktop",
        "-f", "dshow",
        "-i", audio_device,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        output
    ]

    print("\nRecording...")
    print("Press Ctrl+C to stop.\n")
    process = subprocess.Popen(command)
    try:
        process.wait()

    except KeyboardInterrupt:
        print("\nStopping...")

        if os.name == "nt":
            process.send_signal(signal.CTRL_BREAK_EVENT)

        else:
            process.terminate()

        process.wait()
        print("\nSaved to:")
        print(output)
    try:
        process.wait()

    except KeyboardInterrupt:
        print("\nStopping...")

        if os.name == "nt":
            process.send_signal(signal.CTRL_BREAK_EVENT)

        else:
            process.terminate()
        process.wait()
        print("\nSaved to:")
        print(output)

if __name__ == "__main__":
    record_screen()