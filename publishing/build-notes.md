# Publicering och GitHub Actions

Det här projektet använder ett anpassat Romanskaparen-upplägg för reproducerbar EPUB/PDF-generering i GitHub Actions.

## Workflowöversikt

- `.github/workflows/01-validate.yml` kör snabb validering vid pull request och push till `main`.
- `.github/workflows/02-build-preview.yml` kan köras manuellt och laddar upp EPUB och PDF som ett gemensamt Actions-artifact.
- `.github/workflows/03-release.yml` körs vid taggar enligt `v*` och publicerar EPUB och PDF som separata release-assets.

## Bygg lokalt

```bash
python3 scripts/validate_project.py .
python3 scripts/build_book.py --output-dir dist
```

Kräver Pandoc 3.1.11.1 för reproducerbart bygge. PDF kräver XeLaTeX och TeX Gyre Pagella.
