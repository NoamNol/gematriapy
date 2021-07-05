# gematriapy
![CI](https://github.com/NoamNol/gematriapy/workflows/CI/badge.svg)
![PyPI Deploy](https://github.com/NoamNol/gematriapy/workflows/PyPI%20Deploy/badge.svg)

Convert number to Hebrew or Hebrew to number

## Install
```bash
pip install gematriapy
```

## Usage
**`to_hebrew`**:
```python
import gematriapy
gematriapy.to_hebrew(3) # => "ג"
```

```python
gematriapy.to_hebrew(15) # => "טו"
```

```python
gematriapy.to_hebrew(822) # => "תתכב"
```

> **NOTE**: Numbers greater than 999 are not supported yet.

<br/>

**`to_number`**:
```python
import gematriapy
gematriapy.to_number("ג") # => 3
```

```python
gematriapy.to_number("טו") # => 15
```

```python
gematriapy.to_number("אבא") # => 4
```
