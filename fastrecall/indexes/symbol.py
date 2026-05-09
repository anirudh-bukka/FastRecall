"""Symbol index skeleton."""

from fastrecall.models import RetrievalResult, SymbolRecord


class SymbolIndex:
    """Lookup symbols by name, kind, language, or repository."""

    def add_symbol(self, symbol: SymbolRecord) -> None:
        """Add one symbol."""

        raise NotImplementedError

    def find_definition(
        self,
        name: str,
        repo_ids: list[str] | None = None,
    ) -> list[RetrievalResult]:
        """Find where a symbol is defined."""

        raise NotImplementedError

    def search_symbols(
        self,
        query: str,
        repo_ids: list[str] | None = None,
    ) -> list[RetrievalResult]:
        """Search symbols by name/signature/docstring."""

        raise NotImplementedError

