#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo 'not enough arguments (process-infographic.sh type/name.svg)'
    exit 1
fi

input_svg=../infographic/$1
output_png_2x=../static/infographic/${1%.svg}.png

output_jpg_cropped=../static/infographic/${1%.svg}-cropped.jpg
output_jpg_small=../static/infographic/${1%.svg}.jpg

echo "removing " $input_svg

rm $input_svg
rm $output_png_2x
rm $output_jpg_small
rm $output_jpg_cropped

