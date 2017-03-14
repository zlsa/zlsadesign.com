#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo 'not enough arguments (process-infographic.sh type/name.svg)'
    exit 1
fi

input_svg=../infographic/$1
output_png_2x=../static/infographic/${1%.svg}.png

output_jpg_cropped=../static/infographic/${1%.svg}-cropped.jpg
output_jpg_small=../static/infographic/${1%.svg}.jpg

width=1024
height=576

echo "processing " $input_svg

mkdir -p -- "${output_png_2x%/*}"

inkscape $input_svg --export-png=$output_png_2x --export-dpi=192 > /dev/null

convert $output_png_2x -resize $width $output_jpg_small
convert $output_png_2x -resize $width -geometry ${width}x${height}^ -gravity north -crop ${width}x${height}+0+0 $output_jpg_cropped

