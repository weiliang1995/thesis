#!/usr/bin/env python3
"""Fetch candidate PDFs locally. Review licenses before committing files."""
from pathlib import Path
from urllib.request import Request, urlopen
import sys

ROOT = Path(__file__).resolve().parent
DOWNLOADS = [
  [
    "prompt-engineering/schulhoff-et-al-2025-prompt-report.pdf",
    "https://arxiv.org/pdf/2406.06608"
  ],
  [
    "prompt-engineering/liu-et-al-2026-prompt-taxonomy.pdf",
    "https://link.springer.com/content/pdf/10.1007/s11704-025-50058-z.pdf"
  ],
  [
    "context-engineering/mei-et-al-2025-context-engineering-survey.pdf",
    "https://arxiv.org/pdf/2507.13334"
  ],
  [
    "harness-engineering/barbaste-et-al-2026-coding-agent-harnesses.pdf",
    "https://arxiv.org/pdf/2609.00006"
  ],
  [
    "harness-engineering/macedo-2026-harness-definition.pdf",
    "https://arxiv.org/pdf/2606.10106"
  ]
]
failed = 0
for name, url in DOWNLOADS:
    dest = ROOT / name
    if dest.exists():
        print(f"SKIP {name}")
        continue
    try:
        request = Request(url, headers={"User-Agent": "Thesis reference reader/1.0"})
        with urlopen(request, timeout=90) as response:
            data = response.read()
        if not data.startswith(b"%PDF-"):
            raise ValueError("Response is not a PDF")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"OK {name}")
    except Exception as exc:
        failed += 1
        print(f"FAILED {name}: {exc}", file=sys.stderr)
sys.exit(bool(failed))
