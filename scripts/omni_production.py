#!/usr/bin/env python3
"""Deterministic production utilities for Kling 3.0 Omni projects.

This script intentionally exports generation job manifests instead of calling an
undocumented API. Add a transport adapter only after official API documentation
and credentials are available.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BASE_RULES = [
    ("ID-01", "人物身份", "脸部是正确人物，未平均化、未替换肤色或年龄感"),
    ("ID-02", "人物身份", "发型、后脑轮廓、颈肩与身体比例保持参考一致"),
    ("GAR-01", "衣着版型", "T恤衣摆保持在参考身体地标区间，未变长、裁短或塞入裤子"),
    ("GAR-02", "衣着版型", "肩线、袖口、衣身宽度和重磅垂坠保持参考比例"),
    ("GAR-03", "衣着版型", "裤腰、裤型、鞋、项链和配饰未漂移或互换"),
    ("GAR-04", "衣着版型", "正背图案位置、大小和文字结构稳定且不发光"),
    ("ENV-01", "背景环境", "调用正确环境分区且建筑属于同一 ENV-CYPHER"),
    ("ENV-02", "背景环境", "混凝土干燥哑光、结构合理，无湿地、烟雾、卷帘门或随机道具"),
    ("ENV-03", "背景环境", "桥墩、坡道、栏杆、铁网、开口和灯具未呼吸或变形"),
    ("LGT-01", "光影", "自然天光方向连续，弱钠灯位置明确，无蓝橙对打或轮廓灯"),
    ("LGT-02", "光影", "肤色自然、阴影保留眼鼻下颌结构，高光无HDR油亮感"),
    ("ACT-01", "动作", "动作按时码发生，步数固定，无舞蹈化、抽搐、跳帧或脚滑"),
    ("ACT-02", "动作", "辫发、衣摆、裤腿和手臂按真实重量产生有限惯性"),
    ("CAM-01", "摄影机", "焦段、机位、路径、距离、减速和停止点符合镜头配置"),
    ("CAM-02", "摄影机", "无漂浮、变焦、无人机、随机摇镜、过度云台或背景跟随"),
    ("TEX-01", "整体质感", "皮肤、棉布、牛仔和混凝土均为哑光，未塑料化或过度锐化"),
    ("CUT-01", "镜头衔接", "入画方向、出画方向、遮挡或动作落点可衔接相邻镜头"),
    ("NEG-01", "禁止项", "无新增人物、车辆、文字、道具、烟雾、霓虹、CGI或AI变形转场"),
]

MULTI_RULES = [
    ("MUL-01", "多人独立性", "每个人的脸、发型、肤色、体型和年龄感相互独立"),
    ("MUL-02", "多人独立性", "服装、裤子、鞋、项链、配饰和图案没有人物间迁移"),
    ("MUL-03", "多人独立性", "身体没有融合、穿体、复制、消失或新增"),
    ("MUL-04", "多人独立性", "步伐、脚位、表情和手势不完全同步"),
]

GROUP_RULES = [
    ("GRP-01", "四人高风险", "A/B/C/D 四人数量固定且站位层级符合配置"),
    ("GRP-02", "四人高风险", "前后景人物均可辨认，没有变成整齐服装目录队列"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fingerprint(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "exists": False, "sha256": "", "size": 0, "modified_at": ""}
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    stat = path.stat()
    return {
        "path": str(path),
        "exists": True,
        "sha256": digest.hexdigest(),
        "size": stat.st_size,
        "modified_at": datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec="seconds"),
    }


def refresh(config_path: Path) -> None:
    config = load_json(config_path)
    for element in config["elements"]:
        refs = [fingerprint(Path(p)) for p in element["reference_paths"]]
        element["references"] = refs
        short_hash = "-".join(ref["sha256"][:6] if ref["exists"] else "MISSING" for ref in refs)
        element["version"] = f"{element['id']}-v1-{short_hash}"
        element["status"] = "已冻结" if all(ref["exists"] for ref in refs) else "缺少文件"
        element["refreshed_at"] = utc_now()
    config["refreshed_at"] = utc_now()
    save_json(config_path, config)
    print(f"refreshed {config_path}")


def export_queue(config_path: Path, output_dir: Path) -> None:
    config = load_json(config_path)
    shots = config["shots"]
    jobs: list[dict[str, Any]] = []
    for sequence in config["sequences"]:
        seq_shots = [shot for shot in shots if shot["sequence"] == sequence["id"]]
        jobs.append({
            "job_id": f"{config['project_id']}-{sequence['id']}-MASTER",
            "job_type": "custom_multi_shot",
            "transport": "disabled_unverified_api",
            "model": config["model"],
            "duration_sec": sequence["duration_sec"],
            "resolution": config["resolution"],
            "native_audio": False,
            "elements": sorted({e for shot in seq_shots for e in shot["elements"]}),
            "environment": config["environment"]["id"],
            "shots": seq_shots,
            "prompt_source": config["prompt_source"],
            "status": "draft",
        })
    for shot in shots:
        jobs.append({
            "job_id": f"{config['project_id']}-SHOT-{shot['shot_id']}-FALLBACK",
            "job_type": "single_shot_fallback",
            "transport": "disabled_unverified_api",
            "model": config["model"],
            "duration_sec": shot["duration_sec"],
            "resolution": config["resolution"],
            "native_audio": False,
            "elements": shot["elements"],
            "environment": config["environment"]["id"],
            "shot": shot,
            "prompt_source": config["prompt_source"],
            "status": "standby",
        })
    output_dir.mkdir(parents=True, exist_ok=True)
    save_json(output_dir / "generation_queue.json", {"exported_at": utc_now(), "jobs": jobs})
    with (output_dir / "generation_queue.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(["job_id", "job_type", "model", "duration_sec", "elements", "zone", "status", "transport"])
        for job in jobs:
            shot = job.get("shot")
            zone = shot["zone"] if shot else "MULTI"
            writer.writerow([job["job_id"], job["job_type"], job["model"], job["duration_sec"],
                             " ".join(job["elements"]), zone, job["status"], job["transport"]])
    print(f"exported {len(jobs)} jobs to {output_dir}")


def checklist_rules(shot: dict[str, Any]) -> list[tuple[str, str, str]]:
    rules = list(BASE_RULES)
    if len(shot["elements"]) > 1:
        rules.extend(MULTI_RULES)
    if len(shot["elements"]) == 4:
        rules.extend(GROUP_RULES)
    return rules


def generate_checklists(config_path: Path, output_dir: Path) -> None:
    config = load_json(config_path)
    versions = {element["id"]: element.get("version", "未刷新") for element in config["elements"]}
    output_dir.mkdir(parents=True, exist_ok=True)
    for shot in config["shots"]:
        lines = [
            f"# 单镜头验收表｜镜头 {shot['shot_id']}",
            "",
            f"- 项目：{config['project_name']}",
            f"- 时码：{shot['global_time']}",
            f"- Element：{' '.join(shot['elements'])}",
            f"- 环境：{config['environment']['id']} / {shot['zone']}",
            f"- 风险：{shot['risk']}",
            f"- 生成记录 ID：____________",
            f"- 验收时间：____________",
            "",
            "## Element 版本",
            "",
        ]
        for element_id in shot["elements"]:
            lines.append(f"- `{element_id}`：`{versions.get(element_id, '未配置')}`")
        lines.extend(["", "## 检查项", ""])
        current_category = ""
        for code, category, description in checklist_rules(shot):
            if category != current_category:
                lines.extend([f"### {category}", ""])
                current_category = category
            lines.append(f"- [ ] `{code}` {description}")
        lines.extend([
            "",
            "## 判定",
            "",
            "- [ ] 通过：直接进入剪辑",
            "- [ ] 部分通过：后期可修复",
            "- [ ] 失败：重生该镜头",
            "",
            "失败代码：____________",
            "",
            "重生策略：____________",
            "",
        ])
        (output_dir / f"shot_{shot['shot_id']}_checklist.md").write_text("\n".join(lines), encoding="utf-8-sig")
    print(f"generated {len(config['shots'])} checklists in {output_dir}")


def append_log(config_path: Path, output_file: Path, args: argparse.Namespace) -> None:
    config = load_json(config_path)
    valid_shots = {str(shot["shot_id"]) for shot in config["shots"]}
    if args.shot not in valid_shots:
        raise SystemExit(f"shot must be one of {sorted(valid_shots)}")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    exists = output_file.exists()
    with output_file.open("a", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        if not exists:
            writer.writerow(["timestamp", "generation_id", "shot_id", "status", "failure_codes", "notes", "repair_strategy"])
        writer.writerow([utc_now(), args.generation_id, args.shot, args.status, args.codes, args.notes, args.strategy])
    print(f"logged shot {args.shot} to {output_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Kling 3.0 Omni production utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    p_refresh = sub.add_parser("refresh", help="fingerprint Element reference files and update versions")
    p_refresh.add_argument("--config", type=Path, required=True)

    p_queue = sub.add_parser("export-queue", help="export non-sending job manifests")
    p_queue.add_argument("--config", type=Path, required=True)
    p_queue.add_argument("--output-dir", type=Path, required=True)

    p_check = sub.add_parser("checklists", help="generate one Markdown QC checklist per shot")
    p_check.add_argument("--config", type=Path, required=True)
    p_check.add_argument("--output-dir", type=Path, required=True)

    p_log = sub.add_parser("log", help="append one generation result to the failure log")
    p_log.add_argument("--config", type=Path, required=True)
    p_log.add_argument("--output-file", type=Path, required=True)
    p_log.add_argument("--generation-id", required=True)
    p_log.add_argument("--shot", required=True)
    p_log.add_argument("--status", choices=["通过", "部分通过", "失败"], required=True)
    p_log.add_argument("--codes", default="")
    p_log.add_argument("--notes", default="")
    p_log.add_argument("--strategy", default="")

    args = parser.parse_args()
    if args.command == "refresh":
        refresh(args.config)
    elif args.command == "export-queue":
        export_queue(args.config, args.output_dir)
    elif args.command == "checklists":
        generate_checklists(args.config, args.output_dir)
    elif args.command == "log":
        append_log(args.config, args.output_file, args)


if __name__ == "__main__":
    main()

