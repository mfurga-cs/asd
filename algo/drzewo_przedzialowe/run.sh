#!/bin/bash

for i in {0..10000}
do
  python3 generate.py ${i} >in
  python3 segment_tree.py <in >.tree.out
  python3 segment_tree_tester.py <in >.tester.out

  if ! cmp .tree.out .tester.out >/dev/null; then
    echo "[${i}] ERROR"
    echo "INPUT":
    cat in
    echo "TREE:"
    cat .tree.out
    echo "TESTER:"
    cat .tester.out
    exit 1
  fi
  echo -ne "[${i}] OK\r"
done
echo ""

