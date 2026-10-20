"""Validação, reparo e aplicação de matrizes de correlação."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np


class CorrelationService:
    """Serviço puro: sem Qt, sem SQL."""

    def identity(self, n: int) -> List[List[float]]:
        """Método `CorrelationService.identity`.
            Parâmetros: `self`, `n`.
            Retorna o resultado calculado a partir do estado local."""
        return np.eye(n).tolist()

    def to_csv(self, corr: List[List[float]], path) -> None:
        """Método `CorrelationService.to_csv`.
            Parâmetros: `self`, `corr`, `path`."""
        matrix = np.asarray(corr, dtype=float)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(matrix.tolist())

    def load_csv(self, path) -> List[List[float]]:
        """Método `CorrelationService.load_csv`.
            Parâmetros: `self`, `path`.
            Retorna o resultado calculado a partir do estado local."""
        with open(path, "r", encoding="utf-8", newline="") as f:
            rows = [[float(cell) for cell in row] for row in csv.reader(f) if row]
        if not rows:
            return []
        return rows

    def is_valid(self, corr: List[List[float]], tol: float = 1e-6) -> Tuple[bool, str]:
        """Método `CorrelationService.is_valid`.
            Parâmetros: `self`, `corr`, `tol`.
            Retorna o resultado calculado a partir do estado local."""
        try:
            m = np.asarray(corr, dtype=float)
        except Exception:
            return False, "Matriz inválida."

        if m.ndim != 2 or m.shape[0] != m.shape[1]:
            return False, "Matriz não é quadrada."
        if np.any(np.abs(m) > 1.0 + tol):
            return False, "Valores fora de [-1, 1]."
        if not np.allclose(np.diag(m), 1.0, atol=tol):
            return False, "Diagonal deve ser 1."
        if not np.allclose(m, m.T, atol=tol):
            return False, "Matriz não simétrica."
        eig = np.linalg.eigvalsh(m)
        if eig.min() < -tol:
            return False, f"Não é PSD (λmin = {eig.min():.3e})."
        return True, "OK"

    def repair(self, corr: List[List[float]]) -> List[List[float]]:
        """Nearest PSD via eigendecomposition + clip de autovalores."""
        m = np.asarray(corr, dtype=float)
        m = (m + m.T) / 2.0
        np.fill_diagonal(m, 1.0)

        eig, vec = np.linalg.eigh(m)
        eig = np.clip(eig, 1e-8, None)
        repaired = vec @ np.diag(eig) @ vec.T

        d = np.sqrt(np.diag(repaired))
        d[d == 0] = 1.0
        repaired = repaired / np.outer(d, d)
        np.fill_diagonal(repaired, 1.0)
        repaired = np.clip(repaired, -1.0, 1.0)
        return repaired.tolist()
