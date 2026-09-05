# 号捕手社交平台宣传素材包

这套素材面向闲鱼、小红书和抖音首轮验证。所有产品截图来自现有号捕手运行证据；`98 → 94 → 54` 仅代表一次真实试点任务，不是普遍容量或成功率承诺。

## 可以直接使用的文件

| 平台 | 推荐文件 | 尺寸 | 用法 |
| --- | --- | --- | --- |
| 闲鱼 | [`assets/goofish-card.png`](./assets/goofish-card.png) | 1200×900 | 商品首图；后续依次放真实收录、档案、导出、会员截图 |
| 小红书 | `assets/xhs-*.png` | 1080×1440 | 按 cover → workflow → proof → export → pricing 顺序发图文 |
| 抖音 | [`assets/douyin-cover.png`](./assets/douyin-cover.png) | 1080×1920 | 视频封面或图文首图 |
| 抖音视频 | [`video/haobushou-social-24s-silent.mp4`](./video/haobushou-social-24s-silent.mp4) | 1080×1920 | 24 秒无声底片；按脚本补配音和音乐后发布 |

平台文案见 [`copywriting.md`](./copywriting.md)，视频分镜、配音和 WorkBuddy 提示词见 [`video-script.md`](./video-script.md)。

## 推荐配图顺序

### 闲鱼

1. `goofish-card.png`
2. `../assets/screenshots/article-capture.png`
3. `../assets/screenshots/article-archive.png`
4. `../assets/screenshots/export.png`
5. `../assets/screenshots/membership.png`

### 小红书

1. `xhs-cover.png`：一句话价值 + 真实截图
2. `xhs-workflow.png`：从公开链接到本地档案
3. `xhs-proof.png`：真实任务快照
4. `xhs-export.png`：导出与本地数据边界
5. `xhs-pricing.png`：免费/会员和价格

### 抖音

首发可直接使用无声底片，再按 `video-script.md` 添加配音、背景音乐和节奏音效。没有剪辑条件时，可以直接发布 `douyin-cover.png` 加 4 张小红书图文卡片。

## 发布前检查

- 不写“任意公众号”“全量抓取”“无限抓取”“防封”“100% 成功”。
- 不编造用户数、下载量、好评、收入、效率倍数或成功率。
- Windows 只能写“候选验证中”，不能写“已正式支持”。
- 首期只能写人工收款、人工确认、固定天数授权，不写自动支付或自动续费。
- 只处理公开内容或用户已获授权访问的内容；不得售卖公众号账号、文章或数据。
- 不在评论和私信中收集密码、Token、Cookie 或未脱敏日志。
- 各平台标题、分类、外链和虚拟软件授权规则可能变化，发布前以平台当日规则为准。

## 重新生成

macOS 本机执行：

```bash
node marketing/render-social-assets.mjs
bash marketing/render-social-video.sh
```

SVG 是可编辑源文件，PNG 和 MP4 是发布文件。图片生成未使用外部 AI 素材；它们由品牌 Logo、真实截图、文字和几何版式确定性合成。
