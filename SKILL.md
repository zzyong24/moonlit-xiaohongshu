---
name: moonlit-xiaohongshu
description: "月明水清深小红书图文生成 sub-skill。用户说“做小红书图文”“写一篇小红书笔记”“把这个案例写成小红书笔记”时使用，或由 moonlit-content-engine 主入口调用。默认 1 张封面图 + 完整配文（封面交当前激活 gbro-cover-design）；只有后续每张图都承载独立证据、步骤或数据时才启用多图。配文 ≤500 字，标签 5–8 个。只产出图文包，审核通过后交给发布工具 moonlit-social-publisher（月明逐条看预览、批准后才发）；不用于公众号长文、X 线程或视频。"
metadata:
  display_name: 月明·小红书图文
  updated: "2026-10-04"
---

# 🌙 moonlit-xiaohongshu · 小红书图文 sub-skill

## When to use

- 主入口 moonlit-content-engine 引导要做小红书时
- 用户单独要求"做小红书图文"

## When not to use

- 公众号长文 → moonlit-wechat-article；X 线程 → moonlit-x-short；视频 → 视频制作 skill
- 实际发布、上传 → 本 Skill 不做；图文包**审核通过后交给发布工具** `moonlit-social-publisher`，由它给月明看最终预览、等月明对这一条明确批准后才发布，发布后回报链接

## 重要原则

读取 [内容母版合同](references/content-master-contract.md)（随包副本；工程里有 `moonlit-content-engine` 时以当前版为准）。从作品 contentMaster 或已确认简述、实测与证据起稿，不强制先写公众号。围绕可搜索的具体任务、成果与必要步骤组织图文；每图承担独立解释任务，不能机械截段。登记实际 inputs，回流遵守工作区规范。

**默认使用 `single_cover`：只生成 1 张封面图 + 配文。** 不为了凑九图复用公众号插图。

仅当至少 2 张后续图片能各自提供不可由正文替代的步骤、证据、数据或对照时，才使用 `carousel`。多图可复用公众号资产，但必须逐张通过“删掉这张是否损失理解或可信度”的检查。

## 按需参考

表达不具体时可读 [写作工具箱](references/writing-toolkit.md)，只采用有真实依据的动作和例子，不强制挑固定数量的技巧；历史 [品牌令牌](references/brand-tokens.md) 仅在复现旧工程时读取，不覆盖当前 gbro 封面规则。

## 输出位置

写入当前作品的 `content/xiaohongshu/`，不要写入 Skill 目录。

## 文件命名

```
MMDDHHMM-[纯中文主题]-小红书.md
```

**示例**：
```
2608261200-AI工具三个坑-小红书.md
```

## 封面图规范

- 封面统一调用当前激活的 `gbro-cover-design`，先选小红书图文 3:4 槽位并按其平台输出合同交付。默认单封面，原图与缩略图分别打开检查。
- 按题材采用 gbro 的构图、字体与配色自由；身份参考、既有风格与本期覆盖读工作区配置。不叠加旧暖白/深蓝/铜橙母版，不用 SVG 代替封面位图。
- 配图引用：从当前作品共享素材清单取确定版本；公众号正文图与封面职责不同，不直接把正文图称为封面。
- 小标题：`小红书-封面-[主题]`
- 观点、判断、案例总结默认使用 `single_cover`
- 教程步骤、数据证据、前后对照可使用 `carousel`，共 2–18 张

## 配文规范

- ≤500 字
- 开头 1-2 句抓人（含数字/emoji/反常识）
- 3 个 bullet 核心洞察
- 结尾可自然结束或点明实际项目/资产名称；实际上传的标题、配文与标签不含外部 URL，不默认评论扣词、加微信或引流。完整来源链接单独留作品素材清单，不混入上传文案。
- 标签 5-8 个
- 写明 `imageMode: single_cover` 或 `imageMode: carousel`
- 明确列出实际上传图片的绝对路径或作品根目录相对路径；图 1 必须是封面
- 素材包含 AI 生成或 AI 合成内容时标记 `contentTypeDeclaration: 笔记含AI合成内容`

## 上传文案预检

将实际要粘贴的标题、配文与标签保存为 UTF-8 文本，运行 `python3 scripts/preflight_note.py <upload-copy.txt>`；非零退出先修正文案，再交发布器。该脚本只核非空、500 字上限与显式 URL，不替代事实审查、图片文字检查或平台审核。素材清单和文件路径不放进上传文本。

## 自检清单

- [ ] 配文 ≤500 字
- [ ] 标题含数字/emoji/情绪词
- [ ] 开头 1-2 句抓人
- [ ] 标签 5-8 个
- [ ] 封面图已指定（小红书-封面-XXX.png）
- [ ] `single_cover` 只有 1 张图；`carousel` 有 2–18 张且每张都有独立信息价值
- [ ] 所有图片路径存在且顺序固定
- [ ] 已给出原创策略和 AI 内容类型声明，不把两者混为一谈
- [ ] ID 一致：`月明水清深`

## 依赖

- `moonlit-brand-overlay.md`
- `moonlit-topic-engine`
- `gbro-cover-design`：封面与平台槽位输出，实际生图由其能力路由执行
- `moonlit-material-illustration`：需要月明风格解释图时使用；单封面模式通常不调用
- `moonlit-social-publisher`：审核通过后的发布工具（逐条预览、月明逐条批准、发布后回报链接）
