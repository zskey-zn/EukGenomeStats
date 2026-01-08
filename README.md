## Introduction
在 denovo 基因组测序、组装、注释及后续比较基因组学研究中，快速获取已有相关物种的基因组特征，对实验设计、方法选择与结果评估都至关重要。为此，我们开发了 `EukGenomeStats` 工具，基于 NCBI 数据源实现自动化统计信息提取，能够一键生成结构化的真核生物基因组特征表，为多个研究环节提供关键参考。

## Dependencies
[datasets=v15.12.0](https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets)

[python3](https://www.python.org/)

## Quick start
```bash
git clone https://github.com/zskey-zn/EukGenomeStats.git
cd EukGenomeStats
chmod +x datasets_v15.12.0
prefix=`date "+%Y-%m-%d"` && \
# 使用 NCBI datasets 命令行工具，获取所有真核生物基因组的摘要信息，并保存为带日期的 JSON 文件(可能由于网络问题中断，需要重新下载)
./datasets_v15.12.0 summary genome taxon "Eukaryota" > Eukaryota.${prefix}.json && \
#加载 Python 环境，运行解析脚本将 JSON 转换为结构化的 Excel 表格：
python3 ncbi_json2xls.py Eukaryota.${prefix}.json Eukaryota.${prefix}.xls
```
