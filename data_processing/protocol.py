import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class context:
    df:pd.DataFrame

    stats:Dict[str,Any]=field(default_factory=dict)
    cleaning_log:list= field(default_factory=list)
    correlations:Dict[str,Any]= field(default_factory=dict)

    is_cleaned:bool=False
    report_ready:bool=False
    
