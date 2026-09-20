# PS1 v2 artifact links and release record

- GitHub: https://github.com/qingyueliu/PS1-Qingyue
- Published v2 source snapshot: https://github.com/qingyueliu/PS1-Qingyue/commit/2fc74e11f58f4e041498fb0a3a9bd11201915523
- Colab: https://colab.research.google.com/github/qingyueliu/PS1-Qingyue/blob/main/companion/notebooks/strategic_reporting_qlearning.ipynb
- Playable Hugging Face Space: https://huggingface.co/spaces/dku-comsci-econ206-2026/qingyue
- Direct game: https://dku-comsci-econ206-2026-qingyue.static.hf.space/
- Hugging Face v2 game commit: https://huggingface.co/spaces/dku-comsci-econ206-2026/qingyue/commit/691e7209517683153f690a88d176c30bae97bb2a
- Author response: AUTHOR_RESPONSE.md (also summarized in Appendix D)
- Original peer reviews: reviews/original/
- Preserved v1: archive/v1/
- Executed grid and per-seed data: companion/outputs/ps1_revision_panel.json
- Human-readable results: companion/outputs/revision_results.md
- Local browser game source: companion/hf_space/index.html

The 750-run model was tested at local content commit e85f75ac3c6bb1ce65e74f7cb01244db0a2a8478. Published GitHub snapshot 2fc74e11f58f4e041498fb0a3a9bd11201915523 contains the same model code plus the completed revision package. Hugging Face commit 691e7209517683153f690a88d176c30bae97bb2a publishes the matching game; its downloaded index.html has the same SHA-256 as the local source.

No v2 PDF is generated in this workflow. Main source is main.tex, using pdfLaTeX in Overleaf. The Colab URL resolves to the published notebook; hosted execution was not repeated because the code did not change after the recorded 750-run check. Layout and Canvas submission are not claimed complete.
