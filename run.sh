#!/bin/bash
# LeetCode ローカル実行スクリプト
# 使い方: ./run.sh problems/0001_two_sum/solution.py
#          ./run.sh problems/0001_two_sum/solution.cpp

FILE="$1"

if [ -z "$FILE" ]; then
    echo "Usage: ./run.sh <solution_file>"
    exit 1
fi

EXT="${FILE##*.}"

case "$EXT" in
    py)
        echo "=== Running Python ==="
        python3 "$FILE"
        ;;
    cpp)
        echo "=== Compiling & Running C++ ==="
        OUT="${FILE%.cpp}.out"
        g++ -std=c++17 -O2 -o "$OUT" "$FILE" && "./$OUT"
        rm -f "$OUT"
        ;;
    *)
        echo "Unsupported file type: $EXT"
        exit 1
        ;;
esac
