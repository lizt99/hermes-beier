#!/usr/bin/env python3
"""
护工服务宣传图片生成器

直接将现场图和护工图传给 gemini-3.1-flash-image，
让模型以现场为背景、以护工人物和行为为主体生成宣传图，
并保留马甲上的公司名和电话。

用法：
  python generate_image.py --scenes room.jpg --caregivers nurse.jpg
  python generate_image.py --scenes ward.jpg --caregivers nurse.jpg --count 3 --output ./results
"""

import argparse
import base64
import sys
from pathlib import Path
from typing import Optional

import httpx
from openai import OpenAI

GATEWAY_URL  = "https://aigateway-sandbox.mspbots.ai/v1"
API_KEY      = "sk-U9s9IAaKrFvh7qhHdpPdeA"
IMAGE_MODEL  = "gemini-3.1-flash-image"
IMAGE_SIZE   = "1242×1660"
PROMPT       = (
    "以第一张图为场景背景，将后续护工图片中的人物自然融入该场景中。"
    "【核心逻辑要求】：必须根据背景合理设计动作。大厅里是站立/陪诊；病房里是床边护理或整理。"
    "【人体构图要求（极重要）】：为了确保马甲上的电话号码足够大且清晰，必须采用【近景】或【中景】（例如腰部以上的半身照），让护工的背部占据画面的主要比例！【绝对不要生成远景全身照】。只要保证上半身结构完整自然即可，允许画面在腰部或臀部边缘自然截断，核心目的是拉近镜头放大文字！"
    "【文字展示要求（最高优）】：人物动作需要符合场景,必须保持背部相对平挺，尽量避免过度弯腰或扭曲的动作，以确保马甲上的文字完全不被遮挡或变形！一定要极度清晰、无错别字地展示马甲背部的文字：优加陪护，以及电话：15793592202。"
    "生成一张专业的护工服务宣传照片。4K 分辨率，1242×1660，竖图"
)

client = OpenAI(api_key=API_KEY, base_url=GATEWAY_URL)


def img_block(path: str) -> dict:
    if path.startswith(("http://", "https://")):
        r = httpx.get(path, timeout=30, follow_redirects=True)
        r.raise_for_status()
        mime = r.headers.get("content-type", "image/jpeg").split(";")[0].strip()
        data = base64.b64encode(r.content).decode()
    else:
        ext  = Path(path).suffix.lower()
        mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                ".png": "image/png",  ".webp": "image/webp"}.get(ext, "image/jpeg")
        data = base64.b64encode(Path(path).read_bytes()).decode()
    return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{data}"}}


def generate_one(
    scene_paths: list[str],
    caregiver_paths: list[str],
    output_path: str,
    custom_prompt: Optional[str] = None,
) -> bool:
    content = []
    for p in scene_paths:
        content.append(img_block(p))
    for p in caregiver_paths:
        content.append(img_block(p))
    content.append({"type": "text", "text": custom_prompt or PROMPT})

    try:
        resp = client.chat.completions.create(
            model=IMAGE_MODEL,
            messages=[{"role": "user", "content": content}],
            extra_body={"response_modalities": ["IMAGE", "TEXT"]},
        )
    except Exception as exc:
        print(f"  API 错误：{exc}")
        return False

    images = resp.choices[0].message.model_extra.get("images", [])
    if not images:
        print("  未返回图片")
        return False

    # 取第一张（模型有时返回多张）
    url = images[0]["image_url"]["url"]
    img_bytes = base64.b64decode(url.split(",", 1)[1])
    Path(output_path).write_bytes(img_bytes)
    return True


def main():
    parser = argparse.ArgumentParser(
        description="生成专业护工服务宣传图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例：
  python generate_image.py --scenes room.jpg --caregivers nurse.jpg
  python generate_image.py --scenes ward.jpg --caregivers nurse.jpg --count 3 --output results
  python generate_image.py --scenes room.jpg --caregivers nurse.jpg \\
      --prompt "以第一张图为场景，将护工融入，马甲文字清晰可见"
        ''',
    )
    parser.add_argument("--scenes",     nargs="+", required=True, help="现场照片（支持多张）")
    parser.add_argument("--caregivers", nargs="+", required=True, help="护工照片（支持多张）")
    parser.add_argument("--output",     default="output",         help="输出目录（默认 output）")
    parser.add_argument("--count",      type=int, default=1,      help="生成张数（默认 1）")
    parser.add_argument("--prompt",     default=None,             help="自定义 prompt（可选）")
    args = parser.parse_args()

    for p in args.scenes + args.caregivers:
        if not p.startswith(("http://", "https://")) and not Path(p).exists():
            print(f"文件不存在：{p}", file=sys.stderr)
            sys.exit(1)

    Path(args.output).mkdir(parents=True, exist_ok=True)

    print(f"现场图片  : {args.scenes}")
    print(f"护工图片  : {args.caregivers}")
    print(f"生成张数  : {args.count}")
    print(f"输出目录  : {args.output}\n")

    generated = []
    for i in range(args.count):
        out = str(Path(args.output) / f"service_photo_{i+1:02d}.png")
        print(f"生成第 {i+1}/{args.count} 张 → {out}")
        ok = generate_one(args.scenes, args.caregivers, out, args.prompt)
        if ok:
            size_kb = Path(out).stat().st_size // 1024
            print(f"  ✓ 已保存 ({size_kb} KB)")
            generated.append(out)
        else:
            print(f"  ✗ 失败")

    print(f"\\n完成：{len(generated)}/{args.count} 张")
    sys.exit(0 if generated else 1)


if __name__ == "__main__":
    main()