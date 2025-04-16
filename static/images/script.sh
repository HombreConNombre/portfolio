#!/bin/bash

for file in *-min.*; do
    # Verifica que realmente exista algún archivo que coincida
    [ -e "$file" ] || continue

    # Usa 'parameter expansion' para crear el nuevo nombre sin '-min'
    newname="${file/-min/}"

    # Renombra el archivo
    mv "$file" "$newname"
    echo "Renombrado: $file -> $newname"
done

