from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=True,
	help="path to aligned image that check against template")
ap.add_argument("-a", "--aligned", required=True,
	help="path to input aligned image")
args = vars(ap.parse_args())

# load the input image and template from disk
print("[INFO] loading images...")
original = cv2.imread(args['template'])
aligned = cv2.imread(args['aligned'])


print("SSIM: ", ssim(aligned, original))