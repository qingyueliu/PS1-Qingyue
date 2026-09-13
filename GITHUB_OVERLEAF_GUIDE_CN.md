# PS1 GitHub 和 Overleaf 使用指南

## 你需要区分的两个仓库

1. `dku-comsci-econ206-Autumn2026/ps1-overleaf-template` 是课程排版模板，不是你的研究仓库。
2. `qingyueliu/PS1-Qingyue` 是已经创建的个人 fork，也是 Open Science Statement 和 Colab 链接使用的仓库。

## 推荐操作顺序

1. 登录 GitHub，打开 `https://github.com/qingyueliu/PS1-Qingyue`，确认页面显示它 fork 自课程模板。
2. 将本项目 ZIP 解压后的内容放入个人 fork；不要只上传 ZIP 或 PDF。
3. 确认仓库根目录直接包含 `main.tex`、`sections/`、`appendices/`、`figures/`、`references.bib`、`companion/` 和 ACM 样式文件。
4. Commit 并 Push 后打开 GitHub 的 **commits** 页面，复制提交代码快照的 7--40 位哈希，填入 `sections/proposal.tex` 的 `[ADD COMMIT]`。

## 在 Overleaf 中使用

### 如果账户支持 GitHub synchronization

1. 在 Overleaf Account Settings 中连接 GitHub。
2. 回到项目首页，选择 **New Project → Import from GitHub**，选择你自己的 fork。
3. 在项目设置中将 **Main document** 设为 `main.tex`，**Compiler** 设为 `pdfLaTeX`。
4. 点击 **Recompile**；参考文献第一次未出现时再编译一次。
5. GitHub 与 Overleaf 不会自动同步。编辑前先 Pull，完成后再 Push，并确认没有覆盖另一端的新版本。

### 如果账户不支持 GitHub synchronization

1. 在 GitHub fork 中选择 **Code → Download ZIP**。
2. 在 Overleaf 选择 **New Project → Upload Project** 并上传 ZIP。
3. 设置 `main.tex` 和 `pdfLaTeX` 后编译。
4. Overleaf 修改完成后下载 source ZIP，再手动上传回 GitHub fork，形成最终 commit。

## Colab 链接的工作方式

Notebook 路径是：

`companion/notebooks/strategic_reporting_qlearning.ipynb`

本项目的 Colab URL 是：

`https://colab.research.google.com/github/qingyueliu/PS1-Qingyue/blob/main/companion/notebooks/strategic_reporting_qlearning.ipynb`

打开后选择 **Runtime → Run all**。结果应与 notebook 中保存的四行均值接近且在固定种子下完全一致。该 notebook 只用 Python 标准库，不需要 API key、GPU 或额外安装。

## 提交前核对

- `main.tex` 中的个人 GitHub 和 Colab URL 均指向 `qingyueliu/PS1-Qingyue`。
- Open Science Statement 包含你的 GitHub URL、Colab URL 和最终 commit。
- Hugging Face URL 指向你的现有 Space。
- `figures/ps1_teaser.drawio` 可以在 diagrams.net 中逐个编辑对象；同时提交其 vector PDF。
- Overleaf 编译后的正文只有五个编号 section，且主文严格为两页；References、Author Notes 和 Appendices 从第三页开始。
- 最终上传文件使用 `PS1-ql186-Qingyue-Liu.pdf` 和 `PS1-ql186-Qingyue-Liu.zip`；提交前再次确认 NetID。
