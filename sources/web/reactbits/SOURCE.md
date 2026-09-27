# React Bits (stale fork)

| Field | Value |
|---|---|
| Source URL | https://github.com/epodak/reactbits |
| GitHub repository | `epodak/reactbits` (owner "epodak", User account) — GitHub-flagged **fork** of `DavidHDev/react-bits`; stale (1 star, last pushed 2025-07-01, HEAD commit authored by upstream's David, not epodak) |
| Category | web |
| License | MIT text **+ added "Commons Clause Restriction"** — `LICENSE.txt` (root `LICENSE.md`); GitHub API reports license as NOASSERTION |
| Author / organization | David Haz / DavidHDev (copyright holder per `LICENSE.md`); fork owner epodak has no independent commits |
| Acquired | 2026-09-26 |
| Revision | `cdba9dc374d100f3f719f529ad840f481bc1b743` (main, committed 2025-06-30) |
| Attribution required | License notice only, for the uses the license actually permits |
| Status | REVIEW_REQUIRED — the added clause forbids exactly what this kit would do with it |

## License detail — not plain MIT
Root `LICENSE.md` is MIT text plus an added section, quoted in full:
> **Commons Clause Restriction** — The Software is provided under the terms of the MIT License with the following restrictions: 1. **No Redistribution** – You may **not** sell, sublicense, or otherwise redistribute the components of this library as part of a **component library, template, UI kit, or other packaged product**. 2. **No Competing Products** – You may **not** use the Software to create a library, framework, or package that directly competes with React Bits or uses its components without explicit permission. 3. **No Libraries For Alternate Technologies** – You may **not** develop any library/framework/package that replicates React Bits components without explicit permission. 4. **Allowed Commercial Use** – You **are permitted** to use the Software in commercial projects, SaaS apps, websites, or internal business tools.

Concretely: dropping a component straight into a client/product app — commercial or not — is allowed (clause 4). Copying it into `engineering-kit`, a reusable component library meant to be drawn from repeatedly and packaged into other projects, is exactly what clause 1 forbids. The README's "MIT" badge and GitHub's NOASSERTION detection both trace to the *upstream* `DavidHDev/react-bits` license text; this fork's actual `LICENSE.md` overrides it with the clause above. The requester's "plain MIT" belief is incorrect.

## Useful for (reference/inspiration only — do not extract as-is)
- Backgrounds: Aurora, Silk, Iridescence, Waves, Threads, Hyperspeed, LiquidChrome, Orb, Beams, Balatro, Lightning, Particles
- Text: SplitText, BlurText, ShinyText, GradientText, DecryptedText, TextPressure, VariableProximity, TrueFocus, GlitchText
- Scroll: ScrollReveal, ScrollFloat, ScrollVelocity (TextAnimations), InfiniteScroll, CircularGallery, RollingGallery (Components)
- No dedicated "Hero" bit — heroes are composed by pairing a Background with a TextAnimation
- Nav-flavored: GooeyNav, FlowingMenu, Dock (Components)

## Where things live
- `source/src/content/{Animations,Backgrounds,Components,TextAnimations}/<Name>/` — JS + plain CSS, default variant
- `source/src/tailwind/<category>/<Name>/` — JS + Tailwind variant
- `source/src/ts-default/<category>/<Name>/` — TS + plain CSS variant
- `source/src/ts-tailwind/<category>/<Name>/` — TS + Tailwind variant (closest fit to our stack, if ever cleared)

## Known dependencies
- react ^19.0.0, tailwindcss (Vite plugin) ^4.0.3, framer-motion ^12.6.0, gsap ^3.13.0, @react-three/fiber+drei+rapier ^9–10.x, ogl, matter-js — several bits pull heavy 3D/physics deps, not just React/Tailwind

## Do not copy
- Anything, given Status above, unless the user gets explicit permission from the author or restricts use to inline reference rather than redistribution.
- `src/assets/lanyard/card.glb`, `public/assets/3d/{bar,cube,lens}.glb` — 3D models bundled for Lanyard-style components; provenance/license unstated beyond this repo's own restricted license
- `public/assets/fonts/figtreeblack.ttf` — Google's Figtree font (SIL OFL), a separate license from the code

## Notes
- Fork is byte-identical to upstream at this revision (HEAD authored by DavidHDev, not epodak) — treat as `DavidHDev/react-bits` content reached via epodak's fork URL.
- Checkout is 57 MB; `public/assets/` (17 MB) holds demo gifs/webp/3D models for the showcase site, not extraction targets.
- If ever cleared for use, re-derive from the canonical `DavidHDev/react-bits` repo/license, not this stale fork.
