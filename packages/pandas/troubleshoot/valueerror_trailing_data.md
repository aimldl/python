* Draft: 2020-11-09

# ValueError: Trailing data

## Problem

```python
from pathlib import Path

dir_project = Path.cwd()
dir_dataset = dir_project / 'dataset'
input_jsonl_file = dir_dataset / 'train-18k.jsonl'

file = pd.read_json( input_jsonl_file )
  ...
~/anaconda3/lib/python3.8/site-packages/pandas/io/json/_json.py in _parse_no_numpy(self)
   1117         if orient == "columns":
   1118             self.obj = DataFrame(
-> 1119                 loads(json, precise_float=self.precise_float), dtype=None
   1120             )
   1121         elif orient == "split":

ValueError: Trailing data
```

## Cause

JSON 파일의 내용이 1줄 이상일 때 발생하는 에러입니다.

## Solution

`lines=True`를 추가하면 에러 없이 파일을 읽을 수 있습니다.

```python
file = pd.read_json( input_jsonl_file, lines=True )
```

