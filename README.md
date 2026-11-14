# writing-skills

个人写作 skill 仓库:语言得体、风格统一的长文写作规则集,经十几篇真实发布文章打磨(含一次被平台删文的事故复盘)。

## 安装(用户级,所有项目生效)

```bash
mkdir -p ~/.zcode/skills
ln -sfn ~/ZCodeProject/writing-skills/polished-writing ~/.zcode/skills/polished-writing
```

## 覆盖场景

| 类型 | 规则文件 |
|---|---|
| 通用(风格/排版/红线/诚信/结构) | `polished-writing/SKILL.md` |
| 硬核科普 | `references/tech.md` |
| 通俗科普 | `references/popular.md` |
| 开源/产品宣传 | `references/promo.md` |
| 热点评论 | `references/hotspot.md` |
| 知乎平台适配(公式/表格/风控) | `references/zhihu.md` |

## 触发方式

写作/润色/把关长文时自动触发;或显式 `/polished-writing`。
