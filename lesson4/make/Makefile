# Makefile 示例：自动化编译 LaTeX 文档

# 目标：生成 PDF
document.pdf: document.tex plot-data.png
	xelatex document.tex

# 生成图表：使用 Python 脚本
plot-data.png: data.dat plot.py
	./plot.py -i data.dat -o plot-data.png

# 默认目标
all: document.pdf

# 清理生成的文件
clean:
	rm -f *.pdf *.aux *.log *.out *.toc plot-*.png

# 重新构建
rebuild: clean all

.PHONY: all clean rebuild
