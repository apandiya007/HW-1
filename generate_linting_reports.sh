#!/bin/bash

mkdir -p linting_reports

# Only look inside src/ and tests/, excluding .venv
find src tests -name "*.py" | while read -r file; do
    base_name=$(echo "$file" | sed 's|/|_|g')
    json_file="linting_reports/${base_name}.json"
    xml_file="linting_reports/${base_name}.xml"
    temp_file=$(mktemp)

    # Strip both whole-line and inline pylint comments
    sed '/^[[:space:]]*#[[:space:]]*pylint:/d; s/[[:space:]]*#[[:space:]]*pylint:.*//' "$file" > "$temp_file"


    if ! diff -u "$file" "$temp_file" > /dev/null; then
        echo "⚠️ Warning: $file has been modified by stripping pylint comments."
        echo "🔍 Differences in: $file"
        diff -u "$file" "$temp_file"
    fi


    echo "Linting $file -> $xml_file"
    pylint "$temp_file" --output-format=json --disable=import-error > "$json_file"
    pylint-json2checkstyle < "$json_file" > "$xml_file"

    rm "$json_file"  # Optional cleanup
    rm "$temp_file"  # Clean up the temporary file
done

