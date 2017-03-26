#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo 'not enough arguments (process-infographic.sh type/name.svg)'
    exit 1
fi

input_svg=../infographic/$1
output_png_2x=../static/infographic/${1%.svg}.png
output_png_4x=../static/infographic/${1%.svg}-2x.png

output_jpg_cropped=../static/infographic/${1%.svg}-cropped.jpg
output_jpg_small_wide=../static/infographic/${1%.svg}-wide.jpg
output_jpg_small_tall=../static/infographic/${1%.svg}-tall.jpg

crop_width=480
crop_height=270

wide_width=1820
wide_height=1024

tall_width=1024
tall_height=1820

echo "processing " $input_svg

mkdir -p -- "${output_png_2x%/*}"

inkscape $input_svg --export-png=$output_png_2x --export-dpi=192 > /dev/null
inkscape $input_svg --export-png=$output_png_4x --export-dpi=384 > /dev/null

convert $output_png_2x -resize $wide_width $output_jpg_small_wide
convert $output_png_2x -resize $tall_width $output_jpg_small_tall

convert $output_png_2x -quality 70 -resize $crop_width -geometry ${crop_width}x${crop_height}^ -gravity north -crop ${crop_width}x${crop_height}+0+0 $output_jpg_cropped

