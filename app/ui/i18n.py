"""Base de i18n (T5447): PT-BR → EN para strings principais da UI.

Dicionário plano string→string. `translate(text, lang)` retorna a tradução
quando conhecida; caso contrário, o texto original (graceful passthrough).
Extender aqui conforme novas telas forem traduzidas.
"""

from __future__ import annotations

LANGS = ("pt-BR", "en")

PT2EN: dict[str, str] = {
    "Próximo": "Next",
    "Substituir por…": "Replace with…",
    "Substituir": "Replace",
    "Todos": "All",
    "Maiúsc./minúsc.": "Match case",
    "Buscar…": "Search…",
    "Alterações não salvas": "Unsaved changes",
    "Validar template CMG": "Validate CMG template",
    "Salvar arquivo": "Save file",
    "Abrir arquivos": "Open files",
    "Limpar experimentos": "Clear experiments",
    "Erro na amostragem": "Sampling error",
    "Amostragem incompleta": "Incomplete sampling",
    "Não encontrado": "Not found",
    "Recarregar plugins": "Reload plugins",
    "Nenhum INCLUDE encontrado no template.": "No INCLUDE found in the template.",
    "Fechar": "Close",
    "Selecionar": "Select",
    "Salvar": "Save",
    "Cancelar": "Cancel",
    "Baixar": "Download",
    "Comparações": "Comparisons",
    "Experimentos": "Experiments",
    "Variáveis": "Variables",
    "Preview": "Preview",
    "Logs": "Logs",
    "Estudos": "Studies",
    "Tarefas": "Tasks",
    "Configurações": "Settings",
    "Sobre": "About",
    "Abrir": "Open",
    "Exportar": "Export",
    "Importar": "Import",
    "Sim": "Yes",
    "Não": "No",
}

EN2PT = {v: k for k, v in PT2EN.items()}

TABLES = {
    "en": PT2EN,
    "pt-BR": EN2PT,
}


def translate(text: str, lang: str = "en") -> str:
    """Traduz `text` para `lang` (passthrough quando fora da tabela)."""
    table = TABLES.get(lang, {})
    return table.get(text, text)


def has_translation(text: str, lang: str = "en") -> bool:
    """True se existe tradução conhecida para `lang`."""
    return text in TABLES.get(lang, {})
