# typography

Self-hosted fonts, all **SIL OFL 1.1**, fetched from the official `google/fonts` repository (`ofl/googlesans`, `ofl/googlesansflex`, `ofl/vazirmatn`), verified 2026-09-29. Each folder carries its `OFL.txt`; Google Sans folders also `TRADEMARKS.md`.

| Font | File | Axes | Scripts | Use |
|---|---|---|---|---|
| Google Sans Flex | `fonts/google-sans-flex/GoogleSansFlex[GRAD,ROND,opsz,slnt,wdth,wght].ttf` (4.2 MB) | wght 1–1000, wdth 25–151, opsz 6–144, slnt −10–0, GRAD, ROND | Latin, Latin-ext, Vietnamese, … — **no Arabic/Persian** | Default UI face. Italic = `slnt` axis (no italic file) |
| Google Sans | `fonts/google-sans/GoogleSans[GRAD,opsz,wght].ttf` + `GoogleSans-Italic[…].ttf` (5 MB each) | wght, opsz, GRAD | Latin; Arabic coverage **not verified** | Alternative with true italics |
| Vazirmatn | `fonts/vazirmatn/Vazirmatn[wght].ttf` (241 KB) | wght | Persian/Arabic + Latin | Fallback for `fa`/`ar` |

## Rules
- The OFL covers the files, not the brand. "Google", "Google Sans", "Google Sans Flex" are trademarks of Google LLC: don't use them in product/company/domain names or imply affiliation (`TRADEMARKS.md`). Keep `OFL.txt` alongside any copy you ship.
- These are TTFs (~15 MB total). Before shipping convert to **WOFF2 subsets** per script (`pyftsubset`/`fonttools`, keep variable axes you use) — don't serve the TTFs. Modified versions must be renamed only if the license requires; there are no Reserved Font Names, but read `OFL.txt`.
- Don't ship font files a project doesn't use. Copy only the folder you need.

## Next.js
```ts
import localFont from 'next/font/local';
export const sans = localFont({
  src: '../fonts/GoogleSansFlex[GRAD,ROND,opsz,slnt,wdth,wght].woff2', // converted
  variable: '--font-sans', display: 'swap', weight: '100 900',
});
export const persian = localFont({ src: '../fonts/Vazirmatn[wght].woff2', variable: '--font-fa', display: 'swap' });
```
```css
:root { --font-ui: var(--font-sans), var(--font-fa), system-ui, sans-serif; }
:lang(fa), :lang(ar) { font-family: var(--font-fa), var(--font-sans), system-ui, sans-serif; }
```
Use Tailwind logical utilities (`ms-`, `ps-`, `text-start`) for RTL; tabular figures via `font-variant-numeric: tabular-nums`. Flutter: declare in `pubspec.yaml` `fonts:` (variable font support depends on Flutter version — test).
