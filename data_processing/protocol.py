from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

import pandas as pd


@dataclass
class OperationLog:
    step: str
    method: str
    column: str | None = None
    details: dict[str, Any] = field(default_factory=dict)
    status: str = "success"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> dict[str, Any]:
        return {
            "step": self.step,
            "method": self.method,
            "column": self.column,
            "details": self.details,
            "status": self.status,
            "created_at": self.created_at,
        }


@dataclass
class AnalysisContext:
    raw_df: pd.DataFrame
    df: pd.DataFrame | None = None
    stats: dict[str, Any] = field(default_factory=dict)
    correlations: dict[str, Any] = field(default_factory=dict)
    cleaning_log: list[OperationLog] = field(default_factory=list)
    filter_log: list[OperationLog] = field(default_factory=list)
    report: dict[str, Any] = field(default_factory=dict)
    prompt_context: str = ""
    is_cleaned: bool = False
    report_ready: bool = False

    def __post_init__(self) -> None:
        if self.df is None:
            self.df = self.raw_df.copy()

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "AnalysisContext":
        return cls(raw_df=df.copy(), df=df.copy())

    def add_cleaning_log(self, method: str, column: str | None = None, **details: Any) -> None:
        self.cleaning_log.append(
            OperationLog(step="cleaning", method=method, column=column, details=details)
        )
        self.is_cleaned = True

    def add_filter_log(self, method: str, column: str | None = None, **details: Any) -> None:
        self.filter_log.append(
            OperationLog(step="filtering", method=method, column=column, details=details)
        )

    def set_report(self, report: dict[str, Any]) -> None:
        self.report = report
        self.stats = report.get("describe", {})
        self.correlations = report.get("correlations", {})
        self.report_ready = True

    def set_prompt_context(self, prompt_context: str) -> None:
        self.prompt_context = prompt_context

    def logs_as_dict(self) -> dict[str, list[dict[str, Any]]]:
        return {
            "cleaning": [log.to_dict() for log in self.cleaning_log],
            "filtering": [log.to_dict() for log in self.filter_log],
        }

    def summary(self) -> dict[str, Any]:
        return {
            "raw_shape": self.raw_df.shape,
            "current_shape": self.df.shape,
            "is_cleaned": self.is_cleaned,
            "report_ready": self.report_ready,
            "cleaning_steps": len(self.cleaning_log),
            "filtering_steps": len(self.filter_log),
        }


context = AnalysisContext
