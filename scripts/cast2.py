import subprocess

subprocess.call(["ffmpeg", "-f", "avfoundation", "-i", ":3", "-ar", "48000", "-ac", "2", "-af", "aresample=osf=s16", "-c:a", "flac", "-compression_level", "10",
                 "-f", "ogg", "-content_type", "application/ogg", "icecast://"])
