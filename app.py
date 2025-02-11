name: PyLint
on:
  pull_request:
    paths:
      - '**.py'

permissions:
  contents: read

jobs:
  build:
    name: PyLint
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
    - name: Get file changes
      id: get_file_changes
      uses: trilom/file-changes-action@a6ca26c14274c33b15e6499323aac178af06ad4b # v1.2.4
      with:
        output: ' '
    - name: Report list of changed files
      run: |
        echo Changed files: ${{ steps.get_file_changes.outputs.files }}
    - name: Set up Python 3.9
      uses: actions/setup-python@42375524e23c412d93fb67b49958b491fce71c38 # v5.4.0
      with:
        python-version: "3.9"
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint==2.13.9 numpy wheel
    - name: Run PyLint on changed files
      run: |
        echo "${{ steps.get_file_changes.outputs.files}}" | tr " " "\n" | grep ".py$" | xargs pylint --rcfile=tensorflow/tools/ci_build/pylintrc
