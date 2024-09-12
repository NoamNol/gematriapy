# gematriapy
[![PyPI Latest Release](https://img.shields.io/pypi/v/gematriapy.svg?color=b2c5f1)](https://pypi.org/project/gematriapy/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/gematriapy.svg?label=PyPI%20downloads)](https://pypi.org/project/gematriapy/)

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
