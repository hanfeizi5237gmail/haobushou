# 宣发改写执行计划与验收记录

基线：[editorial-design.md](./editorial-design.md)。本次为已授权的宣传重写及推送，非产品开发。

## 联系入口补充节点

- 状态：verified（编辑与本地检查）。依据作者提供的闲鱼链接和微信加好友二维码，已修改 README 套餐下的联系段落及上手第一步，marketing 素材索引指向该入口；新图落点为 assets/contact/wechat-qr.jpg。
- 检查：本地图片尺寸、裁切视觉检查、Markdown 本地链接、git diff --check、远程 SHA。人工验收点为二维码在 GitHub 的展示与实际扫码，后者本轮不添加好友或操作账户。
- 风险与边界：不猜写微信号；不改变产品或套餐；不向闲鱼商品文案添加站外联系方式；不验证交易或线上会员开通。暂无编辑阻塞。
- 验证记录：660×660 联系二维码已目视核对，完整保留码图与白边；README、marketing/README、proof 的本地链接/锚点检查通过，闲鱼 URL 与作者提供内容一致；git diff --check 通过。只改变联系文案和新联系图片，原产品截图与平台发布素材未变。实际扫码加好友、闲鱼登录后跳转及交易未验证；推送与远程 SHA 核对结果在本轮交付消息中报告。

| 节点 | 文件/展示落点 | 检查方式 | 验收点 | 状态 |
| --- | --- | --- | --- | --- |
| 事实冻结与竞品复查 | proof、publicity-review | 阅读五份文档、五张原始图及竞品 README | 不把菜单/示例/规划写成实测 | verified |
| 全文重构 | README、proof、marketing 三份文档 | 对照事实账本逐项复读、链接检查 | 价值先行，边界完整，声口自然 | verified（编辑检查） |
| 海报与视频 | 七份 SVG/PNG、现有视频脚本/MP4 | node --check；SVG 解析；现有渲染命令；OpenCV 解码 | 比例正确、文字清楚、状态不遮挡 | verified（构建与代理视觉检查） |
| 复查与交付 | 本文件、Git 远程 | git diff --check；截图 diff；本地链接检查；远程 SHA | 仅宣发变更，无凭证，无未决承诺 | verified（内容已推送，远程 SHA 一致） |

阻塞项：暂无需要作者决策的编辑阻塞。EPUB 实际导出、Windows 实机安装、macOS 签名/公证、线上邮件和授权链路没有新增验收证据，不得在本轮宣布完成。

人工验收：用户/独立人员尚未验收本轮宣传稿；代理视觉检查单独记录。社交平台规则、审核、裁切与配音成片需发布时确认。

## 执行记录

- 已读取指定文档和全部五张原始截图，确认档案图显示等待离线归档、待处理 3；阅读/导出为示例，会员为本地隔离测试。
- 经本地代理读取竞品 GitHub README；默认 main 路径 404，改用 GitHub README API 成功。仅研究结构，不采纳其产品承诺。
- 已按 qu-ai-wei 冻结事实与限定；选定宣传正文未发现凭证，历史对话中的敏感材料不属于改写输入，不引用或使用。
- 五份完整正文已重构，套餐期限与定价分开；真实图、演示图、资源待归档与 EPUB 菜单范围分别标注。24 秒无声底片与可选配音/40 秒重剪方案已分开。
- 七张 SVG/PNG 和 24 秒 MP4 已重新生成。`node --check marketing/render-social-assets.mjs`、`bash -n marketing/render-social-video.sh`、`xmllint --format` 通过；`bash marketing/render-social-video.sh` 生成全部图片和视频。
- 本地 Node 检查覆盖 8 份 Markdown、38 个本地链接/锚点：全部存在；主要正文和海报无价格显示；常见凭证模式扫描无命中（不是专业秘密审计）；`git diff HEAD -- assets` 为空，五张原始截图及 Logo 均未修改。
- Python/OpenCV 定向回归通过：3:4 卡片等比居中且内容逐像素保留；原生 9:16 卡片保持不变；缺失图片抛出 FileNotFoundError；视频 720/720 帧可解码、1080×1920、30fps、24 秒。
- 代理逐张查看七张 PNG，另查看视频第 1/5/9/13/17/21 秒抽帧拼图。标题、数字、截图说明没有溢出；原截图状态保留。视频中的小字需配合正文阅读，发布平台实际裁切及配音试读尚未检查。
- 提交前约定复查：未发现越界文件或改动产品代码；Guardrails dependency: MISSING（未单建编码护栏，按宣发编辑基线约束现有脚本的一处尺寸修复）；Verification dependency: PASS（仅本轮素材范围）。属于常规约定复查，不宣称产品功能可交付。未触及 wananchi-spider 符号，无该项目 GitNexus impact/detect_changes 适用改动。
- `git diff --check` 通过。未连接生产服务器、操作账号、改变套餐金额或发布社交平台；用户与独立人员人工验收未执行。
- 宣发内容提交 `861733e3a13ab648d693226e239e9dedaffee37f` 已推送至 `hanfeizi5237gmail/haobushou` 的 main；`git ls-remote origin refs/heads/main` 与本地 SHA 一致。本条为推送后证据回写，不包含进一步文案或素材变更。
