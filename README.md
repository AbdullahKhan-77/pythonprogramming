# Python Fundamentals — Practice Exercises

Internship prep repo covering core Python concepts through hands-on exercises, from basic syntax up to decorators and file handling with pandas.

## Topics Covered

- Variables & data types
- Data structures — lists, dictionaries, sets, tuples
- Control flow & loops
- Functions
- Iterators
- Generators
- Decorators
- Working with files (CSV) and an intro to pandas

## Tasks

| Task | Topic | Status |
|------|-------|--------|
| 01 | Basics — variables & types | ✅ Done |
| 02 | Data structures | ✅ Done |
| 03 | Control flow & loops | ✅ Done |
| 04 | Functions | ✅ Done |
| 05 | Iterators | ✅ Done |
| 06 | Generators | ✅ Done |
| 07 | Decorators | ✅ Done |
| 08 | Working with files — reading a CSV (+ pandas) | ✅ Done |

## Project Structure

```
.
├── task01_basics.py
├── task02_data_structures.py
├── task03_control_flow.py
├── task04_functions.py
├── task05_iterators.py
├── task06_generators.py
├── task07_decorators.py
├── task08_files_pandas.py
├── sample_data.csv
└── README.md
```

*(Adjust file names above to match your actual repo layout.)*

## How to Run

Each task can be run individually from the terminal:

```bash
python task01_basics.py
```

Make sure your virtual environment is activated first, and dependencies from Task 08 (`pandas`) are installed:

```bash
pip install pandas
```

## Git Workflow

Each task was developed on its own feature branch and merged into `dev` through a Pull Request:

```bash
git checkout -b task-01-basics
# work, commit, push
git push -u origin task-01-basics
# open PR: task-01-basics -> dev, then merge
```

## Notes

Decorators were the trickiest part to get comfortable with — understanding how a function can wrap another function and modify its behaviour without changing the original code. Working through the basics first (passing functions as arguments) and then building up to wrappers using `*args` and `**kwargs` made the `@decorator` syntax click.