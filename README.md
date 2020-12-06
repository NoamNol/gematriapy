# gematriapy
Convert numbers to Hebrew letters

## Install
```bash
pip install gematriapy
```

## Usage
```python
from gematriapy import Gematria
gematria = Gematria()
gematria.number_to_hebrew(3) # => "ג"
```

```python
gematria.number_to_hebrew(15) # => "טו"
```

```python
gematria.number_to_hebrew(822) # => "תתכב"
```

> **NOTE**: Numbers greater than 999 are not supported yet.
