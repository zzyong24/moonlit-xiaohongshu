![小红书图文：一张封面，配一段值得读的内容](assets/readme/hero.png)

# 月明·小红书图文

把一个观点或案例做成一张封面和配文；需要独立步骤、数据或证据时再展开多图。

## 你会得到什么

- 默认一张封面与不超过 500 字的配文
- 话题标签、图片模式和素材顺序
- 可交给社交发布器的图文交接材料

## 试着这样说

```text
用 moonlit-xiaohongshu。把这个已确认案例做成小红书图文，先按单封面方案写。只有后续图片能补充独立证据时才用多图。
```

## 安装与首次使用

将本仓库的完整目录交给支持本地 Skill 的 Agent 安装，保留 `SKILL.md` 与随附资源。已有同名版本时先检查差异；使用版本锁的工作区沿用自身升级机制。

让 Agent 安装：

```text
请安装这个 Skill：https://github.com/zzyong24/moonlit-xiaohongshu
```

也可通过 Skills CLI 安装：

```bash
npx skills add zzyong24/moonlit-xiaohongshu
```

## 配置与依赖

封面需要 image_gen 和使用方认可的风格／身份参考。选题可以由 moonlit-topic-engine 提供，解释图按需调用 moonlit-material-illustration，平台发布交给 moonlit-social-publisher。

## 数据与使用边界

生图提示词和参考图交给图像服务。文案、封面与素材路径保存在作品中；写作和生图不自动授权上传。正文图不能直接冒充封面，AI 合成声明随素材实际情况填写。

## 配套 Skill

[material-illustration](https://github.com/zzyong24/moonlit-material-illustration) · [social-publisher](https://github.com/zzyong24/moonlit-social-publisher) · [topic-engine](https://github.com/zzyong24/moonlit-topic-engine)

## 详细说明

执行流程与资源导航见 [SKILL.md](SKILL.md)。安装检查不代表真实业务验收；需要外部服务、账号登录或付费生成的步骤，应在使用者自己的环境中验证。

---

月明水清深 · `moonlit-xiaohongshu`

首图为 AI 生成的品牌概念插画，不是工具截图或执行结果。
