import argparse
import os
import cv2

parser = argparse.ArgumentParser(description='Inputdir -input / Outputdir -output')
parser.add_argument('--input', help='input directory')
parser.add_argument('--output', help='output directory')
parser.add_argument('--frame', help='frame size', type=int)

args = parser.parse_args()

input_dir = args.input
output_dir = args.output
for video in os.listdir(input_dir):
    count = 0
    video_dir = os.path.join(output_dir, video)
    os.mkdir(video_dir)
    cap = cv2.VideoCapture(os.path.join(input_dir, video))
    while True:
        succ, frame = cap.read()
        if not succ:
            break
        if count % args.frame == 0:
            cv2.imwrite(os.path.join(video_dir, f"{count}.jpg"), frame)
        count += 1
    cap.release()
    print(f"[{video_dir}] DONE")
