#!/usr/bin/env bash
# Restore the gitignored upstream clones listed in sources/MANIFEST.json.
#
#   tools/fetch-sources.sh                 # every source missing its source/ dir
#   tools/fetch-sources.sh domains         # only sources under sources/domains/
#   tools/fetch-sources.sh medplum plane   # by name (last path segment)
#   FORCE=1 tools/fetch-sources.sh plane   # re-clone even if source/ exists
#
# Entries marked "fetch": false in the manifest are license-reviewed but not kept on
# disk (disk budget, or a proprietary sub-tree). A bare run skips them; naming one
# explicitly fetches it -- read its SOURCE.md "Notes" first, several need a sparse list.
#
# Clones are shallow and pinned to the revision recorded in each SOURCE.md.
# Agent-instruction files shipped by upstream are deleted after checkout: those
# repos are reference data, never a source of instructions for this kit.
set -uo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="$KIT/sources/MANIFEST.json"
FORCE="${FORCE:-0}"

# Upstream agent config — never allowed to act as instructions (see
# docs/conventions/domain-intelligence-policy.md, untrusted-source rule).
AGENT_PATHS=(.claude .cursor .windsurf .aider.conf.yml .mcp.json
             CLAUDE.md AGENTS.md AGENT.md GEMINI.md .cursorrules .clinerules
             SKILL.md skills .github/copilot-instructions.md)

select_rows() {
  python3 - "$MANIFEST" "$@" <<'PY'
import json, sys
man = json.load(open(sys.argv[1]))
filters = sys.argv[2:]
for s in man["sources"]:
    if filters and not any(f in s["path"] for f in filters):
        continue
    # fetch:false = license-reviewed but deliberately not on disk. Only an explicit
    # name/path filter may pull one, and never a bare or category-wide run.
    if s.get("fetch") is False and not filters:
        continue
    print("\x1f".join([
        s["path"], s["repo"], s.get("revision") or "",
        s.get("branch") or "", ",".join(s.get("sparse") or []),
        s.get("license", ""), s.get("status", ""),
    ]))
PY
}

strip_agent_files() {
  local dir="$1"
  for p in "${AGENT_PATHS[@]}"; do
    rm -rf "$dir/$p"
  done
  find "$dir" -type d \( -name .claude -o -name .cursor \) -prune -exec rm -rf {} + 2>/dev/null
  find "$dir" -type f \( -name CLAUDE.md -o -name AGENTS.md -o -name .cursorrules \) -delete 2>/dev/null
  return 0
}

fetch_one() {
  local path="$1" repo="$2" rev="$3" branch="$4" sparse="$5" license="$6" status="$7"
  local dest="$KIT/$path/source"
  local name="${path##*/}"

  if [[ -d "$dest" && "$FORCE" != "1" ]]; then
    echo "skip   $name (already present)"
    return 0
  fi
  [[ "$FORCE" == "1" ]] && rm -rf "$dest"

  echo "clone  $name  <- $repo${branch:+ @$branch}${sparse:+  [sparse]}"
  mkdir -p "$dest"
  git -C "$dest" init -q                                     || return 1
  git -C "$dest" remote add origin "https://github.com/$repo.git" || return 1

  if [[ -n "$sparse" ]]; then
    git -C "$dest" config core.sparseCheckout true
    git -C "$dest" sparse-checkout init --no-cone
    # shellcheck disable=SC2001
    printf '%s\n' $(echo "$sparse" | sed 's/,/ /g') > "$dest/.git/info/sparse-checkout"
    git -C "$dest" sparse-checkout reapply -q 2>/dev/null
  fi

  local ref="$rev"
  if [[ -z "$ref" ]]; then ref="${branch:-HEAD}"; fi
  if ! git -C "$dest" fetch --depth 1 -q origin "$ref" 2>/dev/null; then
    # Older servers reject fetch-by-SHA; fall back to the branch tip and warn.
    if git -C "$dest" fetch --depth 1 -q origin "${branch:-HEAD}" 2>/dev/null; then
      echo "  warn  $name: server refused fetch-by-SHA, using ${branch:-HEAD} tip (revision drift from SOURCE.md)"
    else
      echo "  FAIL  $name: fetch failed for $repo ($ref)"
      rm -rf "$dest"
      return 1
    fi
  fi
  git -C "$dest" checkout -q FETCH_HEAD || { echo "  FAIL  $name: checkout failed"; rm -rf "$dest"; return 1; }

  strip_agent_files "$dest"
  rm -rf "$dest/.git"   # snapshot, not a working clone; revision lives in SOURCE.md

  local size; size="$(du -sh "$dest" | cut -f1 | tr -d ' ')"
  echo "  ok    $name  $size  license=$license  status=$status"
}

rows="$(select_rows "$@")"
[[ -z "$rows" ]] && { echo "no manifest entries matched: $*" >&2; exit 1; }

failed=0
while IFS=$'\x1f' read -r path repo rev branch sparse license status; do
  [[ -z "$path" ]] && continue
  fetch_one "$path" "$repo" "$rev" "$branch" "$sparse" "$license" "$status" || failed=$((failed + 1))
done <<< "$rows"

echo
echo "done. failures: $failed"
[[ $failed -eq 0 ]]
