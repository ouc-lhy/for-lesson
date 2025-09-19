# demo.py - 简化版文本情感分析（PyTorch + spaCy）

import torch
import torch.nn as nn
import spacy
import numpy as np


# ========================
# 1. 加载 spaCy 英文模型
# ========================
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("请先运行：python -m spacy download en_core_web_sm")
    exit()

# ========================
# 2. 模拟数据集（正面/负面评论）
# ========================
from data import reviews
# ========================
# 3. 构建词汇表
# ========================
# 分词并构建词表
all_tokens = []
for text, label in reviews:
    tokens = [token.text.lower() for token in nlp(text) if token.is_alpha]
    all_tokens.extend(tokens)

# 去重并排序
vocab = ['<unk>'] + list(set(all_tokens))
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
VOCAB_SIZE = len(vocab)
EMBEDDING_DIM = 50
print(f"词汇表大小: {VOCAB_SIZE}")

# ========================
# 4. 数据编码函数
# ========================
def encode_text(text):
    tokens = [token.text.lower() for token in nlp(text) if token.is_alpha]
    indices = [word_to_idx.get(t, 0) for t in tokens]  # 未知词用 <unk>
    return indices, len(indices)

# ========================
# 5. LSTM 模型定义
# ========================
class SentimentLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)
        self.dropout = nn.Dropout(0.3)

    def forward(self, x, lengths):
        embedded = self.dropout(self.embedding(x))  # [batch, seq_len, embed_dim]
        packed = nn.utils.rnn.pack_padded_sequence(embedded, lengths, batch_first=True, enforce_sorted=False)
        packed_out, (hidden, cell) = self.lstm(packed)
        
        # 取双向 LSTM 最后两层的 hidden state 拼接
        hidden = self.dropout(torch.cat((hidden[-2], hidden[-1]), dim=1))
        return self.fc(hidden).squeeze(1)

# ========================
# 6. 初始化模型、优化器、损失
# ========================
model = SentimentLSTM(VOCAB_SIZE, EMBEDDING_DIM, 32, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.BCEWithLogitsLoss()

# ========================
# 7. 训练函数
# ========================
def train_model():
    model.train()
    for epoch in range(100):  # 训练 100 轮
        total_loss = 0
        for text, label in reviews:
            indices, length = encode_text(text)
            if length == 0:
                continue
            x = torch.LongTensor([indices])
            y = torch.FloatTensor([label])
            
            # 填充到相同长度（简化处理）
            padded = torch.zeros(1, 20, dtype=torch.long)
            padded[0, :length] = x[0, :20]
            length = min(length, 20)
            
            optimizer.zero_grad()
            output = model(padded, [length])
            loss = criterion(output, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

# ========================
# 8. 预测函数
# ========================
def predict_sentiment(sentence):
    model.eval()
    indices, length = encode_text(sentence)
    if length == 0:
        return 0.5
    x = torch.LongTensor([indices])
    padded = torch.zeros(1, 20, dtype=torch.long)
    padded[0, :length] = x[0, :20]
    length = min(length, 20)
    
    with torch.no_grad():
        output = torch.sigmoid(model(padded, [length]))
    return output.item()

# ========================
# 9. 开始训练
# ========================
print("开始训练...")
train_model()
print("训练完成！")

# ========================
# 10. 测试预测
# ========================
test_reviews = [
    "I love this movie!",
    "This film is terrible.",
    "Great story and excellent acting.",
    "Boring and waste of time."
]

print("\n情感预测结果（越接近1越正面）：")
for r in test_reviews:
    score = predict_sentiment(r)
    print(f"{r:30} → {score:.4f}")