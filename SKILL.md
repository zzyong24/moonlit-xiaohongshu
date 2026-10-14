---
name: moonlit-xiaohongshu
description: 月明水清深小红书图文生成 sub-skill。默认生成 1 张封面图和完整配文；只有后续每张图都承载独立证据、步骤或数据时才启用多图模式。输出可直接交给 moonlit-social-publisher 自动准备和发布。配文 ≤500 字，标签 5–8 个。从 moonlit-content-engine 主入口调用。
metadata:
  display_name: 月明·小红书图文
  icon: icon.svg
  updated: "2026-10-04"
---

# 🌙 moonlit-xiaohongshu · 小红书图文 sub-skill

## When to use

- 主入口 moonlit-content-engine 引导要做小红书时
- 用户单独要求"做小红书图文"

## 重要原则

按当前工程激活目录读取 `moonlit-content-engine/references/content-master-contract.md`。从作品 contentMaster 或已确认简述、实测与证据起稿，不强制先写公众号。围绕可搜索的具体任务、成果与必要步骤组织图文；每图承担独立解释任务，不能机械截段。登记实际 inputs，回流遵守工作区规范。

**默认使用 `single_cover`：只生成并发布 1 张封面图 + 配文。** 不为了凑九图复用公众号插图。

仅当至少 2 张后续图片能各自提供不可由正文替代的步骤、证据、数据或对照时，才使用 `carousel`。多图可复用公众号资产，但必须逐张通过“删掉这张是否损失理解或可信度”的检查。

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

- 必须用 `image_gen` 生成（**1 张**）
- 继承当前工程 AGENTS 与用户认可品牌风格；颜色、字体按 `moonlit-content-engine/references/brand-tokens.md` 的亮色 `paper` 主题：暖白、深蓝、铜橙、本人真实形象与本期具体证据；不因内容类型切回宇航员或科技绿。已有参考时使用图生图，不用 SVG 代替封面。
- 配图引用：从当前作品共享素材清单取确定版本；公众号正文图与封面职责不同，不直接把正文图称为封面。
- 小标题：`小红书-封面-[主题]`
- 观点、判断、案例总结默认使用 `single_cover`
- 教程步骤、数据证据、前后对照可使用 `carousel`，共 2–18 张

## 配文规范

- ≤500 字
- 开头 1–2 句按 `moonlit-business-copywriter/references/writing-toolkit.md` 的“钩子选型”选一种（小红书优先结果型、数字型、问题型）；作者原稿已有钩子时保留
- 正文围绕一个主要收获展开；需要逐项查看时用 2–4 个 bullet，不为凑数补到 3 个
- 结尾可自然结束或分享实际项目/资产链接，不默认评论扣词、加微信或引流。
- 标签 5-8 个
- 写明 `imageMode: single_cover` 或 `imageMode: carousel`
- 明确列出实际上传图片的绝对路径或作品根目录相对路径；图 1 必须是封面
- 素材包含 AI 生成或 AI 合成内容时标记 `contentTypeDeclaration: 笔记含AI合成内容`

## 自检清单

- [ ] 配文 ≤500 字
- [ ] 标题让目标读者一眼知道“讲什么、对我有什么用”；数字只用真实数字，emoji 至多 1 个且与内容相关
- [ ] 开头用了一种钩子类型，且正文兑现
- [ ] 标签 5-8 个
- [ ] 封面图已指定（小红书-封面-XXX.png）
- [ ] `single_cover` 只有 1 张图；`carousel` 有 2–18 张且每张都有独立信息价值
- [ ] 所有图片路径存在且顺序固定
- [ ] 已给出原创策略和 AI 内容类型声明，不把两者混为一谈
- [ ] ID 一致：`月明水清深`

## 依赖

- `moonlit-brand-overlay.md`
- `moonlit-topic-engine`
- `image_gen`：封面图生成
- `moonlit-material-illustration`：需要月明风格解释图时使用；单封面模式通常不调用
- `moonlit-social-publisher`：发布准备、当次授权发布和结果核验
