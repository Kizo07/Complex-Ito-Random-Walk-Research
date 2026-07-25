# TASK-007 verification ledger

## Scope and provenance

This is a concise verification ledger, not a fabricated verbatim terminal
transcript. The initial red-state observation was made before
`phase5_model.py` existed; its raw PTY output was not retained. The final
green-state commands below were rerun after all GLM 5.2 review corrections.

## Test-first red state

Before implementation, running the new Phase 5 test module produced:

```text
ModuleNotFoundError: No module named 'phase5_model'
```

That observation established that the tests could not pass by importing an
earlier implementation. It is preserved here as a contemporaneous result
reported during TASK-007, with the raw transcript limitation stated
explicitly.

## Final green state

Preserved environment: `phase3-paper`, without installing or upgrading any
package.

The environment does not contain `pytest`; the tests use Python's built-in
`unittest`, consistent with the project’s Phase 4 and Phase 5 test modules.

```text
conda run -n phase3-paper python -m unittest tests.test_phase5_model -v
Ran 23 tests in 0.012s
OK

conda run -n phase3-paper python -m unittest discover -s tests -v
Ran 33 tests in 0.012s
OK
```

Both Python sources compile:

```text
conda run -n phase3-paper python -m py_compile \
  phase5_model.py notebooks/build_phase5_one_phase_euler.py
```

## Notebook and evidence gate

After the final reviewer corrections:

- three clean-kernel notebook executions completed;
- all had 38 cells, 18 code cells, execution counts \(1,\ldots,18\), and zero
  error outputs;
- all three produced byte-identical sets of 33 CSV/JSON evidence files;
- the final artifact set contains 18 raster PNG and 18 vector PDF figures;
- two consecutive unexecuted builder runs produced byte-identical notebooks;
  and
- the final notebook was left in its executed state.

Hashes:

```text
ordered relative-name evidence aggregate
fa8fd5f517c9f321f3426cfdbd5fe2e9f8bea4e213ad945a8207a87a9736619e

unexecuted deterministic notebook
105201af9508a908f3466cb4e2ed73ede08a476baa60420c70bd137ce0580576

normalized executed-notebook cell sources
5dd4f3ddb420c8e69e8f2ad4c344b15cbe837c2b63c402a5aa1082cefeefe61d

phase5_model.py
6df77121c9c90a9b419320a82c66da53904865ed6082a9135afaedc575fcdf26

tests/test_phase5_model.py
9513037c6d25c82139a0a3304a6bbf7af32649b77ffe3d9ba1f8d4e9e63595f4

notebooks/build_phase5_one_phase_euler.py
2c8411e87d43356892a5b16ec169c8a0c6d3e6a7b77904d2f6f47c9d23e47f72
```

The evidence aggregate is computed from lexicographically ordered basenames
and their standard `sha256sum` records, not absolute paths.
