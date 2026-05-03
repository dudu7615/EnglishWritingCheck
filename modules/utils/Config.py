from __future__ import annotations

from modules import Paths, DataTypes
from pathlib import Path
import yaml
from typing import TYPE_CHECKING

_configFile = Paths.config / "Api.yaml"

_Base = DataTypes.Config if TYPE_CHECKING else object


class _AutoSaveConfig(_Base):
    """配置代理，修改属性后自动保存到 YAML 文件。"""

    _data: DataTypes.Config

    def __init__(self, file: Path):
        self._file = file
        self._data = DataTypes.Config.model_validate(
            yaml.safe_load(file.read_text(encoding="utf-8"))
        )

    def __getattribute__(self, name: str):
        # 优先返回代理自身的属性
        if name in {"_data", "_file", "__class__", "save"}:
            return super().__getattribute__(name)
        return getattr(self._data, name)

    def __setattr__(self, name: str, value: str | int):
        if name in {"_data", "_file"}:
            super().__setattr__(name, value)
        else:
            setattr(self._data, name, value)
            self.save()

    def __repr__(self):
        return repr(self._data)

    def save(self):
        data = self._data.model_dump()
        self._file.write_text(yaml.dump(data), encoding="utf-8")


config: DataTypes.Config = _AutoSaveConfig(_configFile)
