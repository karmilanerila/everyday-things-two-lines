"""Write the two-line everyday-things entry to entry.txt.

Line 1 explains a sponge to a 10-year-old in one vivid sentence built on a
single analogy; line 2 says what that analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A sponge is like a tiny apartment building where thousands of little water "
    "tenants squeeze into the rooms and stay until you squeeze the building and "
    "they all rush out at once.\n"
    "It maps how the holes hold water and release it when pressed, but leaves out "
    "that a sponge soaks water up by itself, while a real building never drinks.\n"
)


def main():
    lines = ENTRY.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
