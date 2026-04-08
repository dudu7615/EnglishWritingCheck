from modules import Paths
import yaml
from modules import DataTypes

_configFile = Paths.config / "Api.yaml"

config: DataTypes.ApiConfig = yaml.safe_load(_configFile.read_text(encoding="utf-8"))
