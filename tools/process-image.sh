#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WATERMARK=${DIR}/watermark/watermark.png

if [[ $# -ne 1 ]] ; then
    echo 'not enough arguments (process-image.sh original.png)'
    exit 1
fi

input_png=$1

output_jpg=${1%.png}-full.jpg
output_jpg_cropped=${1%.png}-cropped.jpg
output_jpg_hero=${1%.png}-hero.jpg
output_jpg_home=${1%.png}-home.jpg
output_jpg_preview=${1%.png}-preview.jpg

crop_width=480
crop_height=270

hero_width=1920
hero_height=1080

home_width=3840
home_height=2160

preview_width=1820

echo "processing " $input_png

composite $WATERMARK -gravity southeast $input_png $output_jpg

convert $input_png -resize $preview_width $output_jpg_preview
composite $WATERMARK -gravity southeast $output_jpg_preview $output_jpg_preview

convert $input_png -quality 80 -resize $crop_width -geometry ${crop_width}x${crop_height}^ -gravity north -crop ${crop_width}x${crop_height}+0+0 $output_jpg_cropped
#composite $WATERMARK -gravity southeast $output_jpg_cropped $output_jpg_cropped

convert $input_png -quality 80 -resize $home_width -geometry ${home_width}x${home_height}^ -gravity north -crop ${home_width}x${home_height}+0+0 $output_jpg_home
composite $WATERMARK -gravity southeast $output_jpg_home $output_jpg_home

convert $input_png -quality 85 -resize $hero_width -geometry ${hero_width}x${hero_height}^ -gravity north -crop ${hero_width}x${hero_height}+0+0 $output_jpg_hero
composite $WATERMARK -gravity southeast $output_jpg_hero $output_jpg_hero


