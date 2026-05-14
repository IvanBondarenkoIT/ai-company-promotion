"""One-off: FAQ .md -> plain .txt for Notepad editing."""
import pathlib
import re

BT = chr(96)

HEADER = (
    "Источник правды — соседний .md с тем же именем; после правок в .txt "
    "перенесите изменения обратно в .md.\n\n"
)


def strip_md_inline(s: str) -> str:
    while "**" in s:
        s = s.replace("**", "", 1)
        if "**" in s:
            s = s.replace("**", "", 1)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 (\2)", s)
    s = re.sub(r"\[([^\]]+)\]\([^#][^)]*\)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\(#[^)]+\)", r"\1 (раздел в конце файла)", s)
    s = s.replace(BT, "")
    return s


def md_to_txt(s: str) -> str:
    lines = s.splitlines()
    out: list[str] = []
    for line in lines:
        if line.strip() == "---":
            out.append("")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level, text = len(m.group(1)), strip_md_inline(m.group(2).strip())
            if level == 1:
                out.extend(["", "=" * 72, text.upper(), "=" * 72, ""])
            elif level == 2:
                out.extend(["", text.upper(), "-" * min(max(len(text), 3), 72), ""])
            else:
                out.extend(["", text, ""])
            continue
        out.append(strip_md_inline(line))
    text = "\n".join(out)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    base = pathlib.Path(__file__).resolve().parent
    for name in ("FAQ_RU_FOR_WEBSITE_v3_clean.md", "FAQ_RU_FOR_WEBSITE_v3.md"):
        p = base / name
        body = md_to_txt(p.read_text(encoding="utf-8"))
        outp = base / (name.replace(".md", ".txt"))
        outp.write_text(HEADER + body, encoding="utf-8")
        print(outp)


if __name__ == "__main__":
    main()
