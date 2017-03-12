#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo 'not enough arguments (process-infographic.sh infographic-path.png)'
    exit 1
fi

input_filename=$1
output_filename=${input_filename%.png}.jpg

echo $input_filename
echo $output_filename

width=1024

convert $input_filename -resize $width $output_filename
